from array import *
from string import *
from random import *
import numpy as np

def pertenece1(s: list, e: int)->bool:
	res: bool = False
	i: int = 0
	while (i<len(s) and s[i] != e):
		i += 1
	if (i< len(s) or s[i] == e):
		res = True
	return res

def pertenece2(s: list, e: int)->bool:
	res: bool = False
	for x in s:
		if (e == x):
			res = True
			break
	return res

def pertenece3(s: array, e:int)->bool:
	res: bool = False
	for x in range(len(s)):
		if (e == s[x]):
			res = True
			break
	return res	

def pertenece4(s, e)->bool:
	res: bool = False
	for x in range(len(s)):
		if (e == s[x]):
			res = True
			break
	return res

def divideATodos(s: list, e:int)->bool:
	res: bool = True
	for x in s:
		if( x%e != 0):
			res = False
			break
	return res

def sumaTotal(s: list)->int:
	res: int = 0
	for x in s:
		res += x
	return res

def ordenados1(s: list)->bool:
	res: bool = True
	if len(s) > 1:
		for i in range(2, len(s)):
			if (s[i] <= s[i-1]):
				res = False
				break
	return res

def ordenados2(s: list)->bool:
	res: bool = True
	if len(s) > 1:
		i: int = 2
		while i<len(s) and s[i] > s[i-1]:
			i +=1
		if i < len(s)-1 or s[i] <= s[i-1]:
			res=False
	return res

def tiene_palabra_mas_larga_que(s:list)->bool:
	res: bool = False
	for x in s:
		if len(x) > 7:
			res = True
			break
	return res

