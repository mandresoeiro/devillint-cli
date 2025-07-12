from pathlib import Path
import shutil
import typer

def generate_docs(project_path_str: str):
    """
    📚 Gera documentação Markdown do projeto (estrutura de pastas e checklist).
    """
    project_path = Path(project_path_str).resolve()
    project_name = project_path.name
    output_dir = Path(__file__).parent.parent / "docs" / project_name
    output_dir.mkdir(parents=True, exist_ok=True)

    # 📘 index.md
    index_md = output_dir / "index.md"
    index_md.write_text(
        f"# 📘 Documentação do Projeto `{project_name}`\n\n"
        "Gerado automaticamente pelo DevilLint.\n\n"
        "- [Estrutura do projeto](estrutura.md)\n"
        "- [Checklist de Boas Práticas](checklist.md)\n",
        encoding="utf-8"
    )

    # 🗂️ estrutura.md
    estrutura_md = output_dir / "estrutura.md"
    with estrutura_md.open("w", encoding="utf-8") as f:
        f.write("# 🗂️ Estrutura de Pastas\n\n")
        for path in sorted(project_path.rglob("*")):
            indent = "  " * len(path.relative_to(project_path).parts[:-1])
            name = f"{path.name}/" if path.is_dir() else path.name
            f.write(f"{indent}- `{name}`\n")

    # ✅ checklist.md
    checklist_md = output_dir / "checklist.md"
    checklist_md.write_text(
        "# ✅ Checklist de Boas Práticas\n\n"
        "- [ ] Código está organizado por pastas?\n"
        "- [ ] Existe README.md?\n"
        "- [ ] Estrutura clara e nomeada com sentido?\n"
        "- [ ] Uso de virtualenv ou poetry?\n"
        "- [ ] Testes automatizados presentes?\n",
        encoding="utf-8"
    )

    typer.secho(f"📚 Documentação gerada em: docs/{project_name}/", fg=typer.colors.GREEN)

def create_base_project(project_name: str):
    """
    📦 Cria um projeto base copiando tudo que está em devillint/templates/
    para apps/<project_name>. Evita sobrescrever se já existir.
    """
    base_dir = Path(__file__).resolve().parent.parent          # raiz do projeto
    template_dir = base_dir / "devillint" / "templates"
    target_dir = base_dir / "apps" / project_name

    if target_dir.exists():
        typer.secho(f"⚠️ Projeto '{project_name}' já existe em apps/{project_name}", fg=typer.colors.YELLOW)
        raise typer.Exit(code=1)

    def _ignore(_, names):
        return {".venv", ".git", ".secrets"} & set(names)

    shutil.copytree(template_dir, target_dir, ignore=_ignore)
    typer.secho(f"✅ Projeto base '{project_name}' criado em apps/{project_name}", fg=typer.colors.GREEN, bold=True)
