import pandas as pd
import numpy as np

# Read data
dataD = pd.read_csv("./ClassifierData.csv")
dataD = dataD.drop('day', axis=1)
classAtr = dataD.columns[-1]

def info(cD):
    l ={}
    for i in cD:
        if i in l.keys():
            l[i] += 1
        else:
            l[i] = 1
            
    p = {}
    for i in l.keys():
        p[i] = l[i] / len(cD)
        
    return - sum(p[i] * np.log2(p[i]) for i in p)

def makeDj(atr, D):
    l ={}
    j = -1
    for i in D[atr]:
        j += 1
        if i in l.keys():
            l[i].append(list(D.loc[j]))
        else:
            l[i] = list()
            l[i].append(list(D.loc[j]))

    d = {}
    for i in l.keys():
        d[i] = pd.DataFrame(l[i], columns=D.columns).drop(atr, axis=1)

    return d
    
def entropy(atr, D):
    d = makeDj(atr, D)
    
    return sum((len(d[j]) / len(D)) * info(d[i][classAtr]) for j in d.keys())

def makeDecisionTree(D=dataD, count=1):
    class_labels = tuple(D[classAtr].drop_duplicates())
    if len(class_labels) == 1:
        print(count * "\t", "-->", class_labels[0])
        return 0
    if len(D.columns) == 1:
        print(count * "\t", "-->", class_labels)
            return 1
    
    inf = info(D[calssAtr])
    gain = []
    atrs = D.columns[:-1]
    for atr in atrs:
        gain.append(inf - entropy(atr, D))

    max_atr = atrs[np.argmax(gain)]
    print(count * "\t", max_atr)
    d = makeDj(max_atr, D)
    for i in d:
        print(count * "\t", "-->",  i)
        makeDecisionTree(d[i], count + 1)

makeDecisionTree()
