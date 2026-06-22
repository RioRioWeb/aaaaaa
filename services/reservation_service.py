from extensions import db
from models.car import Car
from models.reservation import Reservation
from datetime import datetime, date as date_cls


def get_cars():
	allowed = ["CX-60", "CX-80"]
	cars = Car.query.filter(Car.name.in_(allowed)).order_by(Car.id).all()
	existing_names = {c.name for c in cars}
	to_create = [name for name in allowed if name not in existing_names]
	for name in to_create:
		c = Car(name=name)
		db.session.add(c)
	if to_create:
		db.session.commit()
		cars = Car.query.filter(Car.name.in_(allowed)).order_by(Car.id).all()
	return cars


def create_reservation(data: dict) -> Reservation:
	r = Reservation(
		car_id=int(data["car_id"]),
		reservation_date=datetime.strptime(data["reservation_date"], '%a, %d %b %Y %H:%M:%S %Z').date(),
		reservation_time=data.get("reservation_time"),
		last_name=data["last_name"],
		first_name=data["first_name"],
		phone=data["phone"],
		email=data["email"],
	)
	db.session.add(r)
	db.session.commit()
	return r

