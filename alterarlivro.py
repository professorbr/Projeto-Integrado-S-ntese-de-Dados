# Importa o módulo shelve, que permite armazenar dados de forma persistente como se fosse um dicionário
import shelve

# Função responsável por alterar os dados de um livro já cadastrado
def alterar_livro():
    # Abre o arquivo de banco de dados chamado 'bancodedados.db' com permissão de escrita
    with shelve.open('bancodedados.db', writeback=True) as db:
        # Tenta acessar o dicionário de livros. Se não existir, usa um dicionário vazio
        livros = db.get('livros', {})

        # Solicita ao usuário o código do livro que deseja alterar
        codigo = input("Informe o código do livro que deseja alterar: ").strip()

        # Verifica se o livro com o código informado existe no banco de dados
        if codigo not in livros:
            print("Livro não encontrado.")
            return  # Encerra a função se o livro não existir

        # Recupera os dados do livro a ser alterado
        livro = livros[codigo]

        # Mostra os dados atuais do livro
        print(f"\nLivro atual: {livro}")
        print("Deixe em branco para manter o valor atual.")

        # Para cada campo, solicita uma nova entrada. 
        # Se o usuário não digitar nada, o valor atual é mantido.
        novo_isbn = input(f"Novo ISBN ({livro['isbn']}): ").strip() or livro['isbn']
        novo_titulo = input(f"Novo Título ({livro['titulo']}): ").strip() or livro['titulo']
        novo_autor = input(f"Novo Autor ({livro['autor']}): ").strip() or livro['autor']
        novo_ano = input(f"Novo Ano ({livro['ano']}): ").strip() or livro['ano']

        # Trata a entrada do número de cópias, garantindo que seja um número válido
        try:
            novas_copias = input(f"Novo número de cópias ({livro['copias']}): ").strip()
            novas_copias = int(novas_copias) if novas_copias else livro['copias']
        except ValueError:
            print("Número de cópias inválido.")
            return  # Encerra a função se o valor digitado não for um número

        # Atualiza o dicionário do livro com os novos dados
        livros[codigo] = {
            'isbn': novo_isbn,
            'titulo': novo_titulo,
            'autor': novo_autor,
            'ano': novo_ano,
            'copias': novas_copias
        }

        # Salva as alterações no banco de dados
        db['livros'] = livros

        # Mensagem de confirmação para o usuário
        print("Livro atualizado com sucesso.")
