from openai import OpenAI
from openai import (
    AuthenticationError,
    APITimeoutError,
    APIConnectionError,
    RateLimitError,
    InternalServerError
)


def analisar_contatos(api_key, texto_original, contatos):
    """
    Envia os contatos extraídos para o LLM
    e solicita uma análise organizada.
    """

    if not api_key:
        raise ValueError(
            "Credencial ausente. Configure OPENAI_API_KEY no arquivo .env."
        )

    try:
        client = OpenAI(
            api_key=api_key
        )

        prompt = f"""
Você é um assistente especializado em organização de informações de contato.

Texto original:
{texto_original}

Informações encontradas:
{contatos}

Sua tarefa é:

1. Organizar os dados encontrados.
2. Identificar possíveis relações entre eles.
3. Explicar resumidamente o que foi encontrado.
4. Informar se há inconsistências ou ausência de dados.

Retorne uma resposta clara para o usuário.
"""

        resposta = client.chat.completions.create(
            model="gpt-4o-mini",
            messages=[
                {
                    "role": "system",
                    "content": (
                        "Você organiza informações de contato "
                        "de forma clara e objetiva."
                    )
                },
                {
                    "role": "user",
                    "content": prompt
                }
            ],
            timeout=20
        )

        if not resposta:
            raise RuntimeError(
                "O modelo retornou uma resposta vazia."
            )

        if not resposta.choices:
            raise RuntimeError(
                "Formato de resposta inesperado."
            )

        conteudo = resposta.choices[0].message.content

        if not conteudo:
            raise RuntimeError(
                "O modelo retornou conteúdo vazio."
            )

        return conteudo

    except AuthenticationError:
        raise RuntimeError(
            "Credencial inválida. Verifique OPENAI_API_KEY."
        )

    except APITimeoutError:
        raise RuntimeError(
            "Tempo limite excedido. O serviço demorou para responder."
        )

    except APIConnectionError:
        raise RuntimeError(
            "Falha de comunicação com o serviço."
        )

    except RateLimitError:
        raise RuntimeError(
            "Limite de utilização atingido. Tente novamente mais tarde."
        )

    except InternalServerError:
        raise RuntimeError(
            "O serviço de IA está temporariamente indisponível."
        )

    except Exception as erro:
        raise RuntimeError(
            f"Erro inesperado: {str(erro)}"
        )