import json
import random
from pathlib import Path

from flask import Flask, jsonify, render_template, request

app = Flask(__name__)

QUESTIONS_FILE = Path(__file__).parent / "data" / "questions.json"
# Estructura: {"slug": {"label": "Nombre visible", "questions": ["...", ...]}}
CATEGORIES = json.loads(QUESTIONS_FILE.read_text(encoding="utf-8"))


@app.get("/")
def index():
    labels = {slug: data["label"] for slug, data in CATEGORIES.items()}
    return render_template("index.html", categories=labels)


@app.get("/question/")
def question():
    slug = request.args.get("category")
    if slug:
        if slug not in CATEGORIES:
            return jsonify(error=f"Categoría desconocida: {slug}"), 404
        pool = [(slug, q) for q in CATEGORIES[slug]["questions"]]
    else:
        pool = [(s, q) for s, d in CATEGORIES.items() for q in d["questions"]]

    category, text = random.choice(pool)
    return jsonify(category=category, question=text)


def main():
    app.run(debug=True)


if __name__ == "__main__":
    main()
