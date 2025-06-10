import random

###############################################################################
#                               Caixas binárias                               #
###############################################################################


def gene_cb():
    """Sorteia um valor para uma caixa no problema das caixas binárias"""
    valores_possiveis = [0, 1]
    gene = random.choice(valores_possiveis)
    return gene


def cria_candidato_cb(n):
    """Cria uma lista com n valores zero ou um.

    Args:
      n: inteiro que representa o número de caixas.

    """
    candidato = []
    for _ in range(n):
        gene = gene_cb()
        candidato.append(gene)
    return candidato


def populacao_cb(tamanho, n):
    """Cria uma população para o problema das caixas binárias.

    Args:
      tamanho: tamanho da população
      n: inteiro que representa o número de caixas de cada indivíduo.

    """
    populacao = []
    for _ in range(tamanho):
        populacao.append(cria_candidato_cb(n))
    return populacao


def funcao_objetivo_cb(candidato):
    """Computa a função objetivo no problema das caixas binárias

    Args:
      candidato: uma lista contendo os valores das caixas binárias do problema

    """
    return sum(candidato)


def funcao_objetivo_pop_cb(populacao):
    """Computa a função objetivo para uma população no problema das caixas binárias

    Args:
      populacao: lista contendo os individuos do problema

    """
    fitness = []
    for individuo in populacao:
        fitness.append(funcao_objetivo_cb(individuo))
    return fitness


###############################################################################
#                             Caixas não-binárias                             #
###############################################################################


def gene_cnb(valor_max):
    """Sorteia um valor para uma caixa no problema das caixas não-binárias"""
    valores_possiveis = range(valor_max + 1)
    gene = random.choice(valores_possiveis)
    return gene


def cria_candidato_cnb(n, valor_max):
    """Cria uma lista com n valores entre zero e valor_max.

    Args:
      n: inteiro que representa o número de caixas.
      valor_max: inteiro represtando o valor máximo das caixas
    """
    candidato = []
    for _ in range(n):
        gene = gene_cnb(valor_max)
        candidato.append(gene)
    return candidato


def populacao_cnb(tamanho, n, valor_max):
    """Cria uma população para o problema das caixas não-binárias.

    Args:
      tamanho: tamanho da população
      n: inteiro que representa o número de caixas de cada indivíduo.
      valor_max: inteiro represtando o valor máximo das caixas

    """
    populacao = []
    for _ in range(tamanho):
        populacao.append(cria_candidato_cnb(n, valor_max))
    return populacao


def funcao_objetivo_cnb(candidato):
    """Computa a função objetivo no problema das caixas não-binárias

    Args:
      candidato: uma lista contendo os valores das caixas não-binárias do problema

    """
    return sum(candidato)


def funcao_objetivo_pop_cnb(populacao):
    """Computa a função objetivo para uma população no problema das caixas não-binárias

    Args:
      populacao: lista contendo os individuos do problema

    """
    fitness = []
    for individuo in populacao:
        fitness.append(funcao_objetivo_cnb(individuo))
    return fitness


###############################################################################
#                                    Senha                                    #
###############################################################################


def gene_senha(letras_possiveis):
    """Sorteia uma letra.

    Args:
      letras: letras possíveis de serem sorteadas.

    """
    letra = random.choice(letras_possiveis)
    return letra


def cria_candidato_senha(tamanho_senha, letras_possiveis):
    """Cria um candidato para o problema da senha

    Args:
      tamanho_senha: inteiro representando o tamanho da senha.
      letras_possiveis: letras possíveis de serem sorteadas.

    """
    candidato = []

    for _ in range(tamanho_senha):
        candidato.append(gene_senha(letras_possiveis))

    return candidato

def populacao_senha(tamanho_populacao, tamanho_senha, letras_possiveis):
    """Cria população inicial no problema da senha

    Args
      tamanho_populacao: tamanho da população.
      tamanho_senha: inteiro representando o tamanho da senha.
      letras_possiveis: letras possíveis de serem sorteadas.

    """
    populacao = []

    for _ in range(tamanho_populacao):
        populacao.append(cria_candidato_senha(tamanho_senha, letras_possiveis))

    return populacao

