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

# Convertendo para JSON e removendo barras invertidas
data_frame.to_json(temp_json_path, orient="records", indent=2)  # Passo intermediário
with open(temp_json_path, "r") as temp_file:
    json_data = json.load(temp_file)  # Carrega sem barras invertidas

with open(json_path, "w", encoding="utf-8") as final_file:
    json.dump(json_data, final_file, ensure_ascii=False, indent=2)

# Remove o arquivo temporário, se necessário
os.remove(temp_json_path)

print(f"Arquivo JSON salvo em: {json_path}")