# Importa o módulo shelve para acesso ao banco de dados
import shelve

# Importa o unidecode para facilitar buscas ignorando acentos
from unidecode import unidecode

# Função responsável por consultar livros cadastrados com base em filtros opcionais
def consultar_livro():
    # Abre o banco de dados em modo leitura
    with shelve.open('bancodedados.db') as db:
        # Verifica se há livros cadastrados no sistema
        if 'livros' not in db or not db['livros']:
            print("Nenhum livro cadastrado.")
            return  # Encerra a função caso não existam livros

        # Recupera os livros cadastrados
        livros = db['livros']

        # Solicita os critérios de busca (todos opcionais)
        print("\n--- Consulta Avançada de Livros ---")
        termo_titulo = input("Título (deixe vazio se não quiser filtrar): ").strip().lower()
        termo_autor = input("Autor (deixe vazio se não quiser filtrar): ").strip().lower()
        termo_ano = input("Ano de publicação (deixe vazio se não quiser filtrar): ").strip()

        # Usuário pode escolher se quer ver apenas livros com cópias disponíveis
        mostrar_apenas_disponiveis = input(
            "Mostrar apenas livros com cópias disponíveis? (s/n): "
        ).strip().lower() == 's'

        # Lista para armazenar os livros encontrados
        encontrados = []

        # Percorre todos os livros do sistema
        for codigo, livro in livros.items():
            # Normaliza os dados para facilitar a busca sem acentos e com letras minúsculas
            titulo = unidecode(livro['titulo'].lower())
            autor = unidecode(livro['autor'].lower())
            ano = livro['ano']
            copias = livro['copias']

            # Aplica os filtros de busca, pulando os que não corresponderem
            if termo_titulo and unidecode(termo_titulo) not in titulo:
                continue
            if termo_autor and unidecode(termo_autor) not in autor:
                continue
            if termo_ano and termo_ano != ano:
                continue
            if mostrar_apenas_disponiveis and copias < 1:
                continue

            # Se passou em todos os filtros, adiciona à lista de encontrados
            encontrados.append((codigo, livro))

        # Exibe os resultados encontrados
        if encontrados:
            print(f"\n{len(encontrados)} livro(s) encontrado(s):\n")
            for codigo, livro in encontrados:
                print(f"Código: {codigo}")
                print(f"ISBN: {livro['isbn']}")
                print(f"Título: {livro['titulo']}")
                print(f"Autor: {livro['autor']}")
                print(f"Ano: {livro['ano']}")
                print(f"Cópias disponíveis: {livro['copias']}\n")
        else:
            # Se nenhum livro for encontrado com os filtros informados
            print("Nenhum livro encontrado com os critérios informados.")
