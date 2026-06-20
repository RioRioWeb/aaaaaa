from extensions import db


class Car(db.Model):
	__tablename__ = "cars"

	id = db.Column(db.Integer, primary_key=True)
	name = db.Column(db.String(128), nullable=False)

	def __repr__(self) -> str:
		return f"<Car id={self.id} name={self.name}>"

