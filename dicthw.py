# Restaurant menu



restaurant_menu = {
    "Starters": {"Soup": 5.99, "Bruschetta": 6.50},
    "Main Course": {"Steak": 15.99, "Salmon": 13.99},
    "Desserts": {"Cake": 4.99, "Ice Cream": 3.99}
}

restaurant_menu["Beverages"] = "Cream_soda: 3.25", "Orange_juice: 2.99"
restaurant_menu["Main Course"]["Steak"]=17.99
del restaurant_menu["Starters"]["Bruschetta"]
print(restaurant_menu)

# Customer Service Ticket Tracker
# Tracks customer service tickets, each with a unique ID, customer name, issue description, and status (open/closed).
# Implement functions to:
# Open a new service ticket.
# Update the status of an existing ticket  to "closed".
# Display all tickets.
#   (Bonus) filter by status
# Initialize with some sample tickets and include functionality for additional ticket entry.

service_tickets = {
    "Ticket001": {"Customer": "Alice", "Issue": "Login problem", "Status": "open"},
    "Ticket002": {"Customer": "Bob", "Issue": "Payment issue", "Status": "closed"}
}

service_tickets["Ticket001"]["Status"] = "closed"
new_service_ticket = {
    "Ticket003": {"ID#": "Cumflywus2", "Customer":"James Brown", "Issue": "Ticket_Mixup", "Status": input("(open/closed)")},
                  }
print(service_tickets)
print(new_service_ticket)
