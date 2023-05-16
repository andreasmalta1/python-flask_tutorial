from flask import Blueprint, render_template, request, flash
from werkzeug.security import generate_password_hash, check_password_hash
from .models import User

auth = Blueprint("auth", __name__)


@auth.route("/login", methods=["GET", "POST"])
def login():
    data = request.form
    print(data)
    return render_template("login.html", text="Testing")


@auth.route("/logout")
def logout():
    return render_template("sign_up.html")


@auth.route("/sign-up", methods=["GET", "POST"])
def sign_up():
    if request.method == "POST":
        email = request.form.get("email")
        first_name = request.form.get("firstName")
        password1 = request.form.get("password1")
        password2 = request.form.get("password2")

        if len(email) < 4:
            flash("Email must be greater than 3 characters", category="error")
        elif len(first_name) < 2:
            flash("First name must be greater than 1 character", category="error")
        elif password1 != password2:
            flash("Passowrds don't match", category="error")
        elif len(password1) < 7:
            flash("Passowrds must be at least 8 characters", category="error")
        else:
            new_user = User(email=email, first_name=first_name)
            flash("Account created", category="success")

    return render_template("sign_up.html")
