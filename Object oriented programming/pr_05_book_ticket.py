class Train:
    def __init__(self,name,fare,seats):
        self.name = name
        self.fare = fare
        self.seats = seats
    def status(self):
        print(f"The name of the train is {self.name}")
        print(f"Seats available in the train are {self.seats}")
    def fareInfo(self):
        print(f"The price of the ticket is: Rs {self.fare}")
    def bookTicket(self):
        if self.seats>0:
            print(f"Your Ticket has been booked. Your seat number is {self.seats}")
            self.seats = self.seats - 1
        else:
            print("Sorry, This train is full.Kindly try in tatkaal")
    def cancelTicket(self,seatNo):
        if True:
            print(f"Your ticket is cancelled")
            self.seats = self.seats + 1
        else:
            pass

intercity = Train("InterCity Express: 14015", 90, 2)

intercity.status()
# intercity.bookTicket()
# intercity.cancelTicket(1)
# intercity.status()