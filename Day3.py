n = int(input("Enter number of students:"))
marks = [0]*n
valid_count = 0
failed_count = 0
roll1 = "AP24110011623"
for i in range(n):
    marks[i] = int(input("Enter marks:"))
roll = input("Enter the roll:")
if(int(roll[-1]) == int(roll1[-1])):
    for i in range(n):
        marks[i] += 1
        if (marks[i] >= 0 and marks[i] <= 39):
            print(marks[i], "--> Fail")
            failed_count = failed_count + 1
            valid_count = valid_count + 1
        elif (marks[i] >= 40 and marks[i] <= 59):
            print(marks[i], "--> Average")
            valid_count = valid_count + 1
        elif (marks[i] >= 60 and marks[i] <= 74):
            print(marks[i], "--> Good")
            valid_count = valid_count + 1
        elif (marks[i] >= 75 and marks[i] <= 89):
            print(marks[i], "--> Very Good")
            valid_count = valid_count + 1
        elif(marks[i] >= 90 and marks[i] <= 100):
            print(marks[i], "--> Excellent")
            valid_count = valid_count + 1
        else:
            print(marks[i], "--> Invalid")
else:
    print("Roll last digit mismatches the roll1")
print("Final Marks:", marks)
print("Total Valid Students:", valid_count)
print("Total Failed Students:", failed_count)
