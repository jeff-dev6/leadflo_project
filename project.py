"""
project.py

User interaction and menu
"""
import csv
from lead_score import  evaluate_lead
from storage import get_lead, save_lead, save_history, search_leads, FIELDS
from validators import clean_lead
from report import(total_leads, total_hot_leads, total_warm_leads, 
                   total_nurture_leads, total_low_priority_leads,
                   get_hot_leads)



def main():
    while True:
        print("=" * 40)
        print("LEADFLOW")
        print("=" * 40)
        print("\n1. Add Lead")
        print("2. Search Leads")
        print("3. Generate Report")
        print("4. Export Hot Leads")
        print("5. Import Leads")
        print("6. Exit")

        choice = input("\nSelect an option:")

        if choice == "1":
             add_lead()

        elif choice == "2":
            search_for_leads()

        elif choice == "3":
            display_reports()

        elif choice == "4":
            export_hot_leads()

        elif choice == "5":
            import_leads()

        elif choice == "6":
            print("Goodbye!")
            break

        else:
            print("Invalid option. Please try again.")




def add_lead():
    try:
        lead = get_lead()
        
        cleaned_lead = clean_lead(lead)
        
        score, status = evaluate_lead(cleaned_lead)

        cleaned_lead["score"] = score
        cleaned_lead["status"] = status

        save_lead(cleaned_lead)

        save_history(
            "Lead added", 
            f"Successfully added lead with status '{status}' and score {score}"
        )

        print(
            f"Lead added successfully! "
            f"Status: {status}, | Score: {score}"
        )

        return cleaned_lead
    
    except Exception as e:
        print(f"Error adding lead: {e}")

    return None



def search_for_leads():
    search_term = input("Enter school name to search: ")

    matches = search_leads(search_term)

    if not matches:
        print("No matching schools found.")
        return

    for lead in matches:
        print(lead)

 

def display_reports():
    print("\n" + "=" * 40)
    print("LEAD REPORT")
    print("=" * 40)
    print(f"\nTotal Leads: {total_leads()}")
    print(f"Hot Leads: {total_hot_leads()}")
    print(f"Warm Leads: {total_warm_leads()}")
    print(f"Nurture Leads: {total_nurture_leads()}")
    print(f"Low Priority Leads: {total_low_priority_leads()}")
    print("\n" + " " * 40)



def export_hot_leads():
    hot_leads = get_hot_leads()
    with open("data/output.csv", mode="w", newline="", encoding="utf-8") as file:
        writer = csv.DictWriter(file, fieldnames=FIELDS)

        writer.writeheader()
        writer.writerows(hot_leads)

    print(f"Exported {len(hot_leads)} hot leads.")

    



if __name__ == "__main__":
    main()

