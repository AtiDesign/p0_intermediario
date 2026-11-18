# p0_intermediario
Evolução do p0_basico para o p0_intermediario

# P0 Intermediário - Extrator Inteligente de Informações de Contato

## Descrição

Este projeto tem como objetivo extrair informações de contato presentes em textos livres e complementar a análise utilizando um Modelo de Linguagem (LLM).

A aplicação identifica automaticamente:

- E-mails
- Telefones
- URLs

Após a extração, as informações são enviadas para um LLM que organiza e apresenta uma análise mais amigável dos dados encontrados.

---

# Problema Escolhido

Extrair automaticamente informações de contato presentes em textos não estruturados e apresentar essas informações de forma organizada e compreensível.

Exemplo de cenário:

Uma pessoa recebe um texto contendo informações de contato misturadas ao conteúdo da mensagem e deseja identificar rapidamente os dados relevantes.

---

# Público-Alvo

O sistema foi desenvolvido para:

- Estudantes;
- Pequenos negócios;
- Profissionais administrativos;
- Usuários que precisam localizar rapidamente informações de contato em textos.

---

# Justificativa para Utilização de LLM

Na versão básica do projeto, a extração de e-mails, telefones e URLs foi realizada exclusivamente por Expressões Regulares (Regex), pois essas informações seguem padrões bem definidos.

Na versão intermediária, foi incorporado um Modelo de Linguagem (LLM) para complementar o processamento dos dados extraídos.

O LLM é responsável por:

- Organizar os resultados encontrados;
- Explicar os dados de forma mais amigável;
- Identificar possíveis inconsistências;
- Produzir uma resposta mais útil para o usuário.

Dessa forma, o trabalho combina regras determinísticas (Regex) com inteligência artificial, aproveitando os pontos fortes de cada abordagem.

---

# Arquitetura da Solução

A aplicação foi organizada em componentes com responsabilidades distintas.

## config.py

Responsável por:

- carregar configurações;
- ler variáveis de ambiente;
- validar credenciais.

## extractor.py

Responsável por:

- extrair e-mails;
- extrair telefones;
- extrair URLs.

## llm_client.py

Responsável por:

- comunicar-se com o LLM;
- enviar solicitações;
- tratar erros de autenticação;
- tratar erros de comunicação.

## formatter.py

Responsável por:

- organizar a apresentação dos resultados.

## main.py

Responsável por:

- coordenar o fluxo da aplicação.

---

# Fluxo de Funcionamento

1. O usuário informa um texto.
2. O sistema valida a entrada.
3. O módulo de extração identifica contatos.
4. Os dados extraídos são enviados ao LLM.
5. O LLM produz uma análise complementar.
6. O resultado é apresentado ao usuário.

---

# Estrutura do Projeto

```text
p0_intermediario/
│
├── src/
│   ├── main.py
│   ├── config.py
│   ├── extractor.py
│   ├── formatter.py
│   └── llm_client.py
│
├── tests/
│   ├── test_extracao.py
│   └── test_llm.py
│
├── .env.example
├── .gitignore
├── requirements.txt
└── README.md
```

---

# Instalação

## Pré-requisitos

- Python 3.13 ou superior

## Clonar o repositório

```bash
git clone https://github.com/SEU-USUARIO/SEU-REPOSITORIO.git
cd p0_intermediario
```

## Criar ambiente virtual

```bash
python -m venv venv
```

## Ativar ambiente virtual

Windows:

```bash
venv\Scripts\activate
```

## Instalar dependências

```bash
pip install -r requirements.txt
```

---

# Configuração do LLM

Criar um arquivo `.env` na raiz do projeto:

```env
OPENAI_API_KEY=sua_chave_aqui
```

O arquivo `.env` não deve ser enviado ao GitHub.

O projeto disponibiliza o arquivo `.env.example` como referência.

---

# Testes Reais e Simulados

## Testes Reais

Os testes reais utilizam uma credencial válida da OpenAI configurada no arquivo `.env`.

Esses testes verificam:

- extração de contatos;
- comunicação com o LLM;
- processamento da resposta.

## Testes Simulados

Também foram considerados cenários de falha:

- credencial ausente;
- credencial inválida;
- resposta vazia;
- falha de comunicação;
- timeout.

Esses cenários são utilizados para validar o tratamento de erros da aplicação.

---

# Tratamento de Erros

A aplicação trata os seguintes cenários:

- entrada vazia;
- configuração ausente;
- credencial ausente;
- credencial inválida;
- timeout do serviço;
- indisponibilidade do serviço;
- falha de comunicação;
- resposta vazia ou inesperada.

Em todos os casos são apresentadas mensagens compreensíveis ao usuário.

---

# Execução

Executar:

```bash
python src/main.py
```

A interface será aberta para entrada dos dados.

---

# Exemplos de Entrada e Saída

## Exemplo 1

### Entrada

```text
Meu nome é João.
Entre em contato pelo e-mail joao@email.com
ou pelo telefone (12) 99999-8888.
```

### Saída da Extração

```text
E-MAILS
------------------------------
joao@email.com

TELEFONES
------------------------------
(12) 99999-8888

URLS
------------------------------
Nenhuma encontrada
```

### Saída Complementada pelo LLM

```text
Foi identificado um endereço de e-mail e um número de telefone associados ao contato informado.
```

---

## Exemplo 2

### Entrada

```text
Visite nosso portal:
https://www.empresa.com.br
```

### Saída

```text
Foi identificado um endereço de site válido.
```

---

# Execução dos Testes

Executar:

```bash
pytest
```

Resultado esperado:

```text
==============================
collected 4 items

tests/test_extracao.py ....
tests/test_llm.py ..

==============================
6 passed
```

---

# Limitações Conhecidas

- Nem todos os formatos internacionais de telefone são reconhecidos.
- URLs muito incomuns podem não ser identificadas corretamente.
- O resultado depende da disponibilidade do serviço de IA.
- Respostas produzidas pelo LLM podem variar.
- O sistema não valida a existência real dos contatos encontrados.

---

# Branches e Evolução

O desenvolvimento desta etapa foi realizado em uma branch específica:

```text
feature/intermediario
```

Posteriormente integrada à branch principal através de Pull Request.

---

# Tecnologias Utilizadas

- Python
- Tkinter
- Expressões Regulares (Regex)
- OpenAI API
- python-dotenv
- pytest
- Git
- GitHub