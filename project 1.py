my_tasks = []

def add_task():
    new_task = input("what task would you like to add ? ")
    my_tasks.append(new_task)

def view_tasks():
    for index , task in enumerate(my_tasks,1):
        print(f"{index}.{task}")

def main():
    while True:
        print(" 1 add / 2 view / 3 quit")
        
        choice = input("pick number ")
        if choice == "1":
            add_task()
        elif choice == "2":
            view_tasks()
        elif choice == "3":
            break
        
        else:
            print("invalid input please input a valid number")

                     
if __name__ == "__main__":
    main()        