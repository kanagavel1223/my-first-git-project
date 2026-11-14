a=int(input("Enter the number of subjects:"))
marks=[]
for i in range(a):
    mark=int(input("Enter the marks of subject {}:".format(i+1)))
    if mark<0 or mark>100:
        print("Invalid marks! Please enter marks between 0 and 100.")
    else:
        marks.append(mark)
total=sum(marks)
average=total/len(marks)
print(min(marks ),"is the minimum marks")
print(max(marks),"is the maximum marks")
print(total,"is the total marks")
print(average,"is the average marks")