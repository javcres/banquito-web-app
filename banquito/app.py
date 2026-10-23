import json
import random
from pathlib import Path

from flask import Flask, jsonify, render_template, request

app = Flask(__name__)

QUESTIONS_FILE = Path(__file__).parent / "data" / "questions.json"
# Estructura: {"slug": {"label": "Nombre visible", "questions": ["...", ...]}}
CATEGORIES = json.loads(QUESTIONS_FILE.read_text(encoding="utf-8"))


def category_info():
    """Slug -> etiqueta y modo ("normal" por defecto, o "picante")."""
    return {
        slug: {"label": d["label"], "mode": d.get("mode", "normal")}
        for slug, d in CATEGORIES.items()
    }


@app.get("/")
def index():
    return render_template("index.html", categories=category_info())


@app.get("/question/")
def question():
    slug = request.args.get("category")
    mode = request.args.get("mode", "normal")
    if slug:
        if slug not in CATEGORIES:
            return jsonify(error=f"Categoría desconocida: {slug}"), 404
        slugs = [slug]
    else:
        slugs = [s for s, d in CATEGORIES.items() if d.get("mode", "normal") == mode]
        if not slugs:
            return jsonify(error=f"Modo desconocido: {mode}"), 404

    category, text = random.choice(
        [(s, q) for s in slugs for q in CATEGORIES[s]["questions"]]
    )
    return jsonify(category=category, question=text)


def main():
    app.run(debug=True)


if __name__ == "__main__":
    main()
