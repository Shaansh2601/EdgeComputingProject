from database import db_session
from models import Product


def detection(product_name,sr_no):

    if product_name == "herbal-cream-100-gm":
        sr_no = sr_no
        product_id = 122
        name_of_product = "Herbal Cream 100gm"
        quantity = 1
        cost_of_product = 75
        new_product = Product(sr_no, product_id, name_of_product, quantity, cost_of_product)
        db_session.add(new_product)
        db_session.commit()

    elif product_name == "colgate-50gm":
        sr_no = sr_no
        product_id = 126
        name_of_product = "Colgate 50gm"
        quantity = 1
        cost_of_product = 75
        new_product = Product(sr_no, product_id, name_of_product, quantity, cost_of_product)
        db_session.add(new_product)
        db_session.commit()

    elif product_name == "joy-skin-cream-15ml":
        sr_no = sr_no
        product_id = 243
        name_of_product = "Joy Skin Cream 15ml"
        quantity = 1
        cost_of_product = 20

        new_product = Product(sr_no, product_id, name_of_product, quantity, cost_of_product)
        db_session.add(new_product)
        db_session.commit()

    elif product_name == "colgate-100gm":
        sr_no = sr_no
        product_id = 221
        name_of_product = product_name
        quantity = 1
        cost_of_product = 50

        new_product = Product(sr_no, product_id, name_of_product, quantity, cost_of_product)
        db_session.add(new_product)
        db_session.commit()