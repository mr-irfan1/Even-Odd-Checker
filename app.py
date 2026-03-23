from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def home():
    result = ""
    if request.method == 'POST':
        num = int(request.form['number'])
        if num % 2 == 0:
            result = f"The number {num} is Even"
        else:
            result = f"The number {num} is Odd"
    return render_template('index.html', result=result)

if __name__ == '__main__':
    app.run(debug=True, port=5001)