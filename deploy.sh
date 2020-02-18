#!/bin/sh

set -e

# Initialize environment variables that are defined in .env file
echo "Initializing environment variables..."
export $(grep -v '^#' .env | xargs)
# Currently we generate BUILD_ID based on timestamp, later on git SHA can be used
BUILD_ID="$(date +%s)"

# Create a build for Google Cloud Build
echo "Building image: gcr.io/$GCP_PROJECT/$IMAGE_NAME:$BUILD_ID"
gcloud builds submit --tag gcr.io/"$GCP_PROJECT"/"$IMAGE_NAME":"$BUILD_ID"

# Create ConfigMap object from .env file, if ConfigMap exists then replace it
echo "Creating ConfigMap object..."
kubectl create configmap app-config --from-env-file=.env -o yaml --dry-run | kubectl replace -f -

echo "Deploying..."
envsubst < deployment.yml | kubectl apply -f -
