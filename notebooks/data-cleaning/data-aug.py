import os
from PIL import Image
from torchvision import transforms
import random

# Diretórios
input_dir = "/Users/pedrofs/Library/CloudStorage/OneDrive-ISCTE-IUL/Mestrado/2ªSem/APVC/Projeto/dataset/cnn-kit-dataset"
output_dir = "/Users/pedrofs/Library/CloudStorage/OneDrive-ISCTE-IUL/Mestrado/2ªSem/APVC/Projeto/dataset/augmented-cnn-kit-dataset"

# Transformações de Data Augmentation
augment = transforms.Compose([
    transforms.Resize((224, 224)),
    transforms.RandomRotation(25),
    transforms.ColorJitter(brightness=0.4, contrast=0.4, saturation=0.4, hue=0.1),
    transforms.RandomHorizontalFlip(p=0.5),
    transforms.RandomAffine(degrees=10, translate=(0.1, 0.1), scale=(0.9, 1.1)),
])

# Função para criar dataset aumentado
def augment_dataset(input_base, output_base, num_augmented=300):
    for liga in os.listdir(input_base):
        liga_path = os.path.join(input_base, liga)
        if not os.path.isdir(liga_path):
            continue

        for clube in os.listdir(liga_path):
            clube_path = os.path.join(liga_path, clube)
            if not os.path.isdir(clube_path):
                continue

            # Criar diretório de output
            out_clube_dir = os.path.join(output_base, liga, clube)
            os.makedirs(out_clube_dir, exist_ok=True)

            # Processar cada imagem da pasta do clube
            for image_name in os.listdir(clube_path):
                image_path = os.path.join(clube_path, image_name)
                try:
                    image = Image.open(image_path).convert("RGB").resize((224, 224))
                except:
                    print(f"Erro ao abrir imagem: {image_path}")
                    continue

                # Criar múltiplas versões augmentadas
                for i in range(num_augmented):
                    aug_image = augment(image)
                    aug_name = f"{clube}_{i:03}.png"
                    aug_path = os.path.join(out_clube_dir, aug_name)
                    aug_image.save(aug_path)

                print(f"{clube}: {num_augmented} imagens guardadas em {out_clube_dir}")

print("A começar o processo de data augmentation...")
augment_dataset(input_dir, output_dir)
print("Augmentation concluído com sucesso!")