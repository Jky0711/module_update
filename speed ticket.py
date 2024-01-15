def speeding_ticket(speed, is_birthday):
    # Adjust speed limits if it's the driver's birthday
    adjustment = 5 if is_birthday else 0

    # Determine the ticket type based on adjusted speed limits
    if speed <= 60 + adjustment:
        return "No Ticket"
    elif 61 <= speed <= 80 + adjustment:
        return "Small Ticket"
    else:
        return "Big Ticket"

print(speeding_ticket(60, False))
print(speeding_ticket(65, True)) 