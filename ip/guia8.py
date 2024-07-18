from queue import LifoQueue
from queue import Queue
from random import *

def clonar_sin_comentarios(nom_archivo : str):
	archivo = open(nom_archivo, "r", encoding='utf8')
	lineas = archivo.readlines()
	lineas_nuevo:list = []
	for linea in lineas:
		i = 0
		while linea[i] == " ":
			i += 1
		if i == len(linea) or linea[i] != "#":
			lineas_nuevo.append(linea)
	archivo.close()
	nom_archivo_escritura = "sin-comentarios-" + nom_archivo
	destino = open(nom_archivo_escritura, "w", encoding='utf8')
	destino.truncate()
	for linea_nueva in lineas_nuevo:
		destino.write(linea_nueva)
	destino.close()

def leer_palabras_binario(nom_archivo : str)->list:
	res:[str] = []
	caracteres_legibles = "0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ _"
	with open(nom_archivo, "rb") as archivo:
		caracter = archivo.read(1)
		while(caracter != b''):
			while(caracter in caracteres_legibles):
				palabra += caracter
				caracter = archivo.read(1)
			res.append(palabra)
			palabra:str = ""
			caracter = archivo.read(1)
			print(palabra)
	return res

def promedioEstudiante(lu:str,nom_archivo)->float:
	with open(nom_archivo, "r", encoding='utf8') as archivo:
		res:float = 0
		lineas = archivo.readlines()
		base:list = []
		for linea in lineas:
			renglon:list = ['']*4
			i=0
			for j in range(len(renglon)):
				while(i < len(linea) and linea[i]!='\n' and linea[i]!=','):
					renglon[j] += linea[i]
					i += 1
				i+=1
			base.append(renglon)
		notas:list = []
		for i in range(len(base)):
			if base[i][0] == lu:
				notas.append(float(base[i][3]))
		res = sum(notas)/len(notas)
		return res

def agregar_frase_final(nom_archivo : str, frase:str):
	with open(nom_archivo, "r+", encoding='utf8') as archivo:
		archivo.seek(0, 2)
		archivo.write(frase)

def agregar_frase_principio(nom_archivo : str, frase:str):
	with open(nom_archivo, "r+", encoding='utf8') as archivo:
		lineas = archivo.readlines()
		archivo.seek(0)
		archivo.write(frase)
		for linea in lineas:
			archivo.write(linea)

def reverso(nom_archivo : str):
	archivo = open(nom_archivo, "r", encoding='utf8')
	lineas = archivo.readlines()
	lineas = lineas[::-1]
	archivo.close()
	nom_archivo_escritura = "reverso-" + nom_archivo
	destino = open(nom_archivo_escritura, "w", encoding='utf8')
	destino.truncate()
	for linea in lineas:
		destino.write(linea)
	destino.close()

def contar_lineas(nombre_archivo:str):
	res:int = 0
	archivo = open(nombre_archivo, "r", encoding='utf8')
	lineas = archivo.readlines()			
	res = len(lineas)
	return res

def existe_palabra(palabra:str, nom_archivo:str)->bool:
	res:bool = False
	archivo = open(nom_archivo, "r", encoding='utf8')
	lineas = archivo.readlines()
	for linea in lineas:
		if (palabra in linea.split()):
			res = True
	return res

def cantidad_apariciones(nom_archivo:str, palabra:str)->int:
	res:int = 0
	archivo = open(nom_archivo, "r", encoding='utf8')
	lineas = archivo.readlines()
	for linea in lineas:
		if (palabra in linea.split()):
			res += 1
	return res

def buscar_el_maximo_pila(p: LifoQueue)->int:
	pila = LifoQueue()
	res=p.get()
	pila.put(res)
	while p.empty() == False:
		valor = p.get()
		pila.put(valor)
		if (valor>=res):
			res = valor
	while pila.empty() == False:
		p.put(pila.get())
	return res

def esta_bien_balanceada(formula:str)->bool:
	res:bool = False
	digitos:str = "0123456789"
	operaciones:str = "+-x/"
	parentesis_abre = "("
	parentesis_cierra = ")"
	parentesis:str = parentesis_abre + parentesis_cierra
	espacios:str = " "
	delimitadores:str = operaciones + parentesis
	expresion:list = []
	identificadores:list = []
	fragmento:list = []
	for i in range(len(formula)):
		if formula[i] in digitos:
			fragmento.append(formula[i])
		if formula[i] in delimitadores:
			if (len(fragmento)>0):
				numero = ''.join(fragmento)
				fragmento = []
				expresion.append(numero)
				identificadores.append("num")
			expresion.append(formula[i])
			if formula[i] in operaciones:
				identificadores.append("op")
			if formula[i] in parentesis:
				if formula[i] == parentesis_abre:
					identificadores.append("abrepar")
				else:
					identificadores.append("cierrapar")
	print(expresion,identificadores)

