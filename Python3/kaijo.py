# 階乗 n! を計算する関数fac(n)をプログラムせよ.

def Fac(n):
	result=1;

	for i in range(n,0,-1):
		result=result*i

	return result

def IsEven(n):
	if n==0:
		print (n,"is zero")
	elif n%2==0:
		print (n,"is even")
	else:
		print (n,"is odd")

def Parity(n):
	return n%2

def test(n):
	print ("Fac(",n,") =",Fac(n))
	print ("Parity(",n,") =",Parity(n))
	IsEven(n)
