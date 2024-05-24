#ex1
def converter_lista_para_string(lista):
    
    lista[0] = lista[0].upper()
    
    
    for i in range(1, len(lista)):
        if lista[i - 1] == ' ':
            lista[i] = lista[i].upper()
    
    
    titulo_final = ''.join(lista)
    
    
    titulo_final = titulo_final.replace('/', ' ')
    
    return titulo_final


titulo_filme = ['O', ' Senhor', ' Dos', ' Aneis']
print(converter_lista_para_string(titulo_filme))  # Saída: O Senhor Dos Aneis

#ex2
def pares_e_impares(lista):
    pares = []
    impares = []
    
    for num in lista:
        if num % 2 == 0:
            pares.append(num)
        else:
            impares.append(num)
    
    return [pares, impares]


numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9]
print(pares_e_impares(numeros))  

#ex3
def cria_matriz(M, N):
    matriz = []
    numero = 1
    
    for i in range(M):
        linha = []
        for j in range(N):
            linha.append(numero)
            numero += 1
        matriz.append(linha)
    
    return matriz


M = 3
N = 4
print(cria_matriz(M, N))  

#ex4
def filtrar_palavras(frase, letra):
    
    palavras = frase.split()
    
    
    palavras_com_letra = [palavra for palavra in palavras if letra.lower() in palavra.lower()]
    
    return palavras_com_letra


frase = "João chutou a bola essa manha"
letra = "a"
print(filtrar_palavras(frase, letra)) 

#ex5
def filtrar_palavras(frase, letra):
    
    palavras = frase.split()
    
    
    palavras_com_letra = [palavra for palavra in palavras if letra.lower() in palavra.lower()]
    
    return palavras_com_letra


frase = "João chutou a bola essa manha"
letra = "a"
print(filtrar_palavras(frase, letra)) 