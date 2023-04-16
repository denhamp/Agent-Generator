import yaml

# Read input data from YAML file
with open('Agent Create.yaml', 'r') as file:
    input_data = yaml.safe_load_all(file)
    for data in input_data:
        print(data)

# Generate a YAML file for each document in the input file
for index, document in enumerate(input_data):
    # Generate YAML data structure
    data = {
        'version': '3',
        'services': {
            'agent-init': {
                'image': document['AGENT_INIT_IMAGE'],
                'environment': [
                    f"AGENT_ID={document['AGENT_ID']}",
                    f"AGENT_NAME={document['AGENT_NAME']}",
                    f"AGENT_DATA_BROKER={document['AGENT_DATA_BROKER']}",
                    f"AGENT_DATA_BROKER_PORT={document['AGENT_DATA_BROKER_PORT']}",
                    f"TENANT={document['TENANT']}",
                    f"TENANT_USER={document['TENANT_USER']}",
                    f"TENANT_PASSWORD={document['TENANT_PASSWORD']}"
                ],
                'volumes': ['secrets:/run/secrets']
            },
            'sensor-actuate': {
                'container_name': document['CONTAINER_NAME'],
                'image': document['SENSOR_ACTUATE_IMAGE'],
                'environment': [f"AGENT_MANAGEMENT_PROXY={document['AGENT_MANAGEMENT_PROXY']}"],
                'volumes': ['secrets:/run/secrets'],
                'depends_on': {
                    'agent-init': {
                        'condition': 'service_completed_successfully'
                    }
                }
            }
        },
        'volumes': {
            'secrets': None
        }
    }

    # Write YAML to file
    filename = f"config_{index}.yaml"
    with open(filename, 'w') as file:
        yaml.dump(data, file)
    print(f"Created {filename}")
