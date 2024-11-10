# HR Assistant Setup Guide

## Prerequisites

### Install Azure CLI

winget install -e --id Microsoft.AzureCLI

### Login to Azure

az login

## Setup Resources

### Variables

$RG_NAME="hr-assistant-rg"
$LOCATION="eastus"
$OPENAI_NAME="hr-openai"
$COGNITIVE_NAME="hr-cognitive"

### Create Resource Group

az group create --name $RG_NAME --location $LOCATION

### Create OpenAI Service

az cognitiveservices account create `--name $OPENAI_NAME`
--resource-group $RG_NAME `--kind OpenAI`
--sku S0 `--location $LOCATION`
--yes

### Create Cognitive Services

az cognitiveservices account create `--name $COGNITIVE_NAME`
--resource-group $RG_NAME `--kind TextAnalytics`
--sku S0 `--location $LOCATION`
--yes

## Run and Debug Locally

### Navigate to Project Directory

cd hr-assistant-backend

### Create Virtual Environment

python -m venv venv

### Activate Virtual Environment

.\venv\Scripts\activate

### Install Dependencies

pip install -r requirements.txt

### Run Backend

python backend.py

### Or with Uvicorn

uvicorn backend:app --reload --port 8080

### Test Health Endpoint

curl http://localhost:8080/health

## Test with Docker Desktop

### Run this in PowerShell as Administrator first (one-time setup):

Set-ExecutionPolicy RemoteSigned -Scope CurrentUser

### Then run this in regular PowerShell:

.\build-local.ps1

## Deploy Container to Azure

.\deploy-azure.ps1

## Setup in Azure DevOps

### Create New Pipeline

Create new pipeline using azure-pipeline.yml

Run pipeline

Add Azure service connection

### Configure Pipeline Variables

Configure pipeline variables:
AZURE_OPENAI_ENDPOINT (secret)

AZURE_OPENAI_KEY (secret)
AZURE_COGNITIVE_ENDPOINT (secret)
AZURE_COGNITIVE_KEY (secret)

### Create Production Environment

Create production environment

### Run Pipeline

Run pipeline

### Add Azure Service Connection
