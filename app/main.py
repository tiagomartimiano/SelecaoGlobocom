from flask import Flask, jsonify, request
from flask_restful import reqparse, abort, Api, Resource
import mariadb
import sys
import json

# Front
app = Flask(__name__)

@app.route('/')
def index()
    return "<center><h1>Flash App deployment on AZURE</h1><center>"

if __name__ == "__main__":
    app.run()   
        
# Connect to MariaDB Platform
try:
    conn = mariadb.connect(
        user="root",
        password="teste",
        host="mariadb",
        port=3306,
        database="materiasglobo"

    )
except mariadb.Error as e:
    print(f"Error connecting to MariaDB Platform: {e}")
    sys.exit(1)
    
cursor=conn.cursor() 
    


app = Flask(__name__)
api = Api(app)

# Comment creation class
class CriaComentarios(Resource):
    def post(self):
        json_data = request.get_json(force=True)
        email = json_data['email'] 
        contentid = json_data['content_id']
        comentario = json_data['comment']
       
        cursor.execute( "INSERT INTO comentarios (email, comentario, idmateria) VALUES (?, ?, ?)",  (email, comentario, contentid))
        conn.commit()

        return {'status':'Criado comentario'}

# Class for listing comments
class ListaComentarios(Resource):
    def get(self, idmateria):
        cursor.execute("select * from comentarios where idmateria=?", (idmateria,))
        columns = [col[0] for col in cursor.description]

        # Montar a lista de dicionários com os resultados
        results = []
        for row in cursor:
            results.append(dict(zip(columns, row)))

        # Gerar a saída JSON
        json_output = json.dumps(results)

        return json_output

class Monitoria(Resource):
    def get(self):
        try:
            conn.ping()
        except:
             return {'status':'False'}
        return {'status':'true'}

api.add_resource(CriaComentarios, '/api/comment/new')
api.add_resource(ListaComentarios, '/api/comment/list/<idmateria>')
api.add_resource(Monitoria, '/api/monitoria')

if __name__ == '__main__':
    app.run(debug=True, host="0.0.0.0")
