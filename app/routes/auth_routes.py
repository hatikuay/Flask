from flask import Blueprint, request, jsonify
from app import db
from app.models import User

auth_routes = Blueprint("auth_routes", __name__)

@auth_routes.route("/")
def login():
  return """<!DOCTYPE html>
<html lang="tr">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Bankacılık Uygulaması - Giriş ve Kayıt</title>
    <!-- Bootstrap CSS CDN -->
    <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.0/dist/css/bootstrap.min.css" rel="stylesheet">
    <link rel="stylesheet" href="style.css">
</head>
<body class="d-flex align-items-center justify-content-center min-vh-100 bg-light">

    <div class="container">
        <div class="row justify-content-center">
            <!-- Login Form -->
            <div class="col-md-6">
                <div class="card shadow-sm p-4 mb-4" id="login-card">
                    <h3 class="text-center mb-4">Giriş Yap</h3>
                    <form>
                        <div class="mb-3">
                            <label for="username" class="form-label">Kullanıcı Adı</label>
                            <input type="text" class="form-control" id="username" placeholder="Kullanıcı Adı" required>
                        </div>
                        <div class="mb-3">
                            <label for="password" class="form-label">Şifre</label>
                            <input type="password" class="form-control" id="password" placeholder="Şifre" required>
                        </div>
                        <button type="submit" class="btn btn-primary w-100">Giriş Yap</button>
                        <p class="text-center mt-3">Hesabınız yok mu? <a href="#register-card">Kayıt Ol</a></p>
                    </form>
                </div>
            </div>

            <!-- Register Form -->
            <div class="col-md-6">
                <div class="card shadow-sm p-4 mb-4" id="register-card">
                    <h3 class="text-center mb-4">Kayıt Ol</h3>
                    <form>
                        <div class="mb-3">
                            <label for="name" class="form-label">Adınız</label>
                            <input type="text" class="form-control" id="name" placeholder="Adınız" required>
                        </div>
                        <div class="mb-3">
                            <label for="email" class="form-label">Email</label>
                            <input type="email" class="form-control" id="email" placeholder="Email" required>
                        </div>
                        <div class="mb-3">
                            <label for="register-password" class="form-label">Şifre</label>
                            <input type="password" class="form-control" id="register-password" placeholder="Şifre" required>
                        </div>
                        <div class="mb-3">
                            <label for="confirm-password" class="form-label">Şifre Tekrarı</label>
                            <input type="password" class="form-control" id="confirm-password" placeholder="Şifre Tekrarı" required>
                        </div>
                        <button type="submit" class="btn btn-success w-100">Kayıt Ol</button>
                        <p class="text-center mt-3">Zaten hesabınız var mı? <a href="#login-card">Giriş Yap</a></p>
                    </form>
                </div>
            </div>
        </div>
    </div>

    <!-- Bootstrap JavaScript Bundle with Popper -->
    <script src="https://cdn.jsdelivr.net/npm/bootstrap@5.3.0/dist/js/bootstrap.bundle.min.js"></script>
</body>
</html>"""