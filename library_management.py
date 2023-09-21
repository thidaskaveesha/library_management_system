class LectureCD:
    def __init__(self, cd_no, title, subject, rental_price, copies):
        self.cd_no = cd_no
        self.title = title
        self.subject = subject
        self.rental_price = rental_price
        self.copies = copies

class LectureCDFunction:
    def __init__(self):
        self.cd_list = []

    def add(self):
        cd_no = input("Enter CD number: ")
        title = input("Enter title: ")
        subject = input("Enter subject: ")
        rental_price = input("Enter rental price: ")
        copies = input("Enter number of copies: ")
        cd1 = LectureCD(cd_no, title, subject, rental_price, copies)
        self.cd_list.append(cd1)
        print("CD added successfully!")
    
    
    def remove(self):
        cd_no = input("Please enter the CD Number to remove a CD:")
        matched_cds = list((item for item in self.cd_list if item.cd_no == cd_no))
        if len(matched_cds) > 0:
            for i in matched_cds:
                self.cd_list.remove(i)
            print('CD Removed Successfully')
        else:
            print('You entered an Invalid CD Number')

    def show_available(self):
        matched_cds = list((item for item in self.cd_list if item.copies > 0))
        if len(matched_cds) > 0:
            print("Availables CD")
            for i in matched_cds:
                print('CD NO:',i.cd_no, 'Title:',i.title, 'Copies:',i.copies)
        else:
            print('No CDs are available')

    def show_unavailable(self):
        matched_cds = list((item for item in self.cd_list if item.copies <= 0))
        if len(matched_cds) > 0:
            print("Unavailables CD")
            for i in matched_cds:
                print('CD NO:',i.cd_no, 'Title:',i.title, 'Copies:',i.copies)
        else:
            print('There are CD available')


    def search_by_subject(self, subject_name):
        matched_cds = list((item for item in self.cd_list if item.subject == subject_name))
        if len(matched_cds) > 0:
            for i in matched_cds:
                print('CD NO:',i.cd_no, 'Title:',i.title, ',Subject:',i.subject, 'Copies:',i.copies)

    def lend(self):
        cd_no = input("Please enter the CD Number to lend a CD:")
        matched_cds = list((anitem for anitem in self.cd_list if anitem.cd_no == cd_no))
        if len(matched_cds) > 0:
            cd = matched_cds[0]
            if cd.copies > 0:
                cd.copies -= 1
                print(f"You have rented '{cd.title}'. Enjoy your lecture!")
            else:
                print("Sorry, this CD is currently unavailable.")
        else:
            print('You entered an Invalid CD Number')
            
    def returned(self):
        cd_no = input("Enter CD number: ")
        matched_cds = list((anitem for anitem in self.cd_list if anitem.cd_no == cd_no))
        if len(matched_cds) > 0:
            for i in matched_cds:
                i.copies += 1
            print("CD returned successfully!")
        else:
            print("CD not found in the system")

class Magazine:
    def __init__(self, magazine_no, title, color_bw, subject, rental_price, copies):
        self.magazine_no = magazine_no
        self.title = title
        self.color_bw = color_bw
        self.subject = subject
        self.rental_price = rental_price
        self.copies = copies

class MagazineFunction:
    def __init__(self):
        self.magazine_list = []

    def add(self):
        magazine_no = input("Enter magazine number: ")
        title = input("Enter magazine title: ")
        color_bw = input("Enter color or black and white: ")
        subject = input("Enter magazine subject: ")
        rental_price = float(input("Enter rental price: "))
        copies = int(input("Enter number of copies: "))
        magazine = Magazine(magazine_no, title, color_bw, subject, rental_price, copies)
        self.magazine_list.append(magazine)
        print("Magazine added successfully!")
    
    def returned(self):
        magazine_no = input("Enter Magazine number: ")
        matched_magazine = list((item for item in self.magazine_list if item.magazine_no == magazine_no))
        if len(matched_magazine) > 0:
            for i in matched_magazine:
                i.copies += 1
            print("Magazine returned successfully!")
        else:
            print("Magazine not found in the system")
    
    def remove(self):
        magazine_no = input("Please enter the magazine Number to remove a magazine:")
        matched_magazines = list((item for item in self.magazine_list if item.magazine_no == magazine_no))
        if len(matched_magazines) > 0:
            for i in matched_magazines:
                self.magazine_list.remove(i)
            print('magazine Removed Successfully')
        else:
            print('You entered an Invalid magazine Number')

    def show_available(self):
        matched_magazines = list((item for item in self.magazine_list if item.copies > 0))
        if len(matched_magazines) > 0:
            print("Availables Magazines")
            for i in matched_magazines:
                print('Magazine No:',i.magazine_no, 'Title:',i.title, 'Copies:',i.copies)
        else:
            print('No Magazines are available')

    def show_unavailable(self):
        matched_magazines = list((item for item in self.magazine_list if item.copies <= 0))
        if len(matched_magazines) > 0:
            print("Unavailables CD")
            for i in matched_magazines:
                print('Magazine No:',i.magazine_no, 'Title:',i.title, 'Copies:',i.copies)
        else:
            print('There are no Magazine available')
    
    def lend(self):
        magazine_no = input("Please enter the Magazine Number to lend a Magazine:")
        matched_magazine = list((item for item in self.magazine_list if item.magazine_no == magazine_no))
        if len(matched_magazine) > 0:
            magazine = matched_magazine[0]
            if magazine.copies > 0:
                magazine.copies -= 1
                print("You have rented ",magazine.title,". Enjoy your lecture!")
            else:
                print("Sorry, this Magazine is currently unavailable.")
        else:
            print('You entered an Invalid Magazine Number')


    def search_by_subject(self, subject_name):
        matched_magazines = list((item for item in self.magazine_list if item.subject == subject_name))
        if len(matched_magazines) > 0:
            for i in matched_magazines:
                print('Magazine No:',i.magazine_no, 'Title:',i.title, ',Subject:',i.subject, 'Copies:',i.copies)

