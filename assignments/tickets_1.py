num_tickets = 100

print "We have %d ticket(s) left" % (num_tickets)
print "Get your tickets before we sell out!"

tickets_wanted = raw_input("How many tickets would you like?\n")

tickets_wanted = int(tickets_wanted)
num_tickets = num_tickets - tickets_wanted

print "You bought %d ticket(s)" % (tickets_wanted)
print "There are %d ticket(s) left" % (num_tickets)



