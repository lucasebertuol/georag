from langchain_text_splitters import RecursiveCharacterTextSplitter

def dividir_em_chunks(documentos):

    splitter = RecursiveCharacterTextSplitter(

        chunk_size=500,
        chunk_overlap=100

    )

    chunks = []

    for doc in documentos:

        partes = splitter.split_text(doc["texto"])

        for parte in partes:

            chunks.append({

                "arquivo": doc["arquivo"],
                "texto": parte

            })

    return chunks