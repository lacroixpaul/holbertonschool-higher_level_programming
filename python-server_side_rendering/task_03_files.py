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
    with open(file_path, newline='', encoding='utf-8') as csvfile:
        reader = csv.DictReader(csvfile, quotechar='"')
        data = list(reader)
        if not data:
            print("Data missing")
            return []
        return data

@app.route('/products')
def products():
    source = request.args.get('source')
    product_id = request.args.get('id')
    
    if source == 'json':
        file_path = 'products.json'
        products_data = read_json(file_path)

    elif source == 'csv':
        file_path = 'products.csv'
        products_data = read_csv(file_path)
    else:
        return render_template('product_display.html', error="Wrong source")

    if product_id:
        id_products = []
        for product in products_data:
            if int(product.get('id', 0)) == int(product_id):
                id_products.append(product)
        
        if not id_products:
            products_data = []
            return render_template('product_display.html', products=products_data, error="Product not found")
        else:
            products_data = id_products

        return render_template('product_display.html', products=products_data)


if __name__ == '__main__':
    app.run(debug=True, port=5000)
