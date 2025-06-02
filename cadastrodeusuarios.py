# Importa o módulo shelve, utilizado para armazenamento simples de dados persistentes
import shelve

# Função responsável por cadastrar novos usuários no sistema da biblioteca
def cadastrar_usuario():
    # Abre o banco de dados com permissão para escrita (writeback=True permite modificar objetos diretamente)
    with shelve.open('bancodedados.db', writeback=True) as db:
        # Se ainda não houver um dicionário de usuários no banco, ele é criado
        if 'usuarios' not in db:
            db['usuarios'] = {}

        # Recupera os dados atuais de usuários do banco
        usuarios = db['usuarios']

        # Solicita ao operador um número de identificação único para o novo usuário
        identificacao = input("Número de identificação do usuário (único): ").strip()
        if identificacao in usuarios:
            print("Já existe um usuário com essa identificação.")
            return  # Encerra a função se o número de identificação já estiver em uso

        # Coleta os demais dados do novo usuário
        nome = input("Nome: ").strip()
        telefone = input("Telefone: ").strip()
        email = input("Email: ").strip()

        # Armazena os dados do usuário, utilizando a identificação como chave
        usuarios[identificacao] = {
            'nome': nome,
            'telefone': telefone,
            'email': email
        }

        # Atualiza o banco de dados com o novo cadastro
        db['usuarios'] = usuarios

        # Exibe mensagem de confirmação do cadastro
        print(f"\nUsuário '{nome}' cadastrado com sucesso!")

# Fim da função cadastrar_usuario()
