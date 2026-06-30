from flask import Blueprint, render_template, session

top_bp = Blueprint("top", __name__)


@top_bp.route("/")
def index():
	session.pop("reservation", None)
	session.pop("inquiry", None)
	return render_template("top.html")
