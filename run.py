from app import app, db
from app.routes.auth_routes import auth_routes

app.register_blueprint(auth_routes, url_prefix="/")

if __name__ == "__main__":
  db.create_all()
  app.run(debug=True)
