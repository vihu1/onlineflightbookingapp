import tkinter as tk

flights = {
    'F001': {'departure': 'New York', 'destination': 'Los Angeles', 'available_seats': 100},
    'F002': {'departure': 'Chicago', 'destination': 'Miami', 'available_seats': 75},
    # Add more flights as needed
}

bookings = {}

def display_available_flights():
    available_flights_window = tk.Toplevel(root)
    available_flights_window.title("Available Flights")
    for flight_id, flight_info in flights.items():
        flight_label = tk.Label(available_flights_window, text=f"Flight ID: {flight_id}\nDeparture: {flight_info['departure']}\nDestination: {flight_info['destination']}\nAvailable Seats: {flight_info['available_seats']}\n")
        flight_label.pack()

def book_flight():
    book_flight_window = tk.Toplevel(root)
    book_flight_window.title("Book a Flight")
    flight_id_label = tk.Label(book_flight_window, text="Enter the Flight ID:")
    flight_id_label.pack()
    flight_id_entry = tk.Entry(book_flight_window)
    flight_id_entry.pack()
    passenger_name_label = tk.Label(book_flight_window, text="Enter your Name:")
    passenger_name_label.pack()
    passenger_name_entry = tk.Entry(book_flight_window)
    passenger_name_entry.pack()
    book_button = tk.Button(book_flight_window, text="Book", command=lambda: process_booking(flight_id_entry.get(), passenger_name_entry.get()))
    book_button.pack()

def process_booking(flight_id, passenger_name):
    if flight_id in flights and flights[flight_id]['available_seats'] > 0:
        if flight_id not in bookings:
            bookings[flight_id] = []
        bookings[flight_id].append(passenger_name)
        flights[flight_id]['available_seats'] -= 1
        confirmation_window = tk.Toplevel(root)
        confirmation_window.title("Booking Confirmation")
        confirmation_label = tk.Label(confirmation_window, text=f"Booking successful for {passenger_name} on Flight {flight_id}")
        confirmation_label.pack()
    else:
        error_window = tk.Toplevel(root)
        error_window.title("Booking Error")
        error_label = tk.Label(error_window, text="Sorry, the selected flight is not available.")
        error_label.pack()

def display_bookings():
    bookings_window = tk.Toplevel(root)
    bookings_window.title("Bookings")
    for flight_id, passengers in bookings.items():
        flight_label = tk.Label(bookings_window, text=f"Flight ID: {flight_id}\nPassengers: {', '.join(passengers)}\n")
        flight_label.pack()

root = tk.Tk()
root.title("Flight Booking System")

menu_frame = tk.Frame(root)
menu_frame.pack()

display_button = tk.Button(menu_frame, text="Display Available Flights", command=display_available_flights)
display_button.pack()

book_button = tk.Button(menu_frame, text="Book a Flight", command=book_flight)
book_button.pack()

display_bookings_button = tk.Button(menu_frame, text="Display Bookings", command=display_bookings)
display_bookings_button.pack()

exit_button = tk.Button(menu_frame, text="Exit", command=root.quit)
exit_button.pack()

root.mainloop()
