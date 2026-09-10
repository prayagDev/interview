#!/bin/bash

set -eu

# Usage:
# ./deploy.sh dev <branch_name> <github_username> <github_token>
# ./deploy.sh prod <branch_name> <github_username> <github_token>

ENVIRONMENT="$1"
BRANCH="$2"
GITHUB_USERNAME="$3"
GITHUB_TOKEN="$4"

# Validate arguments
if [ "$#" -ne 4 ]; then
    echo "Usage: ./deploy.sh {dev|prod} {branch_name} {github_username} {github_token}"
    exit 1
fi

case "$ENVIRONMENT" in
    dev)
        PROJECT_PATH="/home/ubuntu/tap-tap-internal-dashboard"
        SERVICE_NAME="tap_tap_internal_dashboard_dev"
        ;;

    prod)
        PROJECT_PATH="/home/ubuntu/tap-tap-prod/tap-tap-internal-dashboard"
        SERVICE_NAME="tap_tap_internal_dashboard_prod"
        ;;

    *)
        echo "Invalid environment: $ENVIRONMENT"
        echo "Use: dev or prod"
        exit 1
        ;;
esac

echo "========================================"
echo "Deploying branch: $BRANCH"
echo "Environment: $ENVIRONMENT"
echo "========================================"

cd "$PROJECT_PATH"

# GitHub repository URL with credentials
REPO_URL="https://${GITHUB_USERNAME}:${GITHUB_TOKEN}@github.com/prayag-befisc/tap-tap-internal-dashboard.git"

echo ">>> Fetching latest code..."
git fetch "$REPO_URL"

echo ">>> Checking out branch: $BRANCH"
git checkout "$BRANCH"

echo ">>> Pulling latest code..."
git pull "$REPO_URL" "$BRANCH"

echo ">>> Activating virtual environment..."
source .venv/bin/activate

echo ">>> Installing dependencies..."
pip install -r requirements.txt

echo ">>> Restarting Supervisor service..."
sudo supervisorctl restart "$SERVICE_NAME"

echo "========================================"
echo "Deployment completed successfully!"
echo "========================================"

