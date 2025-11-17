
# merge_sort_step_simplified.py
# Versión simplificada del Merge Sort paso a paso compatible con step()

items = []
n = 0
stack = []

def init(vals):
    global items, n, stack
    items = list(vals)
    n = len(items)
    stack = []

    if n > 1:
        stack.append((0, n-1, "split", None, None, None, []))

def step():
    global items, stack

    if not stack:
        return {"done": True}

    l, r, stage, i, j, mid, temp = stack.pop()

    if stage == "split":
        mid = (l + r) // 2

        if l < mid:
            stack.append((l, r, "merge", l, mid+1, mid, []))
            stack.append((mid+1, r, "split", None, None, None, []))
            stack.append((l, mid, "split", None, None, None, []))
        else:
            stack.append((l, r, "merge", l, mid+1, mid, []))

        return {"a": l, "b": r, "swap": False, "done": False}

    if stage == "merge":

        if i <= mid and j <= r:
            a, b = i, j
            if items[a] <= items[b]:
                temp.append(items[a]); i += 1
            else:
                temp.append(items[b]); j += 1

            stack.append((l, r, "merge", i, j, mid, temp))
            return {"a": a, "b": b, "swap": False, "done": False}

        if i <= mid:
            temp.append(items[i])
            stack.append((l, r, "merge", i+1, j, mid, temp))
            return {"a": i, "b": i, "swap": False, "done": False}

        if j <= r:
            temp.append(items[j])
            stack.append((l, r, "merge", i, j+1, mid, temp))
            return {"a": j, "b": j, "swap": False, "done": False}

        # Copia final
        k = l + len(temp)
        if k <= r:
            items[k] = temp[k - l]
            stack.append((l, r, "merge", i, j, mid, temp))
            return {"a": k, "b": k, "swap": True, "done": False}

    return {"done": False}
