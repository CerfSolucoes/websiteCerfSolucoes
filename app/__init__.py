from flask import Flask, render_template

def create_app():
    app = Flask(__name__)
    app.secret_key = 'secret'

    # Importa e registra os blueprints
    from .main import main as main_bp
    from .admin import admin as admin_bp

    app.register_blueprint(main_bp)
    app.register_blueprint(admin_bp, url_prefix='/admin')

    # Handler global para erro 404
    @app.errorhandler(404)
    def pagina_nao_encontrada(error):
        return render_template("404.html"), 404
    
    return app