def evaluar_expresion(formula:str)->float:
	res:float = 0
	digitos:str = "0123456789"
	coma:str = "."
	digitosocoma = digitos + coma
	operaciones:str = "+-*/"
	espacios:str = " "
	delimitadores:str = operaciones + espacios
	expresion:list = []
	identificadores:list = []
	fragmento:list = []
	for i in range(len(formula)):
		if formula[i] in digitosocoma:
			fragmento.append(formula[i])
		if formula[i] in delimitadores:
			if (len(fragmento)>0):
				numero = ''.join(fragmento)
				fragmento = []
				expresion.append(numero)
				identificadores.append("num")
			if formula[i] in operaciones:
				expresion.append(formula[i])
				identificadores.append("op")
	pila = LifoQueue()
	for j in range(len(expresion)):
		if identificadores[j] == "op":
			valor2 = pila.get()
			valor1 = pila.get()
			if expresion[j] == '+':
				pila.put(valor1 + valor2)
			elif expresion[j] == '-':
				pila.put(valor1 - valor2)
			elif expresion[j] == '*':
				pila.put(valor1 * valor2)
			elif expresion[j] == '/':
				pila.put(valor1 / valor2)
		if identificadores[j] == "num":
			pila.put(float(expresion[j]))
	res = pila.get()
	return res

def buscar_el_maximo_cola(c:Queue)-> int:
	q = Queue()
	res:int = c.get()
	q.put(res)
	while not c.empty():
		valor = c.get()
		q.put(valor)
		if valor > res:
			res = valor
	while not q.empty():
		c.put(q.get())
	return res

def armar_secuencia_de_bingo() -> Queue:
	res = Queue()
	enteros = [i for i in range(100)]
	#random.shuffle(enteros)
	secuencia = sample(enteros, k=len(enteros))
	#print(secuencia)
	for bolilla in secuencia:
		res.put(bolilla)
	return res

def jugar_carton_de_bingo(carton: list[int], bolillero: Queue):
	res:int = 0
	bolillas_sacadas = Queue()
	carton_tachable = carton.copy()
	while len(carton_tachable) != 0:
		bolilla_actual = bolillero.get()
		res += 1
		#print("bolilla",bolilla_actual)
		bolillas_sacadas.put(bolilla_actual)
		if bolilla_actual in carton_tachable:
			carton_tachable.remove(bolilla_actual)
			#print("res:",res)
	while not bolillero.empty():
		bolillas_sacadas.put(bolillero.get())
	while not bolillas_sacadas.empty():
		bolillero.put(bolillas_sacadas.get())
	return res

def n_pacientes_urgentes(cola: Queue)->int:
	res:int = 0
	cola_vaciado = Queue()
	while not cola.empty():
		tupla = cola.get()
		if tupla[0]<=3:
			res += 1
		cola_vaciado.put(tupla)
	while not cola_vaciado.empty():
		cola.put(cola_vaciado.get())
	return res

def atencion_a_clientes(cola: Queue()) -> Queue():
	cola_prioridad = Queue()
	cola_preferencial = Queue()
	cola_comun = Queue()
	res = Queue()
	while not cola.empty():
		tupla = cola.get()
		if tupla[3] == True:
			cola_prioridad.put(tupla)
		elif tupla[2] == True:
			cola_preferencial.put(tupla)
		else:
			cola_comun.put(tupla)
	while not cola_prioridad.empty():
		res.put(cola_prioridad.get())
	while not cola_preferencial.empty():
		res.put(cola_preferencial.get())
	while not cola_comun.empty():
		res.put(cola_comun.get())
	return res

def agrupar_por_longitud(nom_archivo: str) -> dict:
	archivo = open(nom_archivo, "r", encoding='utf8')
	res:dict = {}
	for linea in archivo.readlines():
		palabras = linea.split()
		for palabra in palabras:
			if len(palabra) not in res:
				res[len(palabra)] = 1
			else:
				res[len(palabra)] += 1
	archivo.close()
	return res

def promediosEstudiantes(nom_archivo)->float:
	res:dict = {}
	with open(nom_archivo, "r", encoding='utf8') as archivo:
		lineas = archivo.readlines()
	base:list = []
	for linea in lineas:
		renglon:list = linea.rstrip().split(',', maxsplit=4)
		base.append(renglon)
	dict_suma = {}
	dict_conteo = {}
	for i in range(len(base)):
		if base[i][0] not in dict_suma:
			dict_suma[base[i][0]] = float(base[i][3])
			dict_conteo[base[i][0]] = 1
		else:
			dict_suma[base[i][0]] += float(base[i][3])
			dict_conteo[base[i][0]] += 1
	for key in dict_suma:
		res[key] = dict_suma[key]/dict_conteo[key]
	return res

def la_palabra_mas_frecuente(nom_archivo: str) -> str:
	with open(nom_archivo, "r", encoding='utf8') as archivo:
		lineas = archivo.readlines()
	dic_palabras = {}
	for linea in lineas:
		palabras = linea.split()
		for palabra in palabras:
			if palabra not in dic_palabras:
				dic_palabras[palabra] = 1
			else:
				dic_palabras[palabra] += 1
	res = max(dic_palabras, key=dic_palabras.get)
	return res

