from models.reservation import Reservation


def get_reservation_by_customer(last_name: str, first_name: str, phone: str):
    if not last_name or not first_name or not phone:
        return None

    return (
        Reservation.query
        .filter_by(
            last_name=last_name.strip(),
            first_name=first_name.strip(),
            phone=phone.strip(),
        )
        .first()
    )


def get_reservation_by_id(reservation_id: int):
    return Reservation.query.get(reservation_id)
