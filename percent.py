print("input the percentage")
percentage = float(input())
print("input the total marks")
total_marks = float(input())
print(f"Your marks are: {percentage / 100 * total_marks}")
print(f"worst case: {100-(percentage / 100 * total_marks)}")
salida=False
while salida==False
    for i in range(1, total_marks):
        print(random.randint(1, 100))
        if random.randint(1, 100) > percentage:
            count=count+1
    print("finished?")
    salida=input()
print("total ammount of times it was succesful:", count)