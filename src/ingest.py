from pathlib import Path
import csv

from pypdf import PdfReader
from docx import Document

def ler_txt(caminho):
    with open(caminho, "r", encoding="utf-8") as arquivo:
        return arquivo.read()

def ler_pdf(caminho):

    leitor = PdfReader(caminho)

    texto = ""

    for pagina in leitor.pages:
        texto += pagina.extract_text() + "\n"

    return texto

def ler_docx(caminho):

    documento = Document(caminho)

    texto = ""

    for paragrafo in documento.paragraphs:
        texto += paragrafo.text + "\n"

    return texto

def ler_csv(caminho):

    linhas = []

    with open(caminho, newline="", encoding="utf-8") as arquivo:

        leitor = csv.reader(arquivo)

        for linha in leitor:
            linhas.append(" | ".join(linha))

    return "\n".join(linhas)

def carregar_documentos(pasta):

    documentos = []

    pasta = Path(pasta)

    for arquivo in pasta.iterdir():

        if arquivo.suffix == ".txt":
            texto = ler_txt(arquivo)

        elif arquivo.suffix == ".pdf":
            texto = ler_pdf(arquivo)

        elif arquivo.suffix == ".docx":
            texto = ler_docx(arquivo)

        elif arquivo.suffix == ".csv":
            texto = ler_csv(arquivo)

        else:
            continue

        documentos.append({
            "arquivo": arquivo.name,
            "texto": texto
        })

    return documentos