from pathlib import Path
from subprocess import run
from jinja2 import Environment, FileSystemLoader, select_autoescape

ENCODING = "utf-8"

def main(root: Path):
    files = [f.stem for f in root.glob("*.tex")]
    for f in files:
        run(["tectonic", f + ".tex"])
    env = Environment(loader=FileSystemLoader(root / "templates"), autoescape=select_autoescape())
    template = env.get_template("index.html")
    (root / "index.html").write_text(template.render(files=files))

if __name__ == "__main__":
    main(Path("."))
