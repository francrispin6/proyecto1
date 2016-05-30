#Proyecto numero 1

def pro1(a):
	if a % 2 == 0:
		return("El numero es par")
	else:
		return("El numero es impar")

#Proyecto numero 2
def pro2(f):
	a = (f-32)*(5/9)
	return(a)

#Proyecto numero 3
def pro3(b, p):
	res = 1
	i = 0
	for i in range(p):
		res = res * b
	return(res)

#Proyecto numero 4
n = int(input("num: "))
p = int(input("palabra: "))
def pro4(n, p):
	l = len(p)	
	cas=(n-l)/2

return(cas)
