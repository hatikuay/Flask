from flask import Blueprint, request, jsonify, render_template, flash, redirect, url_for
from app import db
from app.models import User

auth_routes = Blueprint("auth_routes", __name__)


@auth_routes.route("/", methods=["GET", "POST"])
@auth_routes.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        pass
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
            flash('Kullanıcı adı zaten alınmış!', 'danger')
            return redirect(url_for('auth_routes.register'))
        if User.query.filter_by(email=email).first():
            flash('Bu e-posta adresiyle zaten bir hesap mevcut!', 'danger')
            return redirect(url_for('auth_routes.register'))

        new_user = User(user_name=username, email=email)
        new_user.set_password(password)  # Şifreyi hash'leyip kaydediyoruz

        db.session.add(new_user)
        db.session.commit()

        flash('Başarıyla kayıt oldunuz!', 'success')
        return redirect(url_for('auth_routes.login'))

    return render_template("register.html")
