import random as ran
import operator as oper
import csv
import math



def dividir_dados(doc, proporcao):
	lista_treino = []
	lista_teste = []

	with open(doc, 'r') as csv_doc:
		lista_dados = list(csv.reader(csv_doc))

		for i in range(len(lista_dados)):
			for j in range(len(lista_dados[0])-1):
				lista_dados[i][j] = float(lista_dados[i][j])
			
			if ran.random() <= proporcao:
				lista_treino.append(lista_dados[i])
			else:
				lista_teste.append(lista_dados[i])

	return (lista_treino, lista_teste)


def distancia_euclidiana(p1, p2):
	distancia = 0

	for i in range(len(p2)-1):
		distancia += pow((float(p1[i]) - float(p2[i])), 2)

	return (math.sqrt(distancia))


def achar_vizinhos(lista_treino, instancia_teste, k):
	distancias = []

	for i in range(len(lista_treino)):
		dist_euclidiana = distancia_euclidiana(instancia_teste, lista_treino[i])
		distancias.append((lista_treino[i], dist_euclidiana))

	distancias.sort(key=oper.itemgetter(1))
	vizinhos = []

	for i in range(k):
		vizinhos.append(distancias[i][0])

	return (vizinhos)


def decidir(vizinhos):
	classifica = {}

	for i in range(len(vizinhos)):
		retorno = vizinhos[i][-1]

		if retorno in classifica:
			classifica[retorno] += 1
		else:
			classifica[retorno] = 1

	classif_organizados = sorted(classifica.items(), key=oper.itemgetter(1), reverse=True)

	return (classif_organizados[0][0])


def correto(lista_teste, predicao):
	certo = 0

	for i in range(len(lista_teste)):
		if lista_teste[i][-1] in predicao[i]:
			certo += 1

	return (certo)




proporcao = 0.7
dataset = "datasets/dataset1.txt"
lista_treino,lista_teste = dividir_dados(dataset, proporcao)
predicao = []
k = 1

for i in range(len(lista_teste)):
	vizinhos = achar_vizinhos(lista_treino, lista_teste[i], k)
	resultado = decidir(vizinhos)
	predicao.append(resultado)

certo = correto(lista_teste, predicao)
acuracia = ((certo/float(len(lista_teste)))*100)

print("O dataset usado é", dataset)
print ("O conjunto de treino tem", (len(lista_treino)), "dados.")
print ("O conjunto de teste tem", (len(lista_teste)), "dados.")
print("O conjunto de dados tem", (lista_teste[i][-1]), "classes.")
print("A proporção de divisão entre treino e teste é de", proporcao)
print("O k usado nesse teste é", k)
print("O número de dados corretos foi de", certo, "do total de", (len(lista_teste)), "do conjunto de teste.")
print("A acurácia desse teste é de", acuracia, "%.")
