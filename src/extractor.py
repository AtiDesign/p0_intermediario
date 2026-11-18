import re


def extrair_contatos(texto):
    """
    Extrai e-mails, telefones e URLs de um texto.
    """

    emails = re.findall(
        r'[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}',
        texto
    )

    telefones = re.findall(
        r'(?:\+55\s?)?(?:\(\d{2}\)\s?|\d{2}\s?)?\d{4,5}-?\d{4}',
        texto
    )

    urls = re.findall(
        r'https?://[^\s]+|www\.[^\s]+',
        texto
    )

    return {
        "emails": emails,
        "telefones": telefones,
        "urls": urls
    }