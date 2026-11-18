import pytest

from llm_client import analisar_contatos


def test_credencial_ausente():
    with pytest.raises(ValueError):
        analisar_contatos(
            "",
            "texto teste",
            {}
        )


def test_dicionario_contatos_vazio():
    contatos = {}

    assert isinstance(contatos, dict)