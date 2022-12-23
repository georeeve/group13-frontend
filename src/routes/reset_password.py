from flask import Blueprint, render_template, flash, redirect, url_for

reset_password = Blueprint("reset_password", "reset_password")


@reset_password.route("/", methods=["GET"])
def reset_password_get():
    return render_template("reset-password.html")


@reset_password.route("/", methods=["POST"])
def reset_password_post():
    flash("Sent reset request", "info")
    return redirect(url_for("home.items_get"))
