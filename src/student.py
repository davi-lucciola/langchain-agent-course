import json
from typing import List
import pandas as pd
from pydantic import BaseModel, Field
from langchain.tools import BaseTool
from langchain_openai import ChatOpenAI
from langchain.prompts import PromptTemplate
from langchain_core.output_parsers import JsonOutputParser

from utils import OPENAI_API_KEY, get_path


def get_student_data_by_name(name: str):
    student_db = pd.read_csv(get_path("./docs/estudantes.csv"))
    student_data = student_db[student_db["USUARIO"] == name]

    if student_data.empty:
        return {}

    return student_data.iloc[:1].to_dict()


class StudentExtractor(BaseModel):
    name: str = Field(
        "Nome do estudante informado sempre em letras minúsculas. Exemplo: joão, carlos, joana, carla"
    )


class StudentDataTool(BaseTool):
    name: str = "StudentDataTool"
    description: str = """
    Esta ferramenta extrai os dados de um estudante e suas preferências.
    - Ela recebe o nome do estudante como entrada. 
    - A entrada deve conter somente o nome, sem caracteres especiais ou de caracteres escape.
    """

    def _run(self, input: str) -> str:
        student_name: str = input.strip().lower()
        student = get_student_data_by_name(student_name)

        return json.dumps(student)


class Score(BaseModel):
    value: float = Field("Valor da nota")
    discipline: str = Field("Nome da diciplina da nota")


class StudentAcademicProfile(BaseModel):
    student: str = Field("Nome do Estudante")
    finish_year: int = Field("Ano de Conclusão")
    resume: str = Field(
        "Resumo das principais características desse estudante de forma a torna-lo único para a faculdade. Exemplo: Só esse estudante fez/é/gosta de..."
    )
    notas: List[Score] = Field("Lista de notas das diciplinas e áreas do conhecimento")


class AcademicProfileTool(BaseTool):
    name: str = "AcademicProfileTool"
    description: str = """
    Cria um perfil acadêmico de um estudante.
    Esta ferramenta requer como entrada todos os dados de um estudante 
    que precisam ser resgatados através ferramenta "StudentDataTool" antes de ser utilizada.
    """

    def _run(self, input: str) -> str:
        parser = JsonOutputParser(pydantic_object=StudentAcademicProfile)

        prompt = PromptTemplate(
            template="""
            Você é um consultor de carreira e precisa indicar com detalhes, riqueza, mas direto ao ponto 
            para o estudante e faculdade as opções e conquências possiveis.
            Considere as instruções listadas abaixo e os dados do estudante (em <DadosEstudante>).

            - Formate o estudante para seu perfil acadêmico. 
            - Com os dados, identifique as opções de universidades sugeridas e cursos compativeis com o interesse do aluno.
            - Destaque o perfil do aluno dando enfase principalmente naquilo que faz sentido para as instituições de interesse do aluno.
            
            <DadosEstudante>
            {student_data}
            </DadosEstudante>

            {output_format}
            """,
            input_variables=["student_data"],
            partial_variables={"output_format": parser.get_format_instructions()},
        )

        llm = ChatOpenAI(api_key=OPENAI_API_KEY, model="gpt-4.1-nano")

        chain = prompt | llm | parser
        academic_profile = chain.invoke({"student_data": input})

        return academic_profile
