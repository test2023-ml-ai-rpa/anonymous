import csv
num_att = 6
a = []
print("\nA\n")

with open("enjoysport.csv") as csvfile:
    reader=csv.reader(csvfile)
    for row in reader:
        reader.line_num
        if(row[0]!="sky"):
            a.append(row)
            print(row)

print("HYPO")
hypothesis = ['0']*num_att
print(hypothesis)

for j in range(0,num_att):
    hypothesis[j] = a[0][j]

for i in range(0, len(a)):
  if a[i][num_att]=='yes':
      for j in range(0, num_att): 
          if a[i][j] != hypothesis[j]:
              hypothesis[j] = '?'
          else:
              hypothesis[j] = a[i][j]

print(hypothesis)
