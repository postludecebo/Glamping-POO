from flask import Flask, render_template, request, redirect, flash 
from classes.additionalservice import AdditionalService
from classes.employee import Employee
from classes.glamping import Glamping
from classes.guest import Guest
from classes.hosting import Hosting
from classes.person import Person
from classes.reservation import Reservation

personArray = []



polaris = Glamping("Polaris Camp", "Colombia")

app = Flask(__name__)
# Debug mode
if __name__ == "__main__":
    app.run(debug=True)
app.secret_key = 'polaris1113'



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
        
        polaris.hireEmployees(newEmployee)
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
        
        polaris.registerGuests(newGuest)
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

    service = next((p for p in polaris.additionalServices if p.name == name), None)

    if service:
        return "Service already registered."
    
    try:
        newService = AdditionalService(
            name=name,
            description=description,
            price=price,
            duration=duration
        )
        
        polaris.additionalServices = newService

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
            disponibility=(disponibility == "true"), 
            season=season
        )
        polaris.addHostings(hosting)
        flash("✅ Hosting registered successfully!")
        return redirect("/create-hosting")

    except ValueError as e:
        flash(f"🚫 Error registering hosting: {e}")
        return redirect("/create-hosting")

@app.route("/processReservation", methods=["POST"])
def processReservation():
    idReservation = request.form.get("idReservation")
    guest_id = request.form.get("guestID")
    hosting_phone = request.form.get("hostingPhone")
    checkIn = request.form.get("dateCheckIn")
    checkOut = request.form.get("dateCheckOut")
    selected_services = request.form.getlist("services")
    state = request.form.get("state")

    guest_obj = next((g for g in polaris.guests if g.identification == guest_id), None)
    hosting_obj = next((h for h in polaris.hostings if h.phone == hosting_phone), None)
    services_obj = [s for s in polaris.additionalServices if s.name in selected_services]


    if not checkIn or not checkOut:
        flash("🚫 Both check-in and check-out dates are required.")
        return redirect("/create-reservation")
    if not guest_obj or not hosting_obj:
        flash("🚫 Guest or Hosting not found.")
        return redirect("/create-reservation")
    
    try:
        newReservation = Reservation(
            idReservation=idReservation,
            guest=guest_obj,
            hosting=hosting_obj,
            dateCheckIn=checkIn,
            dateCheckOut=checkOut,
            additionalServices=services_obj,
            totalPrice=0,
            state=state
        )
        newReservation.estimateTotalPrice()
        
        polaris.registerReservation(newReservation)


        flash("✅ Reservation registered successfully!")
        return redirect("/create-reservation")

    except ValueError as e:
        flash(f"🚫 Error registering reservation: {e}")
        return redirect("/create-reservation")



# List registers calls (Estos comments los hice yo Mauro, por si algo 😑)

@app.route("/registersPerson")
def showPersonRegisters():
    return render_template("listPerson.html", persons=personArray)

@app.route("/registersEmployee")
def showEmployeeRegisters():
    return render_template("listEmployee.html", employees=polaris.employees)

@app.route("/registersGuest")
def showGuestRegisters():
    return render_template("listGuest.html", guests=polaris.guests)

@app.route("/registersAdditionalService")
def showAdditionalServices():
    return render_template("listAdditionalService.html", additionalServices=polaris.additionalServices)

@app.route("/registersHosting")
def showHostings():
    return render_template("listHosting.html", hostings=polaris.hostings)

@app.route("/registersReservation")
def showReservations():
    return render_template("listReservation.html", reservations=polaris.reservations)

@app.route("/registersGlamping")
def showGlampings():
    return render_template("listGlamping.html", glampings=[polaris])

# Nav calls
@app.route('/create-additional-service')
def create_additional_service():
    return render_template('createAdditionalService.html', additionalServices=polaris.additionalServices)

@app.route('/create-employee')
def create_employee():
    return render_template('createEmployee.html', personArray=personArray, employeeArray = polaris.employees)

@app.route('/create-guest')
def create_guest():
    return render_template('createGuest.html', personArray=personArray, guests=polaris.guests)

@app.route('/create-hosting')
def create_hosting():
    return render_template('createHosting.html', hostings=polaris.hostings)

@app.route('/create-person')
def create_person():
    return render_template('createPerson.html')

@app.route('/create-reservation')
def create_reservation():
    return render_template('createReservation.html', reservations=polaris.reservations, guests=polaris.guests, hostings=polaris.hostings, additionalServices=polaris.additionalServices)

@app.route('/create-glamping')
def create_glamping():
    return render_template('createGlamping.html', )

