from flask import Flask, render_template, request
from classes.person import Person

app = Flask(__name__)


personArray = []

@app.route("/")
def initiate():
    return render_template("UI.html")

@app.route("/process", methods=["POST"])
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
    
@app.route("/registers")
def show_registers():
    return render_template("listRegister.html", persons=personArray)



if __name__ == "__main__":
    app.run(debug=True)