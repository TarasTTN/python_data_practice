import csv

def process_sales(input_file, output_file):
    """
    Filters raw transaction data, writes valid records to a new CSV,
    and returns core financial metrics.
    """
    total_records = 0
    valid_records = 0
    total_revenue = 0

    with open(input_file, 'r', encoding='utf-8') as f_in:
        with open(output_file, 'w', encoding='utf-8', newline='') as f_out:
            reader = csv.reader(f_in)
            writer = csv.writer(f_out)
            header = next(reader)
            writer.writerow(header)
            for row in reader:
                total_records += 1
                amount = float(row[2])
                status = row[3]
                if status == 'completed' and amount > 0:
                    writer.writerow(row)
                    valid_records += 1
                    total_revenue += amount
    return {
        "total_input": total_records,
        "valid_saved": valid_records,
        "dropped": total_records - valid_records,
        "revenue": total_revenue
    }

if __name__ == "__main__":
    print("ETL pipeline script initialized.")