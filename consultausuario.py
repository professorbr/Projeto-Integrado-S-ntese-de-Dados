# Importa o módulo shelve para acesso ao banco de dados
import shelve 

# Importa o unidecode para remover acentos e facilitar buscas
from unidecode import unidecode

# Função responsável por consultar usuários no sistema com base em filtros opcionais
def consultar_usuario():
    # Abre o banco de dados para leitura
    with shelve.open('bancodedados.db') as db:
        # Verifica se há usuários cadastrados
        if 'usuarios' not in db or not db['usuarios']:
            print("Nenhum usuário cadastrado.")
            return  # Encerra se não houver usuários registrados

        # Recupera o dicionário de usuários
        usuarios = db['usuarios']

        # Solicita filtros de busca ao usuário. Todos são opcionais.
        print("\n--- CONSULTA DE USUÁRIOS ---")
        termo_nome = input("Nome (deixe vazio se não quiser filtrar): ").strip().lower()
        termo_id = input("Identificação (deixe vazio se não quiser filtrar): ").strip()
        termo_email = input("Email (deixe vazio se não quiser filtrar): ").strip().lower()
        termo_telefone = input("Telefone (deixe vazio se não quiser filtrar): ").strip()

        # Lista onde serão armazenados os usuários encontrados
        encontrados = []

        # Percorre todos os usuários cadastrados
        for identificacao, dados in usuarios.items():
            # Prepara os dados para comparação, removendo acentos e deixando minúsculas
            nome = unidecode(dados['nome'].lower())
            email = unidecode(dados['email'].lower())
            telefone = dados['telefone']

            # Verifica se o termo pesquisado está contido nas informações
            if termo_nome and unidecode(termo_nome) not in nome:
                continue
            if termo_id and termo_id != identificacao:
                continue
            if termo_email and unidecode(termo_email) not in email:
                continue
            if termo_telefone and termo_telefone not in telefone:
                continue

            # Se passar por todos os filtros, adiciona à lista de resultados
            encontrados.append((identificacao, dados))

        # Exibe os resultados encontrados
        if encontrados:
            print(f"\n{len(encontrados)} usuário(s) encontrado(s):\n")
            for identificacao, dados in encontrados:
                print(f"Identificação: {identificacao}")
                print(f"Nome: {dados['nome']}")
                print(f"Telefone: {dados['telefone']}")
                print(f"Email: {dados['email']}")
                print("-" * 30)
        else:
            # Caso nenhum usuário atenda aos critérios
            print("Nenhum usuário encontrado com os critérios informados.")
