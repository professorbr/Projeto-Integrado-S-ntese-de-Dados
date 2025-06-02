# Importação das funções principais de cada módulo do sistema
# Cada módulo representa uma parte específica da biblioteca
from cadastrodelivros import cadastrar_livro
from alterarlivro import alterar_livro
from cadastrodeusuarios import cadastrar_usuario
from alterarusuario import alterar_usuario
from emprestimodelivros import emprestar_livro
from devolucaodelivros import devolver_livro
from consultadelivros import consultar_livro
from consultausuario import consultar_usuario
from relatorios import gerar_relatorios

# Função principal que exibe o menu e controla a navegação do usuário
def exibir_menu():
    while True:
        # Exibe o menu principal com todas as opções do sistema
        print("\n======= MENU PRINCIPAL =======")
        print("1 - Cadastrar Livro")
        print("2 - Alterar Livro")
        print("3 - Cadastrar Usuário")
        print("4 - Alterar Usuário")
        print("5 - Emprestar Livro")
        print("6 - Devolver Livro")
        print("7 - Consultar Livros")
        print("8 - Consultar Usuário")
        print("9 - Gerar Relatórios")
        print("0 - Sair")
        print("================================")

        # Recebe a opção escolhida pelo usuário
        opcao = input("Escolha uma opção: ").strip()

        # Executa a função correspondente com base na opção escolhida
        if opcao == "1":
            cadastrar_livro()  # Chama o módulo de cadastro de livros
        elif opcao == "2":
            alterar_livro()  # Chama o módulo de alteração de dados de livros
        elif opcao == "3":
            cadastrar_usuario()  # Chama o módulo de cadastro de usuários
        elif opcao == "4":
            alterar_usuario()  # Chama o módulo de alteração de dados de usuários
        elif opcao == "5":
            emprestar_livro()  # Chama o módulo de empréstimo de livros
        elif opcao == "6":
            devolver_livro()  # Chama o módulo de devolução de livros
        elif opcao == "7":
            consultar_livro()  # Chama o módulo de consulta de livros
        elif opcao == "8":
            consultar_usuario()  # Chama o módulo de consulta de usuários
        elif opcao == "9":
            gerar_relatorios()  # Chama o módulo que gera os relatórios do sistema
        elif opcao == "0":
            print("Encerrando o sistema. Até mais!")  # Finaliza o sistema
            break
        else:
            print("Opção inválida. Tente novamente.")  # Mensagem para entrada incorreta

# Ponto de entrada do programa: executa a função exibir_menu()
if __name__ == "__main__":
    exibir_menu()
