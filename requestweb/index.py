from flask import *
import requests

app = Flask(__name__, static_folder='', static_url_path='')
@app.route('/',methods = ["GET", "POST"])
def index():
    return app.send_static_file('index.html')

@app.route('/posttest',methods = ["GET", "POST"])
def namepage():
    input_data=request.form["name_data"]
    
    return redirect(url_for('display', data=input_data))

@app.route('/display')
def display():
    # リクエストのヘッダーを取得
    headers = request.headers
    # ヘッダーを辞書として整形
    headers_dict = {key: value for key, value in headers.items()}
    
    data = request.args.get('data')
    url = data
    response = requests.get(url,params={'key':'value'},timeout=1)
   # print(response.raise_for_status())#none
    return render_template('display.html', input_data=response.text,a=response.raise_for_status(),b=response.status_code,c=response.headers,d=headers_dict,e=request.data)

app.run(port=8000, debug=True)
