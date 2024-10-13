import datetime as dt #We import the two libraries in our program, 'datetime' as 'dt' and 'time'.
import time           #They will help us throughout the program - 'datetime' will help with accessing dates, and
                      #'time' will give the user the impression that the program is downloading or loading data. 

#Firstly, we open the text file in read and writing mode with the command 'r+', and store the data in a variable called 'user_file'.
user_file = open('user.txt', 'r+')
dic_users = {} #Create an empty dictionary to store the usernames (keys) and their passwords (values).
for line in user_file: #Develop a 'for' loop to iterate all the lines of text in the file.
    (key, value) = line.replace('\n', '').split(', ') #Definition of our keys and values using 'replace()' to remove the '\n' command, and
                                                      #'split()' to let the program know which elements correspond to keys or values.
    dic_users[key] = value #Addition of each key and value in the dictionary.

while True: #Develop a 'while' loop that will run indefinitely using the keyword 'True'.
    given_user_name = input('Enter a username: ') #Ask the user to input a username.
    given_user_password = input('Enter a password: ') #Ask the user to input a password.
    if dic_users.get(given_user_name) == None: #If the username is not in the dictionary, it will run the code below.
        print('Username or password incorrect.')    
    elif dic_users[given_user_name] == given_user_password: #If the username is the 'key' to the password 'value', it will run the code below.
        print('Welcome {0}'.format(given_user_name))
        print('Displaying main menu...')
        break #Terminate the loop with the keyword 'break'.
    else:
        print('Username or password incorrect.')
time.sleep(0.5) #'sleep()' will stop the program for the number of seconds chosen. In this case, half a second.

