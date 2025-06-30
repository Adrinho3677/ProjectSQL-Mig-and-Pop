import sqlite3
import os

# Caminho do banco de dados
db_path = 'database.db'

# Arquivos SQL na ordem de execução
sql_files = [
    'migrations/001_create_tables.sql',
    'seeders/001_seed_users.sql',
    'seeders/002_seed_products.sql',
    'seeders/003_seed_orders.sql',
]

def executar_sql(conn, arquivo_sql):
    with open(arquivo_sql, 'r', encoding='utf-8') as f:
        sql_script = f.read()
    conn.executescript(sql_script)
    print(f'✅ Executado: {arquivo_sql}')

def main():
    # Apagar o banco antigo, se existir
    if os.path.exists(db_path):
        os.remove(db_path)
        print(f'🗑️ Banco anterior "{db_path}" removido.')

    # Criar nova conexão com SQLite
    conn = sqlite3.connect(db_path)

    try:
        for arquivo in sql_files:
            executar_sql(conn, arquivo)

        conn.commit()
        print(f'\n🎉 Banco "{db_path}" criado e populado com sucesso!')

    except Exception as e:
        print(f'❌ Erro ao executar scripts SQL: {e}')
    finally:
        conn.close()

if __name__ == '__main__':
    main()
