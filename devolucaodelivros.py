# Importa o módulo shelve para armazenamento persistente de dados
import shelve

# Importa ferramentas de data e hora
from datetime import datetime, timedelta

# Função responsável por registrar a devolução de um livro
def devolver_livro():
    # Abre o banco de dados com permissão de escrita
    with shelve.open('bancodedados.db', writeback=True) as db:
        # Verifica se há livros e empréstimos registrados
        if 'emprestimos' not in db or 'livros' not in db:
            print("Nenhum empréstimo ou livro cadastrado.")
            return  # Encerra a função caso faltem dados essenciais

        # Cria a estrutura de histórico de devoluções, se ainda não existir
        if 'historico_devolucoes' not in db:
            db['historico_devolucoes'] = []

        # Recupera os dados do banco
        emprestimos = db['emprestimos']
        livros = db['livros']
        historico = db['historico_devolucoes']

        # Solicita ao usuário os dados da devolução
        identificacao = input("Informe a identificação do usuário: ").strip()
        codigo_livro = input("Informe o código do livro: ").strip()

        # Busca o empréstimo correspondente com base no usuário e no livro
        emprestimo_encontrado = None
        for emprestimo in emprestimos:
            if emprestimo['usuario_id'] == identificacao and emprestimo['codigo_livro'] == codigo_livro:
                emprestimo_encontrado = emprestimo
                break

        # Se não encontrar o empréstimo, exibe aviso
        if not emprestimo_encontrado:
            print("Nenhum empréstimo correspondente encontrado.")
            return

        # Atualiza o número de cópias disponíveis do livro
        if codigo_livro in livros:
            livros[codigo_livro]['copias'] += 1

        # Obtém data e hora da devolução ajustadas para UTC-3
        agora_utc3 = datetime.utcnow() - timedelta(hours=3)
        data_devolucao = agora_utc3.strftime('%d/%m/%Y')
        hora_devolucao = agora_utc3.strftime('%H:%M:%S')

        # Registra a devolução no histórico, copiando os dados do empréstimo e adicionando a data/hora de devolução
        historico.append({
            **emprestimo_encontrado,  # Desempacota os dados do empréstimo
            'data_devolucao': data_devolucao,
            'hora_devolucao': hora_devolucao
        })

        # Remove o empréstimo da lista ativa
        emprestimos.remove(emprestimo_encontrado)

        # Atualiza o banco com os novos dados
        db['livros'] = livros
        db['emprestimos'] = emprestimos
        db['historico_devolucoes'] = historico

        # Confirmação final exibida ao usuário
        print(f"\nLivro '{emprestimo_encontrado['titulo_livro']}' devolvido por {emprestimo_encontrado['nome_usuario']} em {data_devolucao} às {hora_devolucao}.")
