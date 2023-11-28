from flask import Flask, render_template, request

app = Flask(__name__)


@app.route('/')
def index():
    return render_template('home.html')


@app.route('/ejercicio1', methods=['GET', 'POST'])
def ejercicio1():
    nombre = ""
    total_sin_descuento = 0
    descuento = 0
    total_con_descuento = 0

    if request.method == 'POST':
        nombre = request.form['nombre']
        edad = int(request.form['edad'])
        tarros_pintura = int(request.form['tarros_pintura'])

        # Calcular el total sin descuento
        total_sin_descuento = tarros_pintura * 9000

        # Calcular el descuento según la edad
        if 18 <= edad <= 30:
            descuento = 0.15
        elif edad > 30:
            descuento = 0.25
        else:
            descuento = 0

        # Calcular el total a pagar con descuento
        total_con_descuento = total_sin_descuento * (1 - descuento)

    return render_template('ejercicio1.html', nombre=nombre, total_sin_descuento=total_sin_descuento,
                           descuento=descuento, total_con_descuento=total_con_descuento)


@app.route('/ejercicio2', methods=['GET', 'POST'])
def ejercicio2():
    if request.method == 'POST':
        usuario = request.form['usuario']
        contrasena = request.form['contrasena']

        # Verificar el usuario y la contraseña
        usuarios = {'juan': 'admin', 'pepe': 'user'}

        if usuario in usuarios and usuarios[usuario] == contrasena:
            mensaje = f"Bienvenido {'administrador' if usuario == 'juan' else 'usuario'} {usuario}"
        else:
            mensaje = "Usuario o contraseña incorrectos"

        return render_template('ejercicio2.html', mensaje=mensaje)

    return render_template('ejercicio2.html')


if __name__ == '__main__':
    app.run(debug=True)
