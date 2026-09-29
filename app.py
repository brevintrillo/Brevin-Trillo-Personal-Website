from flask import Flask, render_template, request, redirect, url_for, flash
from datetime import datetime
import os

app = Flask(__name__)
app.secret_key = os.environ.get("SECRET_KEY", "change-this-secret-key")

PROJECTS = [
    {
        "title": "Personal Portfolio",
        "category": "Web Development",
        "description": "A responsive personal portfolio built with Flask, HTML, CSS and JavaScript.",
        "tags": ["Python", "Flask", "CSS"],
        "link": "#"
    },
    {
        "title": "Photo Gallery",
        "category": "Creative",
        "description": "A clean gallery interface for showcasing favorite photos and memories.",
        "tags": ["UI", "Gallery", "Responsive"],
        "link": "#"
    },
    {
        "title": "Future Project",
        "category": "Coming Soon",
        "description": "This space is ready for another project, business idea or creative work.",
        "tags": ["Ideas", "Build", "Create"],
        "link": "#"
    },
]

@app.context_processor
def inject_globals():
    return {"year": datetime.now().year}

@app.route("/")
def home():
    return render_template("index.html", projects=PROJECTS)

@app.post("/contact")
def contact():
    name = request.form.get("name", "").strip()
    email = request.form.get("email", "").strip()
    message = request.form.get("message", "").strip()

    if not name or not email or not message:
        flash("Please complete all contact fields.", "error")
        return redirect(url_for("home") + "#contact")

    # Replace this section with email/SMTP integration when deploying.
    print(f"[CONTACT] {name} <{email}>: {message}")
    flash("Thanks! Your message was received.", "success")
    return redirect(url_for("home") + "#contact")

@app.route("/admin")
def admin():
    return render_template("admin.html", projects=PROJECTS)

if __name__ == "__main__":
    app.run(debug=True)
