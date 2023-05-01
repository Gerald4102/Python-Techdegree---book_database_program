from models import (Base, session, 
                    Book, engine)
                    

# import models file
# main menu - add, search, analysis, view 
# add books to the database
# edit books
# delete books
# search books
# data cleaning
# loop runs progam


if __name__ == '__main__':
    Base.metadata.create_all(engine)