from google.cloud import aiplatform as vertex_ai

endpoint_list = vertex_ai.Endpoint.list() 

print (len(endpoint_list))
for endpoint in endpoint_list:
    print(endpoint.resource_name)  # This will print the full endpoint name
