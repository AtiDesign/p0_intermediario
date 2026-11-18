import tkinter as tk
from tkinter import scrolledtext

from config import load_config, validar_config
from extractor import extrair_contatos
from formatter import formatar_resultado
from llm_client import analisar_contatos


def extrair():
    """
    Fluxo principal da aplicação.
    """

    resultado.delete("1.0", tk.END)

    texto = entrada.get("1.0", tk.END).strip()

    # Validação da entrada
    if not texto:
        resultado.insert(
            tk.END,
            "Erro: informe um texto para análise."
        )
        return

    try:
        # Carregar configuração
        config = load_config()

        # Validar credenciais
        validar_config(config)

        api_key = config["OPENAI_API_KEY"]

        # Extrair contatos com Regex
        contatos = extrair_contatos(texto)

        # Formatar resultado local
        resultado_local = formatar_resultado(contatos)

        # Consultar LLM
        resposta_llm = analisar_contatos(
            api_key,
            texto,
            contatos
        )

        # Exibir resultado
        resultado.insert(
            tk.END,
            "CONTATOS EXTRAÍDOS\n"
        )
        resultado.insert(
            tk.END,
            "=" * 40 + "\n\n"
        )

        resultado.insert(
            tk.END,
            resultado_local
        )

        resultado.insert(
            tk.END,
            "\n\nANÁLISE DO LLM\n"
        )

        resultado.insert(
            tk.END,
            "=" * 40 + "\n\n"
        )

        resultado.insert(
            tk.END,
            resposta_llm
        )

    except ValueError as erro:
        resultado.insert(
            tk.END,
            f"Erro de configuração:\n\n{erro}"
        )

    except RuntimeError as erro:
        resultado.insert(
            tk.END,
            f"Erro do serviço:\n\n{erro}"
        )

    except Exception as erro:
        resultado.insert(
            tk.END,
            f"Erro inesperado:\n\n{erro}"
        )


# ===================================
# Interface gráfica
# ===================================

janela = tk.Tk()
janela.title("Extrator Inteligente de Contatos")
janela.geometry("800x600")

titulo = tk.Label(
    janela,
    text="Extrator Inteligente de Contatos",
    font=("Arial", 16, "bold")
)
titulo.pack(pady=10)

entrada = scrolledtext.ScrolledText(
    janela,
    height=10
)
entrada.pack(
    fill="both",
    padx=10,
    pady=5
)

botao = tk.Button(
    janela,
    text="Extrair e Analisar",
    command=extrair
)
botao.pack(pady=10)

resultado = scrolledtext.ScrolledText(
    janela,
    height=18
)
resultado.pack(
    fill="both",
    expand=True,
    padx=10,
    pady=5
)

janela.mainloop()