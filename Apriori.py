import itertools as itr
min_sup = int(input("min_sup: "))
dataset = [['Milk', 'Onion', 'Nutmeg', 'Kidney Beans', 'Eggs', 'Yogurt'],
           ['Dill', 'Onion', 'Nutmeg', 'Kidney Beans', 'Eggs', 'Yogurt'],
           ['Milk', 'Apple', 'Kidney Beans', 'Eggs'],
           ['Milk', 'Unicorn', 'Corn', 'Kidney Beans', 'Yogurt'],
           ['Corn', 'Onion', 'Onion', 'Kidney Beans', 'Ice cream', 'Eggs']]

dataset = [['google','amazon',],['amazon','google','python','cse'],['cse','google'],['amazon','python'],
      ['cse','amazon','python','google'],['amazon','google','cse','data',]]

c1 = set()
for i in dataset:
  for j in i:
    c1.add(j)

# Generates combinations (set) of elements in a and b, each set of length == childCount and deletes sets whose subsets are in pop
def makeProductSet(a, b, pop, childCount=2):
    pSet =[]
    p = itr.product(a, b)
    
    for i, j in p:
      if type(i) != str:
        l = list(i)
        l.append(j)
      else:
        l = []
        l.append(i); l.append(j)

      if len(l := set(l)) == childCount:
        for itm in pop:
          if (type(itm) != str and not itm.issubset(l)) or (type(itm) == str and itm not in l):
            pSet.append(frozenset(l))
    return set(pSet)

L1 = {k: 0  for k in c1}

for i in dataset:
  for j in c1:
    if j in i:
      L1[j] += 1

pop = []
for k in L1:
  if L1[k] < min_sup:
    pop.append(k)
for k in pop:
  L1.pop(k)

import pandas as pd
l_current = pd.DataFrame(L1, index=['support'])

import numpy as np
count = 2
l_prev = pd.DataFrame()

while len(l_current.columns) > 0:
  c = makeProductSet(l_current.columns, L1, pop, count)
  l_prev = pd.DataFrame(l_current)

  if len(c) != 0:
    l_current = pd.DataFrame(columns = c)
    l_current.loc['support'] = 0

    for i in dataset:
      for j in l_current.columns:
        if j.issubset(i):
          l_current[j] += 1

    pop = []
    for j in l_current.columns:
      if l_current[j].any() < min_sup:
        l_current[j] = np.nan
        pop.append(j)
    l_current = l_current.dropna(axis=1)
    
  else:
    l_current = pd.DataFrame()
    
  count +=1

print(l_prev)

input("Press Enter to Exit!")
