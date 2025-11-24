"""
Event Management System
A comprehensive system for managing events, attendees, and registrations.

Problem Statement:
Organizations and communities often struggle with managing events efficiently,
tracking registrations, managing capacities, and maintaining attendee records.

Solution:
This system provides a complete event management solution with features for
creating events, registering attendees, tracking capacity, and generating reports.
"""

import json
from datetime import datetime
from typing import List, Dict, Optional

class Attendee:
    """Represents an event attendee"""
    
    def __init__(self, attendee_id: str, name: str, email: str, phone: str):
        self.attendee_id = attendee_id
        self.name = name
        self.email = email
        self.phone = phone
        self.registered_events = []
    
    def to_dict(self) -> Dict:
        return {
            'attendee_id': self.attendee_id,
            'name': self.name,
            'email': self.email,
            'phone': self.phone,
            'registered_events': self.registered_events
        }
    
    @classmethod
    def from_dict(cls, data: Dict):
        attendee = cls(data['attendee_id'], data['name'], data['email'], data['phone'])
        attendee.registered_events = data.get('registered_events', [])
        return attendee


class Event:
    """Represents an event with all its details"""
    
    def __init__(self, event_id: str, title: str, description: str, 
                 date: str, time: str, venue: str, capacity: int, category: str):
        self.event_id = event_id
        self.title = title
        self.description = description
        self.date = date
        self.time = time
        self.venue = venue
        self.capacity = capacity
        self.category = category
        self.registered_attendees = []
    
    def is_full(self) -> bool:
        return len(self.registered_attendees) >= self.capacity
    
    def get_available_seats(self) -> int:
        return self.capacity - len(self.registered_attendees)
    
    def to_dict(self) -> Dict:
        return {
            'event_id': self.event_id,
            'title': self.title,
            'description': self.description,
            'date': self.date,
            'time': self.time,
            'venue': self.venue,
            'capacity': self.capacity,
            'category': self.category,
            'registered_attendees': self.registered_attendees
        }
    
    @classmethod
    def from_dict(cls, data: Dict):
        event = cls(data['event_id'], data['title'], data['description'],
                   data['date'], data['time'], data['venue'], 
                   data['capacity'], data['category'])
        event.registered_attendees = data.get('registered_attendees', [])
        return event


