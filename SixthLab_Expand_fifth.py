from FifthLab_Classes import main
from FifthLab_Classes import News, PrivateAd, NextConcert
from os import remove


class FromFile:
    """
    Rules.
    Please, set all publications you want to add in the following configuration:
    Keys (Title/Text/City/Expiration date/Number of tickets).
    Values should be populated according to rules from previous task.
    Separator - semicolon (without whitespaces!).
    For example.
    Title:News
    """

    def __init__(self, file_path):
        self.file_path = file_path

    def get_values(self):
        titles = list()  # new list with titles
        news_dict = {"title": "News", "text": [], "city": []}  # dictionary with News
        ad_dict = {"title": "Private Ad", "text": [], "exp_dates": []}  # dictionary with Ads
        concert_dict = {"title": "Next Concert", "text": [], "number_of_tickets": []}
        # dictionary with Concerts
        with open(self.file_path) as f:  # open file for read
            rows = f.readlines()  # create list with each row as element of list
            for row in rows:
                if row[:5] == "Title":
                    titles.append(row[6:].strip())  # list with titles added
                elif row[:4] == "Text":
                    if titles[-1] == "News":  # if last title is News
                        news_dict["text"].append(row[5:].strip())
                        # then add element to News dictionary
                    elif titles[-1] == "Private Ad":  # if last title is Ad
                        ad_dict["text"].append(row[5:].strip())
                        # then add element to Private Ad dictionary
                    elif titles[-1] == "Next Concert":  # if last title is Concert
                        concert_dict["text"].append(row[5:].strip())
                        # then add element to Concert dictionary
                    else:  # if title is invalid, then will add error message
                        # and function will be closed
                        print(f"Please, input correct value as Title: {titles[-1]}")
                        return 0
                elif row[:4] == "City":
                    news_dict["city"].append(row[5:].strip())  # add City to News dictionary
                elif row[:15] == "Expiration date":
                    ad_dict["exp_dates"].append(row[16:].strip())  # add Expiration date to
                    # Private Ad dictionary
                elif row[:17] == "Number of tickets":
                    concert_dict["number_of_tickets"].append(row[18:].strip())  # add number of tickets
                    # to Next Concert dictionary
        if len(news_dict["text"]) != len(news_dict["city"]):
            # if Text or City are missed - then error message
            print("Check again! Probably you missed News Text or your city")
            return 0
        elif len(ad_dict["text"]) != len(ad_dict["exp_dates"]):
            # if Text or Expiration dates are missed - then error message
            print("Check again! Probably you missed Ad Text or expiration date")
            return 0
        elif len(concert_dict["text"]) != len(concert_dict["number_of_tickets"]):
            # if Text or Number of tickets are missed - then error message
            print("Check again! Probably you missed Concert Text or number of tickets")
            return 0
        return news_dict, ad_dict, concert_dict  # return all dictionaries

    def set_publications(self):
        news_data = FromFile.get_values(self)[0]  # take news data from news dictionary
        all_publications = ""
        if len(news_data["text"]) == 0:
            pass  # if there isn't News then pass, else add information to File
        else:
            for i in range(len(news_data["text"])):
                news_public = News(news_data["text"][i], news_data["city"][i])
                # create instance as News class from previous Task
                if not isinstance(news_public.add_subscription(), int):
                    all_publications += f"{news_public.add_subscription()}"
                    # if no errors = using method from previous Task
                else:
                    return 0

        ads_data = FromFile.get_values(self)[1]  # take ads data from Ad dictionary

        if len(ads_data["text"]) == 0:
            pass  # if there isn't Ad then pass
        else:
            for i in range(len(ads_data["text"])):
                ad_public = PrivateAd(ads_data["text"][i], ads_data["exp_dates"][i])
            # create instance as Private class from previous Task
            # else check values on errors
                if not isinstance(ad_public.add_subscription(), int):
                    all_publications += f"{ad_public.add_subscription()}"  # if no errors -
                    # use method from previous Task
                else:
                    return 0

        concerts_data = FromFile.get_values(self)[2]  # take concerts data from Concert dictionary

        if len(concerts_data["text"]) == 0:
            pass  # if there isn't Concert then pass, else add information to File
        else:
            for i in range(len(concerts_data["text"])):
                concert_public = NextConcert(concerts_data["text"][i],
                                             concerts_data["number_of_tickets"][i])
                # create instance as NextConcert class from previous Task
                if not isinstance(concert_public.add_subscription(), int):
                    all_publications += f"{concert_public.add_subscription()}"  # if no errors -
                    # use method from previous Task
                else:
                    return 0
        return all_publications

    def add_to_file(self):
        with open("Homework5.txt", "a") as f:
            f.write(self.set_publications())


if __name__ == "__main__":
    answer1 = input('Press "Y" if you want to add publication?\n')  # first question
    while answer1.lower() == "y":
        answer2 = int(input("Which type of publishing you prefer?\n1 - Console Mode"
                            "\n2 - File Mode\n"))
        if answer2 == 1:
            main()  # call function from previous task (line 1)
        elif answer2 == 2:
            print(FromFile.__doc__)  # just to inform which type of
            # file description should be specified
            file = input("Please, input directory of your file: ")
            x = FromFile(file)  # create instance from new class
            if not isinstance(x.get_values(), int):  # if error is in file, method returns 0
                if not isinstance(x.set_publications(), int):
                    x.add_to_file()  # if no errors - then call method that adds new publications
                    remove(file)  # remove file
                    print("Thanks! Your file was imported successfully and then removed!")
        answer1 = input('Press "Y" if you want to add new publication?\n')
        # new question, if answer is yes - call function again
