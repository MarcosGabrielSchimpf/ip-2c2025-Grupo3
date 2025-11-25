# Template genérico — SKELETON
# Contrato: init(vals), step() -> {"a": int, "b": int, "swap": bool, "done": bool}
import math
items = []
n = 0
# Agregá acá tus punteros/estado, p.ej.:
# i = 0; j = 0; fase = "x"; stack = []

def init(vals):
    global items, n,gap,i
    items = list(vals)
    n = len(items)
    i=0
    gap=math.floor(n/2)
    # TODO: inicializar punteros/estado

def step():
    global gap,items,n,i
    if(gap<1):
        return {"done":True}
    a=i
    b=i+gap
    c=i-gap
    print(a,b,c,n)
    if(i+gap>=n):
        i=0
        gap=math.floor(gap/2)
        return {"done":False,"a":a,"b":b,"swap":False}
    if(items[a]>items[b] and b<n):
        items[a],items[b]=items[b],items[a]
        return {"done":False,"a":a,"b":b,"swap":True}
    if(c>=0):
         if(items[a]<items[c]):
          items[a],items[c]=items[c],items[a]
          i-=1
          return {"done":False,"a":a,"b":c,"swap":True}
    i+=1
    return {"done": False}
