#importing random for simulating parked time
import random
from time import sleep


class ParkingGarage:

    """
    class ParkingGarage has the following attributes:

    available parking spots (default to 100),
    tickets(stored in a dictionary),
    next ticket is generated per customer.
   

    Attribute types:
    available_spots: integer
    tickets: dictionary
    next_ticket_numnber: integer

    """

    def __init__(self):
        """

        this function initializes the
        ParkingGarage attributes.
        
        """

        self.available_spots = 100
        self.tickets = {}
        self.next_ticket_number = 1


    
    def take_ticket(self, license_plate):

        """
        this function allows a person to get a ticket
        and park their vehicle.
        amount of tickets available is decreased.
        parking spaces available is decreased.

        """
        # this simulates a customer taking a ticket
        if self.available_spots > 0:
            ticket_number = self.next_ticket_number
            self.tickets[ticket_number] = {'license_plate': license_plate, 'entry_time': 0}
      
            self.next_ticket_number += 1
            self.available_spots -= 1
            print(f"Ticket {ticket_number} issued for license plate {license_plate}")
        else:
            print("Sorry, the garage is full.")

    def pay_for_parking(self):

        """
        this function displays total amount due from customer.
        It also displays a msg after user pays
        stating they have 15 minutes to leave.

        """
        while True: 
            """
            this while True statement will
            verify that the ticket number
            matches the license plate.
            
            """

            # if ticket_number in self.tickets:
            #     ticket = self.tickets[ticket_number]
            verify_license_plate = input("Please enter your license plate number to calculate your parking fee: ")

            # self.verify_license_plate = verify_license_plate
            matching_tickets = []
            for ticket_number, ticket in self.tickets.items():
                if ticket['license_plate'] == verify_license_plate:
                    matching_tickets.append(ticket_number)
            if matching_tickets:
                break
            else:
                print("Invalid entry. Please try again.")


        ticket_number = matching_tickets[0]
        ticket = self.tickets[ticket_number]

        # random module used to generate parking rates 
        self.parked_time = random.randint(60, 1440) / 60

        # using sleep function to generate "calculation time"
        print("Please wait for amount due: ")
        print(f"\n.・。.・゜✭・.・✫・゜・。.")
        sleep(3)
        print(".・。.・゜✭・.・✫・゜・。.")
        sleep(2)

        # really random (and probably expensive parking rate)
        self.parking_rate = (self.parked_time * 5 )
        # rate is $5/hr

      
        print(f"\nYou were parked for {round(self.parked_time)} hours.")
        # used 0.2f to calculate rounded number for parking(i.e 7 hours, 5 hours)
        print(f"Total amount due: ${self.parking_rate:0.2f}")

       # simulating customer paying for parking
        while True:
            pay_for_parking = float(input("Please pay for parking: "))
            if pay_for_parking != self.parking_rate:
                print("Card declined. Please try another form of payment.")
            else:
                print(f"\nNow processing your payment")
                print(f"\n.・。.・゜✭・.・✫・゜・。.")
                sleep(2)
                print("Please wait...")
                sleep(2)
                license_plate = verify_license_plate
                del self.tickets[ticket_number]
                self.available_spots += 1
                print(f"\nPayment successfully processed. Please exit within 15 minutes.")
                print(".・。.・゜✭・.・✫・゜・。.")
                sleep(2)
                print("( ´ ∀ `)ノ～ ♡ THANK YOU, COME BACK SOON! ☆.+")

                break

    

def parking_meter():
    
    """
    this simulates the customer paying at the
    parking meter and exiting the garage.
    
    """
    garage = ParkingGarage()


    print("\n｡･:*:･ﾟ★ Welcome to Lenai Luxury Garage! ｡･:*:･ﾟ☆\n")
    print("\tAvailable spots:\t", garage.available_spots)
    print("\n\tParking rate: $5.00 per hour. ")
        # print("\n\tParking fee: $50 for 24 hours")
        # print("\n\tWARNING: Additional $25 fine per hour after 24 hours")
        
    while True:
        choice = input("\nWhat would you like to do?\n1) Park\n2) Pay and Leave\n3) Quit\n").lower()

        if choice == "1" or choice == "park":
            if garage.available_spots > 0:
                print("Current available spots:", garage.available_spots)
                license_plate = input("\nEnter your license plate: ")
                garage.take_ticket(license_plate)
            else:
                print("Sorry, the garage is full.")
            
        elif choice == "2" or choice in ["pay", "p"]:
             garage.pay_for_parking()
            # = int(input("Enter your ticket number: "))
            # # exit_time = int(input("Enter the exit time (in hours): "))
           
            # print("\nThank you for parking with us! Visit us again.")
        
        elif choice == "3" or choice in ["quit", "q", "stop"]:
            break
        
        else:
            print("Invalid choice. Please choose from valid options.")

if __name__ == "__main__":
    parking_meter()
