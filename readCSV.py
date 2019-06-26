import csv

with open('results.csv','r') as csv_file:
    csv_reader = csv.reader(csv_file)

    for line in csv_reader:
        print(line)
   
    with open('new_file.csv','w') as new_file:
        csv_writer = csv.writer(new_file, delimiter='\t')
        
        for line in csv_reader:
            csv_writer.writerow(line)
            


    