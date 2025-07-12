from typer import Typer
import typer
from devillint import check, audit, generate
from devillint.generate import create_base_project  # ⬅️ IMPORTANTE!

app = Typer(help="🎛️ DevilLint CLI – Organização de projetos e geração de documentação")

@app.command()
def lint():
    """✅ Roda black, isort, flake8 e pytest"""
    check.run_all_checks()

@app.command(name="audit-project")
def audit_project():
    """🕵️ Auditoria manual com checklist"""
    audit.run_audit()

@app.command()
def generate_docs(
    path: str = typer.Argument(".", help="📁 Caminho do projeto a documentar")
):
    """📚 Gera documentação Markdown do projeto"""
    generate.generate_docs(path)

@app.command()
def new(project_name: str):
    """📦 Cria um novo projeto base em apps/<project_name>"""
    create_base_project(project_name)

# 👇 ESSENCIAL para funcionar com pyproject.toml
main = app

if __name__ == "__main__":
    app()
