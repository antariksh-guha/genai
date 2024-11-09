# deploy-azure.ps1

# Variables
$RG_NAME = "hr-assistant-rg"
$ACR_NAME = "hrassistantregistry"
$APP_NAME = "hr-assistant"
$LOCATION = "eastus"

# Validate environment variables
$requiredEnvVars = @(
    "AZURE_OPENAI_ENDPOINT",
    "AZURE_OPENAI_KEY",
    "AZURE_COGNITIVE_ENDPOINT",
    "AZURE_COGNITIVE_KEY"
)

foreach ($var in $requiredEnvVars) {
    if (-not (Get-Item env:$var -ErrorAction SilentlyContinue)) {
        Write-Error "Missing required environment variable: $var"
        exit 1
    }
}

# Login to Azure
Write-Host "Logging in to Azure..."
az login

try {
    # Create Resource Group
    Write-Host "Creating Resource Group..."
    az group create --name $RG_NAME --location $LOCATION

    # Create Container Registry
    Write-Host "Creating Container Registry..."
    az acr create --name $ACR_NAME --resource-group $RG_NAME --sku Standard --admin-enabled true

    # Get ACR Credentials
    $ACR_USERNAME = az acr credential show --name $ACR_NAME --query "username" -o tsv
    $ACR_PASSWORD = az acr credential show --name $ACR_NAME --query "passwords[0].value" -o tsv

    # Login to ACR
    Write-Host "Logging in to Container Registry..."
    az acr login --name $ACR_NAME

    # Tag and Push Image
    Write-Host "Pushing image to Container Registry..."
    docker tag hr-assistant:latest "$ACR_NAME.azurecr.io/hr-assistant:latest"
    docker push "$ACR_NAME.azurecr.io/hr-assistant:latest"

    # Create App Service Plan
    Write-Host "Creating App Service Plan..."
    az appservice plan create --name "${APP_NAME}-plan" --resource-group $RG_NAME --sku B1 --is-linux

    # Create Web App
    Write-Host "Creating Web App..."
    az webapp create `
        --name $APP_NAME `
        --resource-group $RG_NAME `
        --plan "${APP_NAME}-plan" `
        --deployment-container-image-name "$ACR_NAME.azurecr.io/hr-assistant:latest"

    # Configure App Settings
    Write-Host "Configuring App Settings..."
    az webapp config appsettings set `
        --resource-group $RG_NAME `
        --name $APP_NAME `
        --settings `
        WEBSITES_PORT=8080 `
        AZURE_OPENAI_ENDPOINT=$env:AZURE_OPENAI_ENDPOINT `
        AZURE_OPENAI_KEY=$env:AZURE_OPENAI_KEY `
        AZURE_COGNITIVE_ENDPOINT=$env:AZURE_COGNITIVE_ENDPOINT `
        AZURE_COGNITIVE_KEY=$env:AZURE_COGNITIVE_KEY `
        DOCKER_REGISTRY_SERVER_URL="https://$ACR_NAME.azurecr.io" `
        DOCKER_REGISTRY_SERVER_USERNAME=$ACR_USERNAME `
        DOCKER_REGISTRY_SERVER_PASSWORD=$ACR_PASSWORD

    # Enable Logging
    Write-Host "Enabling logging..."
    az webapp log config --resource-group $RG_NAME --name $APP_NAME --web-server-logging filesystem

    # Wait for deployment
    Write-Host "Waiting for deployment to complete..."
    Start-Sleep -Seconds 30

    # Stream logs
    Write-Host "Streaming logs..."
    az webapp log tail --name $APP_NAME --resource-group $RG_NAME
}
catch {
    Write-Error "Deployment failed: $_"
    exit 1
}

Write-Host "Deployment completed successfully!"
Write-Host "Application URL: https://$APP_NAME.azurewebsites.net"