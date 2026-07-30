from langchain_text_splitters import RecursiveCharacterTextSplitter


def dividir_em_chunks(documentos):

    splitter = RecursiveCharacterTextSplitter(
        chunk_size=500,
        chunk_overlap=100
    )

    chunks = []

    contador = 1

    for doc in documentos:

        partes = splitter.split_text(doc["texto"])

        for parte in partes:

            chunks.append({
                "id": f"chunk_{contador:06d}",
                "arquivo": doc["arquivo"],
                "texto": parte
            })

            contador += 1

    return chunks