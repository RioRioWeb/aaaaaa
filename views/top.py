from flask import Blueprint, render_template
from flask import session

top_bp = Blueprint("top", __name__)


@top_bp.route("/")
def index():
	session.pop("reservation", None)
	return render_template("top.html")


@top_bp.route("/inquiry/auth")
def inquiry_auth():
	return "予約照会機能は開発未着手", 200
