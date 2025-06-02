📚 Projeto Integrado: Sistema de Gerenciamento de Biblioteca

Este é um sistema simples de gerenciamento de biblioteca feito em Python, utilizando o módulo `shelve` para armazenamento local dos dados. O sistema roda no terminal (modo texto) e está organizado de forma modular.

🛠 Requisitos

- Python 3.10 ou superior
- Biblioteca `unidecode` instalada (para buscas sem acento)

Como instalar o `unidecode`:

pip install unidecode

📂 Estrutura da pasta do projeto

Projeto Integrado Síntese de Dados/
├── menuprincipal.py
├── cadastrodelivros.py
├── alterar_livro.py
├── cadastrodeusuarios.py
├── alterarusuario.py
├── emprestimodelivros.py
├── devolucaodelivros.py
├── consultadelivros.py
├── consultausuario.py
├── relatorios.py
├── relatorio_biblioteca.txt         ← gerado automaticamente
├── bancodedados.db                  ← gerado automaticamente pelo shelve

▶️ Como executar o sistema

1. Abra o terminal (ou use o terminal do VS Code)
2. Acesse a pasta do projeto:

cd "Projeto Integrado Síntese de Dados"

3. Execute o menu principal:

python menuprincipal.py

📋 Funcionalidades disponíveis

Ao executar o sistema, você verá o seguinte menu:

1 - Cadastrar Livro
2 - Alterar Livro
3 - Cadastrar Usuário
4 - Alterar Usuário
5 - Emprestar Livro
6 - Devolver Livro
7 - Consultar Livros
8 - Consultar Usuário
9 - Gerar Relatórios
0 - Sair

✅ O que cada opção faz

1. Cadastrar Livro
Registra um novo livro com:
- Código único
- ISBN
- Título
- Autor
- Ano de publicação
- Número de cópias

2. Alterar Livro
Permite editar os dados de um livro já cadastrado. Basta informar o código e atualizar os campos desejados.

3. Cadastrar Usuário
Cadastra um novo usuário com:
- Identificação única
- Nome
- Telefone
- Email

4. Alterar Usuário
Permite editar os dados de um usuário já cadastrado.

5. Emprestar Livro
Registra o empréstimo de um livro, associando-o a um usuário com data e hora automáticas (UTC-3). Reduz o número de cópias disponíveis.

6. Devolver Livro
Registra a devolução e adiciona o registro ao histórico. A cópia é novamente disponibilizada.

7. Consultar Livros
Permite buscar livros por título, autor e ano (busca parcial, sem acento). Também é possível filtrar apenas os disponíveis.

8. Consultar Usuário
Permite buscar usuários por nome, identificação, email ou telefone (busca parcial, sem acento).

9. Gerar Relatórios
Exibe no terminal e salva em `relatorio_biblioteca.txt`:
- Livros disponíveis
- Livros emprestados
- Devoluções do mês atual
- Usuários cadastrados

🧠 Observações

- Os dados são salvos automaticamente no arquivo `bancodedados.db` pelo `shelve`, que cria arquivos auxiliares (`.bak`, `.dat`, `.dir`).
- Se quiser começar do zero, apague todos os arquivos `bancodedados.db*`.
- O sistema foi feito para facilitar manutenção e expansão futura (ex: adicionar interface gráfica ou relatórios em CSV).

👨‍💻 Autor
Sistema desenvolvido como projeto de prática em Python orientado a objetos, com foco em modularização, persistência de dados e boas práticas de codificação.
