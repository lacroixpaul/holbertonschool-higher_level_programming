from flask import Flask, render_template, request
import json
import csv 

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/contact')
def contact():
    return render_template('contact.html')

@app.route('/items')
def items():
    with open('items.json', 'r') as file:
        data = json.load(file)
    items_data = data.get("items", [])
    return render_template('items.html', items=items_data)


def read_json(file_path):
    with open(file_path, 'r') as file:
        return json.load(file)

def read_csv(file_path):
    products = []
    with open(file_path, 'r') as file:
        reader = csv.DictReader(file)
        for row in reader:
            row['id'] = int(row['id'])
            row['price'] = float(row['price'])
            products.append(row)
    return products

@app.route('/products')
def products():
    source = request.args.get('source')
    product_id = request.args.get('id')
    
    if source == 'json':
        file_path = 'products.json'
        products_list = read_json(file_path)
    elif source == 'csv':
        file_path = 'products.csv'
        products_list = read_csv(file_path)
    else:
        return render_template('product_display.html', error="Wrong source")
    
    if product_id:
        product_id = int(product_id)
        products_list = [product for product in products_list if product['id'] == product_id]
        if not products_list:
            return render_template('product_display.html', error="Product not found")

    return render_template('product_display.html', products=products_list)


if __name__ == '__main__':
    app.run(debug=True, port=5000)
