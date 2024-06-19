'''Lets create all the tables for cookbook database'''
import cookbook

conn = cookbook.connect()
cursor = conn.cursor()

file = open('D:\\Learn_MYSQL\\workout\\filenames.txt','r')

list_of_names = file.readlines()

for i, name in enumerate(list_of_names):
    list_of_names[i] = name.replace('\n','')

print(list_of_names)

for name in list_of_names:
    cursor.execute(f"\source {name}")

cursor.close()
file.close()
