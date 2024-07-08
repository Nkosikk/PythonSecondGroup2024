import configparser

config = configparser.RawConfigParser()
config.read("./Configurations/inputData.ini")


class ReadConfig():
    def getSauceDemoURL(self):

        # sauceDemoURL = config.get('URLs', 'sauceDemoURL')
        # return sauceDemoURL

        return config.get('URLs', 'sauceDemoURL')

    # ToDo Gomo p[lease do the code to read the username

    # ToDo Kate please do the code to read the password

    # ToDo Alvin please do the code to read the FirstName
    # ToDo Noma please do the code to read the LastName
    # ToDo Tsego please do the code to read the zipCode
