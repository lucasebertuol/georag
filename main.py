from pathlib import Path

from src.ingest import carregar_documentos

BASE_DIR = Path(__file__).resolve().parent
PASTA_DADOS = BASE_DIR / "dataset"

if __name__ == "__main__":

    documentos = carregar_documentos(PASTA_DADOS)

    for doc in documentos:
        print("=" * 60)
        print(doc["arquivo"])
        print("=" * 60)
        print(doc["texto"][:300])
        print()