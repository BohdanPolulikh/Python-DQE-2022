from datetime import datetime
from EightandNineLab_JsonXml import XmlFile, JsonFile, is_right_file
from os import remove
from FifthLab_Classes import main
import sqlite3


class Publication:  # I need to rewrite classes from Homework 5
    # to add method "get_values"

    # create parent class
    def __init__(self, title, text):  # initialization
        self.title = title
        self.text = text

    def add_publication(self):
        edge_mark = '-' * (35 - len(self.title))  # I just use this as separator
        if len(self.text) == 0:  # if text is empty - error
            print("Input at least 1 character!")
            return 0  # if function returns 0 - then nothing to write in the file
        return f'{self.title}{edge_mark}\n{self.text}\n'  # if text is filled - return this text with separatop


class News(Publication):  # create child class
    def __init__(self, text, city):  # initialization with parent title and text, unique city
        super().__init__(title="News", text=text)
        self.city = city

    def add_subscription(self):
        # use parent function publication and unique subscription
        if len(self.city) == 0:  # if city is empty - error
            print("Please, enter city!")
            return 0  # if function returns 0 - then nothing to write in the file
        # use parent function publication and unique subscription
        return f'{Publication.add_publication(self)}' \
               f'{self.city}, {datetime.today()}\n' \
               f'{"-" * 35}\n\n'

    def get_values(self):
        # use parent function publication and unique subscription
        if len(self.city) == 0:  # if city is empty - error
            return 0  # if function returns 0 - then nothing to write in the file
        # use parent function publication and unique subscription
        return {'title': self.title, 'text': self.text, 'city': self.city}


class PrivateAd(Publication):
    def __init__(self, text, expiration_date):  # initialization with parent title and text, unique date
        super().__init__(title="Private Ad", text=text)
        self.expiration_date = expiration_date

    def add_subscription(self):
        # use parent function and unique subscription
        try:  # I used datetime library to calculate difference between dates
            exp_date = datetime.strptime(self.expiration_date, '%Y-%m-%d')
        except ValueError:  # if date doesn't match specified format - raise an error
            print("You entered date that doesn't match the format.")
            return 0
        actual_days = (exp_date - datetime.today()).days + 1  # difference in days.
        # If expiration date = current date, then 0 days left
        if actual_days < 0:  # if difference is negative - error
            print("Please, input correct date! Specified date has "
                  "already passed! ")
            return 0  # if function returns 0 - then nothing to write in the file
        # use parent function publication and unique subscription
        return f'{Publication.add_publication(self)}' \
               f'Actual until {self.expiration_date}, {actual_days}' \
               f' days left,\n' \
               f'{"-" * 35}\n\n'

    def get_values(self):
        # use parent function and unique subscription
        try:  # I used datetime library to calculate difference between dates
            exp_date = datetime.strptime(self.expiration_date, '%Y-%m-%d')
        except ValueError:  # if date doesn't match specified format - raise an error
            return 0
        actual_days = (exp_date - datetime.today()).days + 1  # difference in days.
        # If expiration date = current date, then 0 days left
        if actual_days < 0:  # if difference is negative - error
            return 0  # if function returns 0 - then nothing to write in the file
        # use parent function publication and unique subscription
        return {'title': self.title, 'text': self.text, 'expiration date': self.expiration_date}


class NextConcert(Publication):
    def __init__(self, text, number_of_tickets):  # initialization with parent title and text,
        # unique number of tickets
        Publication.__init__(self, title="Next Concert", text=text)
        self.number_of_tickets = number_of_tickets

    def add_subscription(self):
        if self.number_of_tickets == 0:  # if there are no tickets - message
            print('Sorry, there are no tickets left on the concert.')
            return 0  # if function returns 0 - then nothing to write in the file
        # use parent function publication and unique subscription
        return f'{Publication.add_publication(self)}' \
               f'Hurry up! Only {self.number_of_tickets} tickets left!\n' \
               f'{"-" * 35}\n\n'

    def get_values(self):
        if self.number_of_tickets == 0 or \
                self.number_of_tickets == '0':  # if there are no tickets - message
            return 0  # if function returns 0 - then nothing to write in the file
        # use parent function publication and unique subscription
        return {'title': self.title, 'text': self.text, 'number_of_tickets': self.number_of_tickets}


