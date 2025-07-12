🛠️ DevilLint CLI
🔧 CLI para criação de projetos base, geração de documentação técnica e auditoria de boas práticas.
Ideal para desenvolvedores que desejam iniciar projetos com qualidade, consistência e rapidez.

GPT personalizado

🚀 Instalação
git clone https://github.com/mandresoeiro/devillint-cli.git
cd devillint-cli
pip install -e .
Requer: Python 3.9+ e pip instalado.

💻 Comandos disponíveis
devillint init
📦 Cria um projeto base estruturado com boas práticas.

devillint lint
🔍 Executa checagens de estilo e boas práticas em projetos existentes.

devillint audit
🧠 Audita o projeto em busca de problemas estruturais e sugere melhorias.

devillint generate-docs
📘 Gera documentação técnica automatizada no padrão MkDocs.

📦 Estrutura esperada
devillint_cli_project/
│
├── devillint/
│   ├── __init__.py
│   ├── check.py
│   ├── audit.py
│   ├── generate.py
│   └── init.py
│
├── templates/
│   └── base_project/
│
├── README.md
├── .gitignore
├── pyproject.toml
└── setup.cfg
🧪 Exemplo de uso
devillint init
cd meu_novo_projeto
devillint lint
devillint audit
devillint generate-docs
🧠 GPT Personalizado
Essa CLI é acompanhada por um GPT especializado em revisão de projetos, pronto para revisar e sugerir melhorias diretamente no seu repositório.

🤝 Contribuindo
Sinta-se à vontade para abrir issues ou enviar pull requests com sugestões e melhorias.

📜 Licença
MIT © 2025 — @mandresoeiro
