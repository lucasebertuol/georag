import os

from dotenv import load_dotenv
from huggingface_hub import InferenceClient

from src.retriever import buscar

load_dotenv()

client = InferenceClient(
    provider="cerebras",
    api_key=os.getenv("HF_TOKEN"),
)


def responder(pergunta, caminho_db):

    resultado = buscar(pergunta, caminho_db)

    contexto = "\n".join(
    f"""Arquivo: {metadata['arquivo']}

    Trecho:
    {documento}

    ----------------------------------------"""
        for documento, metadata in zip(
            resultado["documentos"],
            resultado["metadados"]
        )
    )

    prompt = f"""
Você é um geólogo especialista em interpretação de sondagens.

Responda apenas com base no contexto abaixo.

Não invente informações.

Quando houver valores numéricos, preserve exatamente os números.

Quando citar uma profundidade, mantenha a unidade.

Caso a resposta não esteja disponível, diga:

"Não encontrei essa informação nos documentos."

================ CONTEXTO ================

{contexto}

==========================================

Pergunta:

{pergunta}

Resposta:
"""

    resposta = client.chat.completions.create(
        model="google/gemma-4-31B-it",
        messages=[
            {
                "role": "user",
                "content": prompt
            }
        ]
    )

    arquivos = []

    for metadata in resultado["metadados"]:
        if metadata["arquivo"] not in arquivos:
            arquivos.append(metadata["arquivo"])

    return {
        "resposta": resposta.choices[0].message.content,
        "arquivos": arquivos
    }