from flask import (
    Blueprint,
    request,
    jsonify,
    render_template,
    flash,
    redirect,
    session,
    url_for,
)
from app import db, bcrypt
from app.models import User
from werkzeug.security import check_password_hash

auth_routes = Blueprint("auth_routes", __name__)


@auth_routes.route("/", methods=["GET", "POST"])
@auth_routes.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        user_name = request.form["username"]
        password = request.form["password"]

        if not user_name or not password:
            flash("Lütfen tüm alanları doldurun", "danger")
            return redirect(url_for("auth_routes.login"))

        user = User.query.filter_by(user_name=user_name).first()

        if user and bcrypt.check_password_hash(user.password_hash, password):
            session["user_id"] = user.id
            flash("Başarıyla giriş yaptınız!", "success")
            #return redirect(url_for("auth_routes.login"))
            return render_template("dashboard.html")

        flash("Geçersiz kullanıcı adı veya şifre", "danger")
        return redirect(url_for("auth_routes.login"))

    return render_template("login.html")


@auth_routes.route("/register", methods=["GET", "POST"])
def register():
    if request.method == "POST":
        username = request.form["username"]
        email = request.form["email"]
        password = request.form["password"]
        confirm_password = request.form["confirm_password"]

        if password != confirm_password:
            flash("Şifreler eşleşmiyor", "danger")

        if User.query.filter_by(user_name=username).first():
            flash("Kullanıcı adı zaten alınmış!", "danger")
            return redirect(url_for("auth_routes.register"))
        if User.query.filter_by(email=email).first():
            flash("Bu e-posta adresiyle zaten bir hesap mevcut!", "danger")
            return redirect(url_for("auth_routes.register"))

        new_user = User(user_name=username, email=email)
        new_user.set_password(password)  # Şifreyi hash'leyip kaydediyoruz

        db.session.add(new_user)
        db.session.commit()

        flash("Başarıyla kayıt oldunuz!", "success")
        return redirect(url_for("auth_routes.login"))

    return render_template("register.html")


@auth_routes.route("/logout")
def logout():
    session.pop("user_id", None)
    flash("Başarıyla çıkış yaptınız!", "success")
    return redirect(url_for("auth_routes.login"))
