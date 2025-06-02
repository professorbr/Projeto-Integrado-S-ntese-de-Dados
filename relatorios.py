# Importa o módulo shelve para acesso ao banco de dados
import shelve

# Importa ferramentas de data e hora
from datetime import datetime, timedelta

# Importa módulo os (não utilizado neste trecho, mas pode ser útil para manipular caminhos de arquivos)
import os

# Função responsável por gerar relatórios sobre o estado atual da biblioteca
def gerar_relatorios():
    # Abre o banco de dados em modo leitura
    with shelve.open('bancodedados.db') as db:
        linhas = []  # Lista de linhas que serão escritas no relatório

        # Define mês e ano atuais com base no horário de Brasília (UTC-3)
        agora = datetime.utcnow() - timedelta(hours=3)
        mes_atual = agora.strftime('%m')
        ano_atual = agora.strftime('%Y')

        # Função auxiliar para adicionar e exibir uma linha do relatório
        def adicionar_linha(texto=""):
            print(texto)
            linhas.append(texto)

        # Cabeçalho
        adicionar_linha("RELATÓRIOS DA BIBLIOTECA\n")

        # 1. Relatório de livros disponíveis
        adicionar_linha("LIVROS DISPONÍVEIS:")
        livros = db.get('livros', {})
        total_disponiveis = 0
        for codigo, livro in livros.items():
            if livro['copias'] > 0:
                total_disponiveis += 1
                adicionar_linha(f"- {livro['titulo']} (Código: {codigo}, Cópias: {livro['copias']})")
        if total_disponiveis == 0:
            adicionar_linha("Nenhum livro disponível.")
        adicionar_linha(f"Total: {total_disponiveis} livro(s) disponível(is)\n")

        # 2. Relatório de livros emprestados
        adicionar_linha("LIVROS EMPRESTADOS:")
        emprestimos = db.get('emprestimos', [])
        if emprestimos:
            for emp in emprestimos:
                adicionar_linha(f"- {emp['titulo_livro']} emprestado para {emp['nome_usuario']} em {emp['data']} às {emp['hora']}")
        else:
            adicionar_linha("Nenhum livro emprestado no momento.")
        adicionar_linha(f"Total: {len(emprestimos)} empréstimo(s) ativo(s)\n")

        # 3. Histórico de devoluções do mês atual
        adicionar_linha("HISTÓRICO DE DEVOLUÇÕES (mês atual):")
        historico = db.get('historico_devolucoes', [])
        total_devolucoes_mes = 0
        for dev in historico:
            data = dev.get('data_devolucao', '')
            if data:
                dia, mes, ano = data.split('/')
                if mes == mes_atual and ano == ano_atual:
                    total_devolucoes_mes += 1
                    adicionar_linha(f"- {dev['titulo_livro']} devolvido por {dev['nome_usuario']} em {data} às {dev['hora_devolucao']}")
        if total_devolucoes_mes == 0:
            adicionar_linha("Nenhuma devolução registrada neste mês.")
        adicionar_linha(f"Total: {total_devolucoes_mes} devolução(ões) registrada(s) neste mês\n")

        # 4. Relatório de usuários cadastrados
        adicionar_linha("USUÁRIOS CADASTRADOS:")
        usuarios = db.get('usuarios', {})
        if usuarios:
            for id, usuario in usuarios.items():
                adicionar_linha(f"- {usuario['nome']} (ID: {id}, Telefone: {usuario['telefone']}, Email: {usuario['email']})")
        else:
            adicionar_linha("Nenhum usuário cadastrado.")
        adicionar_linha(f"Total: {len(usuarios)} usuário(s) cadastrado(s)\n")

        # Caminho e nome do arquivo onde o relatório será salvo
        nome_arquivo = "relatorio_biblioteca.txt"

        # Tenta salvar o relatório em um arquivo .txt
        try:
            with open(nome_arquivo, "w", encoding="utf-8") as arquivo:
                for linha in linhas:
                    arquivo.write(linha + "\n")
            print(f"\nRelatório salvo com sucesso como '{nome_arquivo}'.")
        except Exception as e:
            print(f"\nErro ao salvar o relatório: {e}")
