from models import (Base, session, Book, engine)
import datetime
import csv

def menu():
    while True:
        print('''
            \nPROGRAMMING BOOKS
            \r1) Add book
            \r2) View all books
            \r3) Search for book
            \r4) Book Analysis
            \r5) Exit\n''')
        choice = input('What would you like to do? ')
        if choice in ['1','2','3','4','5']:
            return choice
        else:
            input('''\nPlease choose one of the options above
            \rPress enter to try again.''')

def clean_date(date_str):
    months = ['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'December']
    split_date = date_str.split(" ")
    print(split_date)
    month = int(months.index(split_date[0]) + 1)
    day = int(split_date[1].split(',')[0])
    year = int(split_date[2])
    return datetime.date(year, month, day)


def clean_price(price_str):
    price_float = float(price_str)
    return int(price_float * 100)

def add_csv():
    with open('suggested_books.csv') as csvfile:
        data = csv.reader(csvfile)
        for row in data:
            book_in_db = session.query(Book).filter(Book.title==row[0]).one_or_none()
            if book_in_db == None:
                date = clean_date(row[2])
                title = row[0]
                author = row[1]
                price = clean_price(row[3])
                new_book = Book(title=title, author=author, published_date=date, price=price)
                session.add(new_book)
        session.commit()

def app():
    app_running = True
    while app_running:
        choice = menu()
        if choice == '1':
            #addbook
            pass
        elif choice =='2':
            #view books
            pass
        elif choice == '3':
            #search
            pass
        elif choice == '4':
            #Book analysis
            pass
        else: 
            print('Goodbye')
            app_running = False

#add books to the database
#edit books
#delete books
#search function
#data cleaning function
#loop that runs the program


if __name__ == '__main__':
    Base.metadata.create_all(engine)
    add_csv()
    for book in session.query(Book):
        print(book)