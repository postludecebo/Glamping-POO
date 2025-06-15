from flask import Flask, render_template, request, redirect, flash 
from classes.additionalservice import AdditionalService
from classes.employee import Employee
from classes.glamping import Glamping
from classes.guest import Guest
from classes.hosting import Hosting
from classes.person import Person
from classes.reservation import Reservation


app = Flask(__name__)
# Debug mode
if __name__ == "__main__":
    app.run(debug=True)
app.secret_key = 'polaris1113'

personArray = []
employeeArray = []
guestArray = []
additionalServiceArray = []
hostingArray = []

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
def processEmployee():
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

@app.route("/processGuest", methods=["POST"])
def processGuest():
    person_id = request.form.get("person_id")
    birthDate = request.form.get("birthDate")
    originCountry = request.form.get("originCountry")
    foodPreferences = request.form.get("foodPreferences")

    person = next((p for p in personArray if p.identification == person_id), None)

    if not person:
        return "Person not found", 404

    try:
        newGuest = Guest(
            person=person,
            birthDate=birthDate,
            originCountry=originCountry, 
            foodPreferences=foodPreferences
        )
        guestArray.append(newGuest)
        flash("✅ Guest registered successfully!")

        return redirect("/create-guest")

    except ValueError as error:
        return f"Error registering guest: {error}", 400

@app.route("/processAdditionalService", methods=["POST"])
def processAdditionalService():
    name = request.form.get("name")
    description = request.form.get("description")
    price = request.form.get("price")
    duration = request.form.get("duration")

    service = next((p for p in additionalServiceArray if p.name == name), None)

    if service:
        return "Service already registered."
    
    try:
        newService = AdditionalService(
            name=name,
            description=description,
            price=price,
            duration=duration
        )
        additionalServiceArray.append(newService)
        flash("✅ Additional Service registered successfully!")

        return redirect("/create-additional-service")

    except ValueError as error:
        return f"Error registering additional service: {error}", 400   

@app.route("/processHosting", methods=["POST"])
def process_hosting():
    phone = request.form.get("phone")
    type = request.form.get("type")
    maxCapacity = request.form.get("maxCapacity")
    baseNightPrice = request.form.get("baseNightPrice")
    amenities = request.form.getlist("amenities")  
    disponibility = request.form.get("disponibility")
    season = request.form.get("season")

    try:
        hosting = Hosting(
            phone=phone,
            type=type,
            maxCapacity=int(maxCapacity),
            baseNightPrice=float(baseNightPrice),
            amenities=amenities,
            disponibility=(disponibility.lower() == "true"), 
            season=season
        )
        hostingArray.append(hosting)
        flash("✅ Hosting registered successfully!")
        return redirect("/create-hosting")

    except ValueError as e:
        flash(f"🚫 Error registering hosting: {e}")
        return redirect("/create-hosting")

# List registers calls

@app.route("/registersPerson")
def showPersonRegisters():
    return render_template("listPerson.html", persons=personArray)


@app.route("/registersEmployee")
def showEmployeeRegisters():
    return render_template("listEmployee.html", employees=employeeArray)

@app.route("/registersGuest")
def showGuestRegisters():
    return render_template("listGuest.html", guests=guestArray)

@app.route("/registersAdditionalService")
def showAdditionalServices():
    return render_template("listAdditionalService.html", additionalServices=additionalServiceArray)

@app.route("/registersHosting")
def showHostings():
    return render_template("listHosting.html", hostings=hostingArray)
# Nav calls
@app.route('/create-additional-service')
def create_additional_service():
    return render_template('createAdditionalService.html', additionalServices=additionalServiceArray)

@app.route('/create-employee')
def create_employee():
    return render_template('createEmployee.html', personArray=personArray, employeeArray = employeeArray)

@app.route('/create-guest')
def create_guest():
    return render_template('createGuest.html', personArray=personArray, guests=guestArray)

@app.route('/create-hosting')
def create_hosting():
    return render_template('createHosting.html', hostings=hostingArray)

@app.route('/create-person')
def create_person():
    return render_template('createPerson.html')

@app.route('/create-reservation')
def create_reservation():
    return render_template('createReservation.html')

@app.route('/create-glamping')
def create_glamping():
    return render_template('createGlamping.html')