class EducationalDVD:
    def __init__(self, dvd_no, title, subject, rental_price, copies):
        self.dvd_no = dvd_no
        self.title = title
        self.subject = subject
        self.rental_price = rental_price
        self.copies = copies

class EducationalDVDFunction:
    def __init__(self):
        self.dvd_list = []
    
    def add_dvd(self):
       dvd_no = input("Enter DVD number: ")
       title = input("Enter DVD title: ")
       subject = input("Enter DVD subject: ")
       rental_price = input("Enter rental price: ")
       copies = input("Enter number of copies: ")
       
       dvd = EducationalDVD(dvd_no, title, subject, rental_price, copies)
       self.dvd_list.append(dvd)
       print("DVD added successfully!")
    
    def returned(self):
        dvd_no = input("Enter Magazine number: ")
        matched_dvds = list((item for item in self.dvd_list if item.dvd_no == dvd_no))
        if len(matched_dvds) > 0:
            for i in matched_dvds:
                i.copies += 1
            print("DVD returned successfully!")
        else:
            print("DVD not found in the system")

    def lend(self):
        dvd_no = input("Please enter the DVD Number to lend a DVD:")
        matched_dvds = list((item for item in self.dvd_list if item.dvd_no == dvd_no))
        if len(matched_dvds) > 0:
            dvd = matched_dvds[0]
            if dvd.copies > 0:
                dvd.copies -= 1
                print("You have rented ",dvd.title,". Enjoy your lecture!")
            else:
                print("Sorry, this DVD is currently unavailable.")
        else:
            print('You entered an Invalid DVD Number')

    def remove(self):
        dvd_no = input("Please enter the DVD Number to remove a DVD:")
        matched_dvds = list((item for item in self.dvd_list if item.dvd_no == dvd_no))
        if len(matched_dvds) > 0:
            for i in matched_dvds:
                self.dvd_list.remove(i)
            print('DVD Removed Successfully')
        else:
            print('You entered an Invalid dvd Number')

    def show_available(self):
        matched_dvds = list((item for item in self.dvd_list if item.copies > 0))
        if len(matched_dvds) > 0:
            print("Availables Magazines")
            for i in matched_dvds:
                print('DVD No:',i.dvd_no, 'Title:',i.title, 'Copies:',i.copies)
        else:
            print('No Magazines are available')

    def show_unavailable(self):
        matched_dvds = list((item for item in self.dvd_list if item.copies <= 0))
        if len(matched_dvds) > 0:
            print("Unavailables CD")
            for i in matched_dvds:
                print('DVD No:',i.dvd_no, 'Title:',i.title, 'Copies:',i.copies)
        else:
            print('There are no Magazine available')


    def search_by_subject(self, subject_name):
        matched_dvds = list((item for item in self.dvd_list if item.subject == subject_name))
        if len(matched_dvds) > 0:
            for i in matched_dvds:
                print('DVD No:',i.dvd_no, 'Title:',i.title, ',Subject:',i.subject, 'Copies:',i.copies)


class Book:
    def __init__(self, isbn_no, title, book_format, subject, rental_price, copies):
        self.isbn_no = isbn_no
        self.title = title
        self.book_format = book_format
        self.subject = subject
        self.rental_price = rental_price
        self.copies = copies

