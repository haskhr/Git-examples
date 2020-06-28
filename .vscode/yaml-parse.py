import yaml
from yaml import load ,load_all
stream = open ('/home/haskhr/Git-examples/.vscode/sample.yaml', 'r')
#haskhr@MacBookAir:~/Git-examples$ /usr/bin/python3 /home/haskhr/Git-examples/.vscode/yaml-parse.py
documents = load_all(stream,Loader=yaml.FullLoader)

#print(type(documents))

for doc in documents:
  #  print (type(doc))
    print(doc[0]['tasks'][2])
