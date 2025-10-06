# 🗃️ CRUD com SQLite em Python

Este projeto é um exemplo simples de como fazer operações **CRUD** (Criar, Ler, Atualizar e Deletar) usando **Python** com o banco de dados **SQLite**.

A tabela utilizada neste exemplo se chama `usuarios`, e armazena apenas o `id` e o `nome` do usuário.

---

## 🚀 Funcionalidades

- ✅ Criar usuários
- ✅ Listar usuários
- ✅ Atualizar nome de um usuário
- ✅ Deletar usuário
- ✅ Tabela criada automaticamente se não existir

---

## 🧾 Requisitos

- Python 3 instalado

Não é necessário instalar bibliotecas externas. O `sqlite3` já faz parte da biblioteca padrão do Python.

---

## 📂 Estrutura do Banco de Dados

Tabela: `usuarios`

| Coluna | Tipo    | Descrição                      |
|--------|---------|--------------------------------|
| id     | INTEGER | Chave primária (auto incremento) |
| nome   | TEXT    | Nome do usuário                |

---

##  Como usar

### 1. Clone ou baixe este repositório

# 🧠 Funções disponíveis

- criar(nome)

Insere um novo usuário no banco de dados.

criar("Thaciane")

- ler()

Lista todos os usuários cadastrados.

ler()

- atualizar(id, nome)

Atualiza o nome de um usuário com o ID especificado.

atualizar(1, "Thaciane Paula")

- deletar(id)

Remove um usuário com o ID especificado.

deletar(1)
