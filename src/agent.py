from typing import List
from langsmith import Client
from college import CollegeDataTool, AllCollegesDataTool
from student import StudentDataTool, AcademicProfileTool
from langchain.tools import BaseTool
from langchain_openai import ChatOpenAI

# from langchain.agents import Tool, create_openai_tools_agent
from langchain.agents import Tool, create_react_agent

from utils import LANGSMITH_API_KEY, OPENAI_API_KEY


# I can use this function to pass to Agent
# def get_tools_agent_prompt(tools: list[Tool]):
#     tool_prompt = "You are a AI Agent and you have tools for use. The tools you can use are described bellow by '- name > description:\n"

#     for tool in tools:
#         tool_prompt += f"- {tool.name} > {tool.description}\n"

#     return tool_prompt


class AcademyOpenAIAgent:
    def __init__(self):
        hub = Client(api_key=LANGSMITH_API_KEY)

        llm = ChatOpenAI(api_key=OPENAI_API_KEY, model="gpt-4.1")

        academy_agent_tools: List[BaseTool] = [
            StudentDataTool(),
            AcademicProfileTool(),
            CollegeDataTool(),
            AllCollegesDataTool(),
        ]

        self.tools = [
            Tool(tool.name, tool._run, tool.description) for tool in academy_agent_tools
        ]
        # self.agent = create_openai_tools_agent(llm, self.tools, prompt)
        # agent = create_openai_tools_agent(llm, tools, get_tools_agent_prompt(tools))

        # React Agent é melhor para debugar, e necessita um  promtp

        prompt = hub.pull_prompt("hwchase17/react")
        # prompt = hub.pull_prompt("hwchase17/openai-functions-agent")

        self.agent = create_react_agent(llm, self.tools, prompt)
