import math

def bhaskara(a, b, c):
    if a == 0:
        return "Erro: 'a' não pode ser zero em uma equação de segundo grau."
        
    delta = b**2 - 4*a*c
    
    if delta >= 0:
        deltaRaiz = math.sqrt(delta)
        x1 = (-b - deltaRaiz) / (a*2)
        x2 = (-b + deltaRaiz) / (a*2)
        
        if x1 == x2:
            return f'A única raiz real é: {x1:.2f}'
        else:
            return f'As duas raízes reais são: {x1:.2f} e {x2:.2f}'
    else:
        return 'A equação não possui raízes reais (delta negativo).'

def area_R(h, l):
    return h*l

def area_T(h, l):
    return h*l/2

def area_C(r):
    return math.pi*r**2

def numero_para_extenso(num):
    if not 0 <= num <= 999:
        return "Número fora do intervalo (0-999)."
    if num == 100: return "Cem"
    if num == 0: return "Zero"

    unidades = ["", "Um", "Dois", "Três", "Quatro", "Cinco", "Seis", "Sete", "Oito", "Nove"]
    dezenas_especiais = ["Dez", "Onze", "Doze", "Treze", "Quatorze", "Quinze", "Dezesseis", "Dezessete", "Dezoito", "Dezenove"]
    dezenas = ["", "", "Vinte", "Trinta", "Quarenta", "Cinquenta", "Sessenta", "Setenta", "Oitenta", "Noventa"]
    centenas = ["", "Cento", "Duzentos", "Trezentos", "Quatrocentos", "Quinhentos", "Seiscentos", "Setecentos", "Oitocentos", "Novecentos"]
    
    partes = []
    c = num // 100
    if c > 0: partes.append(centenas[c])
    
    resto = num % 100
    if resto > 0:
        if c > 0: partes.append("e")
        if 10 <= resto <= 19:
            partes.append(dezenas_especiais[resto - 10])
        else:
            d = resto // 10
            u = resto % 10
            if d > 0: partes.append(dezenas[d])
            if u > 0:
                if d > 0: partes.append("e")
                partes.append(unidades[u])
    return " ".join(partes)

def extenso_para_numero(num_texto):
    mapa_de_numeros = {
        'zero': 0, 'um': 1, 'dois': 2, 'três': 3, 'quatro': 4, 'cinco': 5,
        'seis': 6, 'sete': 7, 'oito': 8, 'nove': 9, 'dez': 10,
        'onze': 11, 'doze': 12, 'treze': 13, 'quatorze': 14, 'quinze': 15,
        'dezesseis': 16, 'dezessete': 17, 'dezoito': 18, 'dezenove': 19,
        'vinte': 20, 'trinta': 30, 'quarenta': 40, 'cinquenta': 50,
        'sessenta': 60, 'setenta': 70, 'oitenta': 80, 'noventa': 90,
        'cem': 100, 'cento': 100, 'duzentos': 200, 'trezentos': 300,
        'quatrocentos': 400, 'quinhentos': 500, 'seiscentos': 600,
        'setecentos': 700, 'oitocentos': 800, 'novecentos': 900
    }
    palavras = num_texto.lower().replace(" e ", " ").split()
    total = 0
    for palavra in palavras:
        if palavra in mapa_de_numeros:
            total += mapa_de_numeros[palavra]
    return total

def validacao_pi(tentativa, pi):
    i = 0
    for i in range(min(len(tentativa), len(pi))):
        if tentativa[i] != pi[i]:
            return i
    return i + 1 if i == len(tentativa) - 1 else i