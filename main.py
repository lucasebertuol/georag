from pathlib import Path

from src.ingest import carregar_documentos
from src.chunk import dividir_em_chunks

BASE_DIR = Path(__file__).resolve().parent
PASTA_DADOS = BASE_DIR / "dataset"

if __name__ == "__main__":

    documentos = carregar_documentos(PASTA_DADOS)

    chunks = dividir_em_chunks(documentos)

    print(f"Foram criados {len(chunks)} chunks.\n")

    for chunk in chunks:

        print("=" * 60)
        print(chunk["arquivo"])
        print("-" * 60)
        print(chunk["texto"])
        print()