# build-local.ps1

# Check if .env file exists and load variables
if (Test-Path "hr-assistant-backend/.env") {
    Get-Content "hr-assistant-backend/.env" | ForEach-Object {
        if ($_ -match '^([^=]+)=(.*)$') {
            Set-Item -Path "Env:$($Matches[1])" -Value $Matches[2]
        }
    }
}

# Validate required environment variables
$requiredVars = @(
    "AZURE_OPENAI_ENDPOINT",
    "AZURE_OPENAI_KEY",
    "AZURE_COGNITIVE_ENDPOINT",
    "AZURE_COGNITIVE_KEY"
)

$missingVars = $requiredVars | Where-Object { -not (Get-Item "env:$_" -ErrorAction SilentlyContinue) }
if ($missingVars) {
    Write-Error "Missing required environment variables: $($missingVars -join ', ')"
    exit 1
}

try {
    # Build image
    Write-Host "Building Docker image..."
    docker build `
        --build-arg AZURE_OPENAI_ENDPOINT=$env:AZURE_OPENAI_ENDPOINT `
        --build-arg AZURE_OPENAI_KEY=$env:AZURE_OPENAI_KEY `
        --build-arg AZURE_COGNITIVE_ENDPOINT=$env:AZURE_COGNITIVE_ENDPOINT `
        --build-arg AZURE_COGNITIVE_KEY=$env:AZURE_COGNITIVE_KEY `
        -t hr-assistant:latest .

    if ($LASTEXITCODE -ne 0) {
        throw "Docker build failed"
    }

    # Verify build
    Write-Host "Verifying build..."
    docker inspect hr-assistant:latest

    # Run container
    Write-Host "Starting container..."
    docker run -p 8080:8080 hr-assistant:latest
}
catch {
    Write-Error "Error: $_"
    exit 1
}