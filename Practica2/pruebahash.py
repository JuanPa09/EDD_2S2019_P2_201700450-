import hashlib
import pandas as pd
import json

#CON ESTO GENERO EL HASH
datos=pd.read_csv('data2.csv',header=None)
#tam=len(datos)
df=pd.DataFrame(data=datos)
archivojson=df.iloc[1,1]
data=json.loads(archivojson)
dat=json.dumps(data)
forhash=dat.replace(" ", "") 
#print(forhash)
j = bytes(forhash, 'utf-8')
m= hashlib.sha256(j)
print(data["PREVIOUSHASH"])
#print(m.hexdigest())

    

#f=open('data.json','w')
#f.write(archivojson)
#f.close()



with open('data.json') as contenido:
    cursos=json.load(contenido)
    #print(cursos)
    #cursos=json.dumps(curso)
#cursos=json.dumps(curso)
index=str(cursos["INDEX"])
timestap=cursos['TIMESTAMP']
classs=cursos['CLASS']
data=cursos["DATA"]
dum=json.dumps(data)
#print(dum)
phash=cursos["PREVIOUSHASH"]

parametros=str(index)+str(timestap)+str(classs)+str(data)+str(phash)
#print(parametros)


#for state in cursos['data']:
#    print(state)
    #data=json.dumps(contenido)
    #print(data)
j = bytes(parametros, 'utf-8')
m= hashlib.sha256(j)
#print(m.hexdigest())


def get_pretty_print(json_object):
    return json.dumps(json_object, sort_keys=True, indent=4, separators=(',', ': '))



a=get_pretty_print(archivojson)
#print(a)

