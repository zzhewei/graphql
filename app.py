from main import create_app

blueprints = ["main.controller.auth:auth"]
app = create_app("development", blueprints)
