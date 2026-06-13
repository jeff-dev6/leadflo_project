"""
project.py

User interaction and menu
"""

from lead_score import  evaluate_lead
from storage import get_lead, save_lead, save_history, search_leads
from validators import clean_lead
from report import generate_report



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
    report = generate_report()

    print(f"Total Leads: {report['total_leads']}")
    print(f"Hot Leads: {report['hot_leads']}")
    print(f"Warm Leads: {report['warm_leads']}")
    print(f"Nurture Leads: {report['nurture_leads']}")
    print(f"Cold Leads: {report['cold_leads']}") 






if __name__ == "__main__":
    main()

