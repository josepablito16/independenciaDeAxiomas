from funciones import *
from pprint import pprint

def main():
	tablas = CreateInitialTables()
	listas = list()
	for i in range(0,3**9):
		listas.append(GetList(i))

	GetCombinations(tablas, listas,'((A-0)>(A>B))')

if __name__ == '__main__':
	main()
	exit()
