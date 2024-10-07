#Get the venue details

venue_name = input("What is the name of the venue? ")
venue_capacity = int(input(f"What is {venue_name}'s max seating capacity? "))
ticket_price = float(input("What is the price of each ticket? $"))

#Initialize the number of tickets sold

num_tickets = 0

#List to keep track of individual ticket sales

tickets_sold = []

#Loop to continously sell tickets

while num_tickets < venue_capacity:
    try:
        
#Ask for the number of tickets being sold in this transaction

       tickets = int(input("How many tickets have sold? "))
       if num_tickets + tickets > venue_capacity:
           print(f"Cannot sell {tickets} tickets. It will exceed venue capacity of {venue_name}.")
       else: 

#Add to the total number of tickets sold
            num_tickets += tickets
            #Record this sales
            tickets_sold.append(tickets)
            print(f"We have sold {tickets} tickets. Total tickets sold {num_tickets}")
            print(f"Total revenue: ${num_tickets * ticket_price:.2f}")
    except ValueError:
        print("Please enter a valid number.")
print(f"We are at max capacity with {num_tickets} tickets sold.")
print("Thank you for coming, goodbye.")
