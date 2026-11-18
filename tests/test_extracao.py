from src.extractor import extrair_contatos


def test_email():
    texto = "Contato: joao@email.com"

    resultado = extrair_contatos(texto)

    assert resultado["emails"] == [
        "joao@email.com"
    ]


def test_telefone():
    texto = "Meu telefone é (12) 99999-8888"

    resultado = extrair_contatos(texto)

    assert resultado["telefones"] == [
        "(12) 99999-8888"
    ]


def test_url():
    texto = "Acesse https://www.exemplo.com.br"

    resultado = extrair_contatos(texto)

    assert resultado["urls"] == [
        "https://www.exemplo.com.br"
    ]


def test_sem_resultados():
    texto = "Este texto não possui informações de contato."

    resultado = extrair_contatos(texto)

    assert resultado["emails"] == []
    assert resultado["telefones"] == []
    assert resultado["urls"] == []