import re
from itertools import *
from pprint import pprint
from prettytable import PrettyTable
import numpy as np
from prueba import *

# Crea todas las posibles tablas iniciales
def CreateInitialTables(printTables=False):
	allTables = list()
	initialTable = PrettyTable()

	initialTable.field_names = ['P', '-P']
	productsList = list(product([0,1,2],repeat=3))

	for combination in productsList:
		initialTable.clear_rows()
		initialMat = np.zeros((3,2))
		initialMat[0][0] = 0
		initialMat[1][0] = 1
		initialMat[2][0] = 2

		for i in range(3):
			initialMat[i][1] = combination[i]
			initialTable.add_row([i, combination[i]])

		# Se imprime la tabla inicial luego de crearla
		if printTables:
			print('='*30)
			print(initialTable)

		allTables.append(initialMat)

	return allTables


# Crea una lista de listas que contiene todas las posibles combinaciones
# de 9 dígitos con un los números 0, 1 y 2
def GetList(initialNumber, showProcess=False):
	values = [3**8, 3**7, 3**6, 3**5, 3**4 ,3**3, 3**2, 3**1 ,3**0]
	lst = [0,0,0,0,0,0,0,0,0]

	counter = 0
	lstCounter = 0

	while initialNumber >= 1:
		currentValue = values[counter]

		string = """
		valor: {}
		numero: {}
		division: {}
		================================
		""".format(currentValue, initialNumber, initialNumber/currentValue)

		if showProcess: print(string) 

		if initialNumber/currentValue < 1:
			lstCounter += 1
			counter += 1
		else:
			lst[lstCounter] += 1
			initialNumber -= currentValue

	return lst


# Crea la impliación dado una tabla inicial, un valor de p, q
# y la matriz de valores
def CreateImplication(p, q, mat, table):

	nP = table[p][1]

	for i in mat:
		if i[0] == nP and i[1] == q:
			return i[2]


def ListFinalValue(lista):
	if all(x == 0 for x in lista):
		return 0
	if all(x == 1 for x in lista):
		return 1
	if all(x == 2 for x in lista):
		return 2
	else:
		return 10


def GetAxioms():
	axiomas = ['((AvA)>A)','(A>(AvB))','((AvB)>(BvA))','((A>B)>((CvA)>(CvB)))']
	return axiomas


def CheckDependency(lista):
	axiomaEvaluado = lista.pop()
	result = lista[0]
	# print(lista, axiomaEvaluado)
	if all(x == result for x in lista) and axiomaEvaluado != result:
		return True
	else:
		return False



# Genera todas las posibles combinaciones de tablas y matrices
def GetCombinations(tablesList, listValues, newAxiom):

	mat = []
	axiomas = GetAxioms()
	axiomas.append(newAxiom)
	print(axiomas)

	for table in tablesList:

		for lst in listValues:

			cont = 0
			for i in range(3):
				for j in range(3):

					pvq = lst[cont]
					arreglo = [i, j, pvq]
					mat.append(arreglo)
					cont += 1

			mat2 = []
			representaciones = []

			for i in mat:
				p = i[0]
				q = i[1]
				piq = CreateImplication(p, q, mat, table)
				i.append(piq)
				mat2.append(i)

			# pprint(table)
			# pprint(mat2)

			mat = []

			for axioma in axiomas:
				a = Arbol()
				resultado = a.interpretarEcuacion(axioma, mat2, table)
				resultadoRep = ListFinalValue(resultado)
				representaciones.append(resultadoRep)

			# pprint(representaciones)
			# print('='*30)

			if CheckDependency(representaciones):
				print("\nESTA FUNCIONAAA:\n")
				print("tabla inicial: ")
				pprint(table)
				print("\n\nTabla grande: ")
				pprint(mat2)
				print('='*60)
				break

