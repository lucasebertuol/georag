import chromadb
from sentence_transformers import SentenceTransformer

modelo = SentenceTransformer(
    "intfloat/multilingual-e5-small"
)

def buscar(pergunta, caminho, quantidade=3):

    cliente = chromadb.PersistentClient(
        path=str(caminho)
    )

    colecao = cliente.get_collection(
        "dados_geologicos"
    )

    embedding = modelo.encode(
        f"query: {pergunta}",
        convert_to_numpy=True
    ).tolist()

    resultado = colecao.query(
        query_embeddings=[embedding],
        n_results=quantidade,
        include=[
            "documents",
            "metadatas",
            "distances"
        ]
    )

    return {
        "documentos": resultado["documents"][0],
        "metadados": resultado["metadatas"][0],
        "distancias": resultado["distances"][0],
    }