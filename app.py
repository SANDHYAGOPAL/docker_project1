from flask import Flask, jsonify, render_template, request
import socket
import json

app = Flask(__name__)


  
# Opening JSON file
f = open('cus.json')
  
# returns JSON object as 
# a dictionary
obj = json.load(f)
customer = obj['data']



# customer =[
#     {
#         'customerID':0,
#         'name': 'Ram',
#         'subscription':'5G'
#     },
#     {
#         'customerID':1,
#         'name': 'sita',
#         'subscription':'4G'
#     },
#     {
#         'customerID':2,
#         'name': 'John',
#         'subscription':'5G'
#     },
#     {
#         'customerID':3,
#         'name': 'Josh',
#         'subscription':'5G'
#     },
#     {
#         'customerID':4,
#         'name': 'Jay',
#         'subscription':'4G'
#     }
    
# ]




@app.route("/")
def amf_network_function(name=None):
    return render_template('amf.html',name=name) 


@app.route("/customers")
def view_subscriber_data():
    return jsonify({'customers':customer})

   

@app.route("/services", methods=['POST'])
def ausf_network_function():
    if request.method == 'POST':
        name = request.form.get("in1")
        pwd = int(request.form.get("in2"))
        for i in range(0,4):
            if name == (customer[i]['name']):
                if pwd == (customer[i]['password']):
                    if customer[i]['Product_&_Services'] == 'Advisor':
                        return render_template('product1.html',name=customer[i]['name'], advisor=customer[i]['subscription_status'],storage='Subscribe',detector='Subscribe',manage='Subscribe')

                    elif customer[i]['Product_&_Services'] == 'Archive Storage':
                        return render_template('product1.html',name=customer[i]['name'], advisor='Subscribe',storage=customer[i]['subscription_status'],detector='Subscribe',manage='Subscribe')

                    elif customer[i]['Product_&_Services'] == 'Anomaly Detector':
                        return render_template('product1.html',name=customer[i]['name'], advisor='Subscribe',storage='Subscribe',detector=customer[i]['subscription_status'],manage='Subscribe')
                
                    elif customer[i]['Product_&_Services'] == 'API Management':
                        return render_template('product1.html',name=customer[i]['name'], advisor='Subscribe',storage='Subscribe',detector='Subscribe',manage=customer[i]['subscription_status'])
                else:
                    return render_template('error1.html',name=name) 
            else:
                    return render_template('error.html',name=name) 

       

if __name__ == '__main__':
    app.run(host='0.0.0.0',port=5000)





