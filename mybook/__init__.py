from flask import Flask,render_template, url_for, request, redirect

from mybook.mytools import insertar_producto_nuevo
from PIL import Image
app = Flask (__name__)




@app.route("/")
def home():
    return render_template(
        "menu/home.html"
        )



@app.route("/login")
def login():
    return render_template(
        "log/login.html"
    )




@app.route("/agregar")
def agregar():
    return render_template(
        "productos/agregar.html"
    )




@app.route("/ver")
def ver():
    productos_array = [["1", "ecomy", "appadmin", "mi apps", "283.994.883.928", "productosImages/ecomyProductsA1.png", "productosImages/ecomyProductsA2.png", "octubre" ],["2", "ecomy", "appadmin", "mi apps", "283.994.883.928",  "productosImages/ecomyProductsA1.png", "productosImages/ecomyProductsA2.png", "octubre" ]]
    return render_template(
        "productos/ver.html",productos_array=productos_array
    )



@app.route("/facturas")
def facturas():
    
    productos_array = [["1", "ecomy", "appadmin", "mi apps" ],["2", "ecomy", "appadmin", "mi apps" ]]
    return render_template(
        "compras/facturas.html" , productos_array=productos_array
    )






@app.route("/enespera")
def enespera():
    
    productos_array = [["1", "ecomy", "appadmin", "mi apps" ],["2", "ecomy", "appadmin", "mi apps" ]]
    return render_template(
        "pedidos/enespera.html",productos_array=productos_array
    )






@app.route("/enproceso")
def enproceso():
    
    productos_array = [["1", "ecomy", "appadmin", "mi apps" ],["2", "ecomy", "appadmin", "mi apps" ]]
    return render_template(
        "pedidos/enproceso.html", productos_array=productos_array
    )





@app.route("/entregados")
def entregados():
    
    productos_array = [["1", "ecomy", "appadmin", "mi apps" ],["2", "ecomy", "appadmin", "mi apps" ]]
    return render_template(
        "pedidos/entregados.html", productos_array=productos_array
    )



@app.route("/quejas")
def quejas():
    
    productos_array = [["1", "ecomy", "appadmin", "mi apps" ],["2", "ecomy", "appadmin", "mi apps" ]]
    return render_template(
        "usuarios/quejas.html",productos_array=productos_array
    )




#funciones
@app.route("/cargar_producto" , methods=['POST'])
def cargar_producto():
    try:
        fotoa = request.files['pic']
        fotob = request.files['pic2']
        name = request.form['namep']
        detalle = request.form['detallep']
        precio = request.form['preciop']
        id_empresa = "id empresa ecomycr"
        print(id_empresa, name, detalle, precio, fotoa, fotob)
        #se debe guardar para despues subirla a la base de datos y hacer backup de imagenes productos y se debe eliminar estas dos fotos luego
        img = Image.open(fotoa)
        img = img.convert('L')
        img.save('outputA12.png')
        
        img = Image.open(fotob)
        img = img.convert('L')
        img.save('outputB12.png')
        
        
    except:
        return "no se agrego nada "