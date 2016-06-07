notas = []
opc="si"
while opc=="si":
	nota= str(input("Ingrese nota: "))
	notas.append(nota)
	opc=input("desea seguir?")
arc= open("Archivo.txt", "w")
for nota in notas:
	arc.write(nota)
	arc.write("\n")
arc.close()