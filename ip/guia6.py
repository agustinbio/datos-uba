def es_multiplo_de(n:int, m:int)->bool:
	res:bool = n/m == int(n/m)
	return res

def es_multiplo_de2(n:int, m:int)->bool:
	res:bool = n%m == 0
	return res

def es_multiplo_de3(n:int, m:int)->bool:
	if n%m == 0:
		res:bool = True
	else:
		res:bool = False
	return res

def es_par(numero:int)->bool:
	res:int = es_multiplo_de(numero,2)
	return res

def es_nombre_largo(nombre:str)->bool:
	largo:int = len(nombre)
	res:bool = (largo >= 3) and (largo <= 8)
	return res

def devolver_el_doble_si_es_par(un_numero:int)->int:
	res:int = un_numero
	if un_numero%2 == 0:
		res *=2
	return res	

def imprimir_dos_veces(estribillo:str):
	print(estribillo*2)
	

#def cantidad_de_pizzas(comensales, min_cant_de_porciones)

def lanzar_cohete(cuenta:int):
	while cuenta > 0:
		print(str(cuenta))
		cuenta -= 1
	print("Despegue")

def viaja_a_aristoteles(anio:int):		
	while(anio+384>0):
		print("Viajó 20 años al pasado, está en el año: ",str(anio))
		anio -= 20	
	print("Conoció a Aristóteles")

def viaja_a_aristoteles_for(anio:int):
	for i in range (anio, -384, -20):
		print("Viajó 20 años al pasado, está en el año: ",str(i))
	print("Conoció a Aristóteles")
	
	
test1 = es_multiplo_de(2,3)
print("Resultado de es_multiplo_de(2,3):",test1)
nombre1 = "Agustin"
test2 = es_nombre_largo(nombre1)
print(test2)
test3 = devolver_el_doble_si_es_par(2)
print(test3)
test4 = devolver_el_doble_si_es_par(3)
print(test4)
estribillo = "and deep beneath the rolling waves\nin labyrinths of coral caves\n"
imprimir_dos_veces(estribillo)
lanzar_cohete(20)
viaja_a_aristoteles_for(-384)
viaja_a_aristoteles_for(30)
