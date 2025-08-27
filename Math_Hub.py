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

def numero_para_extenso(n):
    # Converte um número inteiro (0-999) para texto por extenso. #
    if not 0 <= n <= 999:
        return "Número fora do intervalo (0-999)."
    if n == 100: return "Cem"
    if n == 0: return "Zero"

    unidades = ["", "Um", "Dois", "Três", "Quatro", "Cinco", "Seis", "Sete", "Oito", "Nove"]
    dezenas_especiais = ["Dez", "Onze", "Doze", "Treze", "Quatorze", "Quinze", "Dezesseis", "Dezessete", "Dezoito", "Dezenove"]
    dezenas = ["", "", "Vinte", "Trinta", "Quarenta", "Cinquenta", "Sessenta", "Setenta", "Oitenta", "Noventa"]
    centenas = ["", "Cento", "Duzentos", "Trezentos", "Quatrocentos", "Quinhentos", "Seiscentos", "Setecentos", "Oitocentos", "Novecentos"]
    
    partes = []
    c = n // 100
    if c > 0: partes.append(centenas[c])
    
    resto = n % 100
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

# ==============================================================================
# SEÇÃO 2: FUNÇÕES DE INTERAÇÃO E PROCESSAMENTO
# Responsabilidade: Lidar com menus, inputs e chamar as funções de cálculo.
# ==============================================================================

def exibir_menu_principal():
    # Mostra o menu principal de opções para o usuário. #
    print("""
|-----------------------------------------------------------------|
| Digite o ID da operação desejada:                               |
| 1. Equacao:   Cálculo de equações de 2º grau.                   |
| 2. Area:      Cálculo da área de formas geométricas.            |
| 3. Conversor: Converte um número inteiro (0-999) para extenso.  |
| .off:         Encerra o programa.                               |
|-----------------------------------------------------------------|""")

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
    option2 = input(menu_area)
    try:
        if option2 in ['1', 'Retangulo', 'retangulo']:
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
    # Pede o número para converter para extenso e retorna o resultado. #
    try:
        num = int(input('| Insira um número inteiro de 0 a 999: '))
        return numero_para_extenso(num)
    except ValueError:
        return "Erro: O valor deve ser um número inteiro."
        
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

# ==============================================================================
# SEÇÃO 3: FLUXO PRINCIPAL DO PROGRAMA
# Responsabilidade: Manter o programa rodando, chamar outras funções e
# orquestrar o fluxo geral.
# ==============================================================================

    # Laço principal do programa. #
while True:
    exibir_menu_principal()
    option = input("> ")

    if option == '.off':
        timestamp = time.strftime("%d/%m/%Y às %H:%M:%S")
        print(f"\nPrograma encerrado em {timestamp}. Até logo!")
        break

    result = None
    if option in ['1', 'Equacao', 'equacao','Equaçao', 'equaçao', 'Equação', 'equação']:
        result = processar_equacao()
    elif option in ['2', 'Area', 'area']:
        result = processar_area()
    elif option in ['3', 'Conversor', 'conversor']:
        result = processar_conversor()
    else:
        result = "Opção principal inválida."
    
    exibir_resultado(result)
