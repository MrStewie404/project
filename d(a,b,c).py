def discrimimant(a,b,c):
	D = b**2 - 4 * a * c
	if D<0:
		return ("Уравнение не имеет вещественных корней")
	elif D==0:
		x = -b/(2*a)
		print("Уравнение имеет один корень:", x)
	elif D>0:
		return ("Уравнение имеет два корня")
		x1 = (-b - D**0.5/(2*a))
		x2 = (-b + D**0.5/(2*a))
		return x1, x2
print(discrimimant(2, 9, 3))