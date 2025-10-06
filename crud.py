import sqlite3

con = sqlite3.connect("crud.db")
cur = con.cursor()

cur.execute("CREATE TABLE IF NOT EXISTS usuarios (id PRIMARY KEY, nome text)")

def criar(nome):
    cur.execute("INSERT INTO usuarios (nome) VALUES (?)", (nome, ))
    con.commit()
    print("Usuario criado!")

def ler():
    for linha in cur.execute("SELECT * FROM usuarios"):
        print(linha)

def atualizar(id, nome):
    cur.execute("UPDATE usuarios SET nome = ? WHERE id = ?")
    con.commit()
    print("Usuario atualizado!")

def deletar(id):
    cur.execute("DELETE FROM usuarios WHERE id = ?", (id, ))
    con.commit()
    print("Usuario deletado!")
