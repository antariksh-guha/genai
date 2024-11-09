# Build frontend
FROM node:16-alpine AS frontend-build
WORKDIR /app/frontend
COPY hr-assistant-frontend/package*.json ./
RUN npm install
COPY hr-assistant-frontend/ .
ARG REACT_APP_API_BASE_URL=/api
ENV REACT_APP_API_BASE_URL=$REACT_APP_API_BASE_URL
RUN npm run build

# Build backend
FROM python:3.9-slim
WORKDIR /app

# Preserve React build structure
COPY --from=frontend-build /app/frontend/build ./static

# Install dependencies
COPY hr-assistant-backend/requirements.txt .
RUN apt-get update && \
    apt-get install -y curl && \
    rm -rf /var/lib/apt/lists/* && \
    pip install -r requirements.txt

# Copy application files
COPY hr-assistant-backend/ .
COPY start.sh .
RUN chmod +x start.sh

# Define build args and env vars
ARG AZURE_OPENAI_ENDPOINT
ARG AZURE_OPENAI_KEY
ARG AZURE_COGNITIVE_ENDPOINT
ARG AZURE_COGNITIVE_KEY

ENV AZURE_OPENAI_ENDPOINT=$AZURE_OPENAI_ENDPOINT \
    AZURE_OPENAI_KEY=$AZURE_OPENAI_KEY \
    AZURE_COGNITIVE_ENDPOINT=$AZURE_COGNITIVE_ENDPOINT \
    AZURE_COGNITIVE_KEY=$AZURE_COGNITIVE_KEY \
    PORT=8080

EXPOSE 8080

HEALTHCHECK --interval=30s --timeout=30s --start-period=5s --retries=3 \
    CMD curl -f http://localhost:8080/health || exit 1

CMD ["./start.sh"]