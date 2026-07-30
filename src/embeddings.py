from sentence_transformers import SentenceTransformer

# O modelo é carregado apenas uma vez
modelo = SentenceTransformer("intfloat/multilingual-e5-small")


def gerar_embeddings(chunks):
    """
    Recebe uma lista de chunks e adiciona um embedding a cada um.
    """

    textos = [
        f"passage: {chunk['texto']}"
        for chunk in chunks
    ]

    embeddings = modelo.encode(
        textos,
        convert_to_numpy=True,
        show_progress_bar=True
    )

    for chunk, embedding in zip(chunks, embeddings):
        chunk["embedding"] = embedding

    return chunks