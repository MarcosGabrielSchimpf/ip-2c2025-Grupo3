# Contrato: init(vals), step() -> {"a": int, "b": int, "swap": bool, "done": bool}

items = []
length = 0
pasada = 0
index = 0

def init(vals):
    global items, length, pasada, index
    items = list(vals)
    length = len(items)
    pasada = 0
    index = 0

def step():
    global items, length, pasada, index

    # Si ya terminamos todas las pasadas
    if pasada >= length - 1:
        return {"done": True}
    
    
    # 1) Elegir índices a y b a comparar en este micro-paso (según tu Bubble).
    aux = 0
    swap = False    
    a = index
    b = index+1



    # 2) Si corresponde, hacer el intercambio real en items[a], items[b] y marcar swap=True.
    if items[a] > items[b]:
        aux = items[a]
        items[a] = items[b]
        items[b] = aux
        swap = True

     # 3) Avanzar punteros (preparar el próximo paso).
    index = index+1
    if index >= length - 1 - pasada: #length recorre toda la lista, -1 porque listas cuentan de 1 a n en vez de 0 a n-1, 
        #y por cada pasada el numero mas grande deberia estar al final, por lo tanto lo restamos para evitar una pasada completa por posibles decenas de numeros
        index = 0
        pasada += 1

        #reseteamos index para pasar de nuevo, aumentamos "Pasada", y damos la informacion del contrato

    return {"a": a, "b": b, "swap": swap, "done": False}

    

