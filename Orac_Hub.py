import math
import time

# ==============================================================================
# SEÇÃO 1: FUNÇÕES DE CÁLCULO PURO
# Responsabilidade: Apenas fazer contas. Elas não sabem nada sobre 'input'
# ou 'print'. Recebem números, devolvem números ou texto.
# ==============================================================================



def bhaskara(a, b, c):
    # Calcula as raízes de uma equação de segundo grau. #
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
    # Calcula a área de um retângulo. #
    return h*l

def area_T(h, l):
    # Calcula a área de um triângulo. #
    return h*l/2

def area_C(r):
    # Calcula a área de um círculo. #
    return math.pi*r**2

def numero_para_extenso(num):
    # Converte um número inteiro (0-999) para texto por extenso. #
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

def extenso_para_numero(num):
    # -----------------------------------------------------------------------
    # Converte um número escrito por extenso (entre 0 e 999) para um inteiro.
    # Exemplo: "Vinte e Três" -> 23
    # -----------------------------------------------------------------------
    
    # Cria dicionário de palavras para números.
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

    # Preparação da entrada do usuário
    palavras = num.lower().split()

    # Processamento das palavras para calcular o total.
    total = 0
    for palavra in palavras:
        if palavra in mapa_de_numeros:
            total += mapa_de_numeros[palavra]

    return total

# ==============================================================================
# SEÇÃO 2: FUNÇÕES DE INTERAÇÃO E PROCESSAMENTO
# Responsabilidade: Lidar com menus, inputs e chamar as funções de cálculo.
# ==============================================================================

def exibir_menu_principal():
    # Mostra o menu principal de opções para o usuário. #
    print("""
|----------------------------------------------------------------------------------|
| Digite o ID da operação desejada:                                                |
| 1. Equacao:     Cálculo de equações de 2º grau.                                  |
| 2. Area:        Cálculo da área de formas geométricas.                           |
| 3. Conversor:   Converte um número em extenso para inteiros e inteiros em extenso| 
| 4. Treino Math: Treinamento para decorar o máximo de números de pi que conseguir |
| .off:           Encerra o programa.                                              |
|----------------------------------------------------------------------------------|""")

def processar_equacao():
    # Pede os dados para Bhaskara e retorna o resultado. #
    try:
        a = float(input('| Insira o valor de a: '))
        b = float(input('| Insira o valor de b: '))
        c = float(input('| Insira o valor de c: '))
        return bhaskara(a, b, c)
    except ValueError:
        return "Erro: Os valores de a, b e c devem ser números."
    
def processar_area():
    # Mostra o submenu de áreas, pede os dados e retorna o resultado. #
    menu_area = """| Digite o ID da forma desejada:
| 1. Retangulo
| 2. Triangulo
| 3. Circulo
> """
    option2 = input(menu_area).lower()
    try:
        if option2 in ['1', 'Retangulo', 'retangulo', 'Retângulo', 'retângulo', 'RETANGULO', 'RETÂNGULO']:
            h = float(input('| Insira a altura (cm): '))
            l = float(input('| Insira a largura (cm): '))
            return area_R(h, l)
        elif option2 in ['2', 'Triangulo', 'triangulo']:
            h = float(input('| Insira a altura (cm): '))
            l = float(input('| Insira a largura da base (cm): '))
            return area_T(h, l)
        elif option2 in ['3', 'Circulo', 'circulo']:
            r = float(input('| Insira o raio (cm): '))
            return area_C(r)
        else:
            return "Forma geométrica inválida."
    except ValueError:
        return "Erro: Os valores para o cálculo da área devem ser números."

def processar_conversor():
    menu_conversor = '''| Escolha o método de conversão:
    1. Inteiro -> Extenso 
    2. Extenso -> Inteiro
    '''

    try:
        option2 = input(menu_conversor).lower()
        if option2 in ['1', 'Inteiro -> Extenso']:
            try:
                num = int(input('| Insira um número inteiro de 0 a 999: '))
                return numero_para_extenso(num)
            except ValueError:
                return "Erro: O valor deve ser um número inteiro dentro do intervalo (0 - 999)."
        elif option2 in ['2', 'Extenso -> Inteiro']:
            try:
                num = input('| Escreva um número por extenso dentro do intervalo (0 - 999): ')
                return extenso_para_numero(num)
            except ValueError:
                return "Erro: O valor deve ser um número escrito por extenso dentro do intervalo (0 - 999)."
    except:
        return 'Método de conversão inválido'

def exibir_resultado(result):
    # Formata e imprime o resultado final. # 
    print("-" * 25)
    if isinstance(result, (int, float)):
        if result % 1 == 0:
            print(f"> Resultado: {int(result)}")
        else:
            print(f"> Resultado: {result:.2f}")
    elif result is not None:
        print(f"> {result}")
    print("-" * 25)

def processar_treino_pi():
    pi = '1415926535897932384626433832795028841971693993751058209749445923078164062862089986280348253421170679'
    num = ''

    while True:
        print ('Digite o máximo de números de Pi que lembrar!')
        tentativa = input ('3,')
        res = validacao_pi(tentativa, pi, num)

        print (f'Você acertou {res} números de PI!')
        print (f'| Número de PI: 3,{pi}')
        loop = input('Deseja tentar novamente? \n 1. Sim \n >')
        if loop == '1':
            continue
        else: break

def validacao_pi(tentativa, pi, num):
    i = 0
    num

    for num in tentativa:
        if tentativa[i] == pi[i]:
            i += 1
    return i
# ==============================================================================
# SEÇÃO 3: FLUXO PRINCIPAL DO PROGRAMA
# Responsabilidade: Manter o programa rodando, chamar outras funções e
# orquestrar o fluxo geral.
# ==============================================================================

    # Laço principal do programa. #
while True:
    exibir_menu_principal()
    option = input("> ").lower()

    if option == '.off':
        timestamp = time.strftime("%d/%m/%Y às %H:%M:%S")
        print(f"\nPrograma encerrado em {timestamp}. Até logo!")
        break

    result = None
    if option in ['1', 'equacao', 'equaçao', 'equação']:
        result = processar_equacao()
    elif option in ['2', 'area', 'área']:
        result = processar_area()
    elif option in ['3', 'conversor']:
        result = processar_conversor()
    elif option in ['4', 'treino de pi', 'pi']:
        result = processar_treino_pi()
    else:
        result = "Opção principal inválida."
    
    exibir_resultado(result)