import json
jsonstr = """ {"colors":[{"color": "black","category": "hue","type": "primary","code": {"rgba": [255,255,255,1],"hex": "#000"}},{"color": "white","category": "value","code": {"rgba": [0,0,0,1],"hex": "#FFF"}},{"color": "red","category": "hue","type":"primary","code": {"rgba": [255,0,0,1],"hex": "#FF0"}}]}"""

#jsonobj = json.loads(jsonstr) 
jsonobj = json.load(open('/home/haskhr/Git-examples/.vscode/sample.json')) 
print(jsonobj['colors'])  