import pymongo


client = pymongo.MongoClient("mongodb+srv://AlejandroGrisalesP:alejandroinfo2@clustera.mmuq0jw.mongodb.net/?retryWrites=true&w=majority")
db = client.test

mydb = client["prueba1"]
mycol = mydb["clientes"]

mydict = {"nombre":"Jose","direccion":3}

x = mycol.insert_one(mydict)
print(x.inserted_id)

for x in mycol.find({"direccion":0}):
    print(x)

#Buscar e imprimir todos los datos
#for y in mycol.find():
#    print(y)

#Buscar e imprimir un dato en especifico
#for x in mycol.find({"direccion": 0}):
#    print(x)

#actualizar o reemplazar valores en la base de datos
#myquery = {"nombre":"Jose","direccion":3}
#newvalues = {"$set": {"Nombre":"Luis"}}

#mycol.update_one(myquery, newvalues)