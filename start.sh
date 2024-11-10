#!/bin/bash
cd /app
uvicorn backend:app --host 0.0.0.0 --port 8080 --log-level info