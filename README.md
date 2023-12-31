# Solve sudoku challenge
Algoritmo que resolve um problema de Sudoku. (Aplicação com Integração Contínua implementada).

# Sudoku_solver
Passado um problema de Sudoku não resolvido, no qual os espaços a serem preenchidos com os números estão representados por -1 o algoritmo identifica quais espaços precisam ser preenchidos e utiliza da estratégio backtracking para solucionar o problema retornando como True e modificando o array original caso seja possível uma solução. Caso não seja a função retorna um False como resultado de um problema que não pode ser resolvido seguindo as regras do sudoku.

# Sudoku
As regras do Sudoku são simples. O jogo é baseado em um tabuleiro de 9x9 células, dividido em 9 blocos de 3x3 células. O objetivo é preencher todas as células com números de 1 a 9, seguindo estas regras:

Cada linha deve conter todos os números de 1 a 9, sem repetição.
Cada coluna deve conter todos os números de 1 a 9, sem repetição.
Cada bloco de 3x3 deve conter todos os números de 1 a 9, sem repetição.
O jogo começa com algumas células já preenchidas, e cada solução de Sudoku é única

# Experiência adquirida no desafio:
Estudar sobre complexidade de algoritmos foi algo que abriu demais minha cabeça, fiquei totalmente envolvido com esse assunto e ao ler mais sobre me deparei com esse desafio que era criar um algoritmo capaz de resolver um problema de sudoku utilizando o backtraking e a força bruta.
Recursividade, backtracking e empilhamento são conceitos que fazem sua cabeça fritar, mas expande MUITO sua visão sobre a lógica de programação. Eu demorei bastante tempo para resolver esse desafio, obviamente por ser um desafio recorrente e popular eu não desenvolvi tudo do zero pois fui influenciado pelos artigos que li, mas fiquei contente que ao ler sobre os assuntos e entender os conceitos eu consegui juntar as peças do quebra-cabeça e finalizar com um código que seja funcional.


# Para rodar localmente

Clone esse repositório:

```bash
git clone git@github.com:nelsonhamada/solve-sudoku-challenge.git
```

Entre no diretório raiz:

```bash
cd solve-sudoku-callenge
```

Crie um ambiente isolado de desenvolvimento para evitar modificar suas versões python:

```bash
python3 -m venv .venv
```

Ative o ambiente criado:

```bash
source .venv/bin/activate
```

Instale as dependências necessárias para o projeto:

```bash
pip install -r requirements.txt
```

Para rodar o arquivo principal:

```bash
python3 sudoky.py
```

Para rodar os testes:

```bash
pytest test_sudoku.py
```


## Contato

Linkedin: https://www.linkedin.com/in/nelson-hamada
Email: fumiyuki.hamada@gmail.com
