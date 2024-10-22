from app import app, db
from app.routes.auth_routes import auth_routes

app.register_blueprint(auth_routes, url_prefix="/")

with app.app_context():
  db.create_all()

if __name__ == "__main__":
  app.run(debug=True)
