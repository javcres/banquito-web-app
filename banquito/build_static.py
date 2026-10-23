"""Genera dist/index.html, una versión estática para GitHub Pages."""

from pathlib import Path

from flask import render_template

from banquito.app import CATEGORIES, app, category_info

OUTPUT = Path("dist")


def main():
    questions = {slug: data["questions"] for slug, data in CATEGORIES.items()}
    with app.app_context():
        html = render_template(
            "index.html",
            categories=category_info(),
            questions=questions,
            static=True,
        )
    OUTPUT.mkdir(exist_ok=True)
    (OUTPUT / "index.html").write_text(html, encoding="utf-8")
    print(f"Generado {OUTPUT / 'index.html'}")


if __name__ == "__main__":
    main()
