def formatar_resultado(contatos):
    emails = contatos.get("emails", [])
    telefones = contatos.get("telefones", [])
    urls = contatos.get("urls", [])

    texto = ""

    texto += "E-MAILS\n"
    texto += "-" * 30 + "\n"

    if emails:
        texto += "\n".join(emails)
    else:
        texto += "Nenhum encontrado"

    texto += "\n\nTELEFONES\n"
    texto += "-" * 30 + "\n"

    if telefones:
        texto += "\n".join(telefones)
    else:
        texto += "Nenhum encontrado"

    texto += "\n\nURLS\n"
    texto += "-" * 30 + "\n"

    if urls:
        texto += "\n".join(urls)
    else:
        texto += "Nenhuma encontrada"

    return texto