def populacao_senha_variavel(tamanho_micro_populacao, tamanho_min,tamanho_max, letras_possiveis):
    """Cria população inicial no problema da senha

    Args
      tamanho_micro_populacao: tamanho da micropopulação, onde micropopulação é uma população de mesmo tamanho.
      tamanho_min: inteiro representando o tamanho mínimo da senha.
      tamanho_min: inteiro representando o tamanho máxima da senha.
      letras_possiveis: letras possíveis de serem sorteadas.

    """
    populacao = []
    for i in range (tamanho_min, tamanho_max+1):
        tamanho_senha = i
        for _ in range(tamanho_micro_populacao):
            populacao.append(cria_candidato_senha(tamanho_senha, letras_possiveis))

    return populacao

def funcao_objetivo_senha(candidato, senha_verdadeira):
    """Computa a funcao objetivo de um candidato no problema da senha

    Args:
      candidato: um palpite para a senha que você quer descobrir
      senha_verdadeira: a senha que você está tentando descobrir

    """
    distancia = 0

    for letra_candidato, letra_senha in zip(candidato, senha_verdadeira):
        num_letra_candidato = ord(letra_candidato)
        num_letra_senha = ord(letra_senha)
        distancia += abs(num_letra_candidato - num_letra_senha)

    return distancia

def funcao_objetivo_senha_variavel(candidato, senha_verdadeira):
    """Computa a funcao objetivo de um candidato no problema da senha

    Args:
      candidato: um palpite para a senha que você quer descobrir
      senha_verdadeira: a senha que você está tentando descobrir

    """
    distancia = 0
    candidato_objetivo = candidato.copy()
    senha_verdadeira_objetivo = senha_verdadeira.copy()
    # Preenche a senha verdadeira e o candidato com caracteres nulos para que eles tenham o mesmo tamanho
    if len(candidato_objetivo) < len(senha_verdadeira_objetivo):
        diferenca = len(senha_verdadeira_objetivo) - len(candidato_objetivo)
        for i in range(diferenca):
            candidato_objetivo.append(chr(0))
    elif len(candidato_objetivo) > len(senha_verdadeira_objetivo):
        diferenca = len(candidato_objetivo) - len(senha_verdadeira_objetivo)
        for i in range(diferenca):
            senha_verdadeira_objetivo.append(chr(0))

    for letra_candidato_objetivo, letra_senha in zip(candidato_objetivo, senha_verdadeira_objetivo):
        num_letra_candidato_objetivo = ord(letra_candidato_objetivo)
        num_letra_senha = ord(letra_senha)
        distancia += abs(num_letra_candidato_objetivo - num_letra_senha)

    return distancia

def funcao_objetivo_pop_senha(populacao, senha_verdadeira):
    """Computa a funcao objetivo de uma populaçao no problema da senha.

    Args:
      populacao: lista contendo os individuos do problema
      senha_verdadeira: a senha que você está tentando descobrir

    """
    fitness = []

    for individuo in populacao:
        fitness.append(funcao_objetivo_senha(individuo, senha_verdadeira))

    return fitness

def f_objetivo_pop_senha_variavel(populacao, senha_verdadeira):
    """Computa a funcao objetivo de uma populaçao no problema da senha.

    Args:
      populacao: lista contendo os individuos do problema
      senha_verdadeira: a senha que você está tentando descobrir

    """
    fitness = []

    for individuo in populacao:
        fitness.append(funcao_objetivo_senha_variavel(individuo, senha_verdadeira))

    return fitness


###############################################################################
#                                   Seleção                                   #
###############################################################################


def selecao_roleta_max(populacao, fitness):
    """Realiza seleção da população pela roleta

    Args:
      populacao: lista contendo os individuos do problema
      fitness: lista contendo os valores computados da funcao objetivo

    """
    selecionados = random.choices(populacao, fitness, k=len(populacao))
    return selecionados 


def selecao_torneio_max(populacao, fitness, tamanho_torneio):
    """Faz a seleção de uma população usando torneio.

    Nota: da forma que está implementada, só funciona em problemas de
    maximização.

    Args:
      populacao: lista contendo os individuos do problema
      fitness: lista contendo os valores computados da funcao objetivo
      tamanho_torneio: quantidade de invíduos que batalham entre si

    """
    selecionados = []

    for _ in range(len(populacao)):
        sorteados = random.sample(populacao, tamanho_torneio)

        fitness_sorteados = []
        for individuo in sorteados:
            indice_individuo = populacao.index(individuo)
            fitness_sorteados.append(fitness[indice_individuo])

        max_fitness = max(fitness_sorteados)
        indice_max_fitness = fitness_sorteados.index(max_fitness)
        individuo_selecionado = sorteados[indice_max_fitness]

        selecionados.append(individuo_selecionado)

    return selecionados


