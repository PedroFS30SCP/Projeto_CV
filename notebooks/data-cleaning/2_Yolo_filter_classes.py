import os

# Diretórios
LABEL_DIR = "/Users/pedrofs/Library/CloudStorage/OneDrive-ISCTE-IUL/Mestrado/2ªSem/APVC/Projeto/dataset-yolo-completo/valid/labels"
IMG_DIR = LABEL_DIR.replace("labels", "images")

# IDs de logos de clubes reais
CLUB_IDS = {"2", "3", "5"}

# Contadores
removed_count = 0
total = 0

for file in os.listdir(LABEL_DIR):
    if not file.endswith(".txt"):
        continue

    total += 1
    label_path = os.path.join(LABEL_DIR, file)
    img_path = os.path.join(IMG_DIR, file.replace(".txt", ".jpg"))

    with open(label_path, "r") as f:
        lines = f.readlines()

    # Filtrar apenas os logos de clubes
    club_lines = [line for line in lines if line.split()[0] in CLUB_IDS]

    if club_lines:
        # Reescreve o ficheiro só com logos válidos
        with open(label_path, "w") as f:
            f.writelines(club_lines)
    else:
        # Remove txt e imagem
        os.remove(label_path)
        if os.path.exists(img_path):
            os.remove(img_path)
        removed_count += 1

print(f"Limpeza concluída: {removed_count} imagens removidas (sem logos de clubes).")
print(f"Total de ficheiros processados: {total}")
