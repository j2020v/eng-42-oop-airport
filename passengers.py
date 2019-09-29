from people import *

class Passenger(People):

    def __init__(self, fname, lname, customer_id):
        super().__init__(fname, lname)
        self.customer_id = customer_id

