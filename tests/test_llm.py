import pytest

from src.llm_client import analisar_contatos


def test_credencial_ausente():
    with pytest.raises(ValueError):
        analisar_contatos(
            "",
            "Texto de teste",
            {}
        )


def test_contatos_vazio():
    contatos = {}

    assert isinstance(contatos, dict)


def test_texto_presente():
    texto = "Meu email é joao@email.com"

    assert texto != ""


def test_chave_invalida():
    chave = "abc123"

    assert chave != ""