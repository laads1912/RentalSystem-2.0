import sqlite3

# Conecta ou cria o banco de dados RentalSystem.db
conn = sqlite3.connect('RentalSystem.db')
cursor = conn.cursor()

# Remove a tabela User, se ela existir
cursor.execute('''
DROP TABLE IF EXISTS Users
''')

# Cria a tabela Users com a estrutura atualizada
cursor.execute('''
CREATE TABLE IF NOT EXISTS Users (
    email TEXT PRIMARY KEY NOT NULL,
    full_name TEXT NOT NULL,
    age INTEGER NOT NULL,
    gender TEXT NOT NULL CHECK(gender IN ('MALE', 'FEMALE')),
    height INTEGER NOT NULL,
    weight INTEGER NOT NULL,
    shoe_size INTEGER NOT NULL,
    is_active BOOLEAN NOT NULL,
    is_employee BOOLEAN NOT NULL,
    password_hash TEXT NOT NULL
)
''')

# Confirma as mudanças e fecha a conexão
conn.commit()
conn.close()

print("Tabela Users criada com sucesso.")
