import funcionlimites
print ("Bienvenido")
estudiantes= {}
opc= 0
while opc!=4:
	opc= int(input("1.crear estudiante \n2.ingresar nota \n3.reporte de notas \n4.Salir \n"))
	if opc== 1:
		estudiantes={
		input("Ingrese nombre "):[]
		}
	elif opc==2:
		opc2="si"
		nombre= input("Ingrese estudiante: ")
		while opc2=="si":
			notas= int(input("Ingrese nota: "))
			if funcionlimites.validar(notas)==False:
				notas= int(input("Ingrese nota entre 0 y 100: "))
				estudiantes[nombre].append(notas)
			else:
				estudiantes[nombre].append(notas)
			opc2= input("desea seguir? ")
	elif opc==3:
		nombre= input("Ingrese estudiante: ")
		for nota1 in estudiantes[nombre]:
			print(nota1)
		print(funcionlimites.promedio(estudiantes[nombre]))
print("Bai Bai")

