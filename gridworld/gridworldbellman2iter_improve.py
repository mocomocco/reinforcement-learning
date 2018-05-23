import numpy as np
r=np.zeros((4,5,5),dtype=np.float)
#v_pisdash=sp.Array(range(100),(4,5,5))
#print("状態と行動に対して得られる報酬")
#print("")
for i in range(0,5):
  for j in range(0,5):
    if (i==0) and (j==1):#Aは10ポイント
      for a in range(0,4):
        r[a,i,j]=10
    elif (i==0) and (j==3):#Bは5ポイント
      for a in range(0,4):
        r[a,i,j]=5
    else:#4辺は-1ポイント
      if i==0:
        r[0,i,j]=-1
      elif i==4:
        r[2,i,j]=-1
      if j==0:
        r[3,i,j]=-1
      elif j==4:
        r[1,i,j]=-1
print("Debug r=",r)
#r[a,i,j][i,j]からアクションa(0:上,1:右,2:下,3:左)上に行こうとしたとき得られる報酬

v_pi=np.zeros((5,5), dtype=np.float)
def v_pisdash(a,i,j):
  if (i,j)==(0,1):
    return v_pi[4,1]
  elif (i,j)==(0,3):
    return v_pi[2,3]
  elif a==0: return v_pi[max(i-1,0),j]
  elif a==1: return v_pi[i,min(j+1,4)]
  elif a==2: return v_pi[min(i+1,4),j]
  elif a==3: return v_pi[i,max(j-1,0)]

g=0.9 # gamma
def righthand(i,j,v):#billman
  S=0
  MAX=0
  for a in range(0,4):
    S=1./4*1.*(r[a,i,j]+g*v_pisdash(a,i,j))
    if(MAX<S):MAX=S
    S=0
  return MAX

eps=0.00001
while(1):
  delta=0
  for i in range(0,5):
    for j in range(0,5):
      v0=v_pi[i,j]
      v_pi[i,j]=righthand(i,j,v_pi)
      delta+=abs(v0-v_pi[i,j])
  #print("Debug; delta={0:f}".format(delta))
  if delta<eps: break#だいたい収束したら終わり
for i in range(0,5):
  for j in range(0,5):
    print("{0:8.5f}".format(v_pi[i][j]),end=",")
  print("")