class EventManagementSystem:
    """Main system for managing events and attendees"""
    
    def __init__(self):
        self.events = {}
        self.attendees = {}
    
    def create_event(self, title: str, description: str, date: str, 
                    time: str, venue: str, capacity: int, category: str) -> str:
        """Create a new event"""
        event_id = f"EVT{len(self.events) + 1:04d}"
        event = Event(event_id, title, description, date, time, venue, capacity, category)
        self.events[event_id] = event
        print(f"✓ Event created successfully! Event ID: {event_id}")
        return event_id
    
    def register_attendee(self, name: str, email: str, phone: str) -> str:
        """Register a new attendee"""
        attendee_id = f"ATT{len(self.attendees) + 1:04d}"
        attendee = Attendee(attendee_id, name, email, phone)
        self.attendees[attendee_id] = attendee
        print(f"✓ Attendee registered successfully! Attendee ID: {attendee_id}")
        return attendee_id
    
    def book_event(self, attendee_id: str, event_id: str) -> bool:
        """Book an event for an attendee"""
        if attendee_id not in self.attendees:
            print("✗ Error: Attendee not found!")
            return False
        
        if event_id not in self.events:
            print("✗ Error: Event not found!")
            return False
        
        event = self.events[event_id]
        attendee = self.attendees[attendee_id]
        
        if event.is_full():
            print(f"✗ Error: Event '{event.title}' is fully booked!")
            return False
        
        if event_id in attendee.registered_events:
            print(f"✗ Error: Already registered for '{event.title}'!")
            return False
        
        event.registered_attendees.append(attendee_id)
        attendee.registered_events.append(event_id)
        print(f"✓ Successfully booked '{event.title}' for {attendee.name}")
        return True
    
    def cancel_booking(self, attendee_id: str, event_id: str) -> bool:
        """Cancel an event booking"""
        if attendee_id not in self.attendees or event_id not in self.events:
            print("✗ Error: Invalid attendee or event ID!")
            return False
        
        event = self.events[event_id]
        attendee = self.attendees[attendee_id]
        
        if event_id not in attendee.registered_events:
            print("✗ Error: No booking found for this event!")
            return False
        
        event.registered_attendees.remove(attendee_id)
        attendee.registered_events.remove(event_id)
        print(f"✓ Booking cancelled for '{event.title}'")
        return True
    
    def view_event(self, event_id: str):
        """Display detailed information about an event"""
        if event_id not in self.events:
            print("✗ Error: Event not found!")
            return
        
        event = self.events[event_id]
        print(f"\n{'='*60}")
        print(f"Event: {event.title}")
        print(f"{'='*60}")
        print(f"ID: {event.event_id}")
        print(f"Description: {event.description}")
        print(f"Date: {event.date}")
        print(f"Time: {event.time}")
        print(f"Venue: {event.venue}")
        print(f"Category: {event.category}")
        print(f"Capacity: {event.capacity}")
        print(f"Registered: {len(event.registered_attendees)}")
        print(f"Available Seats: {event.get_available_seats()}")
        print(f"{'='*60}\n")
    
    def view_attendee(self, attendee_id: str):
        """Display information about an attendee"""
        if attendee_id not in self.attendees:
            print("✗ Error: Attendee not found!")
            return
        
        attendee = self.attendees[attendee_id]
        print(f"\n{'='*60}")
        print(f"Attendee: {attendee.name}")
        print(f"{'='*60}")
        print(f"ID: {attendee.attendee_id}")
        print(f"Email: {attendee.email}")
        print(f"Phone: {attendee.phone}")
        print(f"Registered Events: {len(attendee.registered_events)}")
        if attendee.registered_events:
            print("\nEvents:")
            for evt_id in attendee.registered_events:
                if evt_id in self.events:
                    print(f"  - {self.events[evt_id].title} ({evt_id})")
        print(f"{'='*60}\n")
    
    def list_all_events(self):
        """List all events in the system"""
        if not self.events:
            print("No events available.")
            return
        
        print(f"\n{'='*80}")
        print(f"{'ID':<10} {'Title':<25} {'Date':<12} {'Venue':<20} {'Available':<10}")
        print(f"{'='*80}")
        for event in self.events.values():
            available = f"{event.get_available_seats()}/{event.capacity}"
            print(f"{event.event_id:<10} {event.title[:24]:<25} {event.date:<12} {event.venue[:19]:<20} {available:<10}")
        print(f"{'='*80}\n")
    
    def search_events(self, keyword: str) -> List[Event]:
        """Search events by keyword in title or category"""
        results = []
        keyword_lower = keyword.lower()
        for event in self.events.values():
            if (keyword_lower in event.title.lower() or 
                keyword_lower in event.category.lower()):
                results.append(event)
        return results
    
    def get_event_report(self, event_id: str):
        """Generate a detailed report for an event"""
        if event_id not in self.events:
            print("✗ Error: Event not found!")
            return
        
        event = self.events[event_id]
        print(f"\n{'='*60}")
        print(f"EVENT REPORT: {event.title}")
        print(f"{'='*60}")
        print(f"Total Capacity: {event.capacity}")
        print(f"Total Registered: {len(event.registered_attendees)}")
        print(f"Available Seats: {event.get_available_seats()}")
        print(f"Occupancy Rate: {len(event.registered_attendees)/event.capacity*100:.1f}%")
        print(f"\nRegistered Attendees:")
        print(f"{'-'*60}")
        for att_id in event.registered_attendees:
            if att_id in self.attendees:
                att = self.attendees[att_id]
                print(f"{att.name:<25} {att.email:<30}")
        print(f"{'='*60}\n")
    
    def save_data(self, filename: str = "event_system_data.json"):
        """Save all data to a JSON file"""
        data = {
            'events': {eid: evt.to_dict() for eid, evt in self.events.items()},
            'attendees': {aid: att.to_dict() for aid, att in self.attendees.items()}
        }
        with open(filename, 'w') as f:
            json.dump(data, f, indent=2)
        print(f"✓ Data saved to {filename}")
    
    def load_data(self, filename: str = "event_system_data.json"):
        """Load data from a JSON file"""
        try:
            with open(filename, 'r') as f:
                data = json.load(f)
            
            self.events = {eid: Event.from_dict(evt) for eid, evt in data['events'].items()}
            self.attendees = {aid: Attendee.from_dict(att) for aid, att in data['attendees'].items()}
            print(f"✓ Data loaded from {filename}")
        except FileNotFoundError:
            print(f"✗ File {filename} not found. Starting with empty system.")


