import json

data = {}

with open('tsconfig.json','r') as json_file:
    data = json.load(json_file)
data['compilerOptions']['jsx'] = "react"
with open('tsconfig.json','w') as json_file:
    json.dump(data,json_file)
