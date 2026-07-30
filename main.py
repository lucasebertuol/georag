from pathlib import Path

from src.ingest import carregar_documentos
from src.chunk import dividir_em_chunks
from src.embeddings import gerar_embeddings

BASE_DIR = Path(__file__).resolve().parent
PASTA_DADOS = BASE_DIR / "dataset"

if __name__ == "__main__":

    documentos = carregar_documentos(PASTA_DADOS)

    chunks = dividir_em_chunks(documentos)

    chunks = gerar_embeddings(chunks)

    print(chunks[0]["id"])
    print(chunks[0]["arquivo"])
    print(chunks[0]["texto"][:100])

    print(type(chunks[0]["embedding"]))
    print(len(chunks[0]["embedding"]))