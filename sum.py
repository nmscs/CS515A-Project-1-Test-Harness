import argparse
import csv

def csv_sum(filename, columns):
    try:
        with open(filename, 'r') as file:
            reader = csv.DictReader(file)
            data = list(reader)

            for column in columns:
                if column not in reader.fieldnames:
                    print(f"Column '{column}' not found in the CSV file.")
                    return

            column_sums = {column: sum(float(row[column]) if row[column] else 0 for row in data) for column in columns}

            print("Column sums:")
            for column, total in column_sums.items():
                print(f"{column}: {total}")

    except FileNotFoundError:
        print(f"File '{filename}' not found.")
    except Exception as e:
        print(f"An error occurred: {str(e)}")

def main():
    parser = argparse.ArgumentParser(description="Calculate sum of specified columns in a CSV file.")
    parser.add_argument('filename', help='Path to the CSV file')
    parser.add_argument('columns', nargs='+', help='Columns for which to calculate the sum')
    
    args = parser.parse_args()
    csv_sum(args.filename, args.columns)

if __name__ == '__main__':
    main()
