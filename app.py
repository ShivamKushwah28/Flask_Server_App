from flask import Flask, render_template,request

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('home.html')


@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/services')
def services():
    return render_template('services.html')

@app.route('/contacts')
def contacts():
    return render_template('contacts.html')
@app.route('/prediction')
def prediction():
    return render_template('prediction.html')

@app.route('/client1')
def client1():
    return render_template('client1.html')


@app.route('/client2')
def client2():
    return render_template('client2.html')

@app.route('/contact_us')
def contact_us():
    return render_template('contact_us.html')


@app.route('/submit', methods=['POST'])
def submit():
    cc_num = request.form['cc_num']
    print("******************")
    print("******************")
    print(cc_num)    # Handle the form data as needed
    return render_template('prediction.html', success=True)


if __name__ == '__main__':
    app.run(debug=True)
