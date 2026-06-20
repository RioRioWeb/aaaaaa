from flask import Flask, redirect, url_for
from config import Config
from extensions import db


def create_app():
	app = Flask(__name__)
	app.config.from_object(Config)

	db.init_app(app)

	# register blueprints lazily to avoid circular imports
	from views.reservation import reservation_bp

	app.register_blueprint(reservation_bp)

	@app.route("/")
	def index():
		return redirect(url_for("reservation.select"))

	# create DB tables if they don't exist
	with app.app_context():
		db.create_all()
		# seed sample car data if empty
		from models.car import Car
		if not Car.query.first():
			Car.query.delete()
			Car(name="モデルA")
			Car(name="モデルB")
			db.session.add_all([Car(name="モデルA"), Car(name="モデルB")])
			db.session.commit()

	return app


if __name__ == "__main__":
	app = create_app()
	app.run(debug=True)

