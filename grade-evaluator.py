import csv
import sys
import os

def load_csv_data():
    """
    Prompts the user for a filename, checks if it exists, 
    and extracts all fields into a list of dictionaries.
    """
    filename = input("Enter the name of the CSV file to process (e.g., grades.csv): ")
    
    if not os.path.exists(filename):
        print(f"Error: The file '{filename}' was not found.")
        sys.exit(1)
        
    assignments = []
    
    try:
        with open(filename, mode='r', encoding='utf-8') as file:
            reader = csv.DictReader(file)
            for row in reader:
                # Convert numeric fields to floats for calculations
                assignments.append({
                    'assignment': row['assignment'],
                    'group': row['group'],
                    'score': float(row['score']),
                    'weight': float(row['weight'])
                })
        return assignments
    except Exception as e:
        print(f"An error occurred while reading the file: {e}")
        sys.exit(1)

def validate_scores(data):
    """Return the rows whose score is outside 0 to 100."""
    invalid = []
    for row in data:
        if row['score'] < 0 or row['score'] > 100:
            invalid.append(row)
    return invalid

def validate_weights(data):
    """Return a list of error messages. Empty list means weights are valid."""
    total = 0.0
    formative = 0.0
    summative = 0.0
    for row in data:
        total += row['weight']
        if row['group'] == 'Formative':
            formative += row['weight']
        elif row['group'] == 'Summative':
            summative += row['weight']
        else:
            return [f"Unknown group '{row['group']}' for '{row['assignment']}'. Use Formative or Summative."]

    errors = []
    if abs(total - 100) > 0.001:
        errors.append(f"Total weight is {total}, expected 100.")
    if abs(formative - 60) > 0.001:
        errors.append(f"Formative weight is {formative}, expected 60.")
    if abs(summative - 40) > 0.001:
        errors.append(f"Summative weight is {summative}, expected 40.")
    return errors

def validate_weights(data):
    """Return a list of error messages. Empty list means weights are valid."""
    total = 0.0
    formative = 0.0
    summative = 0.0
    for row in data:
        total += row['weight']
        if row['group'] == 'Formative':
            formative += row['weight']
        elif row['group'] == 'Summative':
            summative += row['weight']
        else:
            return [f"Unknown group '{row['group']}' for '{row['assignment']}'. Use Formative or Summative."]

    errors = []
    if abs(total - 100) > 0.001:
        errors.append(f"Total weight is {total}, expected 100.")
    if abs(formative - 60) > 0.001:
        errors.append(f"Formative weight is {formative}, expected 60.")
    if abs(summative - 40) > 0.001:
        errors.append(f"Summative weight is {summative}, expected 40.")
    return errors

def evaluate_grades(data):
    """
    Implement your logic here.
    'data' is a list of dictionaries containing the assignment records.
    """
    print("\n--- Processing Grades ---")

    if not data:
        print("Error: grades.csv has no assignment records.")
        return

    invalid = validate_scores(data)
    if invalid:
        for row in invalid:
            print(f"Error: '{row['assignment']}' has score {row['score']}, expected 0 to 100.")
        return

   
    weight_errors = validate_weights(data)
    if weight_errors:
        for message in weight_errors:
            print(f"Error: {message}")
        return    
    # TODO: a) Check if all scores are percentage based (0-100)
    # TODO: b) Validate total weights (Total=100, Summative=40, Formative=60)
    # TODO: c) Calculate the Final Grade and GPA
    # TODO: d) Determine Pass/Fail status (>= 50% in BOTH categories)
    # TODO: e) Check for failed formative assignments (< 50%)
    #          and determine which one(s) have the highest weight for resubmission.
    # TODO: f) Print the final decision (PASSED / FAILED) and resubmission options
    


if __name__ == "__main__":
    # 1. Load the data
    course_data = load_csv_data()

    # 2. Process the features
    evaluate_grades(course_data)