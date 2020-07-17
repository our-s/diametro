import matplotlib.pyplot as plt
import time

class Grafo(object):
    def __init__(grafo, path=''):
        grafo._adj = []
        grafo._aresta = 0
        grafo._vertice = 1
 
        for i in range(grafo._vertice):
            grafo._adj.append([])

        else:
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
        self._edgeTo = []
        self._bandeira = []
        self._vertice = vertice

        for i in range(Grafo.obterVertice()):
            self._bandeira.append(False)
            self._edgeTo.append(0)
        
        self._buscaEmLargura(Grafo, self.__vertice)

    
    def _buscaEmLargura(self, Grafo, vertice_original):
        fila = Fila()
        self._bandeira[vertice_original] = True
        fila.enfileira(vertice_original)

        while not fila.estaVazio():
            vertice = fila.desenfileira()
            for i in Grafo.obterAdj(vertice):
                if not self._bandeira[i]:
                    self._edgeTo[i] = vertice
                    self._bandeira[i] = True
                    fila.enfileira(i)

    def caminho(self, vertice):
        pilha = Pilha()
        x = vertice
        if not self._bandeira[vertice]:
            return []
        
        while x != self._vertice: 
            pilha.empilha(x)
            x = self._edgeTo[x]
            
        pilha.empilha(self._vertice)
        return pilha

if __name__ == "__main__":
    inicio = time.time()
    dicionario = {}
    dicionarioOrdenado = {}
    soma = 0
    pesos = 0
    
    grafo = Grafo('traducao3.txt')

    for i in range(grafo.obterVertice()):
        buscaEmLargura = BuscaEmLargura(grafo, i)
        for j in range(grafo.obterVertice()):
            if i != j: 
                pilha = buscaEmLargura.caminho(j)
                if pilha != []:
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
    print(f'Diâmetro médio: {media}')
    
    eixo_x = dicionarioOrdenado.keys()

    plt.bar(x=[i for i in range(1, len(eixo_x) + 1)], height = dicionarioOrdenado.values())
    plt.xticks([i for i in range(1, len(eixo_x) + 1)], labels = eixo_x)
    plt.grid(axis = 'y', alpha = 0.5)
    plt.title("Quantidade de distâncias entre pares de nós")
    plt.xlabel("Distância")
    plt.ylabel("Quantidade")    

    print("Tempo de execução:" %(fim-inicio))