def display_menu():
    """Display the main menu"""
    print("\n" + "="*60)
    print("EVENT MANAGEMENT SYSTEM")
    print("="*60)
    print("1. Create Event")
    print("2. Register Attendee")
    print("3. Book Event")
    print("4. Cancel Booking")
    print("5. View Event Details")
    print("6. View Attendee Details")
    print("7. List All Events")
    print("8. Search Events")
    print("9. Generate Event Report")
    print("10. Save Data")
    print("11. Load Data")
    print("0. Exit")
    print("="*60)


def main():
    """Main function to run the Event Management System"""
    system = EventManagementSystem()
    
    # Sample data for demonstration
    print("Initializing Event Management System...")
    print("\nAdding sample events...")
    
    system.create_event(
        "Tech Conference 2025", 
        "Annual technology conference featuring AI and ML talks",
        "2025-12-15", "09:00 AM", "Convention Center", 200, "Technology"
    )
    
    system.create_event(
        "Music Festival", 
        "Live music performances by popular artists",
        "2025-12-20", "06:00 PM", "Open Air Stadium", 500, "Entertainment"
    )
    
    system.create_event(
        "Startup Pitch Day", 
        "Startup founders pitch their ideas to investors",
        "2025-12-10", "10:00 AM", "Business Hub", 100, "Business"
    )
    
    while True:
        display_menu()
        choice = input("\nEnter your choice: ").strip()
        
        if choice == "1":
            print("\n--- Create Event ---")
            title = input("Title: ")
            description = input("Description: ")
            date = input("Date (YYYY-MM-DD): ")
            time = input("Time: ")
            venue = input("Venue: ")
            capacity = int(input("Capacity: "))
            category = input("Category: ")
            system.create_event(title, description, date, time, venue, capacity, category)
        
        elif choice == "2":
            print("\n--- Register Attendee ---")
            name = input("Name: ")
            email = input("Email: ")
            phone = input("Phone: ")
            system.register_attendee(name, email, phone)
        
        elif choice == "3":
            print("\n--- Book Event ---")
            attendee_id = input("Attendee ID: ")
            event_id = input("Event ID: ")
            system.book_event(attendee_id, event_id)
        
        elif choice == "4":
            print("\n--- Cancel Booking ---")
            attendee_id = input("Attendee ID: ")
            event_id = input("Event ID: ")
            system.cancel_booking(attendee_id, event_id)
        
        elif choice == "5":
            event_id = input("\nEnter Event ID: ")
            system.view_event(event_id)
        
        elif choice == "6":
            attendee_id = input("\nEnter Attendee ID: ")
            system.view_attendee(attendee_id)
        
        elif choice == "7":
            system.list_all_events()
        
        elif choice == "8":
            keyword = input("\nEnter search keyword: ")
            results = system.search_events(keyword)
            print(f"\nFound {len(results)} event(s):")
            for event in results:
                print(f"  {event.event_id}: {event.title}")
        
        elif choice == "9":
            event_id = input("\nEnter Event ID: ")
            system.get_event_report(event_id)
        
        elif choice == "10":
            system.save_data()
        
        elif choice == "11":
            system.load_data()
        
        elif choice == "0":
            print("\nThank you for using Event Management System!")
            break
        
        else:
            print("\n✗ Invalid choice! Please try again.")


if __name__ == "__main__":
    main()