while True: #Develop another indefinite loop to display the menu and run the options available to the user.
    if given_user_name =='admin': #If the active user is the admin, it will show the expanded menu. Otherwise, the regular menu will be displayed.
        menu = input('''Select one of the following options:
r - register a user
a - add task
va - view all tasks
vm - view my tasks
stats - statistics
e - exit
''').lower()
    else:
        menu = input('''Select one of the following options:
a - add task
va - view all tasks
vm - view my tasks
e - exit
''').lower()
    time.sleep(0.5)

    if menu == 'r':
        if given_user_name != 'admin': #If the active user is not the admin, but types 'r' by mistake, the program will run the code below.
            print('This option is only allowed for the admin user.')
            print('Redirecting to main menu...')
            time.sleep(0.5)
            continue  #we return to the beginning of the loop with the keyword 'continue'.
        new_user_name = input('Please enter new username: ')
        if dic_users.get(new_user_name) == None: #Check whether the new username is in the dictionary. If it is not, it will run the code below.
            new_user_password = input("Please enter {0}'s password: ".format(new_user_name))
            new_password_conffirmed = input('Please confirm the password: ')   
            if new_user_password != new_password_conffirmed: #If the password and its confirmation are not the same, it will return the admin to the main menu.
                print('Passwords and its confirmation are not the same.')
                print('Redirecting to main menu...')
                time.sleep(0.5)
                
            else:
                user_file.write(new_user_name + ', ' + new_user_password + '\n') #Apend the new user and password at the end of the file with 'write()'.
                dic_users[new_user_name] = new_password_conffirmed #Add them to the dictionary.
                user_file.close() #Close the file with 'close()'.
                print('Username and password saved succesfully!')
                print('Redirecting to main menu...')
                time.sleep(0.5)      
        else: #If the username already exists, the program returns to the main menu.
            print('Sorry, this username already exists.')
            print('Redirecting to main menu...')
            time.sleep(0.5)
 #Please note that 'lower()' has not been applied to the username and password requests, because that could lead to security breaches.  
    elif menu == 'a':
        print('Starting the creation of a new task...')
        time.sleep(0.5)
        assigned_user = input('Please enter username assigned to the task: ')
        task_title = input('Please enter the title of the task: ').lower()
        task_descr = input("Please enter the description of the task '{0}': ".format(task_title)).lower()
        task_date = input("Please introduce the due date of the task '{0}' (day month year): ".format(task_title)).lower()
        current_day = dt.date.today().strftime('%d %B %Y').lower() #Get the current date using 'date.today()' and change its format with 'strftime()'.
        task_file = open('tasks.txt', 'a') 
        task_file.write(assigned_user + ', ' + task_title + ', ' + task_descr + ', ' + current_day + ', ' + task_date + ', ' + 'No' + '\n') #We add 'No' as the task status 
        task_file.close()                                                                                                                   #and create a new line with '\n'.
        time.sleep(0.5)
        print('New task saved succesfully!')
        print('Redirecting to main menu...')
        time.sleep(0.5)

    elif menu == 'va':
        print('Preparing all tasks...')
        time.sleep(0.5)
        task_file = open('tasks.txt', 'r+')
        for line in task_file: #For loop to iterate all the lines in the file and display each task on the screen.
            assigned_users = [] + line.split(', ')[0:1]
            tasks_titles = [] + line.split(', ')[1:2]
            tasks_descr = [] + line.split(', ')[2:3] #We add each taks's title, description, dates, user assigned, etc., to each correspondent list.
            tasks_dates = [] + line.split(', ')[3:4]
            tasks_due = [] + line.split(', ')[4:5]
            results = [] + line.replace('\n', '').split(', ')[5:] #We remove the '\n' command, which is printed along with the status of the tasks.
            print('''{0}
Task: {1}
Assigned to: {2}
Date assignated: {3}
Due date: {4}
Task complete? {5}
Task description: {6}
'''.format('-'*50, tasks_titles, assigned_users, tasks_dates, tasks_due, results, tasks_descr))
        task_file.close()
        print('Redirecting to main menu...')
        time.sleep(0.5)

    elif menu == 'vm':
        print('Preparing your tasks...')
        time.sleep(0.5)
        task_file = open('tasks.txt', 'r+')
        for line in task_file:
                if given_user_name in line: #If the active username appears on a line, the task will be displayed on the screen.
                    assigned_users = [] + line.split(', ')[0:1]
                    tasks_titles = [] + line.split(', ')[1:2]
                    tasks_descr = [] + line.split(', ')[2:3]
                    tasks_dates = [] + line.split(', ')[3:4]
                    tasks_due = [] + line.split(', ')[4:5]
                    results = [] + line.replace('\n', '').split(', ')[5:]
                    print('''{0}
Task: {1}
Assigned to: {2}
Date assignated: {3}
Due date: {4}
Task complete? {5}
Task description: {6}
'''.format('-'*50, tasks_titles, assigned_users, tasks_dates, tasks_due, results, tasks_descr))    
        task_file.close()
        print('Redirecting to main menu...')
        time.sleep(0.5)
    
    elif menu == 'stats': #In this option, the total number of users and the total number of tasks (both completed and not completed), will be displayed.
            print('Preparing statistics...')
            time.sleep(0.5)
            task_file = open('tasks.txt', 'r')
            total_tasks, results, tasks_done, tasks_not_done = [], [], [], [] #Create lists to accumulate values in the following loop.
            for line in task_file:
                total_tasks = total_tasks + line.split(', ')[1:2]
                results = results + line.replace('\n', '').split(', ')[5:] 
            for i in results: #Differenciate between task status (done and not done).
                if i == 'No':
                    tasks_not_done.append(i)
                elif i == 'Yes':
                    tasks_done.append(i)       
            print('''{0}
Total number of users: {1}
Total number of tasks: {2}
Completed tasks: {3}
Tasks to be completed: {4}
{5}'''.format('-'*50, len(dic_users), len(total_tasks), len(tasks_done), len(tasks_not_done), '-'*50)) #Display numbers using 'len()' to calculate the length of each list.
            task_file.close()
            print('Redirecting to main menu...')
            time.sleep(0.5)
                   
    elif menu == 'e':
        print('See you soon!')
        exit() #'exit()' terminates the indefinite loop, ending the program.

    else: #If the user inputs a wrong command, the program will run the code below.
        print("Invalid input.")
        print('Redirecting to main menu...')
        time.sleep(0.5)