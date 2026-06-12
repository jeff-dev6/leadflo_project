"""
project.py

User interaction and menu
"""

from lead_score import calculate_score, evaluate_lead
from storage import get_lead, save_lead, save_history
from validators import clean_text



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
            search_leads()

        elif choice == "3":
            generate_report()

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
        cleaned_lead = clean_text(lead)

        score_lead = calculate_score(cleaned_lead)
        lead_status = evaluate_lead(score_lead)

        cleaned_lead["score_lead"] = score_lead
        cleaned_lead["lead_status"] = lead_status

        save_lead(cleaned_lead)

        save_history(
            "Lead added", 
            f"Successfully added lead with status '{lead_status}' and score {score_lead}"
        )

        print(
            f"Lead added successfully! "
            f"Status: {lead_status}, | Score: {score_lead}"
        )

        return cleaned_lead
    
    except Exception as e:
        print(f"Error adding lead: {e}")
        return None



if __name__ == "__main__":
    main()