class ToDataBase:
    def __init__(self, db_path):
        self.db_path = db_path
        with sqlite3.connect(self.db_path) as self.connection:
            # self.connection = sqlite3.connect(f'Database={db_path}')
            self.cursor = self.connection.cursor()

    def create(self, table_name):
        if table_name == 'News':
            self.cursor.execute(f'CREATE TABLE IF NOT EXISTS {table_name}'
                                f'(text TEXT,'
                                f'city TEXT)')
        elif table_name == 'PrivateAd':
            self.cursor.execute(f'CREATE TABLE IF NOT EXISTS {table_name}'
                                '(text TEXT,'
                                'expiration_date TEXT)')
        elif table_name == 'NextConcert':
            self.cursor.execute(f'CREATE TABLE IF NOT EXISTS {table_name}'
                                '(text TEXT,'
                                'number_of_tickets INT)')

    def selection(self, table_name):
        result = self.cursor.execute(f'SELECT * from {table_name}')
        return result.fetchall()

    def insert(self, lst_of_values):
        for record in lst_of_values:
            if record['title'] == 'News':
                self.create('News')
                params = (record['text'], record['city'])
                self.cursor.execute("INSERT INTO News (text, city) VALUES (?, ?)", params)
                # self.cursor.execute(f"INSERT INTO News VALUES (tertew, fwf)")

            elif record['title'] == 'Private Ad':
                self.create('PrivateAd')
                params = (record['text'], record["expiration date"])
                self.cursor.execute(f'INSERT INTO PrivateAd VALUES (?, ?)', params)
            elif record['title'] == 'Next Concert':
                self.create('NextConcert')
                params = (record['text'], record["number of tickets"])
                self.cursor.execute(f'INSERT INTO NextConcert VALUES (?, ?)', params)


# p = JsonFile('new1.json')
# db = ToDataBase('myFile.db')
# db.insert(p.from_file_to_dict())
# print(db.selection('PrivateAd'))
# print(db.selection('News'))


if __name__ == "__main__":
    answer1 = input('Press "Y" if you want to add publication?\n')  # first question
    while answer1.lower() == "y":
        answer2 = int(input("Do you want to publish record to...\n1 - File\n"
                            "2 - database\n"))
        if answer2 == 1:
            answer3 = int(input("Which type of publishing you prefer?\n1 - Console Mode"
                                "\n2 - File Mode\n"))
            if answer3 == 1:
                main()  # call function from previous task (line 1)
            elif answer3 == 2:
                answer4 = int(input("Which type of import file you use>\n"
                                    "1 - .txt (not implemented)\n2 - .json\n3 - .xml\n"))
                if answer4 == 2:  # choose JSON option
                    print(JsonFile.__doc__)
                    file = input("Please, input directory of your file: ")
                    x = JsonFile(file)  # create JSON instance
                    if not isinstance(x.set_information(), int):
                        remove(file)  # remove file
                        print("Thanks! Your file was imported successfully and then removed!")
                elif answer4 == 3:  # choose XML option
                    print(XmlFile.__doc__)
                    file = input("Please, input directory of your file: ")
                    x = XmlFile(file)  # create XML instance
                    if not isinstance(x.set_information(), int):
                        remove(file)  # remove file
                        print("Thanks! Your file was imported successfully and then removed!")
        else:
            database_filepath = input("Input database file: ")
            db = ToDataBase(database_filepath)
            answer32 = int(input("Which type of import file you use?\n"
                                 "1 - .txt (not implemented)\n2 - .json\n3 - .xml\n"))
            if answer32 == 2:
                json_filepath = input("Input JSON file: ")
                p = JsonFile(json_filepath)
            elif answer32 == 3:
                xml_filepath = input("Input XML file: ")
                p = XmlFile(xml_filepath)
            else:
                print("You specified incorrect option.")
                break
            if is_right_file(p.from_file_to_dict()):
                db.insert(p.from_file_to_dict())
            else:
                break
            answer42 = input('Press "Y" if you want to see records from database\n')
            if answer42.lower() == "y":
                answer52 = int(input('Which type of publications you want to check?\n'
                                     '1 - News\n2 - Private Ad\n3 - Next Concert\n'))
                if answer52 == 1:
                    print(db.selection('News'))
                elif answer52 == 2:
                    print(db.selection('PrivateAd'))
                else:
                    print(db.selection('NextConcert'))
        answer1 = input('Press "Y" if you want to add new publication?\n')
        # new question, if answer is yes - call function again
