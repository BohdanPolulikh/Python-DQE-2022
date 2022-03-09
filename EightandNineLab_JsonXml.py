import json
from FifthLab_Classes import News, PrivateAd, NextConcert, main
from SixthLab_Expand_fifth import FromFile
from os import remove
import xml.etree.ElementTree as ET


def is_right_file(lst_of_dicts):
    """
    Static function to check whether prepared list of dictionaries will map with correct data.
    :param lst_of_dicts:
    :return: True - if correct, False - if wrong and error message will appear
    """
    for public in lst_of_dicts:
        try:
            if public['title'] == "News":
                try:
                    p = News(public['text'], public['city'])
                except KeyError:
                    print("Review your file! You missed mandatory value Text or City!")
                    return False
                else:
                    if isinstance(p.add_subscription(), int):
                        return False
            elif public['title'] == "Private Ad":
                try:
                    p = PrivateAd(public['text'], public['expiration date'])
                except KeyError:
                    print("Review your file! You missed mandatory value Text "
                          "or Expiration Date!")
                    return False
                else:
                    if isinstance(p.add_subscription(), int):
                        return False
            elif public['title'] == "Next Concert":
                try:
                    p = NextConcert(public['text'], public['number of tickets'])
                except KeyError:
                    print("Review your file! You missed mandatory value Text "
                          "or Number of tickets!")
                    return False
                else:
                    if isinstance(p.add_subscription(), int):
                        return False
            else:
                print("Check file again! Change wrong title in specified file.")
                return False
        except KeyError:
            print("Review your file! You missed mandatory value Title!")
            return False
    return True


def create_information(lst_of_dicts):
    """
    Static function to write all information from the processed file.
    :param lst_of_dicts:
    :return: result string
    """
    if not is_right_file(lst_of_dicts):
        return 0
    else:
        result = ''
        for public in lst_of_dicts:
            if public['title'] == 'News':
                p = News(public['text'], public['city'])
                result += p.add_subscription()
            elif public['title'] == 'Private Ad':
                p = PrivateAd(public['text'], public['expiration date'])
                result += p.add_subscription()
            elif public['title'] == 'Next Concert':
                p = NextConcert(public['text'], public['number of tickets'])
                result += p.add_subscription()
    return result


def add_to_file(lst_of_dicts):
    """
    Write information to file Homework5.txt
    :param lst_of_dicts:
    :return:
    """
    if not isinstance(create_information(lst_of_dicts), int):
        with open("Homework5.txt", 'a') as f:
            f.write(create_information(lst_of_dicts))
    else:
        return 0


class JsonFile:
    """
    You should specify file with .json type. Each element should contain Title
    and Text.
    """
    def __init__(self, pathfile):
        self.pathfile = pathfile

    def from_file_to_dict(self):
        with open(self.pathfile) as json_file:
            try:
                data = json.load(json_file)
            except json.decoder.JSONDecodeError:
                print("Failed! Please, check JSON file structure.")
                return 0
            else:
                return data

    def set_information(self):
        try:
            return add_to_file(self.from_file_to_dict())
        except TypeError:
            return 0


class XmlFile:
    """
    You should specify file with .xml type. Each element should contain Title
    and Text.
    Expected xml structure:
    <root>
        <publication title="">
            <text>...</text>
        </publication>
    </root>
    """
    def __init__(self, pathfile):
        self.pathfile = pathfile

    def from_file_to_dict(self):
        try:
            xml_file = ET.parse(self.pathfile)
        except ET.ParseError:
            print("Failed! Please, check XML file structure.")
            return 0
        else:
            root = xml_file.getroot()
            all_publication_lst = list()
            for publications in root.findall('publication'):
                all_publication_lst.append({'title': publications.attrib['title']})
                for elem in publications:
                    all_publication_lst[-1][elem.tag] = elem.text
            for dct in all_publication_lst:
                if "expiration_date" in dct.keys():
                    dct["expiration date"] = dct.pop("expiration_date")
                elif "number_of_tickets" in dct.keys():
                    dct["number of tickets"] = dct.pop("number_of_tickets")
            return all_publication_lst

    def set_information(self):
        try:
            return add_to_file(self.from_file_to_dict())
        except TypeError:
            return 0

'''

'''
if __name__ == "__main__":
    answer1 = input('Press "Y" if you want to add publication?\n')  # first question
    while answer1.lower() == "y":
        answer2 = int(input("Which type of publishing you prefer?\n1 - Console Mode"
                            "\n2 - File Mode\n"))
        if answer2 == 1:
            main()  # call function from previous task (line 1)
        elif answer2 == 2:
            answer3 = int(input("Which type of import file you use>\n"
                                "1 - .txt\n2 - .json\n3 - .xml\n"))
            if answer3 == 1:
                print(FromFile.__doc__)  # just to inform which type of
                # file description should be specified
                file = input("Please, input directory of your file: ")
                x = FromFile(file)  # create instance from new class
                if not isinstance(x.get_values(), int):  # if error is in file, method returns 0
                    if not isinstance(x.set_publications(), int):
                        x.add_to_file()  # if no errors - then call method that adds new publications
                        remove(file)  # remove file
                        print("Thanks! Your file was imported successfully and then removed!")
            elif answer3 == 2:  # choose JSON option
                print(JsonFile.__doc__)
                file = input("Please, input directory of your file: ")
                x = JsonFile(file)  # create JSON instance
                if not isinstance(x.set_information(), int):
                    remove(file)  # remove file
                    print("Thanks! Your file was imported successfully and then removed!")
            elif answer3 == 3:  # choose XML option
                print(XmlFile.__doc__)
                file = input("Please, input directory of your file: ")
                x = XmlFile(file)  # create XML instance
                if not isinstance(x.set_information(), int):
                    remove(file)  #remove file
                    print("Thanks! Your file was imported successfully and then removed!")
        answer1 = input('Press "Y" if you want to add new publication?\n')
        # new question, if answer is yes - call function again

