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

    def getFirstName(self):
        firstname = config.get('Billing Information', 'firstName')
        return firstname

    # ToDo Noma please do the code to read the LastName
    def getZipCode(self):
        return config.get('Billing Informations', 'ZipCode')
