from datetime import datetime
import sqlite3

def conectar_db():
    conn = sqlite3.connect('vendas.db')
    cursor = conn.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS vendas (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            item TEXT NOT NULL,
            preco REAL NOT NULL,
            quantidade INTEGER NOT NULL,
            tipo_quantidade TEXT NOT NULL,
            tipo_pagamento TEXT NOT NULL,
            data_venda TEXT NOT NULL
        )
    ''')
    conn.commit()
    return conn, cursor

def cadastrar_venda(item, preco, quantidade, tipo_quantidade, tipo_pagamento):
    conn, cursor = conectar_db()
    data_venda = datetime.now().strftime('%d/%m/%Y %H:%M:%S')
    cursor.execute('''
        INSERT INTO vendas (item, preco, quantidade, tipo_quantidade, tipo_pagamento, data_venda)
        VALUES (?, ?, ?, ?, ?, ?)
    ''', (item, preco, quantidade, tipo_quantidade, tipo_pagamento, data_venda))
    conn.commit()
    conn.close()

def obter_vendas():
    conn, cursor = conectar_db()
    cursor.execute('SELECT * FROM vendas')
    vendas = cursor.fetchall()
    conn.close()
    return vendas

def excluir_venda_db(venda_id):
    conn, cursor = conectar_db()
    cursor.execute('DELETE FROM vendas WHERE id = ?', (venda_id,))
    conn.commit()
    conn.close()

def alterar_venda_db(venda_id, item, preco, quantidade, tipo_quantidade, tipo_pagamento):
    conn, cursor = conectar_db()
    cursor.execute('''
        UPDATE vendas
        SET item = ?, preco = ?, quantidade = ?, tipo_quantidade = ?, tipo_pagamento = ?
        WHERE id = ?
    ''', (item, preco, quantidade, tipo_quantidade, tipo_pagamento, venda_id))
    conn.commit()
    conn.close()