class BookFunction:
    def __init__(self):
        self.book_list= []

    def add(self):
        isbn_no = input("Please enter the ISBN Number:")
        title  = input("Title:")
        book_format = input("Format:")
        subject = input("Subject:")
        rental_price = float(input("Rental Price:"))
        copies = int(input("Available Copies:"))
        book =  Book(isbn_no, title,book_format,subject,rental_price,copies)
        self.book_list.append(book)
        print('Book added successfully!')

    def lend(self):
        isbn_no = input("Please enter the ISBN Number to lend a BOOK:")
        matched_books = list((item for item in self.book_list if item.isbn_no == isbn_no))
        if len(matched_books) > 0:
            book = matched_books[0]
            if book.copies > 0:
                book.copies -= 1
                print("You have rented ",book.title,". Enjoy your book!")
            else:
                print("Sorry, this book is currently unavailable.")
        else:
            print('You entered an Invalid book Number')

    def returned(self):
        isbn_no = input("Enter Magazine number: ")
        matched_book = list((item for item in self.book_list if item.isbn_no == isbn_no))
        if len(matched_book) > 0:
            for i in matched_book:
                i.copies += 1
            print("Book returned successfully!")
        else:
            print("Book not found in the system")

    def remove(self):
        isbn_no = input("Please enter the ISBN Number to remove a book:")
        matched_books = list((item for item in self.book_list if item.isbn_no == isbn_no))
        if len(matched_books) > 0:
            for i in matched_books:
                self.book_list.remove(i)
            print('Book Removed Successfully')
        else:
            print('You entered an Invalid ISBN Number')

    def show_available(self):
        matched_books = list((item for item in self.book_list if item.copies > 0))
        if len(matched_books) > 0:
            print("Availables Books")
            for i in matched_books:
                print('ISBN NO:',i.isbn_no, 'Title:',i.title, 'Copies:',i.copies)
        else:
            print('No books are available')

    def show_unavailable(self):
        matched_books = list((item for item in self.book_list if item.copies <= 0))
        if len(matched_books) > 0:
            print("Unavailables Books")
            for i in matched_books:
                print('ISBN NO:',i.isbn_no, 'Title:',i.title, 'Copies:',i.copies)
        else:
            print('There are no books available')


    def search_by_subject(self, subject_name):
        matched_books = list((item for item in self.book_list if item.subject == subject_name))
        if len(matched_books) > 0:
            for i in matched_books:
                print('ISBN NO:',i.isbn_no, 'Title:',i.title, ',Subject:',i.subject, 'Copies:',i.copies)

def mainmenu():
    while True:
        print("Main Menu")
        print("1-Book")
        print("2-Magazine")
        print("3-DVD")
        print("4-CD")
        print("5-Search By Subject")
        print("0-Quit")

 
        main_choice = int(input("Please enter your choice:"))


        if main_choice == 1 or  main_choice == 2 or main_choice == 3 or main_choice == 4:
            submenu(main_choice=main_choice)
        elif main_choice == 5:
            subjectname = input("Please Enter the Subject Name to Search:")
            print('Search Result for subject',subjectname)
            BookFunction.search_by_subject(subjectname)
            MagazineFunction.search_by_subject(subjectname)
            EducationalDVD.search_by_subject(subjectname)
            LectureCDFunction.search_by_subject(subjectname)
            input("Press any key to continue...")
        elif main_choice == 0:
            print("Thank you for using our library system.")
            quit()


def submenu(main_choice):
    if main_choice == 1:
        resource_name = 'Book'
        ExecutorFunction = BookFunction()
    elif main_choice == 2:
        resource_name = 'Magazine'
        ExecutorFunction = MagazineFunction()
    elif main_choice == 3:
        resource_name = 'DVD'
        ExecutorFunction = EducationalDVD()
    elif main_choice == 4:
        resource_name = 'CD'
        ExecutorFunction = LectureCDFunction()

    while True:
        print("Sub Menu")
        print("1-Add",resource_name)
        print("2-Remove", resource_name)
        print("3-Show Available" ,resource_name)
        print("4-Show Unavailable", resource_name)
        print("5-Lend", resource_name)
        print("6-Return the", resource_name)
        print("7-Back to Main menu")
        print("8-Quit")
        sub_choice = int(input("Please enter your choice:"))

        if sub_choice == 1:
            ExecutorFunction.add()
        elif sub_choice == 2:
            ExecutorFunction.remove()
        elif sub_choice == 3:
            ExecutorFunction.show_available()
        elif sub_choice == 4:
            ExecutorFunction.show_unavailable()
        elif sub_choice == 5:
            ExecutorFunction.lend()
        elif sub_choice == 6:
            ExecutorFunction.returned()
        elif sub_choice == 7:
            mainmenu()
            break
        elif sub_choice == 8:
            print("Exiting from the library system.")
            quit()

        input("Press any key to continue...")

mainmenu()
