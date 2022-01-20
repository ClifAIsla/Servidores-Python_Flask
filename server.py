from flask import Flask, render_template

app = Flask(__name__)

"""
@app.route('/play', methods=['GET'])
def index():
    return render_template("index.html", num=3)

@app.route('/play/<int:num>',methods=['GET'])
def generador( num ):
    return render_template("index.html", num = num)
"""

@app.route('/play/<int:num>/<color>',methods=['GET'])
def generador( num, color ):
    return render_template("index.html", num = num, color = color)

if __name__=="__main__":
    app.run(debug=True)







"""
@app.route('/',methods=['GET'])       
def bienbenida():
        return '¡Hola mundo!'

@app.route('/dojo',methods=['GET'])
def bootcamp():
    return '¡Dojo!'

@app.route('/says/<string:nombre>',methods=['GET'])
def saludar( nombre ):
    return f'¡Hola, {nombre}!'

@app.route('/repetir/<int:num>/<string:sujeto>',methods=['GET'])
def repite ( num, sujeto):
    return f'<h1> {sujeto*num} </h1>'

@app.errorhandler(404)
def URL_invalido(e):
    return 'Lo siento! No hay respuesta. Inténtalo otra vez.'
"""