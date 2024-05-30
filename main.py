"""Python script to automatically generate Oracle Forms .fmb files based on SQL query results"""

from pyoracle_forms import Module, initialize_context
import csv

# Enter csv file name here:
CSV_FILE = ''


def main():
    reports_generated = 0
    with open(CSV_FILE, 'r') as csv_file:
        for row in csv.reader(csv_file, delimtiter = ','):
            generate_report(row)
            reports_generated += 1
    
    print(f"Successfully generated {reports_generated}")


def generate_report(leave_request_id):

if __name__ == "__main__":
    main()