import requests
import json
import re
import sys

# We need to pass several items to the script to operate
# Base_Name. Agent type, Number of instances, tenant details
base_name = sys.argv[1]
agent_type = sys.argv[2]
no_instances = sys.argv[3]
tenant_name = sys.argv[4]


#Iterate through the Instances to build the file

for instance = 1 to no_instances:
    filename = basename + str(instance).zfill(3)
    with open(filename,"w") as docker_file:
        f.write('version: \'3\'')
        f.write{'services:'}
        f.write('\tagent-init:')
        f.write{'\t\timage: "docker.io/nathanielhoaccedian/agent-init-container:latest"')
        f.write('\t\tenvironment:')
        f.write('\t\t\t- AGENT_ID=')
      - AGENT_NAME=Mac-Transfer
      - AGENT_DATA_BROKER=192.168.0.24
      - AGENT_DATA_BROKER_PORT=55888
      - TENANT=https://denham.dhus-labs.analytics.accedian.io
      - TENANT_USER=dpearce@accedian.com
      - TENANT_PASSWORD=
    volumes:
      - secrets:/run/secrets
  sensor-actuate:
    container_name: "Mac-Transfer"
    image: "gcr.io/sky-agents/agent-transfer-amd64:r22.11"
    environment:
      - AGENT_MANAGEMENT_PROXY=192.168.0.24
    volumes:
      - secrets:/run/secrets
    depends_on:
      agent-init:
        condition: service_completed_successfully
volumes:
   secrets:
