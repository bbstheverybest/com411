import csv


with open('example.csv') as f:

   reader = csv.reader(f)
   headings= next(reader)


for row in reader:
    print(row[0])




