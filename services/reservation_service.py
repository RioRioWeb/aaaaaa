from extensions import db
from models.car import Car
from models.reservation import Reservation
from datetime import datetime


def get_cars():
	return Car.query.order_by(Car.id).all()


def create_reservation(data: dict) -> Reservation:
	# assumes data contains parsed `scheduled_at` as datetime
	r = Reservation(
		car_id=int(data["car_id"]),
		scheduled_at=data["scheduled_at"],
		last_name=data["last_name"],
		first_name=data["first_name"],
		phone=data["phone"],
		email=data["email"],
	)
	db.session.add(r)
	db.session.commit()
	return r

