import json
data = {'name' : 'ramin' , 'age' : 51 , 'city' : 'tabriz'}
with open ('info.json' , 'w') as file :
    json.dump(data,file)
with open ('info.json' , 'r') as file :
    loaded_data = json.load (file)
    print(loaded_data)
