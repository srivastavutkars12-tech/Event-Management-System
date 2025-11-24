# Event-Management-System
This is only made for VITyarthi Coellge project under the assistance in Dr.Adyasha Sahu,VIT BHOPAL

A comprehensive, command-line interface (CLI) application built in Python designed to streamline the process of managing events, attendees, and registrations. This system allows organizations to track capacity, manage bookings, and generate reports efficiently.

🚀 Features
Event Administration: Create events with detailed metadata (title, description, date, time, venue, capacity, category).

Attendee Management: Register attendees with personal contact details.

Booking System: Link attendees to events with automatic capacity validation (prevents overbooking).

Search Functionality: Find events by keyword or category.

Reporting: Generate detailed reports showing occupancy rates and attendee lists.

Data Persistence: Save and load the entire system state using JSON files, ensuring data isn't lost between sessions.

Interactive Menu: User-friendly CLI menu for easy navigation.

🛠 Tech Stack
Language: Python 3.x

Libraries:

json (Data storage)

datetime (Date/Time handling)

typing (Type hinting for code clarity)

No external dependencies required.


🔍 Code Explanation
This project is structured around Object-Oriented Programming (OOP) principles to ensure modularity and maintainability.

1. The Data Models (Attendee & Event)
These classes represent the core entities of the system.

Attendee Class:

Stores user details (name, email, phone) and a list of registered_events.

Serialization: Uses to_dict() and from_dict() methods to convert objects into JSON-compatible formats and back.

Event Class:

Stores event details including capacity (max seats) and registered_attendees (list of IDs).

Logic: Includes methods like is_full() to check availability and get_available_seats() to calculate remaining spots.

2. The Controller (EventManagementSystem)
This is the central engine that manages the logic and interaction between Events and Attendees.

ID Generation: Automatically generates unique IDs (e.g., EVT0001, ATT0005) using formatted strings based on the current count of items.

Booking Logic (book_event):

Validates if the Event and Attendee exist.

Checks if the event is_full().

Prevents duplicate bookings (if the user is already registered).

Updates both the Event object (adding the attendee ID) and the Attendee object (adding the event ID).

Data Persistence (save_data, load_data):

Dumps the dictionary representation of all objects into a local event_system_data.json file.

Allows the system to resume exactly where it left off.

3. The Interface (main & display_menu)
main(): Contains the application loop (while True) that keeps the program running until the user chooses to exit.

Input Handling: Captures user input and routes it to the specific methods in the EventManagementSystem.

📊 Workflow Example
Create Event: User adds "Python Workshop" (Capacity: 50).

Register: User adds "John Doe".

Book: User links "John Doe" to "Python Workshop".

Report: System shows 49 seats remaining and lists John Doe in the event report.

Save: Data is written to JSON.


Submitted by:-
Utkarsh Srivastava
