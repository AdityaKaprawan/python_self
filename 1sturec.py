#for academic evaluation 
def acad():
    marks = []
    for i in range(5):
        m = float(input(f"Enter marks for subject {i+1}: "))
        marks.append(m)

    total = sum(marks)
    percentage = total / 5
    cgpa = percentage / 10

    # Grades
    if cgpa >= 9:
        grade = "A+"
    elif cgpa >= 8:
        grade = "A"
    elif cgpa >= 7:
        grade = "B"
    elif cgpa >= 6:
        grade = "C"
    elif cgpa >= 5:
        grade = "D"
    else:
        grade = "F"

    print("\nVXVXV Grade Sheet VXVXV")
    print(f"Marks: {marks}")
    print(f"Percentage: {percentage:.2f}%")
    print(f"CGPA: {cgpa:.2f}")
    print(f"Grade: {grade}")
# for maths analyzer part 
def is_prime(n):
    if n <= 1:
        return False
    
    for i in range(2, n):
        if n % i == 0:
            return False
    
    return True

def is_armstrong(n):
    temp = n
    sum = 0

    while temp > 0:
        digit = temp % 10
        sum += digit ** 3
        temp = temp // 10

    return sum == n

def is_palindrome(n):
    temp = n
    rev = 0

    while temp > 0:
        digit = temp % 10
        rev = rev * 10 + digit
        temp = temp // 10

    return rev == n


def factorial(n):
    fact = 1
    for i in range(1, n+1):
        fact *= i
    return fact


def fibonacci(n):
    a, b = 0, 1
    series = []
    for _ in range(n):
        series.append(a)
        a = b
        b = a+b
    return series

def math():
    n = int(input("Enter a number: "))

    print(f"Prime: {is_prime(n)}")
    print(f"Armstrong: {is_armstrong(n)}")
    print(f"Palindrome: {is_palindrome(n)}")
    print(f"Factorial: {factorial(n)}")

    terms = int(input("Enter number of Fibonacci terms: "))
    print("Fibonacci Series:", fibonacci(terms))

    a = int(input("Enter first number: "))
    b = int(input("Enter second number: "))
    c = int(input("Enter third number: "))
    print("Greatest number is:", max(a, b, c))

#for string processing 
def string():
    text = input("Enter a sentence: ")

    vowels = "aeiouAEIOU"
    vcount = sum(1 for ch in text if ch in vowels)
    ucount = sum(1 for ch in text if ch.isupper())

    substring = input("Enter substring to count: ")
    subcount = text.count(substring)

    print("\nString Analysis")
    print(f"Vowels: {vcount}")
    print(f"Uppercase Letters: {ucount}")
    print(f"Occurrences of '{substring}': {subcount}")

    print("\nWords in new lines:")
    for word in text.split():
        print(word)


#now code for data management 
contacts = {}
tasks = []

def contact_book():
    while True:
        print("\nContact Book")
        print("1. Add Contact")
        print("2. Search Contact")
        print("3. Delete Contact")
        print("4. Back")

        choice = input("Enter choice: ")

        if choice == "1":
            name = input("Enter name: ")
            phone = input("Enter phone: ")
            contacts[name] = phone
            print("Contact added!")

        elif choice == "2":
            name = input("Enter name to search: ")
            if name in contacts:
                print("Phone:", contacts[name])
            else:
                print("Contact not found!")

        elif choice == "3":
            name = input("Enter name to delete: ")
            if name in contacts:
                del contacts[name]
                print("Deleted successfully!")
            else:
                print("Contact not found!")

        elif choice == "4":
            break
        else:
            print("Invalid choice!")


def todo_list():
    while True:
        print("\n--- To-Do List ---")
        print("1. Add Task")
        print("2. View Tasks")
        print("3. Remove Task")
        print("4. Back")

        choice = input("Enter choice: ")

        if choice == "1":
            task = input("Enter task: ")
            tasks.append(task)
            print("Task added!")

        elif choice == "2":
            print("\nTasks:")
            for i, t in enumerate(tasks, 1):
                print(f"{i}. {t}")

        elif choice == "3":
            idx = int(input("Enter task number to remove: ")) - 1
            if 0 <= idx < len(tasks):
                tasks.pop(idx)
                print("Task removed!")
            else:
                print("Invalid index!")

        elif choice == "4":
            break
        else:
            print("Invalid choice!")


def data():
    while True:
        print("\nData Management")
        print("1. Contact Book")
        print("2. To-Do List")
        print("3. Back")

        choice = input("Enter choice: ")

        if choice == "1":
            contact_book()
        elif choice == "2":
            todo_list()
        elif choice == "3":
            break
        else:
            print("Invalid choice!")




while True:
    print("\nSMART STUDENT UTILITY SYSTEM ")
    print("1. Academic Evaluation")
    print("2. Mathematical Analyzer")
    print("3. String Processing")
    print("4. Data Management")
    print("5. Exit")
    n=input("enter an option: ")
    if (n=="1"):
        acad()
    elif(n=="2"):
        math()
    elif(n=="3"):
        string()
    elif(n=="4"):
        data()
    elif(n=="5"):
        print("exiting...")
        break
    else:
        print("invalid input")

