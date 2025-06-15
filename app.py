from flask import Flask, render_template, request, redirect, flash 
from classes.additionalservice import AdditionalService
from classes.employee import Employee
from classes.glamping import Glamping
from classes.guest import Guest
from classes.hosting import Hosting
from classes.person import Person
from classes.reservation import Reservation


app = Flask(__name__)
app.secret_key = 'polaris1113'

personArray = []
employeeArray = []
guestArray = []


# Init
@app.route("/")
def initiate():
    return render_template("UI.html")

# Forms getters
@app.route("/processPerson", methods=["POST"])
def processPerson():
    name = request.form.get("name")
    phone = request.form.get("phone")
    email = request.form.get("email")
    identification = request.form.get("identification")

    newPerson = Person(name, phone, email, identification)

    personArray.append(newPerson)
    flash("✅ Person registered successfully!")

    return redirect("/create-person")

@app.route("/processEmployee", methods=["POST"])
def process_employee():
    person_id = request.form.get("person_id")
    position = request.form.get("position")
    wage = request.form.get("wage")
    entryDate = request.form.get("entryDate")

    person = next((p for p in personArray if p.identification == person_id), None)

    if not person:
        return "Person not found", 404

    try:
        newEmployee = Employee(
            person=person,
            position=position,
            wage=int(wage), 
            entryDate=entryDate
        )
        employeeArray.append(newEmployee)
        flash("✅ Employee registered successfully!")

        return redirect("/create-employee")

    except ValueError as error:
        return f"Error registering employee: {error}", 400


# List registers calls

@app.route("/registersPerson")
def showPersonRegisters():
    return render_template("listPerson.html", persons=personArray)


@app.route("/registersEmployee")
def showEmployeeRegisters():
    return render_template("listEmployee.html", employees=employeeArray)

# Nav calls
@app.route('/create-additional-service')
def create_additional_service():
    return render_template('createAdditionalService.html')

@app.route('/create-employee')
def create_employee():
    return render_template('createEmployee.html', personArray=personArray, employeeArray = employeeArray)

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

# Debug mode
if __name__ == "__main__":
    app.run(debug=True)