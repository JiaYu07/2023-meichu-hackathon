from datetime import datetime
import csv
import re
output_csv_file = 'output.csv'

processed_numbers = set()
cnt=0
with open(output_csv_file, mode='a', newline='') as output_file:
    csv_writer = csv.writer(output_file)
    csv_writer.writerow(['index', 'event_date'])
    for i in range(29, 32):
        name = 'data/log_202308'+ str(i) +'_000000.tsv'
        with open(name, mode='r', newline='') as file:
            tsv_reader = csv.reader(file, delimiter='\t')
            for row in tsv_reader:
                if len(row) > 7:
                    index = row[7].find("ed6df309547d106232a7e4ea12953b4c") # id of a member
                    if index != -1:
                        match = re.search(r'"/item/news/(\d+)"', row[10])
                        if match:
                            extracted_number = match.group(1)
                            cnt+=1
                            if cnt==100:
                                break
                            if extracted_number in processed_numbers:
                                continue
                            # print data and time
                            date_str = row[15]
                            date_parts = date_str.split('-')
                            year = int(date_parts[0])
                            month = int(date_parts[1])
                            day = int(date_parts[2])
                            date_tuple = (year, month, day)
                            print(row)
                            csv_writer.writerow([extracted_number, date_tuple])
                            processed_numbers.add(extracted_number)

print("Saved:", output_csv_file)
