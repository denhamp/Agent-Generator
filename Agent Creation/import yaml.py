import yaml
import uuid


filename = 'docker-compose'


with open(f'{filename}.yml','r') as f:
    file = yaml.safe_load(f)
print(file)

file['services']['agent-init']['environment'][0] = f'AGENT-ID={uuid.uuid4()}'

print(file)

with open('output.yml','w') as output:
    yaml.dump(file,output,sort_keys=False)

print('Done !')
