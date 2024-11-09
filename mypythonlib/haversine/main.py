import os
import csv
from haversine import haversine

def process_file(input_file, output_file):
    try:
        with open(input_file, 'r') as infile, open(output_file, 'w', newline='') as outfile:
            reader = csv.reader(infile)
            for row in reader:
                lon1 = (float(row[0]))
                lat1 = (float(row[1]))
                lon2 = (float(row[2]))
                lat2 = (float(row[3]))
                distance = haversine(lon1, lat1, lon2, lat2)
                distance = str(distance)
                outfile.write("Distance: " + distance + " km")

        print(f"Processed file saved as {output_file}")
    except Exception as e:
        print(f"An error occurred: {e}")

def validate_input_file(file_path):
    return os.path.isfile(file_path)

def validate_output_file(file_path):
    try:
        with open(file_path, 'w') as f:
            pass
        os.remove(file_path)
        return True
    except:
        return False

def main():
    print("Welcome to the Haversine Distance Calculator!")

    while True:
        input_file = input("Please enter the path to the input CSV file: ")
        if not input_file:
            print("No input file provided. Exiting.")
            return
        if validate_input_file(input_file):
            break
        print("Invalid input file path. Please try again or press Enter to exit.")

    while True:
        output_file = input("Please enter the path to save the output TXT file: ")
        if not output_file:
            print("No output file provided. Exiting.")
            return
        if validate_output_file(output_file):
            break
        print("Invalid output file path. Please try again or press Enter to exit.")

    process_file(input_file, output_file)
    input("Processing complete. Press Enter to exit...")

if __name__ == "__main__":
    main()
