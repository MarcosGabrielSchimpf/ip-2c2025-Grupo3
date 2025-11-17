
# =============================
# QuickSort paso a paso (SKELETON)
# Contrato: init(vals), step() -> {"a": int, "b": int, "swap": bool, "done": bool}
# =============================

items = []
n = 0

# Estado
stack = []          # Pila de (inicio, fin)
i = 0               # Puntero izquierdo
j = 0               # Puntero derecho
pivot = None        # Valor del pivote
phase = "idle"      # idle, partitioning, pushing

def init(vals):
    global items, n, stack, i, j, pivot, phase
    items = list(vals)
    n = len(items)

    # Reiniciar todo
    stack = []
    if n > 1:
        stack.append((0, n - 1))  # Primer rango
    phase = "idle"
    i = 0
    j = 0
    pivot = None


def step():
    global items, stack, i, j, pivot, phase

    # Si no queda nada por ordenar
    if not stack:
        return {"done": True}

    # Tomamos el rango actual
    if phase == "idle":
        low, high = stack.pop()
        pivot = items[(low + high) // 2]  # pivote central
        i = low
        j = high
        phase = "partitioning"

    # -----------------------------
    # FASE: partitioning
    # -----------------------------
    if phase == "partitioning":

        # Mover i hacia la derecha
        if items[i] < pivot:
            ret = {"a": i, "b": j, "swap": False, "done": False}
            i += 1
            return ret

        # Mover j hacia la izquierda
        if items[j] > pivot:
            ret = {"a": i, "b": j, "swap": False, "done": False}
            j -= 1
            return ret

        # Si i <= j hacemos swap
        if i <= j:
            a, b = i, j
            items[i], items[j] = items[j], items[i]
            i += 1
            j -= 1
            return {"a": a, "b": b, "swap": True, "done": False}

        # Cuando i > j terminamos la partición
        phase = "pushing"

    # -----------------------------
    # FASE: pushing — empujar subrangos
    # -----------------------------
    if phase == "pushing":
        low = min(i, j)
        high = max(i, j)

        # Rango izquierdo
        if (j_orig := (i - 1)) > (low_orig := low):
            stack.append((low_orig, j_orig))

        # Rango derecho
        if (i_orig := i) < (high_orig := high):
            stack.append((i_orig, high_orig))

        phase = "idle"
        return {"a": 0, "b": 0, "swap": False, "done": False}

    return {"done": True}
