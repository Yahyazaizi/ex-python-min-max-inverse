def maxi (m):
    maxi=m[0]
    for i in m:
        if maxi< i :
           maxi= i
        return maxi
def min (m):
    min=m[0]
    for i in m:
        if min > i :
           min = i
        return min
def renvirse (m):
  tab=[]
  for i in range(9,-1,-1):
    tab.append(m[i])
  return tab


m=[1,2,4,5,4,7,5,4,7,10]
print(max(m))
print(min(m))
print(renvirse(m))












