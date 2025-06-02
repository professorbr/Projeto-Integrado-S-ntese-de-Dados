# Importa o módulo shelve, que permite armazenar dados de forma persistente como um dicionário
import shelve

# Função responsável por cadastrar um novo livro no banco de dados
def cadastrar_livro():
    # Abre o banco de dados no modo de escrita com suporte a modificações diretas (writeback=True)
    with shelve.open('bancodedados.db', writeback=True) as db:
        # Cria a estrutura de livros no banco caso ainda não exista
        if 'livros' not in db:
            db['livros'] = {}

        # Recupera o dicionário de livros
        livros = db['livros']

        # Solicita o código único do livro (usado para diferenciar cópias específicas)
        codigo = input("Código do livro (único para cada cópia): ").strip()
        if codigo in livros:
            print("Já existe um livro com esse código.")
            return  # Encerra a função se o código já estiver cadastrado

        # Coleta as demais informações do livro
        isbn = input("ISBN: ").strip()
        titulo = input("Título: ").strip()
        autor = input("Autor: ").strip()
        ano = input("Ano de publicação: ").strip()

        # Tenta converter o número de cópias para inteiro, com tratamento de erro
        try:
            copias = int(input("Número de cópias disponíveis: ").strip())
        except ValueError:
            print("Número de cópias inválido.")
            return  # Encerra a função se a conversão falhar

        # Armazena os dados do livro no dicionário usando o código como chave
        livros[codigo] = {
            'isbn': isbn,
            'titulo': titulo,
            'autor': autor,
            'ano': ano,
            'copias': copias
        }

        # Atualiza o banco de dados com os livros cadastrados
        db['livros'] = livros

        # Confirma o sucesso do cadastro
        print(f"\nLivro '{titulo}' cadastrado com sucesso!")

# Fim da função cadastrar_livro()
