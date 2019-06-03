
class User(object):
    def __init__(self, name , email):
        self.name = name
        self.email = email
        self.books = {} #   book:rating
        self.ratings = []
    def get_email(self):
        return self.email
    def change_email(self,email):
        self.email = email
        print("email changed for " + self.name)
        return(self.name)
    def __repr__(self):
        return "User " +self.name + " ,email: "+self.email + " books read: "+ str( len(self.books))
    def __eq__(self,other):
        return self.name == other.name and self.email == other.email
    def read_book(self,book, rating = None):
        self.book = book
        self.rating = rating
        if rating != None and rating in [0,1,2,3,4]:
          self.books[book] = rating
        else:
          self.books[book] = None
        return(rating)
    def get_average_rating(self):
        total_rate =0
        for k in self.ratings:
            total_rate += k
        return total_rate / len(books)
class Books(object):
    def __init__(self,title,isbn):
        self.title = title
        self.isbn = isbn
        self.ratings = []
    def get_title(self):
        return self.title
    def get_isbn(self):
        return self.isbn
    def set_isbn(self,isbn):
        if type(isbn) == int:
            self.isbn = isbn
            print("The isbn for :{} has been updated".format(self.title ) )
    def __eq__(self,other):
        return self.title == other.title and self.isbn == other.isbn
    def __hash__(self):
        return hash ( ( self.title, self.isbn) )
    def add_rating( self,rating):
        if rating >= 0 and rating <= 4:
            self.ratings.append(rating)
        else:
            print("Invalid Rating")

class Fiction (Books):
    def __init__(self, title,author,isbn):
        self.author = author
        super(Fiction,self).__init__(title,isbn)
        self.title = title
        self.isbn = isbn
    def get_author(self):
        return self.author
    def  __repr__(self):
        return self.title + " by " + self.author
class Non_Fiction (Books):
    def __init__(self, title,subject,level,isbn):
        self.subject = subject
        self.level = level
        self.isbn = isbn
        super(Non_Fiction,self).__init__(title,isbn)
        self.title = title
        self.isbn = isbn
    def get_subject(self):
        return self.subject
    def get_level(self):
        return self.level
    def  __repr__(self):
        return self.title + " a  " + self.level + " manual on " + self.subject



class TomeRater():
    def __init__(self):
        self.users = {}  # email:User Object  is key to User object
        self.books ={}  # bookObject:readCount
    def create_book(self,title,isbn):
        self.title = title
        self.isbn = isbn
        #test this out
        self.books[Books(self.title,self.isbn)] = 0
        return Books(self.title, self.isbn)

    def create_novel( self,title,author,isbn):
        self.title = title
        self.author = author
        self.isbn = isbn
        return Fiction(self.title, self.author, self.isbn)
    def create_non_fiction(self,title,subject,level,isbn):
        self.title = title
        self.subject = subject
        self.level = level
        self.isbn = isbn
        return Non_Fiction(self.title,self.subject,self.level,self.isbn)
    def add_user(self,name,email,user_books = None):
        book_read_cnt = 0
        self.users[email] = User(name, email)
        if user_books != None:
          for  the_book  in user_books:
            print(the_book)
            self.add_book_to_user(the_book,email)
    def add_book_to_user(self,book, email, rating = None): # book is an object of type books
        self.book = book
        self.email = email
        self.rating = rating
        if  ( email  in self.users.keys() )  == False:
            print("Unable to add book to non_existent email")
        else:
            self.users[email].read_book(book, rating)
    def add_rating(self,book,rating):
        self.book = book
        self.rating = rating
        if book in self.books.keys():
            self.books[book] += 1
        else:
            self.books[book] = 1
            # if book exists in TomeRater self.books , increment its value by 1_
            # if book does not exist in TomeRate self.books add it with default value of 1 ( first reader of book)

    def print_catalog(self):
        for book in self.books.keys():
            print(book)
    def print_users(self):
        k ={}
        for j  in self.users.values():
          print(j)
    def highest_rated_book(self):
        highest = None
        highest_rating =0
        for  book in self.books.keys():
            avg_user_rating = books.get_average_rating()
            if avg_user_rating > highest_rating:
                highest = book
                highest_rating = avg_user_rating
        return highest
    def get_most_read_book(self):
        max_read_cnt =0
        max_read_book = None
        for k in books.keys():
            if books[k] > max_read_cnt:
                max_read_cnt = books[k]
                max_read_book = k
        return k

    def most_positive_user(self):
        positive_user = None
        highest_rating =0
        for  user in self.users.values():
            print(user)
            avg_rating = user.get_average_rating()
            if avg_rating > highest_rating:
                highest_rating = avg_rating
                positive_user = user
        return positive_user













