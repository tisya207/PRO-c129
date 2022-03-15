import csv

dataset1=[]
dataset2=[]

with open("bright_stars.csv","r") as f:
    csv_reader= csv.reader(f)
    for row in csv_reader:
        dataset1.append(row)

with open("dwarf_stars.csv","r") as f:
    csv_reader= csv.reader(f)
    for row in csv_reader:
        dataset2.append(row)

header1= dataset1[0]
stars_data1= dataset1[1:]

header2= dataset1[0]
stars_data2= dataset1[1:]

headers= header1 + header2
all_stars_data=[]

for index, data_row in enumerate(stars_data1):
    all_stars_data.append(stars_data1[index]+ stars_data2[index])

with open("merged_stars_data_final.csv","a+") as f:
    csv_writer= csv.writer(f)
    csv_writer.writerow(headers)
    csv_writer.writerows(all_stars_data)