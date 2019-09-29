class Flight:

    def __init__(self, flight_number, destination, origin, time):
        self.flight_number = flight_number
        self.destination = destination
        self.origin = origin
        self.time = time
        self.passenger_list = []


    def get_destination(self):
        return self.destination

    def get_origin(self):
        return self.origin

    def get_passengers(self):
        return self.passenger_list

    def get_time(self):
        return self.time

    def get_passport(self):
        passport_no = []
        for passenger in self.passenger_list:
            passport_no.append(passenger.customer_id)
        return passport_no

    def flight_details(self):
        all_pass = []
        for passenger in self.passenger_list:
            all_pass.append(passenger.fullname())
        return f'{self.flight_number} is going to {self.get_destination()} from {self.get_origin()}. Flight time: {self.time}'\
    f' Calling all passengers: {all_pass} {self.get_passport()}'

    def add_passenger(self, *passengers): # *args is used to pass a variable number of arguments to a function. Will accept the arguments supplied in the function that are not identified as a list.
        for passenger in passengers:
            self.passenger_list.append(passenger)