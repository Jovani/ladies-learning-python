num_tickets = 100

print("There are {} ticket(s) left".format(num_tickets))
print("Get your tickets before we sell out!")

tickets_wanted = raw_input("How many tickets would you like?\n")

tickets_wanted = int(tickets_wanted)
num_tickets = num_tickets - tickets_wanted

print("You bought %d ticket(s)".format(tickets_wanted))
print("There are %d ticket(s) left".format(num_tickets))
