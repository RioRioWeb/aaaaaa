from datetime import datetime
from extensions import db


class Reservation(db.Model):
	__tablename__ = "reservations"

	id = db.Column(db.Integer, primary_key=True)
	car_id = db.Column(db.Integer, db.ForeignKey("cars.id"), nullable=False)
	scheduled_at = db.Column(db.DateTime, nullable=False)

	last_name = db.Column(db.String(64), nullable=False)
	first_name = db.Column(db.String(64), nullable=False)
	phone = db.Column(db.String(32), nullable=False)
	email = db.Column(db.String(120), nullable=False)

	created_at = db.Column(db.DateTime, default=datetime.utcnow)

	car = db.relationship("Car", backref=db.backref("reservations", lazy=True))

	def __repr__(self) -> str:
		return f"<Reservation id={self.id} car_id={self.car_id} at={self.scheduled_at}>"

