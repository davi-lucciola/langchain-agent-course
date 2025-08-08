import dotenv as env
from agent import AcademyOpenAIAgent
from langchain.agents import AgentExecutor

env.load_dotenv()

pergunta = "Quais os dados da Ana?"
pergunta = "Quais os dados da Bianca?"
pergunta = "Quais os dados de Ana e Bianca?"
pergunta = "Crie um perfil acadêmico para a Ana!"
pergunta = "Crie um perfil acadêmico para a bianca e para a brenda e compare-os!"
pergunta = "Tenho sentido Ana desanimada com cursos de matématica. Seria uma boa parear ela com a Bianca?"
pergunta = "Tenho sentido Ana desanimada com cursos de matématica. Seria uma boa parear ela com o Marcos?"
pergunta = "Quais os dados da usp?"
pergunta = "Quais os dados do uNI camP?"
pergunta = "Dentre a USP e UFRJ, qual você recomenda para a aluna Ana?"
pergunta = "Dentre uni camp e USP, qual você recomenda para a Ana?"
pergunta = "Quais as faculdades com melhores chances para a Ana entrar?"
pergunta = "Dentre todas as faculdades existentes, quais as faculdades com melhores chances para a Ana entrar?"

academy_ai = AcademyOpenAIAgent()
agent_runner = AgentExecutor(
    agent=academy_ai.agent, tools=academy_ai.tools, verbose=True
)

resposta = agent_runner.invoke({"input": pergunta})

print(resposta["output"])
