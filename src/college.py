import pandas as pd
from langchain.tools import BaseTool
from pydantic import BaseModel, Field
from langchain_openai import ChatOpenAI
from langchain.prompts import PromptTemplate
from langchain_core.output_parsers import JsonOutputParser


from utils import OPENAI_API_KEY, get_path


def get_all_colleges():
    student_db = pd.read_csv(get_path("./docs/universidades.csv"))
    return student_db.to_dict()


def get_college_data_by_name(name: str):
    student_db = pd.read_csv(get_path("./docs/universidades.csv"))
    student_data = student_db[student_db["NOME_FACULDADE"] == name]

    if student_data.empty:
        return {}

    return student_data.iloc[:1].to_dict()


class CollegeExtractor(BaseModel):
    name: str = Field("Nome ou sigla da universidade.")


class CollegeDataTool(BaseTool):
    name: str = "CollegeDataTool"
    description: str = """
    Esta ferramenta extrai os dados de uma universidade e suas características.
    - Ela recebe o nome da universidade como entrada. 
    - A entrada deve conter somente o nome, sem caracteres especiais ou de caracteres escape.
    """

    def _run(self, input: str):
        parser = JsonOutputParser(pydantic_object=CollegeExtractor)
        prompt = PromptTemplate(
            template="""
            Extraia da entrada dentro da delimitação "<Input>" o nome a universidade.
            - Caso seja uma sigla (Exemplo: UFMG, USP, MIT) deve retornar tudo em maiusculo
            - Caso seja por extenso, deve retornar em formato de titulo garantindo que somente as preposições não começem com maiúsculo (Exemplo: Technical University of Berlin, University of Sydney)
            
            <Input>
            {input}
            <Input />

            {output_format}
            """,
            input_variables=["input"],
            partial_variables={"output_format": parser.get_format_instructions()},
        )

        llm = ChatOpenAI(api_key=OPENAI_API_KEY, model="gpt-4.1-nano")

        chain = prompt | llm | parser

        college_data = chain.invoke({"input": input})

        college_name: str = college_data["name"]
        college_name = college_name.strip()

        college_data = get_college_data_by_name(college_name)
        return college_data


class AllCollegesDataTool(BaseTool):
    name: str = "CollegesDataTool"
    description: str = """
    Essa ferramenta trás os dados de todas as universidades cadastradas. 
    Não é necessário nenhum parametro de entrada.
    """

    def _run(self, _: str):
        colleges = get_all_colleges()
        return colleges
