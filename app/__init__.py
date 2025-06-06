from flask import Flask

def create_app():
    app = Flask(__name__)
    app.config.from_object('config.Config')

    # Registrar blueprints
    from app.routes import main_bp
    app.register_blueprint(main_bp)

    return app
# Crear instancia de la aplicación para Gunicorn
app = create_app()  # <-- Esta línea adicional es crucial