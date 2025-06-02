# Sistema de Gerenciamento de Biblioteca

Este é um sistema de gerenciamento de biblioteca desenvolvido em Python com o objetivo de aplicar, na prática, os conceitos de programação orientada a objetos, modularização, persistência de dados e boas práticas de codificação.

## Funcionalidades

- Cadastro, consulta e alteração de livros
- Cadastro, consulta e alteração de usuários
- Empréstimo e devolução de livros com controle de data/hora
- Relatórios em terminal e arquivo `.txt`
- Buscas por critérios (nome, autor, ano etc.)
- Relatório com filtros por mês e totais

## Requisitos

- Python 3.10 ou superior
- Biblioteca externa: `unidecode`

Para instalar a biblioteca:

```bash
pip install unidecode
```

## Como usar

1. Clone ou baixe o repositório
2. Acesse a pasta do projeto
3. Execute o arquivo `menuprincipal.py` com o Python:

```bash
python menuprincipal.py
```

## Estrutura

O projeto é modular e composto por arquivos organizados por função. Todos os dados são armazenados localmente com o módulo `shelve`.

## Licença

Este projeto está licenciado sob a [Creative Commons BY-NC 4.0](https://creativecommons.org/licenses/by-nc/4.0/deed.pt-br).

Você pode copiar, modificar e redistribuir este projeto, **desde que cite o autor original e não o utilize com fins comerciais**.

> ⚠️ Este projeto **não utiliza** licenças padrão de software como MIT ou GPL, pois tem restrição explícita contra uso comercial. Consulte o arquivo [LICENSE](./LICENSE) para mais informações.

## Autor

Projeto desenvolvido como exercício acadêmico para integração e aplicação dos conteúdos aprendidos no semestre.
