import os
import requests
from PIL import Image
from io import BytesIO
from duckduckgo_search import DDGS
import time

# Caminhos
root_dir = "/Users/pedrofs/Library/CloudStorage/OneDrive-ISCTE-IUL/Mestrado/2ªSem/APVC/Projeto/dataset/logo-dataset"
output_dir = "/Users/pedrofs/Library/CloudStorage/OneDrive-ISCTE-IUL/Mestrado/2ªSem/APVC/Projeto/dataset/yolo-kit-dataset"

# Função para guardar imagem
def save_image_from_url(url, save_path):
    try:
        response = requests.get(url, timeout=10)
        img = Image.open(BytesIO(response.content)).convert("RGB")
        img = img.resize((640, 640))
        img.save(save_path)
        print(f"Guardado: {save_path}")
    except Exception as e:
        print(f"Erro ao guardar imagem: {e}")

# Processamento
for league in sorted(os.listdir(root_dir)):
    league_path = os.path.join(root_dir, league)
    if not os.path.isdir(league_path): continue

    for club in sorted(os.listdir(league_path)):
        club_output_dir = os.path.join(output_dir, league, club)
        image_path = os.path.join(club_output_dir, f"{club}.jpg")

        # Pular se imagem já existe
        if os.path.exists(image_path):
            print(f"Já existe: {club}")
            continue

        query = f"{club} kit"
        print(f"\nA pesquisar: {query}")
        with DDGS() as ddgs:
            try:
                results = list(ddgs.images(query, max_results=1))
                time.sleep(5)
            except Exception as e:
                print(f"Erro na pesquisa DuckDuckGo: {e}")
                continue

        if results:
            image_url = results[0]['image']
            print(f"URL encontrada: {image_url}")

            try:
                response = requests.get(image_url, timeout=10)
                img = Image.open(BytesIO(response.content)).convert("RGB")
                img = img.resize((640, 640))
                img.show()

                approval = input(f"Guardar imagem para {club}? (y/n): ").strip().lower()
                if approval == 'y':
                    os.makedirs(club_output_dir, exist_ok=True)
                    img.save(image_path)
                    print(f"Imagem guardada: {image_path}")
                else:
                    print("Imagem rejeitada.")
            except Exception as e:
                print(f"Erro ao processar imagem: {e}")
        else:
            print(f"Nenhum resultado para {query}")
