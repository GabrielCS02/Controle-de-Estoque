📦 Sistema de Controle de Estoque em Python
Este projeto é um sistema de controle de estoque desenvolvido em Python para gerenciar o inventário de uma loja de eletrônicos. Ele permite adicionar, atualizar, excluir, visualizar produtos e gerenciar a quantidade de itens em estoque. É uma aplicação simples e funcional, baseada em linha de comando.

⚙️ Funcionalidades
O sistema oferece as seguintes funcionalidades:

Adicionar Produto

Permite adicionar novos produtos ao estoque com nome, preço e quantidade.
O nome do produto deve conter pelo menos uma letra.
Atualizar Produto

Atualiza as informações de um produto existente (preço e quantidade).
Excluir Produto

Remove um produto completamente do estoque.
Remover Quantidade do Estoque

Permite diminuir uma quantidade específica de um produto no estoque.
Exibe uma mensagem quando a quantidade chega a zero.
Visualizar Estoque

Lista todos os produtos com nome, preço e quantidade.
Sair do Sistema

Finaliza o programa.
🛠️ Tecnologias Utilizadas
Linguagem de Programação: Python 3.10 ou superior
Conceitos: Controle de fluxo, estruturas condicionais, loops, dicionários, boas práticas de programação.
🚀 Como Executar o Projeto
Clone este repositório:
bash
Copiar código
git clone https://github.com/seu-usuario/sistema-controle-estoque.git
Entre no diretório do projeto:
bash
Copiar código
cd sistema-controle-estoque
Execute o script:
bash
Copiar código
python sistema_estoque.py
📋 Requisitos
Python 3.10 ou superior instalado.
Um editor de texto ou IDE para visualizar e editar o código, como VSCode ou PyCharm.
📖 Como Funciona o Sistema?
Ao executar o script, será exibido um menu de opções:

markdown
Copiar código
--- Sistema de Controle de Estoque ---
1. Adicionar Produto
2. Atualizar Produto
3. Excluir Produto
4. Remover Quantidade do Estoque
5. Visualizar Estoque
6. Sair
Escolha uma das opções digitando o número correspondente e siga as instruções exibidas no terminal.

Exemplo de uso:

Adicione um produto informando seu nome, preço e quantidade.
Atualize o preço ou a quantidade de um produto existente.
Remova produtos do estoque ou visualize a lista completa de itens.
🛡️ Boas Práticas no Código
Validação do Nome: O sistema garante que o nome do produto contenha pelo menos uma letra.
Validação de Quantidades: A quantidade removida do estoque não pode ser maior do que a disponível.
Organização: Funções separadas para cada funcionalidade, garantindo a modularidade do código.
✨ Melhorias Futuras
Implementar salvamento de dados em um arquivo (ex.: JSON ou CSV) para persistência das informações.
Adicionar suporte a usuários/admins com autenticação.
Criar uma interface gráfica simples (ex.: com Tkinter ou PyQt).
Implementar relatórios de estoque, como produtos em falta ou com quantidade mínima.
🧑‍💻 Contribuição
Contribuições são bem-vindas! Siga os passos abaixo para contribuir:

Faça um fork do repositório.
Crie uma branch para a funcionalidade/melhoria:
bash
Copiar código
git checkout -b minha-feature
Implemente suas alterações e faça o commit:
bash
Copiar código
git commit -m "Descrição da minha funcionalidade"
Envie para sua branch remota:
bash
Copiar código
git push origin minha-feature
Abra um Pull Request.

Abraços✌️