def selecao_torneio_min(populacao, fitness, tamanho_torneio):
    """Faz a seleção de uma população usando torneio.

    Nota: da forma que está implementada, só funciona em problemas de
    minimização.

    Args:
      populacao: lista contendo os individuos do problema
      fitness: lista contendo os valores computados da funcao objetivo
      tamanho_torneio: quantidade de invíduos que batalham entre si

    """
    selecionados = []

    for _ in range(len(populacao)):
        sorteados = random.sample(populacao, tamanho_torneio)

        fitness_sorteados = []
        for individuo in sorteados:
            indice_individuo = populacao.index(individuo)
            fitness_sorteados.append(fitness[indice_individuo])

        min_fitness = min(fitness_sorteados)
        indice_min_fitness = fitness_sorteados.index(min_fitness)
        individuo_selecionado = sorteados[indice_min_fitness]

        selecionados.append(individuo_selecionado)

    return selecionados


###############################################################################
#                                  Cruzamento                                 #
###############################################################################


def cruzamento_uniforme(pai, mae, chance_de_cruzamento):
    """Realiza cruzamento uniforme

    Args:
      pai: lista representando um individuo
      mae: lista representando um individuo
      chance_de_cruzamento: float entre 0 e 1 representando a chance de cruzamento

    """
    if random.random() < chance_de_cruzamento:
        filho1 = []
        filho2 = []

        for gene_pai, gene_mae in zip(pai, mae):
            if random.choice([True, False]):
                filho1.append(gene_pai)
                filho2.append(gene_mae)
            else:
                filho1.append(gene_mae)
                filho2.append(gene_pai)

        return filho1, filho2
    else:
        return pai, mae
    
def cruzamento_uniforme_tamanho_variavel(pai, mae, chance_de_cruzamento):
    """Realiza cruzamento uniforme

    Args:
      pai: lista representando um individuo
      mae: lista representando um individuo
      chance_de_cruzamento: float entre 0 e 1 representando a chance de cruzamento

    """
    if random.random() < chance_de_cruzamento:
        filho1 = []
        filho2 = []

        if len (pai) == len(mae): # se os pais tem o mesmo tamanho
            for gene_pai, gene_mae in zip(pai, mae):
                if random.choice([True, False]):
                    filho1.append(gene_pai)
                    filho2.append(gene_mae)
                else:
                    filho1.append(gene_mae)
                    filho2.append(gene_pai)

        else: # se os pais tem tamanhos diferentes
            if len(pai) > len(mae): # se o pai é maior que a mãe
                for i in range(len(mae)):
                    if random.choice([True, False]):
                        filho1.append(pai[i])
                        filho2.append(mae[i])
                    else:
                        filho1.append(mae[i])
                        filho2.append(pai[i])

                for i in range(len(mae), len(pai)):
                    if random.choice([True, False]):
                        filho1.append(pai[i])
                    else:
                        filho2.append(pai[i])

            else: # se a mae é maior que o pai
                for i in range(len(pai)):
                    if random.choice([True, False]):
                        filho1.append(pai[i])
                        filho2.append(mae[i])
                    else:
                        filho1.append(mae[i])
                        filho2.append(pai[i])

                for i in range(len(pai), len(mae)):
                    if random.choice([True, False]):
                        filho1.append(mae[i])
                    else:
                        filho2.append(mae[i])

        return filho1, filho2
    
    else:
        return pai, mae


def cruzamento_ponto_duplo(pai, mae, chance_de_cruzamento):
    """Realiza cruzamento de ponto duplo

    Args:
      pai: lista representando um individuo
      mae: lista representando um individuo
      chance_de_cruzamento: float entre 0 e 1 representando a chance de cruzamento

    """
    if random.random() < chance_de_cruzamento:
        corte1 = random.randint(1, len(mae) - 2)
        corte2 = random.randint(corte1 + 1, len(mae) - 1)
        filho1 = pai[:corte1] + mae[corte1:corte2] + pai[corte2:]
        filho2 = mae[:corte1] + pai[corte1:corte2] + mae[corte2:]
        return filho1, filho2
    else:
        return pai, mae


