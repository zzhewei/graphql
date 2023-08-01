from appsample import create_app

blueprints = ['appsample.controller.auth:auth']
app = create_app('development', blueprints)
