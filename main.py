from flask import Flask,request,render_template
from utils import car_price



app=Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')


@app.route('/get_data',methods=['POST'])
def get_data():
    data=request.form
    class_object=car_price(data)
    result = class_object.price_prediction()

    return render_template('index.html',prediction=result)

if __name__=='__main__':
    app.run(host='0.0.0.0')