candies = int(input("Enter number of candies: "))
students = int(input("Enter number of students: "))

remaining_candies = candies

while remaining_candies >= students:
    remaining_candies -= students
    #print(remaining_candies)
    
print("Number of remaining candies:", remaining_candies)