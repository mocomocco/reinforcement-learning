import numpy as np
import sympy as sp
v_pi=[[sp.Symbol('v00'),sp.Symbol('v01'),sp.Symbol('v02'),sp.Symbol('v03'),sp.Symbol('v04')],
      [sp.Symbol('v10'),sp.Symbol('v11'),sp.Symbol('v12'),sp.Symbol('v13'),sp.Symbol('v14')],
      [sp.Symbol('v20'),sp.Symbol('v21'),sp.Symbol('v22'),sp.Symbol('v23'),sp.Symbol('v24')],
      [sp.Symbol('v30'),sp.Symbol('v31'),sp.Symbol('v32'),sp.Symbol('v33'),sp.Symbol('v34')],
      [sp.Symbol('v40'),sp.Symbol('v41'),sp.Symbol('v42'),sp.Symbol('v43'),sp.Symbol('v44')]]
r=np.zeros((4,5,5),dtype=np.float)
#v_pisd=sp.Array(range(100),(4,5,5))
for i in range(0,5):
  for j in range(0,5):
    if (i==0) and (j==1):
      r[0,i,j]=9 
      for a in range(1,4):
        r[a,i,j]=10
    elif (i==0) and (j==3):
      r[0,i,j]=4 
      for a in range(1,4):
        r[a,i,j]=5
    else:
      if i==0:
        r[0,i,j]=-1
      elif i==4:
        r[2,i,j]=-1
      if j==0:
        r[3,i,j]=-1
      elif j==4:
        r[1,i,j]=-1
print("Debug r=",r)
def v_pisd(a,i,j):
  if (i,j)==(0,1):
    return v_pi[4][1]
  elif (i,j)==(0,3):
    return v_pi[2][3]
  elif a==0: return v_pi[max(i-1,0)][j]
  elif a==1: return v_pi[i][min(j+1,4)]
  elif a==2: return v_pi[min(i+1,4)][j]
  elif a==3: return v_pi[i][max(j-1,0)]
# p[sd,r|s,a]=1., pi[a|i,j]=1./4
g=0.9 # gamma
w=[]
for i in range(0,5):
  for j in range(0,5):
    S=0
    for a in range(0,4): S+=1./4*1.*(r[a,i,j]+g*v_pisd(a,i,j)) 
    print(v_pi[i][j],"=",S)
    w.append(v_pi[i][j]-(S))
z=sp.linsolve(w,v_pi[0]+v_pi[1]+v_pi[2]+v_pi[3]+v_pi[4])
print(type(z))
#zz=z.tolist()
#print(type(zz))
#zz=np.array(np.array(z),float)
for i in range(0,5):
  for j in range(0,5):
    print("{0:8.5f}".format(z.args[0][i*5+j]),end=",")
  print("")

