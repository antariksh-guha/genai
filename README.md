# HR Assistant Setup Guide

![alt text](image.png)

## Azure Steps

winget install -e --id Microsoft.AzureCLI

### `Login to Azure`

az login

### `Variables`

$RG_NAME="hr-assistant-rg"
$LOCATION="eastus"
$OPENAI_NAME="hr-openai"
$COGNITIVE_NAME="hr-cognitive"

### `Create Resource Group`

az group create --name $RG_NAME --location $LOCATION

### `Create OpenAI Service`

az cognitiveservices account create `--name $OPENAI_NAME`
--resource-group $RG_NAME `--kind OpenAI`
--sku S0 `--location $LOCATION`
--yes

### `Create Cognitive Services`

az cognitiveservices account create `--name $COGNITIVE_NAME`
--resource-group $RG_NAME `--kind TextAnalytics`
--sku S0 `--location $LOCATION`
--yes

## Test locally with Docker Desktop

### `Run this in PowerShell as Administrator first (one-time setup)`

Set-ExecutionPolicy RemoteSigned -Scope CurrentUser

### `Then run this in regular PowerShell`

.\build-local.ps1

## Deploy Container to Azure

.\deploy-azure.ps1

## Setup in Azure DevOps

### `Create New Pipeline`

Create new pipeline using azure-pipeline.yml

### `Add Azure service connection`

1. Azure Resource Manager service connection:

   - Name: Azure-Service-Connection
   - Subscription: Your Azure subscription
   - Resource Group: hr-assistant-rg

2. Azure Container Registry service connection:
   - Name: ACR-Service-Connection
   - Registry: hrassistantregistry.azurecr.io
   - Subscription: Your Azure subscription

### `Configure Pipeline Variables`

Configure pipeline variables:

- AZURE_SERVICE_CONNECTION: Name of your Azure Resource Manager service connection
- ACR_SERVICE_CONNECTION: Name of your Azure Container Registry service connection
- AZURE_OPENAI_ENDPOINT: (secret)
- AZURE_OPENAI_KEY: (secret)
- AZURE_COGNITIVE_ENDPOINT: (secret)
- AZURE_COGNITIVE_KEY: (secret)

### `Create Production Environment`

Create production environment

### `Run Pipeline`

Run pipeline
