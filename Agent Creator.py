import uuid
import requests
import json
import yaml
import getpass




tenant_url = 'denham.dhus-labs.analytics.accedian.io'
agent_uuid = '4ead6f28-49ae-4369-98ac-165f461e0fe0' #use this as the test agent uuid
agent_name = 'AgentCreateTest'

def login_func():
    with open('config.yml', 'r') as yaml_file:
        yaml_data = yaml.safe_load(yaml_file)
    tenant_url = yaml_data['tenant']['url']
    print(f"Url: {tenant_url}")
    username = yaml_data['tenant']['username']
    print(f"Username: {username}")
    rr_ip = yaml_data['roadrunner']['ip']
    rr_port = yaml_data['roadrunner']['port']
    print(f'ip {rr_ip}')
    print(f'port {rr_port}')

    url = tenant_url + "/api/v1/auth/login"
    headers = {
        "Cache-Control": "no-cache",
        "Content-Type": "application/x-www-form-urlencoded",
        "Accept": "application/json",
    }
    password = getpass.getpass(prompt='Enter your tenant password: ')
    data = {"username": username, "password": password}
    resp = requests.post(url, headers=headers, data=data, verify=False)
    resp.raise_for_status()
    token = (resp.headers['Authorization'])

    return token, tenant_url, rr_ip, rr_port


def create_config(tenant_url,agent_uuid,agent_name,rr_ip,rr_port,token):

    url = tenant_url + '/api/orchestrate/v3/agents/configuration'
    data = {"data": 
    {
        "type": "agentConfigs",
        "attributes": {
            "agentId": f'{agent_uuid}',
            "dataGateway": {
                "server": rr_ip,
                "port": rr_port
            },
            "identification": {
                "agentName": agent_name
            }
        }
    }
    }
    headers = {
        "Cache-Control": "no-cache",
        "Content-Type": "application/x-www-form-urlencoded",
        "Accept": "application/json",
        "Authorization" : token,
    }
    print(data)
    #resp = requests.get(url, headers=headers, json=data, verify=False)
    #resp.raise_for_status()

    return



data = login_func()
create_config(data[1],agent_uuid,agent_name,data[2],data[3], data[0])
headers = {
        "Cache-Control": "no-cache",
        "Content-Type": "application/x-www-form-urlencoded",
        "Accept": "application/json",
        "Authorization" : data[0],
    }
url = data[1] + '/api/orchestrate/v3/agents/' + f'{agent_uuid}' + '/secrets'
print(url)
resp = requests.post(url, headers=headers, verify=False)
resp.raise_for_status()
print(resp)