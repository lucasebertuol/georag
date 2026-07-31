from pathlib import Path

from src.rag import responder

BASE_DIR = Path(__file__).resolve().parent
CAMINHO_DB = BASE_DIR / "chroma_db"

while True:

    pergunta = input("\nPergunta: ")

    if pergunta.lower() in ["sair", "exit", "quit"]:
        break

    resposta = responder(pergunta, CAMINHO_DB)

    print("\nResposta:")
    print(resposta)