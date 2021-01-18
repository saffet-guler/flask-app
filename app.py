from flask import Flask
from flask import request
app = Flask(__name__)

@app.route('/home') # burdaki /home end pointtir
def index():
    return "Hello Flask"
@app.route('/users/<user_id>', methods = ['GET', 'POST', 'PUT', 'DELETE'])
def parameter(user_id):
    if request.method == 'GET':
        return 'GET method'

    elif request.method == 'POST':
        data = request.form
        return data

    elif request.method == 'PUT':
        return 'Put method'

    elif request.method == 'DELETE':
        return 'Delete method'

    else:
        return 'Not allowed method'

    return user_id

app.run()

# app.run(host='localhost', port=81)
# host = "localhost" yazarlarsa
# çıkan url'nin sonuna /home ilave ederlerse istenen tüm portlar aktif oluyor.