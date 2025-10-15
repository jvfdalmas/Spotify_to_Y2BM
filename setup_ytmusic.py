#!/usr/bin/env python3

import sys
from ytmusicapi.setup import setup

# Nome do arquivo de saída
AUTH_FILE = "headers_auth.json"

print("Lendo os cabeçalhos da entrada padrão (stdin)...")
print("Certifique-se de ter copiado os cabeçalhos de requisição do seu navegador.")
print(f"O arquivo de autenticação '{AUTH_FILE}' será criado/substituído.")

# Lê os dados brutos da entrada padrão (pipe)
headers_raw = sys.stdin.read()

if not headers_raw or len(headers_raw) < 10:
    print("\nERRO: Nenhum dado de cabeçalho recebido da entrada padrão.")
    print("Por favor, execute este script usando um pipe, por exemplo:")
    print("pbpaste | python setup_ytmusic.py  (no macOS)")
    sys.exit(1)

try:
    # Usa a função setup importada para criar o arquivo de autenticação
    setup(filepath=AUTH_FILE, headers_raw=headers_raw)
    print(f"\n✅ Arquivo de autenticação '{AUTH_FILE}' gerado com sucesso.")
    print("Agora você pode executar o script principal 'spotify_to_ytmusic.py'.")

except Exception as e:
    print(f"\n❌ ERRO: Ocorreu um erro ao processar os cabeçalhos: {e}")
    print("Verifique se você copiou os cabeçalhos de requisição completos e corretos do seu navegador.")
    sys.exit(1)