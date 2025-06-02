# Importa o módulo shelve para armazenamento persistente
import shelve

# Importa datetime e timedelta para obter data e hora do empréstimo ajustada para UTC-3
from datetime import datetime, timedelta

# Função responsável por registrar o empréstimo de um livro
def emprestar_livro():
    # Abre o banco de dados com permissão de escrita
    with shelve.open('bancodedados.db', writeback=True) as db:
        # Verifica se as estruturas de usuários e livros estão presentes no banco
        if 'usuarios' not in db or 'livros' not in db:
            print("Não há usuários ou livros cadastrados.")
            return  # Encerra se algum dos dois não estiver disponível

        # Cria a lista de empréstimos, caso ainda não exista
        if 'emprestimos' not in db:
            db['emprestimos'] = []

        # Acessa os dados do banco
        usuarios = db['usuarios']
        livros = db['livros']
        emprestimos = db['emprestimos']

        # Solicita a identificação do usuário e valida se está cadastrado
        identificacao = input("Informe a identificação do usuário: ").strip()
        if identificacao not in usuarios:
            print("Usuário não encontrado.")
            return

        # Recupera o nome do usuário a partir da identificação
        nome_usuario = usuarios[identificacao]['nome']

        # Solicita o código do livro e valida se está cadastrado
        codigo_livro = input("Informe o código do livro: ").strip()
        if codigo_livro not in livros:
            print("Livro não encontrado.")
            return

        # Verifica se o livro possui cópias disponíveis
        livro = livros[codigo_livro]
        if livro['copias'] < 1:
            print("Não há cópias disponíveis deste livro.")
            return

        # Obtém a data e hora atual ajustada para UTC-3
        agora_utc3 = datetime.utcnow() - timedelta(hours=3)
        data_emprestimo = agora_utc3.strftime('%d/%m/%Y')
        hora_emprestimo = agora_utc3.strftime('%H:%M:%S')

        # Adiciona o empréstimo à lista com os dados principais
        emprestimos.append({
            'usuario_id': identificacao,
            'nome_usuario': nome_usuario,
            'codigo_livro': codigo_livro,
            'titulo_livro': livro['titulo'],
            'data': data_emprestimo,
            'hora': hora_emprestimo
        })

        # Reduz o número de cópias disponíveis do livro
        livro['copias'] -= 1

        # Atualiza os dados no banco
        db['livros'] = livros
        db['emprestimos'] = emprestimos

        # Mensagem de confirmação exibida ao usuário
        print(f"\nLivro '{livro['titulo']}' emprestado para {nome_usuario} em {data_emprestimo} às {hora_emprestimo}.")
