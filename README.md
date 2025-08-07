# LangChain Academic Agent

Este projeto foi desenvolvido como parte do curso de Agentes de AI da Alura. Ele implementa um **Agente Acadêmico** capaz de analisar dados de estudantes e universidades, sugerindo perfis acadêmicos, recomendações de cursos e possíveis combinações de mentorias entre alunos.

## Funcionalidades

- Consulta de dados detalhados de estudantes a partir de um banco de dados CSV.
- Geração de perfis acadêmicos personalizados para cada estudante.
- Sugestão de universidades e cursos compatíveis com o perfil e interesses do aluno.
- Recomendações de pareamento entre estudantes para mentorias ou apoio acadêmico.
- Integração com modelos de linguagem da OpenAI via LangChain.

## Estrutura do Projeto

```text
.
├── src/
│   ├── agent.py                # Implementação do agente principal
│   ├── main.py                 # Script de execução do agente
│   ├── student.py              # Manipulação de dados de estudantes
│   ├── utils.py                # Funções utilitárias
│   └── docs/
│       ├── estudantes.csv      # Base de dados dos estudantes
│       └── universidades.csv   # Base de dados das universidades
├── pyproject.toml              # Configuração e dependências do projeto
├── uv.lock                     # Lockfile de dependências
└── README.md                   # Documentação do projeto
```

## Como Executar

1. **Clone o repositório e instale as dependências:**

   ```sh
   git clone https://github.com/seu-usuario/langchain-agents-course.git
   cd langchain-agents-course
   uv sync  # ou use poetry/pipenv conforme preferir
   ```

2. **Configure suas credenciais da OpenAI:**
   Crie um arquivo `.env` na raiz do projeto e adicione sua chave de API da OpenAI:

   ```env
   OPENAI_API_KEY=your_openai_api_key
   LANGSMITH_API_KEY=your_langsmith_api_key
   ```

3. **Execute o agente:**
   ```sh
   uv run src/main.py
   ```

## Tecnologias Utilizadas

- [LangChain](https://python.langchain.com/)
- [OpenAI API](https://platform.openai.com/)
- [LangSmith](https://www.langchain.com/langsmith)
- [Pandas](https://pandas.pydata.org/)
- Python 3.12+
