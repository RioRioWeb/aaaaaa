from flask import Flask
from config import Config
from extensions import db
from models.car import Car
from views.reservation import reservation_bp
from views.top import top_bp
from views.inquiry import inquiry_bp


def create_app():
	app = Flask(__name__)
	app.config.from_object(Config)

	db.init_app(app)

	app.register_blueprint(reservation_bp)
	app.register_blueprint(inquiry_bp)
	app.register_blueprint(top_bp)

	with app.app_context():
		db.create_all()
		# Initialize master data
		if not Car.query.first():
			db.session.add_all([Car(name="CX-60"), Car(name="CX-80")])
			db.session.commit()

	return app


if __name__ == "__main__":
	app = create_app()
	app.run(debug=True)

