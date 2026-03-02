from bs4 import BeautifulSoup
from datetime import datetime
import csv
import re

output_csv_file = 'cleaned_data.csv'
def clean_html(html):
    soup = BeautifulSoup(html, 'html.parser')
    text = soup.get_text()
    cleaned_text = re.sub(r'(\r\n|\n|\r)|\s*reporter[^\n]*\n|▲|▼', '', text) 
    cleaned_text = ' '.join(cleaned_text.split())
    cleaned_text  = cleaned_text .replace(chr(10), "\t")
    return cleaned_text


with open(output_csv_file, mode='w', newline='') as output_file:
    csv_writer = csv.writer(output_file)
    csv_writer.writerow(['time', 'title', 'content', 'type'])
    with open('data.csv', mode='r', newline='') as file:
        reader = csv.DictReader(file)
        for row_c in reader:
          with open('ettoday_news.tsv', mode='r', newline='') as file:
            tsv_reader = csv.reader(file, delimiter='\t')
            for row in tsv_reader:
              if row_c['index'] == row[1]:
                time = row_c['event_date']
                title = row[0]                
                content = clean_html(row[11])
                print(content)
                type = ""
                type1 = row[3]
                type2 = row[5]
                if type1 == type2:
                    type = type1
                else:
                    type = type1 + " " + type2
                csv_writer.writerow([time, title, content, type])
                break

print("Saved:", output_csv_file)
