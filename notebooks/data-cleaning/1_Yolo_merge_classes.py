import os
from glob import glob

# Caminho para as labels do dataset YOLO
base_path = "/Users/pedrofs/Library/CloudStorage/OneDrive-ISCTE-IUL/Mestrado/2ªSem/APVC/Projeto/dataset-yolo-completo"
label_dirs = [
    os.path.join(base_path, "train", "labels"),
    os.path.join(base_path, "valid", "labels"),
]

def merge_classes_to_logo(label_path):
    with open(label_path, "r") as f:
        lines = f.readlines()

    new_lines = []
    for line in lines:
        parts = line.strip().split()
        if len(parts) == 5:
            # Força a classe a 0, mantém as coordenadas (x, y, w, h)
            parts[0] = "0"
            new_lines.append(" ".join(parts) + "\n")

    with open(label_path, "w") as f:
        f.writelines(new_lines)

# Processar todas as labels
for folder in label_dirs:
    label_files = glob(os.path.join(folder, "*.txt"))
    for label_file in label_files:
        merge_classes_to_logo(label_file)

print("Labels atualizadas: todas as classes agora são '0' (logo)")
