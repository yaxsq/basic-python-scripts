# Dictionary to store the tasks: String/boolen
tasks = {}

def get_task_info():
    return input("What is the task?: ")


def add_new_task(task: str):
    tasks[task] = False


def get_update_choice():
    return input("Would you like to set the task as (T)rue or (F)alse?: ")[0].lower()

while True:
    choice = input("Would you like to (V)iew, (A)dd, (U)pdate or (R)emove a task?: ")[0].lower()
    # print(choice[0].lower())

    if choice == 'v':                 # if view
        print(tasks)
    elif choice == 'a':               # if add
        add_new_task(get_task_info())               # getting then adding the task
    elif choice == 'u':               # if update
        # task = get_task_info()
        # update_choice = get_update_choice()
        task = get_task_info()
        update_choice = get_update_choice()
        if update_choice == 't':           # getting task and choice and setting as T or F
            tasks[task] = True
        elif update_choice == 'f':
            tasks[task] = False
    elif choice == 'r':              # if remove
        del tasks[get_task_info()]

# Not adding () after lower would result in an address being printed