def es_palindromo(s:str)->bool:
	res: bool = True
	for i in range(len(s)//2):
		if (s[i] != s[len(s)-1-i]):
			res = False
			break
	return res


def pertenece(s, e)->bool:
	for x in s:
		if (e == x):
			return True
	return False

def fortaleza_password(passwd:str)->str:
	res: str = "AMARILLA"
	tiene_mayus:bool = False
	tiene_minus:bool = False
	tiene_num:bool = False
	for c in passwd:
		if pertenece(ascii_uppercase,c):
			tiene_mayus = True
		elif pertenece(ascii_lowercase,c):
			tiene_minus = True
		elif pertenece(digits,c):
			tiene_num = True
	if len(passwd) < 5:
		res = "ROJA"
	elif len(passwd) > 8 and tiene_mayus and tiene_minus and tiene_num:
		res = "VERDE"
	return res

def saldo_actual(movimientos:list)->int:
	res: int = 0
	for movimiento in movimientos:
		if movimiento[0] == 'I':
			res += movimiento[1]
		elif movimiento[0] == 'R':
			res -= movimiento[1]
		else:
			break
	return res
	
def tiene_3_vocales(palabra:str)-> bool:
	res:bool = False
	tiene_a = tiene_e = tiene_i = tiene_o = tiene_u = False
	for c in palabra:
		if c == 'a':
			tiene_a = True
		elif c == 'e':
			tiene_e = True
		elif c == 'i':
			tiene_i = True
		elif c == 'o':
			tiene_o = True
		elif c == 'u':
			tiene_u = True
	tiene_vocales = [tiene_a,tiene_e,tiene_i,tiene_o,tiene_u]
	if sum(tiene_vocales) >= 3:
		res = True
	return res

def borra_pos_pares_inout (lista:list):
	for i in range(1,len(lista),2):
		lista[i] = 0
	return
	
def borra_pos_pares (lista:list)->list:
	res = list.copy(lista)
	for i in range(1,len(res),2):
		res[i] = 0
	return res

def elimina_vocales (cadena:str)->str:
	res:list = []
	vocales = 'aeiou'
	for c in cadena:
		if not pertenece(vocales,c):
			res += c
	return "".join(res)
	
	
def reemplazaVocales (s:str)->str:
	res = list(s)
	vocales = 'aeiou'
	for i in range(len(res)):
		if pertenece(vocales,res[i]):
			res[i] = '_'
	return "".join(res)
	
def darVueltaStr (s:str)->str:
	res = list(s)
	for i in range(len(s)):
		res[i] = s[len(s)-1-i]
	return "".join(res)	

def eliminar_c_de_cadena (cadena:list, caracter: str)->list:
	res:list = []
	if pertenece(cadena,caracter):
		for c in cadena:
			if c != caracter:
				res += c
	else:
		res=cadena.copy()
	return res
def eliminarRepetidos (s:str)->str:
	res = list(s)
	i:int = 0
	while i < len(res):
		res = res[0:i+1] + eliminar_c_de_cadena(res[(i+1):len(res)],res[i])
		i += 1
	return "".join(res)
def suma(s: list):
	res = 0
	for x in s:
		res += x
	return res

def promedio (s:list)->float:
	res = suma(s)/len(s)
	return res
	
def mayor_igual_que (s:list, valor)->bool:
	res = True
	for x in s:
		if x<valor:
			res = False
			break
	return res

def aprobado (notas:list)->int:
	res:int = 3
	if mayor_igual_que(notas,4):
		if promedio(notas)>=7:
			res = 1
		elif promedio(notas)>=4:
			res = 2
	return res

def lista_nombres()->list:
	res = []
	i:int = 0
	nombre = str(input())
	while (nombre !='listo'):
		res.append(nombre)
		nombre = str(input())
		i +=1
	return res

def ingresar_monto()->float:
	print("Monto:")
	monto = float(input())
	return monto
	
def ingresar_operacion()->float:
	print("Operacion (Cargar, Descontar, Salir(X)?: ")
	operacion = str(input())
	return operacion

def monedero()->list:
	historial = []
	operacion = ingresar_operacion()
	while operacion !='X':
		if operacion == 'C' or operacion == 'D':
			monto = ingresar_monto()
			historial.append([operacion,monto])
		else:
			print("Operacion no valida")
		operacion = ingresar_operacion()
	return historial
		

def producto_cartesiano(lista1:list, lista2:list)->list:
	res = []
	for x in lista1:
		for y in lista2:
			res.append([x,y])
	return res

numeros = [x for x in range (1,8)]
figuras = [10,11,12]
valores_posibles = numeros + figuras
palo = ["Espadas","Copas", "Bastos", "Oro"]
mazo = producto_cartesiano(palo,valores_posibles)

def otra_carta()->int:
	print("Decida: sacar otra carta (c) o Plantarse (p):")
	decision = str(input())
	if decision == 'c':
		res = 0
	elif decision == 'p':
		res = 1
	else:
		res = -1
	return res

def siete_y_medio()->list:
	barajado = sample(mazo, k=len(mazo))
	historial = []
	suma:float = 0
	decision = otra_carta()
	i:int = 0
	while(decision == -1 or decision == 0):
		if (decision == 0):
			print("Usted obtuvo", str(barajado[i][1])," de ", str(barajado[i][0]))
			historial.append(barajado[i])
			if(pertenece(numeros,barajado[i][1])):
				suma += 1
			else:
				suma = 0.5
			print("Sus cartas suman:", str(suma))
			if (suma>7.5):
				print("Usted se ha pasado.")
				break
			elif(suma ==7.5):
				print("Felicitaciones, ha ganado.")
				break
			else:
				i += 1
				decision = otra_carta()
		if (decision == -1):
			print("Opcion no valida, vuelva a intentarlo.")
			decision = otra_carta()
	if (decision == 1):
		print("Usted ha decidido plantarse")
		print("Sus cartas suman:", str(suma))
	return historial

def perteneceACadaUno(s:list,e)->list:
	res = [False]*len(s)
	for i in range(len(s)):
		res[i] = pertenece(s[i],e)
	return res
def esMatriz(s:list)->bool:
	res:bool = False
	filas = len(s)
	largo_filas = len(s[0])
	if(filas > 0 and largo_filas > 0):
		res = True
		for i in range(filas):
			if len(s[i]) != largo_filas:
				res = False
				break
	return res

def ordenados(s: list)->bool:
	res: bool = True
	if len(s) > 1:
		for i in range(2, len(s)):
			if (s[i] <= s[i-1]):
				res = False
				break
	return res

def filasOrdenadas(m: list)->list:
	res = [False]*len(m)
	for i in range(len(m)):
		res[i] = ordenados(m[i])
	return res

def multiplicar_matrices(matriz1: list, matriz2:list)->list:
	filas = len(matriz1)
	columnas = len(matriz2[0])
	iterador = len(matriz1[0])
	res = [[0 for x in range(columnas)] for y in range(filas)]
	for i in range(filas):
		for j in range(columnas):
			for k in range(iterador):
					res[i][j] += matriz1[i][k]*matriz2[k][j]
	return res

def matriz_identidad(dim: int)->list:
	res = [[0 for x in range(dim)] for y in range(dim)]
	for i in range(dim):
		res[i][i] = 1
	return res

def matriz_a_la_p(matriz: list, p: int)->list:
	dimension = len(matriz)
	res = matriz_identidad(dimension)
#	res = np.identity(dimension)
	for i in range(p):
		res = multiplicar_matrices(res, matriz)
#		res = np.matmul(res,matriz)
	return res

def matriz_random_a_la_p(d: int,p: int)->list:
	m = np.random.random((d,d))
	print(m)
	res = matriz_a_la_p(m,p)
	return res


matriz_rect1 = [[1,1,1],[2,2,2]]
matriz_rect2 = [[1,2],[1,2],[1,2]]
matriz4 = [[2,2,2],[2,2,2],[2,2,2]]
matriz5 = [[.1]*3]*3
matriz3=[[1,2,3],[4,5,6],[7,8,8]]
notas2 = [4,4,5,4]
notas1 = [7,8,9,7]
notas3 = [4,4,3,4]
lista1 = [1,2,3] 
arreglo1 = array('q', lista1)
lista2 = [3,9,27]
lista3 = [1,2,1,3]
matriz1 = [notas1,notas2,notas3]
matriz2 = [lista1,lista2,lista3]
palabra4 = "inocular"
palabra5 = "subrepticio"
palabra6 = "soda"
movimientos1 = [('I',2000),('R',20),('R',1000),('I',300)]	
password1 = "Alma"
password2 = "Bono12345"
password3 = "Chaja"
palabra1 = "neuquen"
palabra2 = "2002"
palabra3 = "neuqueN"
lista4 = ['perejil', 'albahaca', 'tomillo']
lista5 = ['pera', 'banana', 'kiwi']

#print(matriz_random_a_la_p(30,10))
#print(matriz_a_la_p(matriz5,3))
print(multiplicar_matrices(matriz_rect1,matriz_rect2))
print(filasOrdenadas(matriz3))
print(esMatriz(matriz2))
print(perteneceACadaUno(matriz1,9))
#print(siete_y_medio())
#print(monedero())
#print(lista_nombres())
print(aprobado(notas2))
print(eliminarRepetidos(palabra1))
print(darVueltaStr(palabra6))
print(reemplazaVocales(palabra4))
print(borra_pos_pares(lista3))
print(lista3)
print(tiene_3_vocales(palabra5))
print(saldo_actual(movimientos1))
print(fortaleza_password(password2))
print(es_palindromo(palabra1))
print(tiene_palabra_mas_larga_que(lista4))
print(ordenados2(lista3))
print(sumaTotal(lista1))
print(divideATodos(lista2,3))
print(pertenece3(arreglo1,4))
print(pertenece4("Agustin", 'i'))
print(pertenece4("Agustin", 'k'))
