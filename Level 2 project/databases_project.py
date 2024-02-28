import sqlite3 as sq #Importation of the 'sqlite3' library to have access to its functions.
db = sq.connect('ebookstore.db') #With '.connect()' the program will open or create the database selected.
cursor = db.cursor() #Creation of the cursor allows for the execution of actions in the database.

class Book(): #Declaration of a class named 'Book'.
        def __init__(self, id, author, title, synopsis, quantity): #Set of id, author, title, synopsis and quantity as instance variables of the class.
            self.id = id                         
            self.author = author                           
            self.title = title
            self.synopsis = synopsis
            self.quantity = quantity

book_list = [] #Creation of an empty list to store all the objects that will be defined below.

cursor.execute('''SELECT id, title, author, synopsis, quantity FROM book''')
for row in cursor:
    print('id: {0}\ntitle: {1}'.format(row[0], row[1]))
    book = Book(row[0], row[1], row[2], row[3], row[4]) #Creation of objects with each variable's value being each row of the table 'book' in our database.
    book_list.append(book) #Addition of the objects into the list, one by one.

def select_book(): #'select_book()' will allow the user to display all the information about a book.
    cursor.execute('''SELECT id, title, author, quantity FROM book''')
    print('Listing available books...')
    for row in cursor:
        print('id: {0}\ntitle: {1}\n{2}'.format(row[0], row[1], '-'*50)) #Print out of all books' id and titles.
    try: #Use of 'try'-'except' block to get rid off any ValueError the user may introduce in the program.
        user_id_input = int(input("Please enter the id number to display book's information: "))
        if user_id_input not in range(3001, len(book_list) + 3001, 1): #If the 'id' given is not on the database, the program returns to the main menu.
            print('Sorry, wrong id number received.')
            exit()
        for i in book_list:
            if user_id_input == i.id: #'For' loop to iterate all the objects and print out the items of the one selected by the user.
                print('''id: {0}
author: {1}       
title: {2}           
synopsis: {3}           
quantity: {4}         
'''.format(i.id, i.author, i.title, i.synopsis, i.quantity)) #Display of the information of the chosen book.         
    except ValueError:
        print('Wrong command detected.')

def add_book(): #'add_book()' will allow the user to add new books to the database.
    user_title = input('Please introduce the title of the book: ')
    for i in book_list: #'For' loop to iterate all the books and check that the new book is not in the database already. If that is the case,
        if user_title == i.title: #the program will return to the main menu.
            print('Sorry, we have {0} already available to buy.'.format(user_title))
            exit()
    user_author = input('Please introduce the author of the book {0}: '.format(user_title))
    user_synopsis = input('Please introduce the synopsis of {0}: '.format(user_title))
    user_qty = input('Please introduce the quantity of books available: ')
    cursor.execute('''INSERT INTO book(title, author, synopsis, quantity) VALUES(?, ?, ?, ?)''', (user_title, user_author, user_synopsis, user_qty))
    db.commit()
    book = Book(id, user_title, user_author, user_synopsis, user_qty) #Creation of a new object with the new book details.
    book_list.append(book) #Addition of the new book into the list.
    print("Book titled '{0}', saved succesfully...".format(user_title))

def update_book(): #'update_book()' will allow the user to update the number of books available to buy.
    cursor.execute('''SELECT id, title, author, quantity FROM book''')
    print('Listing available books...')
    for row in cursor: #Print out all ids and titles on the screen.
        print('id: {0}\ntitle: {1}\n{2}'.format(row[0], row[1], '-'*50))
    try: #'try-block' to get rid off any ValueError given by a wrong input.
        user_id_input = int(input('Please introduce the id of the book to be updated: '))
        if user_id_input not in range(3001, len(book_list) + 3001, 1): #If the 'id' given is not on the database, the program returns to the main menu.
            print('Sorry, wrong id number received.')
            exit()
        user_quantity = int(input('Please introduce the new number of books available: '))
        cursor.execute('''UPDATE book SET quantity = ? WHERE id = ? ''', (user_quantity, user_id_input))
        for i in book_list: #'For' loop to update the quantity number of the selected book in the list.
            if user_id_input == i.id:
                i.quantity = user_quantity
        db.commit()
        print('Change saved succesfully!')
    except ValueError:
        print('Wrong command detected.')

def delete_book(): #'delete_book()' will allow the user to delete a book from the database.
    cursor.execute('''SELECT id, title, author, quantity FROM book''')
    print('Listing available books...')
    for row in cursor: #Print out ids and titles of the books.
        print('id: {0}\ntitle: {1}\n{2}'.format(row[0], row[1], '-'*50))
    try: #'try-block' to get rid off any ValueError given by a wrong input.
        user_id_input = int(input('Please introduce the id of the book to be deleted: '))
        if user_id_input not in range(3001, len(book_list) + 3001, 1): #If the 'id' given is not on the database, the program returns to the main menu.
            print('Sorry, wrong id number received. Redirecting to main menu...')
            exit() #'exit()' will terminate the function, redirecting the user to the main menu.
        cursor.execute('''DELETE FROM book WHERE id = ? ''', (user_id_input,)) 
        db.commit() 
        for i in book_list: #'For' loop to delete the book from the list.
            if user_id_input == i.id:
                book_list.remove(i)
        print("Book deleted succesfully...")
    except ValueError:
        print('Wrong command detected.')

print('Welcome to our ebook store app.') #Welcome the user to the program.
while True: #'while True' will create an indefinite loop to run the program until the user selects the 'Exit' option.
    menu = input('''Please select one of the options below 
1. Add new book
2. Update book
3. Delete book
4. Information about a book
5. Exit 
''') #Display the menu to the user.
#Development of a conditional statement series to evaluate the user's choice and fulfill each action with one of the functions previously defined.
    if menu == '1':
        add_book()
        print('Returning to main menu...')
    elif menu == '2':
        update_book()
        print('Returning to main menu...')
    elif menu == '3':
        delete_book()
        print('Returning to main menu...')
    elif menu == '4':
        select_book()
        print('Returning to main menu...')
    elif menu == '5':
        print('See you soon!')
        db.close() #'db.close()' will close the database.
        exit() #exit() will terminate the loop.
    else:
        print('You have introduced an invalid command.')
        print('Returning to main menu...')
    
