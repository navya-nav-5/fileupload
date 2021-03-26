from flask import Flask,request

app = Flask(__name__)


@app.route('/')
def upload():
    return render_template("file_upload_form.html")


@app.route('/success', methods=['POST'])
def success():
    print(request.json)
    if request.method == 'POST':
        f = request.files['file']
       # f.save(f.file)
        return  {"message":"success"}


if __name__ == '__main__':
    app.run(debug=True)
