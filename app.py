from flask import Flask, render_template, request
from classes.person import Person

app = Flask(__name__)


personArray = []


@app.route("/")
def initiate():
    return render_template("UI.html")

@app.route("/processPerson", methods=["POST"])
def process():
    name = request.form.get("name")
    phone = request.form.get("phone")
    email = request.form.get("email")
    identification = request.form.get("identification")

    newPerson = Person(name, phone, email, identification)

    personArray.append({
        "name": newPerson.name,
        "phone": newPerson.phone,
        "email": newPerson.email,
        "identification": newPerson.identification,
    })
    return render_template("listRegister.html", persons=personArray)
    
@app.route("/registersPersons")
def show_registers():
    return render_template("listRegister.html", persons=personArray)

@app.route('/create-additional-service')
def create_additional_service():
    return render_template('createAdditionalService.html')

@app.route('/create-employee')
def create_employee():
    return render_template('createEmployee.html')

@app.route('/create-guest')
def create_guest():
    return render_template('createGuest.html')

@app.route('/create-hosting')
def create_hosting():
    return render_template('createHosting.html')

@app.route('/create-person')
def create_person():
    return render_template('createPerson.html')

@app.route('/create-reservation')
def create_reservation():
    return render_template('createReservation.html')

@app.route('/create-glamping')
def create_glamping():
    return render_template('createGlamping.html')

if __name__ == "__main__":
    app.run(debug=True)