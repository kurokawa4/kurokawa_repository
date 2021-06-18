import csv

with open('./file/lesson.csv',encoding='UTF-8-sig') as reder_csv_file:
    reader = csv.DictReader(reder_csv_file)
    reader_list = []
    for row in reader:
        total = int(row['国語']) + int(row['数学']) + int(row['社会'])
        reader_list.append({'seq':row['seq'], 'name':row['name'], '合計':str(total)})

with open('./file/lesson2.csv', 'w',encoding='UTF-8', newline="") as writer_csv_file:
    fieldnames= ['seq','name','合計']
    writer = csv.DictWriter(writer_csv_file, fieldnames= fieldnames)
    writer.writeheader()
    for i in reader_list:
        writer.writerow(i)
