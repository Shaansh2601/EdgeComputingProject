from sqlalchemy import Column, Integer, String
from database import Base

class Product(Base):
    __tablename__ = 'product'
    id = Column(Integer)
    sr_no=Column(String(50))
    product_id = Column(String(50),primary_key=True)
    name_of_product = Column(String(120))
    quantity = Column(String(120))
    cost_of_product=Column(String(120))
    final_cost_of_product=Column(String(50))
    def __init__(self,sr_no,product_id=None, name_of_product=None, quantity=None,cost_of_product=None):
        self.sr_no= sr_no
        self.product_id = product_id
        self.name_of_product = name_of_product
        self.quantity = quantity
        self.cost_of_product = cost_of_product
        self.final_cost_of_product=int(quantity)*int(cost_of_product)

    def __repr__(self):
        return '<Product %r>' % (self.name_of_product)

