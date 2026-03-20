from flask import Flask, render_template, request, redirect # type: ignore
from models import Patient, ClinicQueue

app = Flask(__name__)
clinic = ClinicQueue()

# Home page (view queue)
@app.route('/')
def index():
    patients = clinic.get_all_patients()
    total = clinic.get_total_served()
    return render_template('index.html', patients=patients, total=total)


# Add patient page
@app.route('/add', methods=['GET', 'POST'])
def add_patient():
    if request.method == 'POST':
        name = request.form['name']
        patient = Patient(name)
        clinic.add_patient(patient)
        return redirect('/')
    return render_template('add_patient.html')


# Serve next patient
@app.route('/serve')
def serve():
    clinic.serve_patient()
    return redirect('/')


if __name__ == '__main__':
    app.run(debug=True)