from models import (Base, engine,
                    session, Book)


import csv
import datetime
import time


def menu():
    while True:
        print('''
        \nPROGRAMMING BOOKS
        \r1) Add book
        \r2) View all books
        \r3) Search for book
        \r4) Book analysis
        \r5) Exit
        ''')
        choice = int(input('What would you like to do: '))
        if choice in [1, 2, 3, 4, 5]:
            return choice
        else:
            input('''
            \rPlease choose an option.
            \rA number from 1-5.
            \rPress ENTER to try again.
            ''')


# add books to the database
# edit books
# delete books
# search books
# data cleaning
# loop runs program


def clean_date(date_str):
    months = ['January', 'February', 'March', 'April', 'May', 'June', 
              'July', 'August', 'September', 'October', 'November', 'December']
    split_date = date_str.split(' ')
    month = months.index(split_date[0]) + 1
    day = int(split_date[1].split(',')[0])
    year = int(split_date[2])
    return datetime.date(year, month, day)


def add_csv():
    with open('suggested_books.csv') as csvfile:
        data = csv.reader(csvfile)
        for row in data:
            print(row)


def app():
    app_running = True
    while app_running:
        choice = menu()
        if choice == 1:
            #add book
            pass
        elif choice == 2:
            #view all books
            pass
        elif choice == 3:
            #edit book
            pass
        elif choice == 4:
            #book analysis
            pass
        else:
            print('GOODBYE')
            time.sleep(1)
            app_running = False



if __name__ == '__main__':
    Base.metadata.create_all(engine)
    #app()
    print(clean_date('May 1, 2014'))