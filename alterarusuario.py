# Importa o módulo shelve, que permite salvar dados em arquivos com estrutura de dicionário
import shelve

# Função responsável por alterar os dados de um usuário já cadastrado
def alterar_usuario():
    # Abre o arquivo do banco de dados 'bancodedados.db' com permissão de escrita
    with shelve.open('bancodedados.db', writeback=True) as db:
        # Tenta acessar o dicionário de usuários. Se não existir, usa um dicionário vazio
        usuarios = db.get('usuarios', {})

        # Solicita a identificação do usuário que será alterado
        identificacao = input("Informe a identificação do usuário: ").strip()

        # Verifica se o usuário existe no banco de dados
        if identificacao not in usuarios:
            print("Usuário não encontrado.")
            return  # Encerra a função caso o ID não esteja registrado

        # Recupera os dados do usuário
        usuario = usuarios[identificacao]

        # Mostra os dados atuais do usuário
        print(f"\nUsuário atual: {usuario}")
        print("Deixe em branco para manter o valor atual.")

        # Para cada campo, solicita um novo valor.
        # Se o usuário deixar em branco, o valor anterior será mantido.
        novo_nome = input(f"Novo Nome ({usuario['nome']}): ").strip() or usuario['nome']
        novo_telefone = input(f"Novo Telefone ({usuario['telefone']}): ").strip() or usuario['telefone']
        novo_email = input(f"Novo Email ({usuario['email']}): ").strip() or usuario['email']

        # Atualiza o dicionário com os novos valores
        usuarios[identificacao] = {
            'nome': novo_nome,
            'telefone': novo_telefone,
            'email': novo_email
        }

        # Salva as alterações no banco de dados
        db['usuarios'] = usuarios

        # Mensagem de confirmação para o usuário
        print("Usuário atualizado com sucesso.")
