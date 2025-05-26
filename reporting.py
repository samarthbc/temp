import sqlite3
from datetime import datetime

def initialize_database():
    conn = sqlite3.connect("incident_report.db")
    cursor = conn.cursor()
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS incident (
            id INTEGER PRIMARY KEY,
            timestamp TEXT,
            category TEXT,
            description TEXT,
            reporter TEXT
        )
    """)
    conn.commit()
    conn.close()

def submit_incident(category, description, reporter):
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    conn = sqlite3.connect("incident_report.db")
    cursor = conn.cursor()
    cursor.execute("""
        INSERT INTO incident (timestamp, category, description, reporter)
        VALUES (?, ?, ?, ?)
    """, (timestamp, category, description, reporter))
    conn.commit()
    conn.close()

def view_incidents():
    conn = sqlite3.connect("incident_report.db")
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM incident")
    incidents = cursor.fetchall()
    conn.close()
    return incidents

def main():
    initialize_database()
    while True:
        print("\nIncident Reporting Tool")
        print("1. Report an Incident")
        print("2. View all Incidents")
        print("3. Exit")

        choice = input("Enter your choice: ")

        if choice == '1':
            category = input("Enter the category of incident: ")
            description = input("Enter a brief description: ")
            reporter = input("Your Name: ")
            submit_incident(category, description, reporter)
            print("Incident reported successfully!\n")

        elif choice == '2':
            incidents = view_incidents()
            print("\nAll Incidents:")
            for incident in incidents:
                print(f"ID: {incident[0]}, Timestamp: {incident[1]}, "
                      f"Category: {incident[2]}, Description: {incident[3]}, "
                      f"Report: {incident[4]}")
        
        elif choice == '3':
            print("Exiting...")
            break

        else:
            print("Invalid choice.")

if __name__ == "__main__":
    main()
