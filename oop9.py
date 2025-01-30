import csv

l=[]
with open("data.csv",'r') as f:
    data=csv.DictReader(f)
    for item in data:
        l.append(item)


for i in l:
         print(i['price'])

