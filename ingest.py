from pathlib import Path

from src.ingest import carregar_documentos
from src.chunk import dividir_em_chunks
from src.embeddings import gerar_embeddings
from src.vector_store import salvar_no_chroma

BASE_DIR = Path(__file__).resolve().parent

PASTA_DADOS = BASE_DIR / "dataset"
CAMINHO_DB = BASE_DIR / "chroma_db"

documentos = carregar_documentos(PASTA_DADOS)

chunks = dividir_em_chunks(documentos)

chunks = gerar_embeddings(chunks)

salvar_no_chroma(chunks, CAMINHO_DB)

# Validação do Retrieve
# resultado = buscar(
#     "O que foi retirado a 22 metros?",
#     CAMINHO_DB
# )

# for documento, metadata, distancia in zip(resultado["documentos"],
#                                           resultado["metadados"],
#                                           resultado["distancias"]
#                                         ):

#     print("=" * 60)
#     print(f"Arquivo: {metadata['arquivo']}")
#     print(f"Distância: {distancia:.4f}")
#     print("-" * 60)
#     print(documento)
#     print()

print("Base vetorial criada com sucesso!")