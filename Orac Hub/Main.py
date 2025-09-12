import interacao  
import time

def rodar_programa():
    while True:
        interacao.exibir_menu_principal()
        option = input("> ").lower()

        if option == '.off':
            timestamp = time.strftime("%d/%m/%Y às %H:%M:%S")
            print(f"\nPrograma encerrado em {timestamp}. Até logo!")
            break

        result = None
        if option in ['1', 'equacao', 'equaçao', 'equação']:
            result = interacao.processar_equacao()
        elif option in ['2', 'area', 'área']:
            result = interacao.processar_area()
        elif option in ['3', 'conversor']:
            result = interacao.processar_conversor()
        elif option in ['4', 'treino math', 'treino de pi', 'pi']:
            result = interacao.processar_treino_pi()
        else:
            result = "Opção principal inválida."
        
        interacao.exibir_resultado(result)

# Bloco que garante que o programa só rode quando este arquivo for executado
if __name__ == "__main__":
    rodar_programa()