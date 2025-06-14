from langchain.agents import initialize_agent, Tool
from langchain.agents.agent_types import AgentType
from langchain_community.utilities import SQLDatabase
from langchain_openai import ChatOpenAI
from dotenv import load_dotenv, find_dotenv
import re
import json

_ = load_dotenv(find_dotenv())

with open("dicionarios.json", "r", encoding="utf-8") as f:
    dicionarios = json.load(f)

def traduzir_sql(sql: str) -> str:
    print('>>> traduzir_sql ')
    for nome_legivel, dados in dicionarios["tabelas"].items():
        if nome_legivel in sql:
            codigo_tabela = dados["codigo_identificador_tabela"]
            sql = re.sub(rf'\b{re.escape(nome_legivel)}\b', codigo_tabela, sql, flags=re.IGNORECASE)
            

    for dados in dicionarios["tabelas"].values():
        for nome_coluna_legivel, codigo_coluna in dados["colunas"].items():
            sql = re.sub(rf'\b{re.escape(nome_coluna_legivel)}\b', codigo_coluna, sql, flags=re.IGNORECASE)

    print('>>> sql ', sql)
    return sql


db = SQLDatabase.from_uri("sqlite:///banco.db")

def executar_sql_com_traducao(query: str) -> str:
    try:
        query_traduzida = traduzir_sql(query)
        print(f"\nConsulta original: {query}")
        print(f"Consulta traduzida: {query_traduzida}")
        resultados = db.run(query_traduzida)
        return (
                f"Resultado da consulta SQL:\n{resultados}\n\n"
                f"Analise os dados e responda conforme a pergunta do usuário."
            )
    except Exception as e:
        return f"Erro ao executar a query: {str(e)}"

def listar_tabelas(_: str) -> str:
    return ", ".join(db.get_usable_table_names())

def consultar_dicionario(entrada: str) -> str:
    entrada = entrada.lower()
    resultados = []

    for nome_legivel, dados in dicionarios["tabelas"].items():
        sinonimos = dados.get("sinonimos", [])
        if entrada in nome_legivel.lower() or entrada in sinonimos:
            resultados.append(f"Tabela: {nome_legivel} (Código: {dados['codigo_identificador_tabela']})")
            for nome_coluna_legivel, codigo_coluna in dados["colunas"].items():
                resultados.append(f"  Coluna: {nome_coluna_legivel} (Código: {codigo_coluna})")

    if not resultados:
        return f"Nenhuma correspondência encontrada para '{entrada}'. Tente usar um nome mais específico."

    return "\n".join(resultados)


tools = [
    Tool(
        name="sql_db_query",
        func=executar_sql_com_traducao,
        description="Use esta ferramenta para EXECUTAR consultas SQL e OBTER os resultados reais do banco, não apenas gerar o SQL."
    ),

    Tool(
        name="sql_db_list_tables",
        func=listar_tabelas,
        description="Use esta ferramenta para listar todas as tabelas disponíveis no banco."
    ),
   Tool(
    name="consultar_dicionario",
    func=consultar_dicionario,
    description=(
        "Use esta ferramenta para descobrir o nome real de tabelas ou colunas usando palavras comuns como 'endereço', 'cliente', etc. "
        "Ela retorna os nomes codificados a partir de termos legíveis."
    )
)

]

llm = ChatOpenAI(temperature=0, model="gpt-3.5-turbo")

prompt_prefix = """
Você está interagindo com um banco de dados onde os nomes reais das tabelas e colunas são codificados.
Sempre que for necessário responder perguntas com dados do banco, você deve usar a ferramenta 'sql_db_query' para EXECUTAR a consulta e exibir os RESULTADOS reais, e não apenas montar o SQL.
Use a ferramenta 'consultar_dicionario' se não souber qual tabela ou coluna utilizar.
Não tente adivinhar nomes. Use sempre as ferramentas para consultar e executar.
"""

agent_executor = initialize_agent(
    tools=tools,
    handle_parsing_errors=True,
    llm=llm,
    agent=AgentType.ZERO_SHOT_REACT_DESCRIPTION,
    verbose=True,
    max_iterations=5,
    agent_kwargs={"prefix": prompt_prefix.strip()}
)

from langchain.callbacks import get_openai_callback
def main():
    pergunta = "Tem alguem chamada Julia?"

    with get_openai_callback() as cb:
        resposta = agent_executor.invoke({"input": pergunta})

        print("\nResposta final:\n", resposta)
        print(f"\nTokens usados: {cb.total_tokens}")
        print(f"Prompt tokens: {cb.prompt_tokens}")
        print(f"Completion tokens: {cb.completion_tokens}")
        print(f"Custo estimado (USD): ${cb.total_cost:.6f}")

if __name__ == "__main__":
    main()
