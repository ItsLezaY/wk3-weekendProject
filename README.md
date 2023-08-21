Parking Garage Program - Week 3 Weekend Assignment
Created by Kenai Epps and Leza Younan

Leza and I created our own versions of the parking garage program.
We then collectively merged our ideas together.

We had to do some debugging especially with the "Pay For Parking" function
but we eventually got it to work.

Leza: license/ticket validation

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

- Left detailed doc string comments in parking_garage.py


Hope you enjoy the program!

