import matplotlib.pyplot as plt
import time

class Grafo(object):
    def __init__(grafo, path=''):
        grafo._adj = []
        grafo._aresta = 0
        grafo._vertice = 1
 
        for i in range(grafo._vertice):
            grafo._adj.append([])

        with open(path, 'r') as arquivo:
            grafo._vertice = int(arquivo.readline().rstrip('\n'))
            for v in range(grafo._vertice):
                grafo._adj.append([])
            grafo._aresta = int(arquivo.readline().rstrip('\n'))

            for i in range(grafo._aresta):
                linha = arquivo.readline().rstrip('\n')
                a, b = linha.split()
                grafo._adj[int(a)].append(int(b))
                grafo._adj[int(b)].append(int(a))
                    
    def obterVertice(grafo):
        return grafo._vertice

    def obterAdj(grafo, v):
        return grafo._adj[v]

class Fila(object):
    def __init__(fila):
        fila.items = []

    def estaVazio(fila):
        return fila.items == []

    def enfileira(fila, item):
        fila.items.insert(0, item)

    def desenfileira(fila):
        return fila.items.pop()

class Pilha(object):
    def __init__(pilha):
        pilha.items = []

    def empilha(pilha, item):
        pilha.items.append(item)

    def tamanho(pilha):
        return len(pilha.items)

class BuscaEmLargura(object):
    def __init__(self, Grafo, vertice):
        self._nos = []
        self._bandeira = []
        self._vertice = vertice

        for i in range(Grafo.obterVertice()):
            self._bandeira.append(False)
            self._nos.append(0)       
        self.buscaEmLargura(Grafo, self._vertice)
   
    def buscaEmLargura(self, Grafo, vertice_original):
        fila = Fila()
        self._bandeira[vertice_original] = True
        fila.enfileira(vertice_original)

        while not fila.estaVazio():
            vertice = fila.desenfileira()
            for i in Grafo.obterAdj(vertice):
                if not self._bandeira[i]:
                    self._nos[i] = vertice
                    self._bandeira[i] = True
                    fila.enfileira(i)

    def caminho(self, vertice):
        pilha = Pilha()
        vert = vertice
        
        if self._bandeira[vertice]:
            while vert != self._vertice: 
                pilha.empilha(vert)
                vert = self._nos[vert]    
            pilha.empilha(self._vertice)
            return pilha
        else:
            return []

if __name__ == "__main__":
    inicio = time.time()
    dicionario = {}
    dicionarioOrdenado = {}
    soma = 0
    pesos = 0
    grafo = Grafo('traducao3.txt')
    vertice = grafo.obterVertice()

    for i in range(vertice):
        buscaEmLargura = BuscaEmLargura(grafo, i)
        for j in range(vertice):
            if i == j: 
                break
            else:
                pilha = buscaEmLargura.caminho(j)
                if pilha == []:
                    break
                else:
                    distancia = pilha.tamanho() - 1
                    if distancia in dicionario.keys():
                        dicionario[distancia] = 1 + dicionario[distancia] 
                    else:
                        dicionario[distancia] = 1                        
    chaves = sorted(dicionario)  
    
    for i in chaves:
        dicionarioOrdenado[i] = int(dicionario[i] / 2)
        soma = (i * dicionarioOrdenado[i]) + soma
        pesos = dicionarioOrdenado[i] + pesos
    media = soma / pesos
    fim = time.time()
    print("Diâmetro médio: {:.2f}".format(media))

    plt.bar(x=[i for i in range(1, len(dicionarioOrdenado.keys()) + 1)], height = dicionarioOrdenado.values())
    plt.xticks([i for i in range(1, len(dicionarioOrdenado.keys()) + 1)], labels = dicionarioOrdenado.keys())
    plt.grid(axis = 'y', alpha = 0.5)
    plt.title("Histograma das distâncias entre pares de nós")
    plt.xlabel("Distância")
    plt.ylabel("Quantidade")  
    plt.savefig('Gráfico.png')
    
    print("Tempo de execução: {:.2f} segundos".format(fim-inicio))