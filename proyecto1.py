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
