# Template genérico — SKELETON
# Contrato: init(vals), step() -> {"a": int, "b": int, "swap": bool, "done": bool}

items = []
n = 0
i=0
j=0
role='build'
l=0
ismax=False
def MaxheapTree(array:list):
    global n
    for x in range(n//2,-1,-1):
        current=x
        while True:
            left=2*current+1
            right=2*current+2
            leftElement=array[left] if left<n else float('-inf')
            rightElement=array[right] if right<n else float ('-inf')
            greatChild=leftElement if leftElement>rightElement else rightElement
            if(array[current]<greatChild):
                if(greatChild==rightElement):
                    temp=array[current]
                    array[current]=greatChild
                    array[right]=temp
                    current=right
                else:
                    temp=array[current]

                    array[current]=greatChild
                    array[left]=temp
                    current=left
            else:
                break
            
def init(vals):
    global items, n,i,j,current,role,l,ismax
    items = list(vals)
    role='build'
    n = len(items)
    j=(len(items)//2)-1
    l=(len(items))-1
    current=j
    ismax=False
    # TODO: inicializar punteros/estado

def step():
    global n,items,current,j,role,l,ismax
    if(role=='build'):
        if(j<=0):
            role="sort"
            current=0
            ismax=True
            return{"done":False}
        left=2*current+1
        right=2*current+2
        
        if(left>n-1 and right>n-1):
            a=current
            b=0
            j-=1
            current=j

            return {'done':False,'swap':False,"a":current,"b":2*current+1}
        leftElement=items[left] if left<n else float('-inf')
        rightElement=items[right] if right<n else float ('-inf')
        greatChild=leftElement if leftElement>rightElement else rightElement
        greatIndex=left if leftElement>rightElement else right
        if(items[current]<greatChild):
                a=current
                b=greatIndex
                items[a],items[b]=items[b],items[a]
                current=greatIndex
                return {"done":False,"swap":True,"a":a,"b":b}
        j-=1
        current=j
        return {"done":False}
    else:
       
        if l<=0: return {"done":True}
        if(items[current]>items[l] and ismax):
            a=current
            b=l
            items[current], items[l] = items[l], items[current]  
            l-=1
            ismax=False
            return {"a":a,"b":b,"swap":True,"done":False}
        left=2*current+1
        right=2*current+2
        leftElement=items[left] if left<=l else float('-inf')
        rightElement=items[right] if right<=l else float ('-inf')
        greatChild=leftElement if leftElement>rightElement else rightElement
        greatIndex=left if leftElement>rightElement else right
        if(items[current]<greatChild):
                        a=current
                        b=greatIndex
                        items[a], items[b] = items[b], items[a]
                        current=greatIndex
                        return {"a":a,"b":b,"swap":True,"done":False}

        ismax=True
        current=0
        return {"done":False,'a':current,'b':greatIndex,"swap":False}