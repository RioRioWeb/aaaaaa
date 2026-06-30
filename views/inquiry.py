from flask import Blueprint, render_template, request, redirect, url_for, session
from services.inquiry_service import get_reservation_by_customer, get_reservation_by_id

inquiry_bp = Blueprint("inquiry", __name__, url_prefix="/inquiry")


def _get_session_data():
    return session.setdefault("inquiry", {})


@inquiry_bp.route("/auth", methods=["GET", "POST"])
def auth():
    error = None
    auth_data = _get_session_data()

    if request.method == "GET":
        return render_template("inquiry/auth.html", auth_data=auth_data, error=error)

    if request.method == "POST":
        auth_data["last_name"] = request.form.get("last_name", "").strip()
        auth_data["first_name"] = request.form.get("first_name", "").strip()
        auth_data["phone"] = request.form.get("phone", "").strip()
        session.modified = True

        reservation = get_reservation_by_customer(
            last_name=auth_data["last_name"],
            first_name=auth_data["first_name"],
            phone=auth_data["phone"],
        )

        if reservation:
            auth_data["reservation_id"] = reservation.id
            session.modified = True
            return redirect(url_for("inquiry.detail"))
        else:
            error = "入力された情報に一致する予約が見つかりませんでした。"
            return render_template("inquiry/auth.html", auth_data=auth_data, error=error)


@inquiry_bp.route("/detail")
def detail():
    auth_data = _get_session_data()
    reservation_id = auth_data.get("reservation_id")
    reservation = get_reservation_by_id(reservation_id)

    return render_template("inquiry/detail.html", reservation=reservation)
