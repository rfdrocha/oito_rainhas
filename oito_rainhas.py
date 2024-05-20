from random import randint
import numpy as np

# cria um indivíduo (tabuleiro) aleatório
def individuo_aleatorio():
    # retorna um individuo aleatorio
    individuo = np.array([[randint(1,8),randint(1,8),randint(1,8),randint(1,8),randint(1,8),randint(1,8),randint(1,8),randint(1,8)]])
    return individuo

# cria uma populacao com 'n' individuos
def criar_populacao(n):
    # Cria uma populacao com n individuos
    populacao = np.empty((0,8),int)
    for i in range(0,n):
        populacao = np.append(populacao,individuo_aleatorio(),axis=0)

    return populacao

# retorna um vetor com os numeros de rainhas nao atacantes para cada individuo da populacao
def fitness(populacao):
    n = len(populacao)
    fitness = np.zeros(n,dtype=int)
    for i in range(0,n):
        fitness[i] = nao_atacantes(populacao[i])
    
    return fitness

# retorna a quantidade de pares de rainhas não atacantes de uma populacao
def nao_atacantes(individuo):
    contador = 0 # contador de pares nao atacantes
    
    for i in range(0,8):
        for j in range(i+1,8):
            atacantes = False
            
            # testando se as rainhas são atacantes ou não
            # atacantes podem estar na mesma linha ou mesma coluna
            if(individuo[i] == individuo[j]):
                # Rainhas na mesma horizontal -> são atacantes
                atacantes = True
            
            elif(individuo[i] - individuo[j] == i-j or individuo[i] - individuo[j] == j-i):
                # Rainhas na mesma diagonal -> são atacantes
                atacantes = True

            if(not atacantes):
               # caso não sejam atacantes, somar um ao contador
               contador += 1
    
    return contador

# utilizada no crossover da populacao
def crossover(i1,i2):
    # realiza o crossover entre dois individuos
    corte = randint(1,7)
    new_i1 = np.empty((0,8),int)
    new_i1 = np.append(new_i1,i1[:corte])
    new_i1 = np.append(new_i1,i2[corte:])

    new_i2 = np.empty((0,8),int)
    new_i2 = np.append(new_i2,i2[:corte])
    new_i2 = np.append(new_i2,i1[corte:])

    #possibilidade ou não de ocorrer mutação
    prob = 0.5 # 50% de chance de ocorrer a mutação

    # mutacao do primeiro descendente
    if (np.random.choice([True,False],size=1,p=[prob,1-prob])[0]):
        indice = randint(0,7)
        posicao = randint(1,8)
        new_i1[indice] = posicao

    # mutacao do segundo descendente
    if (np.random.choice([True,False],size=1,p=[prob,1-prob])[0]):
        indice = randint(0,7)
        posicao = randint(1,8)
        new_i2[indice] = posicao

    # retorna os dois individuos após o crossover
    return [new_i1,new_i2]

# realiza o crossover entre os individuos da populacao
def crossover_populacao(populacao):
    # Tarefas dessa função:
    # - receber uma população
    # - seleciona os indivíduos para o crossover segundo a funcao fitness
    # - atualiza e retorna a nova geracao da população

    nova_populacao = populacao
    # retorna uma nova populacao após realizar o crossover
    probabilidades = fitness(populacao)
    soma = probabilidades.sum()
    probabilidades = probabilidades/soma #vertor com os probabilidades para o crossover


    # escolha ponderada de individuos da populacao
    escolhas = np.random.choice(range(0,len(populacao)),size=len(populacao),p=probabilidades)
    individuos_escolhidos = populacao[escolhas]

    # realizando o crossover entre dois individuos
    for i in range(0,int(len(populacao)/2)):
        [nova_populacao[2*i],nova_populacao[2*i+1]] = crossover(individuos_escolhidos[2*i],individuos_escolhidos[2*i+1])

    return nova_populacao

# verifica se o problema foi resolvido, ou seja, se numero de pares não atacantes é igual a 28
def resolvido(populacao):
    resolvido = False
    individuo_resolvido = np.array([])

    # retorna True caso algum individuo tenha resolvido o problema e retorna o próprio indivídio
    for individuo in populacao:
        if(nao_atacantes(individuo) == 28):
            resolvido = True
            individuo_resolvido = individuo

    return [resolvido,individuo_resolvido]
            

## INICIO DO ALGORITMO

# Criando matriz com a populacao
num_populacao = 100                        # Esse numero necessariamente deve ser PAR para poder realizar o crossover
populacao = criar_populacao(num_populacao) # matriz com a população em seu estado atual
resposta = np.array([])                    # receberá a resposta do teste se o algoritmo terminou ou não
terminou = False                           # flag para verificar se foi encontrada uma solução


# verificando se ao criar a populacao, o problema já está resolvido
[terminou,resposta] = resolvido(populacao)
geracao = 0                                # contador da geracao da populacao


# Caso a primeira populacao aleatoria não solucione, continuar com o crossover até encontrar uma solução
# Continua tentando resolver o problema enquando não estiver encontrado uma soluçao
while (terminou == False):

    # Atualizando populacao
    populacao = crossover_populacao(populacao)
    geracao += 1

    # Imprimindo o numero da geração atual
    print(f"Geracao atual: {geracao}")
    [terminou,resposta] = resolvido(populacao)


# Ao sair do loop while, significa que terminou == True, portanto o problema foi resolvido
print(f"Uma das solucoes para o problema das 8 rainhas é: {resposta}")