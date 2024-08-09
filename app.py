from flask import Flask, redirect, render_template

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])

def login():

    if request.method == 'POST':

        username = request.form['username']

        password = request.form['password']



        # Check if the username and password are correct

        if username == 'HASSAN-RAJPUT' and password == 'HELL-INXIDE':

            # Redirect to the specified link if login is successful

            return redirect('https://creepy-jillayne-hassanmaster-56070bbd.koyeb.app')

        else:

            return render_template('index.html')



if __name__ == '__main__':

        app.run(host='0.0.0.0', port=5000)
