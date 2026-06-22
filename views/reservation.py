from flask import Blueprint, render_template, request, redirect, url_for, session
from datetime import datetime, date

from services.reservation_service import get_cars, create_reservation

reservation_bp = Blueprint("reservation", __name__, url_prefix="/reservation")


def _get_session_data():
	return session.setdefault("reservation", {})


@reservation_bp.route("/select", methods=["GET", "POST"])
def select():
	if request.method == "GET":
		cars = get_cars()
		data = _get_session_data()
		return render_template("reservation/select.html", cars=cars, data=data)
	
	if request.method == "POST":
		data = _get_session_data()
		data["car_id"] = request.form.get("car_id")
		data["reservation_date"] = datetime.fromisoformat(request.form.get("reservation_date")).date()
		data["reservation_time"] = request.form.get("reservation_time")
		session.modified = True
		return redirect(url_for("reservation.customer"))


@reservation_bp.route("/customer", methods=["GET", "POST"])
def customer():
	if request.method == "GET":
		data = _get_session_data()
		return render_template("reservation/customer.html", data=data)

	if request.method == "POST":
		data = _get_session_data()
		data["last_name"] = request.form.get("last_name")
		data["first_name"] = request.form.get("first_name")
		data["phone"] = request.form.get("phone")
		data["email"] = request.form.get("email")
		session.modified = True
		return redirect(url_for("reservation.confirm"))


@reservation_bp.route("/confirm", methods=["GET", "POST"])
def confirm():
	data = _get_session_data()
	
	if request.method == "GET":
		cars = get_cars()
		car_name = None
		try:
			cid = int(data.get("car_id")) if data.get("car_id") else None
			for c in cars:
				if c.id == cid:
					car_name = c.name
		except Exception:
			car_name = None
		return render_template("reservation/confirm.html", data=data, car_name=car_name)

	if request.method == "POST":
		payload = {
			"car_id": data.get("car_id"),
			"reservation_date": data.get("reservation_date"),
			"reservation_time": data.get("reservation_time"),
			"last_name": data.get("last_name"),
			"first_name": data.get("first_name"),
			"phone": data.get("phone"),
			"email": data.get("email"),
		}
		create_reservation(payload)
		session.pop("reservation", None)
		return redirect(url_for("reservation.complete"))

@reservation_bp.route("/complete", methods=["GET"])
def complete():
	return render_template("reservation/complete.html")

