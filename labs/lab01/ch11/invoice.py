# Starting file for Lab 1 Chapter 11 invoice.py program
# Jasmine Djuned, 10/09/26, DEV128

from datetime import datetime, timedelta, date

def get_invoice_date():
    while True:
        invoice_date_str = input("Enter the invoice date (MM/DD/YYYY): ") 
        # validate for proper input
        try:
            dt = datetime.strptime(invoice_date_str, "%m/%d/%Y")
        except ValueError:
            print("Invalid date format. Please enter your date in MM/DD/YYYY format. Please try again.")
            continue

        invoice_date = date(dt.year, dt.month, dt.day)

        # validate that the invoice date is today or earlier (not in the future)
        if invoice_date > date.today():
            print("Invoice must be today's date or earlier. Please try again.")
        else:
            return invoice_date

def main():
    print("The Invoice Due Date program")
    print()

    again = "y"
    while again.lower() == "y":
        invoice_date = get_invoice_date()
        print()

        # calculate due date and days overdue
        due_date = invoice_date + timedelta(days=30)
        current_date = date.today()
        days_overdue = (current_date - due_date).days

        # display results
        date_format = "%B %d, %Y"
        print(f"Invoice Date: {invoice_date:{date_format}}")
        print(f"Due Date:     {due_date:{date_format}}")
        print(f"Current Date: {current_date:{date_format}}")
        if days_overdue > 0:
            print(f"This invoice is {days_overdue} day(s) overdue.")
        else:
            days_due = days_overdue * -1
            print(f"This invoice is due in {days_due} day(s).")
        print()

        # ask if user wants to continue
        again = input("Continue? (y/n): ")
        print()
        
    print("Bye!")      

if __name__ == "__main__":
    main()
