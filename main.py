from data import get_sample_data
from logic import process_student, rank_students
from display import display_all_students
from export import export_to_csv

def main():
    students = get_sample_data()

    
    processed_students = [process_student(s) for s in students]

  
    ranked_students = rank_students(processed_students)

  
    display_all_students(ranked_students)


    export_to_csv(ranked_students)
    print("Results have been exported to 'results.csv'.")

if __name__ == "__main__":
    main()
