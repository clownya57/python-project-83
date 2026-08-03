import os

from dotenv import load_dotenv
from flask import (
    Flask,
    abort,
    flash,
    redirect,
    render_template,
    request,
    url_for,
)

from page_analyzer import db
from page_analyzer.url_utils import is_valid_url, normalize_url

load_dotenv()

app = Flask(__name__)
app.config["SECRET_KEY"] = os.getenv(
    "SECRET_KEY",
    "development-secret-key",
)

@app.get("/")
def index():
    return render_template(
        "index.html",
        url="",
    )

@app.get("/urls")
def urls_index():
    urls = db.get_urls()

    return render_template(
        "urls/index.html",
        urls=urls,
    )

@app.post("/urls")
def urls_create():
    entered_url = request.form.get("url", "").strip()

    if not is_valid_url(entered_url):
        flash("Некорректный URL", "danger")

        return (
            render_template(
                "index.html",
                url=entered_url,
            ),
            422,
        )

    normalized_url = normalize_url(entered_url)
    existing_url = db.get_url_by_name(normalized_url)

    if existing_url:
        flash("Страница уже существует", "info")

        return redirect(
            url_for(
                "urls_show",
                url_id=existing_url["id"],
            )
        )

    new_url = db.create_url(normalized_url)

    flash("Страница успешно добавлена", "success")

    return redirect(
        url_for(
            "urls_show",
            url_id=new_url["id"],
        )
    )

@app.get("/urls/<int:url_id>")
def urls_show(url_id):
    url = db.get_url(url_id)

    if url is None:
        abort(404)

    return render_template(
        "urls/show.html",
        url=url,
    )
