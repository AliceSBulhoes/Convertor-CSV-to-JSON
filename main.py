# Importando bibliotecas
import os
import pandas as pd
import json

# Entrada dos nomes dos arquivos
file_csv = input("Escreva exatamente o nome do arquivo (sem o .csv): ")
file_json = input("Escreva o nome do arquivo JSON (sem o .json): ")

# Criando os caminhos de forma compatível com o sistema operacional
csv_path = os.path.join("archive", f"{file_csv}.csv")
json_path = os.path.join("json", f"{file_json}.json")
temp_json_path = os.path.join("json", f"temp.json")

# Lendo o CSV
try:
    data_frame = pd.read_csv(csv_path, low_memory=False)
except FileNotFoundError:
    print(f"Erro: O arquivo {csv_path} não foi encontrado.")
    exit()