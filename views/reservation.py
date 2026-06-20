from flask import Blueprint, render_template, request, redirect, url_for, session
from datetime import datetime

from services.reservation_service import get_cars, create_reservation

reservation_bp = Blueprint("reservation", __name__, url_prefix="/reservation")


def _get_session_data():
	return session.setdefault("reservation", {})


@reservation_bp.route("/select", methods=["GET", "POST"])
def select():
	# 車種・日時選択
	if request.method == "POST":
		data = _get_session_data()
		data["car_id"] = request.form.get("car_id")
		scheduled = request.form.get("scheduled_at")
		# parse naive datetime from input
		try:
			data["scheduled_at"] = datetime.fromisoformat(scheduled)
		except Exception:
			data["scheduled_at"] = None
		session.modified = True
		return redirect(url_for("reservation.customer"))

	cars = get_cars()
	return render_template("reservation/select.html", cars=cars)


@reservation_bp.route("/customer", methods=["GET", "POST"])
def customer():
	# お客様情報入力
	if request.method == "POST":
		data = _get_session_data()
		data["last_name"] = request.form.get("last_name")
		data["first_name"] = request.form.get("first_name")
		data["phone"] = request.form.get("phone")
		data["email"] = request.form.get("email")
		session.modified = True
		return redirect(url_for("reservation.confirm"))

	data = _get_session_data()
	return render_template("reservation/customer.html", data=data)


@reservation_bp.route("/confirm", methods=["GET", "POST"])
def confirm():
	data = _get_session_data()
	if request.method == "POST":
		# create reservation
		payload = {
			"car_id": data.get("car_id"),
			"scheduled_at": data.get("scheduled_at"),
			"last_name": data.get("last_name"),
			"first_name": data.get("first_name"),
			"phone": data.get("phone"),
			"email": data.get("email"),
		}
		create_reservation(payload)
		# clear session data
		session.pop("reservation", None)
		return redirect(url_for("reservation.complete"))

	# show confirmation
	return render_template("reservation/confirm.html", data=data)


@reservation_bp.route("/complete", methods=["GET"])
def complete():
	return render_template("reservation/complete.html")

