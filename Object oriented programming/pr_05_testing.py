class Train:
    def __init__(self,name,fare,seats):
        self.name = name
        self.fare = fare
        self.seats = seats
        self.seatsNo = []

    def seatsManager(self):
        for i in range(self.seats):
            self.seatsNo.append(i+1)
        print(self.seatsNo)
    def status(self):
        print(f"The name of the train is {self.name}")
        print(f"Seats available in the train are {self.seats}")
    def fareInfo(self):
        print(f"The price of the ticket is: Rs {self.fare}")
    def bookTicket(self):
        if self.seats>0:
            print(f"Your Ticket has been booked. Your seat number is {self.seatsNo[self.seats-1]}")
            self.seats = self.seats - 1
            self.seatsNo.pop()
        else:
            print("Sorry, This train is full.Kindly try in tatkaal")
    def cancelTicket(self,seatNo):
        self.seats = self.seats + 1
        self.seatsNo.append(seatNo)
        self.seatsNo.sort()
        print(self.seatsNo)
        

intercity = Train("InterCity Express: 14015", 90, 4)

intercity.status()
intercity.seatsManager()
intercity.bookTicket()
intercity.bookTicket()
intercity.bookTicket()
intercity.bookTicket()
intercity.bookTicket()
intercity.cancelTicket(1)
intercity.cancelTicket(3)
intercity.cancelTicket(2)
intercity.cancelTicket(4)
intercity.bookTicket()
intercity.bookTicket()
intercity.status()