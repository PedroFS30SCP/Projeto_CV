import os
import shutil
import json

# Diretórios
src_base = "/Users/pedrofs/Library/CloudStorage/OneDrive-ISCTE-IUL/Mestrado/2ªSem/APVC/Projeto/dataset/cnn-kit-dataset-final"
dst_base = "/Users/pedrofs/Library/CloudStorage/OneDrive-ISCTE-IUL/Mestrado/2ªSem/APVC/Projeto/dataset/flat-cnn-kit-dataset-final"
mapping_path = os.path.join(dst_base, "clube_para_liga.json")

# Criar diretório destino
os.makedirs(dst_base, exist_ok=True)

# Mapeamento de clube → liga
clube_para_liga = {}

# Copiar clubes
for liga in os.listdir(src_base):
    liga_path = os.path.join(src_base, liga)
    if not os.path.isdir(liga_path):
        continue

    for clube in os.listdir(liga_path):
        clube_path = os.path.join(liga_path, clube)
        dst_path = os.path.join(dst_base, clube)

        if not os.path.exists(clube_path) or not os.path.isdir(clube_path):
            continue

        # Copiar pasta inteira (imagens já augmentadas)
        if os.path.exists(dst_path):
            print(f"[Aviso] {clube} já existe em {dst_base}, a saltar.")
            continue

        shutil.copytree(clube_path, dst_path)
        clube_para_liga[clube] = liga

# Guardar mapeamento
with open(mapping_path, 'w') as f:
    json.dump(clube_para_liga, f, indent=2)

print(f" Clubes copiados para {dst_base}")
print(f" Mapeamento salvo em {mapping_path}")
print(f"Total de clubes: {len(clube_para_liga)}")
