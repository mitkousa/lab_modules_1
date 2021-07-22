from modules.input import *
from modules.task_list import *
from data.task_list import *


while (True):
 #   print_menu()
    option = get_input("Select an option 1, 2, 3, 4, 5 or (Q)uit: ")
    if (option.lower() == 'q'):
        break
    if option == '1':
        print_list(tasks)
    elif option == '2':
        print_list(get_uncompleted_tasks(tasks))
    elif option == '3':
        print_list(get_completed_tasks(tasks))
    elif option == '4':
        description = get_input("Enter task description to search for: ")
        task = get_task_with_description(tasks, description)
        if task != "Task Not Found":
            mark_task_complete(task)
    elif option == '5':
        time = int(get_input("Enter task duration: "))
        print_list(get_tasks_taking_longer_than(tasks, time))
    elif option == '6':
        description = get_input("Enter task description to search for: ")
        print(get_task_with_description(tasks, description))
    elif option == '7':
        description = get_input("Enter description: ")
        time_taken = int(get_input("Enter time taken: "))
        task = create_task(description, time_taken)
        tasks.append(task)
    else:
        print("Invalid Input - choose another option")