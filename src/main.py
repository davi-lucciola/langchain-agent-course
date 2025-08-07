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

academy_agent = AcademyOpenAIAgent()
agent_runner = AgentExecutor(
    agent=academy_agent.agent, tools=academy_agent.tools, verbose=True
)

resposta = agent_runner.invoke({"input": pergunta})

print(resposta["output"])
