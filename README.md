# El Banquito

Preguntas abiertas para charlar con tus amigos a las 4 de la mañana.

## Instalación

    poetry install

## Ejecutar

    poetry run python -m banquito.app

Abre http://127.0.0.1:5000. API: `GET /question/?category=filosofica`

## Formato y lint

    poetry run black .
    poetry run ruff check --fix .

Las preguntas se editan a mano en `banquito/data/questions.json`.

## Despliegue (GitHub Pages)

Cada push a `main` ejecuta `.github/workflows/deploy.yml`: lint, genera la
versión estática (`poetry run python -m banquito.build_static` → `dist/index.html`)
y la publica en GitHub Pages. En producción no existe `/question/`: la página
lleva las preguntas embebidas y elige una al azar en el navegador.

Configuración única: en el repositorio, *Settings → Pages → Source: GitHub Actions*.
