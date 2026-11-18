import os

from dotenv import load_dotenv


def load_config():
    """
    Carrega as configurações do arquivo .env.
    """

    load_dotenv()

    return {
        "OPENAI_API_KEY": os.getenv("OPENAI_API_KEY")
    }


def validar_config(config):
    """
    Verifica se as configurações obrigatórias estão presentes.
    """

    api_key = config.get("OPENAI_API_KEY")

    if not api_key:
        raise ValueError(
            "Credencial ausente. Configure OPENAI_API_KEY no arquivo .env."
        )

    return True