import calculos 

def exibir_menu_principal():
    print("""
|----------------------------------------------------------------------------------|
| Digite o ID da operação desejada:                                                |
| 1. Equacao:     Cálculo de equações de 2º grau.                                  |
| 2. Area:        Cálculo da área de formas geométricas.                           |
| 3. Conversor:   Converte um número em extenso para inteiros e vice-versa.        | 
| 4. Treino Math: Treinamento para decorar o máximo de números de pi que conseguir.|
| .off:           Encerra o programa.                                              |
|----------------------------------------------------------------------------------|""")

def processar_equacao():
    try:
        a = float(input('| Insira o valor de a: '))
        b = float(input('| Insira o valor de b: '))
        c = float(input('| Insira o valor de c: '))
        return calculos.bhaskara(a, b, c)
    except ValueError:
        return "Erro: Os valores de a, b e c devem ser números."
    
def processar_area():
    menu_area = """| Digite o ID da forma desejada:
| 1. Retangulo
| 2. Triangulo
| 3. Circulo
> """
    option2 = input(menu_area).lower()
    try:
        if option2 in ['1', 'retangulo', 'retângulo']:
            h = float(input('| Insira a altura (cm): '))
            l = float(input('| Insira a largura (cm): '))
            return calculos.area_R(h, l)
        elif option2 in ['2', 'triangulo', 'triângulo']:
            h = float(input('| Insira a altura (cm): '))
            l = float(input('| Insira a largura da base (cm): '))
            return calculos.area_T(h, l)
        elif option2 in ['3', 'circulo', 'círculo']:
            r = float(input('| Insira o raio (cm): '))
            return calculos.area_C(r)
        else:
            return "Forma geométrica inválida."
    except ValueError:
        return "Erro: Os valores para o cálculo da área devem ser números."

def processar_conversor():
    menu_conversor = '''| Escolha o método de conversão:
    1. Inteiro -> Extenso 
    2. Extenso -> Inteiro
> '''
    try:
        option2 = input(menu_conversor).lower()
        if option2 in ['1', 'inteiro -> extenso']:
            num = int(input('| Insira um número inteiro de 0 a 999: '))
            return calculos.numero_para_extenso(num)
        elif option2 in ['2', 'extenso -> inteiro']:
            num_texto = input('| Escreva um número por extenso (0 a 999): ')
            return calculos.extenso_para_numero(num_texto)
        else:
            return 'Método de conversão inválido'
    except ValueError:
        return "Erro: Entrada inválida."

def processar_treino_pi():
    pi = '1415926535897932384626433832795028841971693993751058209749445923078164062862089986280348253421170679'
    while True:
        print('Digite o máximo de números de Pi que lembrar!')
        tentativa = input('3,')
        res = calculos.validacao_pi(tentativa, pi)
        
        print(f'Você acertou {res} números de PI!')
        print(f'| Número de PI: 3,{pi}')
        
        loop = input('Deseja tentar novamente? (1 para Sim)\n> ')
        if loop != '1':
            return None 

def exibir_resultado(result):
    if result is None:
        return
        
    print("-" * 25)
    if isinstance(result, (int, float)):
        if result % 1 == 0:
            print(f"> Resultado: {int(result)}")
        else:
            print(f"> Resultado: {result:.2f}")
    else:
        print(f"> {result}")
    print("-" * 25)