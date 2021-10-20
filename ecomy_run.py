from mybook import app 

if __name__=="__main__":
    app.run(debug = True, port = 2394, host = "0.0.0.0")
    
#insert into compras (id,idFactura, idUser, monto) values (2, "asda","sadsda","asdasds");
#`FechaHora` TIMESTAMP DEFAULT CURRENT_TIMESTAMP, 
#`FechaModif` TIMESTAMP NULL DEFAULT NULL ON UPDATE CURRENT_TIMESTAMP, 