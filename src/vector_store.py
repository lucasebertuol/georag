import chromadb


def salvar_no_chroma(chunks, caminho):

    cliente = chromadb.PersistentClient(
        path=str(caminho)
    )

    colecao = cliente.get_or_create_collection(
        name="dados_geologicos"
    )

    ids = [
        chunk["id"]
        for chunk in chunks
    ]

    documentos = [
        chunk["texto"]
        for chunk in chunks
    ]

    embeddings = [
        chunk["embedding"]
        for chunk in chunks
    ]

    metadados = [
        {
            "arquivo": chunk["arquivo"]
        }
        for chunk in chunks
    ]

    colecao.add(
        ids=ids,
        documents=documentos,
        embeddings=embeddings,
        metadatas=metadados
    )

    print(f"{len(chunks)} chunks gravados no ChromaDB.")