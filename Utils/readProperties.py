import configparser

config = configparser.RawConfigParser()
config.read("./Configurations/inputData.ini")


class ReadConfig():
    def getSauceDemoURL(self):
        # sauceDemoURL = config.get('URLs', 'sauceDemoURL')
        # return sauceDemoURL

        return config.get('URLs', 'sauceDemoURL')

    def getUsername(self):
        username = config.get('Login Details', 'username')
        return username

    def getPassword(self):
        password = config.get('Login Details', 'password')
        return password

    # ToDo Alvin please do the code to read the FirstName
    # ToDo Noma please do the code to read the LastName
    # ToDo Tsego please do the code to read the zipCode
