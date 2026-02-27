from flask import Flask, render_template, request, url_for

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('landing.html') # Main Landing Page

@app.route('/venues')
def venues():
    return render_template('venues.html')

@app.route('/catering')
def catering():
    return render_template('catering.html')

@app.route('/visual')
def visual():
    return render_template('visual.html')

@app.route('/architecture')
def architecture():
    return render_template('architecture.html')

@app.route('/onboarding')
def onboarding():
    return render_template('providerdash.html')

@app.route('/contact')
def contact():
    return render_template('contact.html') # New Contact Page

if __name__ == '__main__':
    app.run(debug=True)