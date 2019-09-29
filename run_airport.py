from passengers import *
from flights import *

passenger1 = Passenger('Lebron', 'James', '527499961')
passenger2 = Passenger('Stephen', 'Curry', '637611593')
passenger3 = Passenger('Kobe', 'Bryant', '945234712')

flight1 = Flight('EASYJET123', 'Amsterdam', 'Paris', '1 hour 30')
flight2 = Flight('RYANAIR760', 'Alicante', 'London', '2 hours')
flight3 = Flight('NORWEGIAN747', 'Sweden', 'Lisbon', '4 hours')

trip1 = flight1.add_passenger(passenger3)
trip2 = flight2.add_passenger(passenger2)
trip3 = flight3.add_passenger(passenger1)

for flight in (flight1, flight2, flight3):
    print(flight.flight_details())


