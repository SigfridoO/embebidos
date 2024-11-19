print("hola mundo")

import json

nachito = {
    "edad" : 23,
    "nombre": "Jesús",
    "hobby" : [
        "programar", "escuchar música", "faltar a clase"
    ],
    "altura":2.0,
    "peso":55
}


print (nachito)

# Convirtiendo a JSON
nachito_json = json.dumps(nachito)
print(nachito_json)