def cruzamento_ponto_simples(pai, mae, chance_de_cruzamento):
    """Realiza cruzamento de ponto simples

    Args:
      pai: lista representando um individuo
      mae: lista representando um individuo
      chance_de_cruzamento: float entre 0 e 1 representando a chance de cruzamento

    """
    if random.random() < chance_de_cruzamento:
        corte = random.randint(1, len(mae) - 1)
        filho1 = pai[:corte] + mae[corte:]
        filho2 = mae[:corte] + pai[corte:]
        return filho1, filho2
    else:
        return pai, mae


###############################################################################
#                                   Mutação                                   #
###############################################################################


def mutacao_salto(populacao, chance_de_mutacao, valores_possiveis):
    """Realiza mutação de salto

    Args:
      populacao: lista contendo os indivíduos do problema
      chance_de_mutacao: float entre 0 e 1 representando a chance de mutação
      valores_possiveis: lista com todos os valores possíveis dos genes

    """
    for individuo in populacao:
        if random.random() < chance_de_mutacao:
            gene = random.randint(0, len(individuo) - 1)
            valor_gene = individuo[gene]
            indice_letra = valores_possiveis.index(valor_gene)
            indice_letra += random.choice([1, -1])
            indice_letra %= len(valores_possiveis)
            individuo[gene] = valores_possiveis[indice_letra]


def mutacao_simples(populacao, chance_de_mutacao, valores_possiveis):
    """Realiza mutação simples

    Args:
      populacao: lista contendo os indivíduos do problema
      chance_de_mutacao: float entre 0 e 1 representando a chance de mutação
      valores_possiveis: lista com todos os valores possíveis dos genes

    """
    for individuo in populacao:
        if random.random() < chance_de_mutacao:
            gene = random.randint(0, len(individuo) - 1)
            valor_gene = individuo[gene]
            valores_sorteio = set(valores_possiveis) - set([valor_gene])
            individuo[gene] = random.choice(list(valores_sorteio))


def mutacao_simples_cb(populacao, chance_de_mutacao):
    """Realiza mutação simples no problema das caixas binárias

    Args:
      populacao: lista contendo os indivíduos do problema
      chance_de_mutacao: float entre 0 e 1 representando a chance de mutação

    """
    for individuo in populacao:
        if random.random() < chance_de_mutacao:
            gene = random.randint(0, len(individuo) - 1)
            individuo[gene] = 0 if individuo[gene] == 1 else 1


def mutacao_sucessiva_cb(populacao, chance_de_mutacao, chance_mutacao_gene):
    """Realiza mutação simples no problema das caixas binárias

    Args:
      populacao: lista contendo os indivíduos do problema
      chance_de_mutacao: float entre 0 e 1 representando a chance de mutação
      chance_mutacao_gene: float entre 0 e 1 representando a chance de mutação de cada gene

    """
    for individuo in populacao:
        if random.random() < chance_de_mutacao:
            for gene in range(len(individuo)):
                if random.random() < chance_mutacao_gene:
                    individuo[gene] = 0 if individuo[gene] == 1 else 1


def mutacao_simples_cnb(populacao, chance_de_mutacao, valor_max):
    """Realiza mutação simples no problema das caixas não-binárias

    Args:
      populacao: lista contendo os indivíduos do problema
      chance_de_mutacao: float entre 0 e 1 representando a chance de mutação
      valor_max: inteiro represtando o valor máximo das caixas

    """
    for individuo in populacao:
        if random.random() < chance_de_mutacao:
            gene = random.randint(0, len(individuo) - 1)
            valor_gene = individuo[gene]
            valores_possiveis = list(range(valor_max + 1))
            valores_possiveis.remove(valor_gene)
            individuo[gene] = random.choice(valores_possiveis)


def mutacao_sucessiva_cnb(
    populacao, chance_de_mutacao, chance_mutacao_gene, valor_max
):
    """Realiza mutação simples no problema das caixas não-binárias

    Args:
      populacao: lista contendo os indivíduos do problema
      chance_de_mutacao: float entre 0 e 1 representando a chance de mutação
      chance_mutacao_gene: float entre 0 e 1 representando a chance de mutação de cada gene
      valor_max: inteiro represtando o valor máximo das caixas

    """
    for individuo in populacao:
        if random.random() < chance_de_mutacao:
            for gene in range(len(individuo)):
                if random.random() < chance_mutacao_gene:
                    valores_possiveis = list(range(valor_max + 1))
                    valor_gene = individuo[gene]
                    valores_possiveis.remove(valor_gene)
                    individuo[gene] = random.choice(valores_possiveis)
