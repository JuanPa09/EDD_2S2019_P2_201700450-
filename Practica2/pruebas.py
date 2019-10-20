import pandas as pd
import json,sys

datos=pd.read_csv('data.csv',header=None)
tam=len(datos)
df=pd.DataFrame(data=datos)
archivojson=df.iloc[1,1]
#print(archivojson)

f=open('data.json','w')
#f.write("[\n")
f.write(archivojson)
#f.write("\n]")
f.close()



with open('data.json') as contenido:
    cursos=json.load(contenido, strict=False)
for curso in cursos:
    print(curso.get('left'))
    #print(curso.get('left').get('left'))
    #print(curso['left']['left']["left"])
    #name='left'+chr(44)+'left'
    #print(name)
    #print(curso.get('left'))
    #guardado=curso.get('left')
    #print(guardado.get('left'))
    #guardado2=guardado.get('left')
    #print(guardado2.get('valuecombi'))

