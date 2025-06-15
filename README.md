# ⚽ Projeto de Visão por Computador — Detecção e Classificação de Emblemas de Clubes de Futebol

Este projeto tem como objetivo detetar automaticamente emblemas de clubes de futebol em imagens de kits/jogadores usando **YOLOv8**, e classificar o clube correspondente com uma **CNN personalizada**.

---

## 📁 Estrutura do Projeto

Projeto_CV/
├── notebooks/
│ ├── classification/
│ │ ├── CNN.ipynb ← Primeira tentativa de classificação com dataset do Kaggle (Nota: não foi usada para classificação final)
│ │ └── best_model.pt ← Modelo CNN treinado com logos do Kaggle
│ │
│ ├── final-classification/
│ │ ├── CNN.ipynb ← CNN final treinada com logos recortados através do YOLO de kits reais retirados da net com scraping
│ │ └── best_model.pt ← Modelo final de classificação
│ │
│ ├── detection/
│ │ ├── Yolo.ipynb ← Treino e análise do modelo YOLOv8
│ │ ├── Yolo_com_CNN.ipynb ← Integração YOLO + CNN para classificação completa
│ │ └── yolov8n.pt ← Modelo base YOLO usado no treino
│ │
│ ├── data-cleaning/
│ │ ├── 1_Yolo_merge_classes.py ← Junta todas as classes do dataset original YOLO numa só ("logo")
│ │ ├── 2_Yolo_filter_classes.py ← Remove imagens sem logos de futebol 
│ │ └── data-aug.ipynb ← Aplicação de Data Augmentation aos recortes YOLO de kits reais retirados da net com scraping
│ │
│ └── scraping/
│ └── cnn-scraping.py ← Script para extrair imagens de kits por clube da internet

## 📌 Notas finais

- A CNN inicialmente treinada com imagens do Kaggle foi mantida por registo histórico, mas **não foi usada no produto final**.
- A versão final usa apenas imagens reais de kits, garantindo maior fidelidade ao problema real.

## 👥 Grupo G11

- Bernardo Coelho, nº 98445  
- Rafael Alexandre Dias Andorinha, nº 131000  
- Nuno Martins, nº 98863  
- Pedro Fonte Santa, nº 105306  
