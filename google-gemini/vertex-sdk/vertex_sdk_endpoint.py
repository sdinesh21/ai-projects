import google.cloud.aiplatform as aiplatform

# Replace with your project, location, and endpoint details
PROJECT_ID = "583864262541"
LOCATION = "us-central1"  # e.g., "us-central1"
ENDPOINT_ID = "138830935192764416"

# Authentication (if using service account)
# See here for details: https://cloud.google.com/docs/authentication/getting-started
# If running in a GCP environment like Vertex AI Workbench, authentication may be automatic 

# Initialize the Vertex AI Endpoint object
endpoint = aiplatform.Endpoint(ENDPOINT_ID)

# Create the instances (data) you want to send for prediction. 
# Format should match your model's input requirements
instances = [
    {"age": 41, "job": 'technician'},  # Single instance
    # ... add more instances if required
]

# Get predictions from the Endpoint
predictions = endpoint.predict(instances=instances)

# Print/use prediction results
for prediction in predictions.predictions:
    print(prediction)