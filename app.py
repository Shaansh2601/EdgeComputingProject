from flask import Flask, request, render_template, redirect
import pusher
from database import db_session
from models import Product
import faces

app = Flask(__name__)
pusher_client = pusher.Pusher(
        app_id='875481',
        key='8ad4d5b94378b706db99',
        secret='f58778540dddcf583e41',
        cluster='ap2',
        ssl=True)


@app.route('/',methods=['POST','GET'])
def index():
    if request.method=="POST":
        if request.form['Submit_btn'] == 'create_bill':
            faces.start()
        elif request.form['Submit_btn'] == 'checkout':
            pass
        else:
            Product.query.delete()
            db_session.commit()
        return redirect("/", code=302)
    else:
        products = Product.query.all()
        return render_template('index.html', products=products)



@app.route('/backend', methods=["POST", "GET"])
def backend():
    if request.method == "POST":
        sr_no = request.form["sr_no"]
        product_id = request.form["product_id"]
        name_of_product = request.form["name_of_product"]
        quantity = request.form["quantity"]
        cost_of_product = request.form["cost_of_product"]

        new_product = Product(sr_no, product_id, name_of_product,quantity,cost_of_product)
        db_session.add(new_product)
        db_session.commit()

        data = {
            "sr_no": sr_no,
            "product_id": product_id,
            "name_of_product": name_of_product,
            "quantity": quantity,
            "cost_of_product":cost_of_product
        }

        pusher_client.trigger('table', 'new-record', {'data': data})

        return redirect("/backend", code=302)
    else:
        products = Product.query.all()
        return render_template('backend.html', products=products)


@app.route('/edit/<int:id>', methods=["POST", "GET"])
def update_record(id):
    if request.method == "POST":
        sr_no = request.form["sr_no"]
        product_id = request.form["product_id"]
        name_of_product = request.form["name_of_product"]
        quantity = request.form["quantity"]
        cost_of_product = request.form["cost_of_product"]

        update_product = Product.query.get(id)
        update_product.sr_no = sr_no
        update_product.product_id = product_id
        update_product.name_of_product = name_of_product
        update_product.quantity =quantity
        update_product.cost_of_product =cost_of_product
        update_product.final_cost_of_product = int(quantity) * int (cost_of_product)
        db_session.commit()

        data = {
            "sr_no": sr_no,
            "product_id": product_id,
            "name_of_product": name_of_product,
            "quantity": quantity,
            "cost_of_product": cost_of_product
        }

        pusher_client.trigger('table', 'update-record', {'data': data})

        return redirect("/backend", code=302)
    else:
        new_product = Product.query.get(id)

        return render_template('update_product.html', data=new_product)

@app.route('/delete/<int:id1>', methods=["POST", "GET"])
def delete_record(id1):
    Product.query.filter_by(id=id1).delete()
    db_session.commit()
    return redirect('/', code=302)

@app.teardown_appcontext
def shutdown_session(exception=None):
    db_session.remove()
# run Flask app
if __name__ == "__main__":
    app.run()

