from cuadrado import Cuadrado
from triangulo import Triangulo
desea_continuar=True

opc=int(input("1.Crear figura\n2.Salir\n"))
while opc==1:
	fig=int(input("1.Cuadrado \n2.Triangulo\n"))
	if fig==1:
		l=int(input("Ingrese lado: "))
		Mcuadrado=Cuadrado(l)
		comp=int(input("1.Area\n2.Dibujo\n3.Ambos\n"))
		if comp==1:
			print ("Area: ",Mcuadrado.calcular_area())
		if comp==2:
			print (Mcuadrado.imprimir())
		if comp==3:
			print ("Area: ",Mcuadrado.calcular_area())
			print (Mcuadrado.imprimir())
	if fig==2:
		h=int(input("Ingrese altura: "))
		b=int(input("Ingrese base: "))
		Mtriangulo=Triangulo(b, h)
		comp=int(input("1.Area\n2.Dibujo\n3.Ambos\n"))
		if comp==1:
			print ("Area: ",Mtriangulo.calcular_area())
		if comp==2:
			print (Mtriangulo.imprimir())
		if comp==3:
			print ("Area: ",Mtriangulo.calcular_area())
			print (Mtriangulo.imprimir())
	opc=int(input("1.Crear figura\n2.Salir\n"))

