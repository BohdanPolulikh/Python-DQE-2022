from datetime import datetime


class Publication:  # create parent class
    def __init__(self, title, text):  # initialization
        self.title = title
        self.text = text

    def add_publication(self):
        edge_mark = '-' * (35 - len(self.title)) # I just use this as separator
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


def main():
    x = int(input("Select which type of publication you want to add?\n"
                  "1 - News\n"
                  "2 - Private Ad\n"
                  "3 - Next Concert\n"))
    if x not in [1, 2, 3]:  # if user chooses incorrect option - error
        print("Please choose option 1, 2 or 3.")
        return 0
    t = input("Input text you want to publish.\n")  # text to input
    if x == 1:
        c = input("Input city: ")
        p = News(t, c)  # use class News to public
    elif x == 2:
        d = input("Input expiration date (use format Year-Month-Day): ")
        p = PrivateAd(t, d)  # use class PrivateAd to public
    elif x == 3:
        n = int(input("Input number of tickets: "))
        p = NextConcert(t, n)  # use class NextConcert to public
    with open('Homework5.txt', 'a') as f:  # open file with append function
        if not isinstance(p.add_publication(), int) and \
                not isinstance(p.add_subscription(), int):
            # if no errors - add publication to file
            f.write(p.add_subscription())


answer = input('Press "Y" if you want to add publication?\n')  # first question
while answer.lower() == "y":
    main()  # if answer is yes - call the main function
    answer = input('Press "Y" if you want to add new publication?\n')
    # new question, if answer is yes - call function again


