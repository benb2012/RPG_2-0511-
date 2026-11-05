# RPG_2-0511-



Projeto desenvolvido em Python como parte dos estudos de programação. A proposta é construir um pequeno sistema de RPG dividido em três etapas, aplicando conceitos de programação, manipulação de arquivos e bancos de dados.

##  Objetivo

Desenvolver um jogo de RPG em que o jogador possa enfrentar inimigos em batalhas por turnos, comprar e vender itens em uma loja e participar de uma arena que registra o histórico das batalhas e mantém um ranking de jogadores.

O projeto é dividido em três exercícios progressivos, cada um utilizando os conhecimentos adquiridos anteriormente.

## 📁 Estrutura do projeto

```text
Python-no-mundo-do-RPG/
│
├── ex1/
│   └── batalha.py
│
├── ex2/
│   ├── arquivos.py
│   ├── loja.py
│   ├── main.py
│   ├── catalogo.json
│   └── heroi.json
│
├── ex3/
│   ├── batalha.py
│   ├── arquivos.py
│   ├── banco.py
│   ├── arena.py
│   ├── heroi.json
│   ├── inimigos.json
│   └── arena.db
│
└── README.md
```

*Observação: a estrutura pode ser atualizada conforme o desenvolvimento dos exercícios.*

## 🗡️ Exercício 1 — Batalha por turnos

**Arquivo:** `ex1/batalha.py`

Desenvolvimento de um sistema de combate entre o herói e seus inimigos.

### Funcionalidades

- [ ] Calcular dano de ataques.
- [ ] Implementar ataques críticos.
- [ ] Aplicar dano sem permitir vida negativa.
- [ ] Implementar sistema de cura.
- [ ] Criar uma barra de vida visual.
- [ ] Classificar o resultado da batalha.
- [ ] Validar as ações do jogador.
- [ ] Implementar o sistema de batalha por turnos.
- [ ] Implementar ataques dos inimigos.
- [ ] Implementar o uso de poções.
- [ ] Implementar a possibilidade de fugir.

**Conteúdos praticados:** `while`, `for`, `if`, `elif`, `else`, funções, parâmetros e `return`.

## 🛒 Exercício 2 — Loja do herói

**Arquivos:** `ex2/arquivos.py` e `ex2/loja.py`

Desenvolvimento de uma loja onde o jogador pode comprar e vender itens. Os dados do herói e do catálogo são armazenados em arquivos JSON.

### Funcionalidades

- [ ] Implementar carregamento de arquivos JSON.
- [ ] Implementar salvamento de arquivos JSON.
- [ ] Buscar itens no catálogo.
- [ ] Exibir o catálogo da loja.
- [ ] Implementar sistema de compras.
- [ ] Verificar se o item existe.
- [ ] Verificar se a quantidade é válida.
- [ ] Verificar se o jogador possui ouro suficiente.
- [ ] Atualizar o inventário após compras.
- [ ] Implementar sistema de vendas.
- [ ] Atualizar o ouro após vendas.
- [ ] Garantir que os dados sejam salvos corretamente.

**Conteúdos praticados:** módulos, `import`, JSON, funções, dicionários, listas, laços e estruturas condicionais.

## 🏆 Exercício 3 — Arena, histórico e ranking

**Arquivo:** `ex3/banco.py`

Integração dos sistemas anteriores com um banco de dados SQLite. O jogador poderá enfrentar diferentes inimigos e acompanhar seu desempenho através de um histórico e ranking.

### Funcionalidades

- [ ] Integrar o sistema de batalha.
- [ ] Integrar o sistema de arquivos JSON.
- [ ] Registrar partidas no banco de dados.
- [ ] Utilizar a data atual quando nenhuma data for informada.
- [ ] Consultar o histórico de partidas.
- [ ] Contabilizar vitórias, derrotas e fugas.
- [ ] Criar um ranking de jogadores.
- [ ] Ordenar o ranking pela vida restante.
- [ ] Utilizar o número de turnos como critério de desempate.
- [ ] Limitar a quantidade de resultados do ranking.
- [ ] Exportar o ranking para um arquivo JSON.

**Conteúdos praticados:** SQLite, SQL, `INSERT`, `SELECT`, `WHERE`, `ORDER BY`, `LIMIT`, `fetchall()`, módulos e JSON.

## 🧠 Tecnologias e conhecimentos

| Tecnologia / conceito | Aplicação |
|---|---|
| Python | Linguagem principal |
| Funções | Organização das regras do jogo |
| Estruturas condicionais | Decisões e regras |
| Laços de repetição | Batalhas, catálogos e consultas |
| Dicionários e listas | Dados dos personagens e itens |
| JSON | Salvamento de dados |
| SQLite | Histórico e ranking |
| SQL | Consultas e manipulação do banco |

## 🧪 Testes

Cada exercício possui um arquivo de testes próprio.

| Exercício | Testes esperados |
|---|---:|
| Exercício 1 | 16 testes |
| Exercício 2 | 11 testes |
| Exercício 3 | 8 testes |
| **Total** | **35 testes** |

O objetivo é concluir cada etapa com todos os testes passando antes de avançar para a próxima.

## 📌 Entrega final

- [ ] Concluir os três exercícios.
- [ ] Passar em todos os 35 testes.
- [ ] Responder às perguntas Q1–Q13.
- [ ] Testar os programas principais.
- [ ] Organizar os arquivos nas pastas correspondentes.
- [ ] Compactar as três pastas em um arquivo `.zip`.

---

**Projeto de estudos — Python | IFSC | Técnico em Informática**