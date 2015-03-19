num_tickets = 100

print("There are {} tickets available".format(num_tickets))
print("Get your tickets before we sell out!")

tickets_wanted = raw_input("How many tickets would you like?\n")

tickets_wanted = int(tickets_wanted)

# Check that the number of tickets available is less than
# the number of tickets wanted
if tickets_wanted > num_tickets:
    # Tell the user you don't have that many tickets

else:
    # Calculate how many tickets will be left.
    # Tell the user how many tickets they've bought.
    # Tell the user how many tickets are avaliable.
