# Projeto SQLite: Sistema de Loja Simples

Este projeto simula um pequeno sistema de pedidos com clientes, produtos e vendas, usando **SQLite3** puro com scripts de migração e população.

## 📁 Estrutura

- `migrations/`: scripts para criação das tabelas
- `seeders/`: dados fictícios (usuários, produtos, pedidos)
- `database.db`: banco gerado após execução
- `populate_all.py`: script para rodar tudo de uma vez

## 🚀 Como usar

1. Certifique-se de ter o `sqlite3` instalado:
   ```bash
   sqlite3 --version