def visitar_sitio(historiales:dict, usuario:str, sitio:str):
	historiales[usuario][0].put(sitio)
	while not historiales[usuario][1].empty():
		historiales[usuario][1].get()

def navegar_atras(historiales:dict, usuario:str)->str:
	if not historiales[usuario][0].empty():
		res:str = historiales[usuario][0].get()
		historiales[usuario][1].put(res)
		return res

def navegar_adelante(historiales:dict, usuario:str)->str:
	if not historiales[usuario][1].empty():
		res:str = historiales[usuario][1].get()
		historiales[usuario][0].put(res)
		return res


def agregar_producto(inventario:dict, nombre:str, precio:float, cantidad:int):
	producto:dict = {}
	producto['nombre']= nombre
	producto['precio']= precio
	producto['cantidad']= cantidad
	if nombre not in inventario:
		inventario[nombre] = producto
	
def actualizar_stock(inventario:dict, nombre:str, cantidad:int):
	if nombre in inventario:
		inventario[nombre]["cantidad"] = cantidad

def actualizar_precios(inventario:dict, nombre:str, precio:float):
	if nombre in inventario:
		inventario[nombre]["precio"] = precio

def calcular_valor_inventario(inventario):
	res:float = 0
	for nombre in inventario:
		res += inventario[nombre]["precio"]*inventario[nombre]["cantidad"]
	return res

inventario = {}
agregar_producto(inventario, "Camisa", 20.0, 50)
agregar_producto(inventario, "Pantalón", 30.0, 30)
actualizar_stock(inventario, "Camisa", 10)
valor_total = calcular_valor_inventario(inventario)
print("Valor total del inventario:", valor_total)


pila_web_vacia1 = LifoQueue()
pila_web_vacia2 = LifoQueue()
pila_web1 = LifoQueue()
pila_web1.put("google.com")
pila_web2 = LifoQueue()
pila_web2.put("yahoo.com")
historiales = {"agustin":(pila_web1,pila_web_vacia1),"miranda":(pila_web2,pila_web_vacia1)}
visitar_sitio(historiales,"agustin","openai.com")
visitar_sitio(historiales,"agustin","python.org")
print(navegar_atras(historiales,"agustin"))
print(navegar_atras(historiales,"agustin"))
print(navegar_atras(historiales,"agustin"))
print(navegar_adelante(historiales,"agustin"))
print(navegar_adelante(historiales,"agustin"))
nombre_texto_palabras = "texto.txt"
print(existe_palabra("gliptodonte",nombre_texto_palabras))
diccionario = agrupar_por_longitud(nombre_texto_palabras)
print(diccionario)
print(promediosEstudiantes("notas.csv"))
print(la_palabra_mas_frecuente(nombre_texto_palabras))

pila = LifoQueue()
pila.put(1)
pila.put(2)
pila.put(3)
pila.put(2)
pila.put(1)
pila.put(-1)

cola = Queue()
cola.put(1)
cola.put(2)
cola.put(3)
cola.put(2)
cola.put(1)
cola.put(-1)

cola_hosp = Queue()
cola_hosp.put((1,"joaquin","otorrino"))
cola_hosp.put((2,"romina","gastro"))
cola_hosp.put((4,"alberto","dermato"))
cola_hosp.put((5,"florencia","oftalmo"))
print(n_pacientes_urgentes(cola_hosp))
#while not cola_hosp.empty(): print(cola_hosp.get())

cola_banco = Queue()
cola_banco.put(("Agustin H.",31602893,False,False))
cola_banco.put(("Ramon G.",44672872,False,False))
cola_banco.put(("Elizabeth R.",21903876,True,False))
cola_banco.put(("Barbara C.",7543286,False,True))
cola_procesada = atencion_a_clientes(cola_banco)
#while not cola_procesada.empty(): print(cola_procesada.get())


enteros = [i for i in range(100)]
carton = sample(enteros, k=12)
#print(carton)
cola_bingo = armar_secuencia_de_bingo()
print(jugar_carton_de_bingo(carton, cola_bingo))
#while not cola_bingo.empty():
#	print(cola_bingo.get())
print(buscar_el_maximo_pila(pila))
print(buscar_el_maximo_cola(cola))
print(cola.get())

print(evaluar_expresion("3 4 + 5 * 2 -"))
#esta_bien_balanceada("1 + (2 x 3 - (20 / 5))")
print(promedioEstudiante("609","notas.csv"))
#leer_palabras_binario("codigo.zip")
#agregar_frase_principio("archivo_frases.txt","frase agregada al principio!")
#agregar_frase_final("archivo_frases.txt","frase agregada al final!")
reverso("archivo_reverso.txt")
clonar_sin_comentarios("archivo_comentarios.txt")


