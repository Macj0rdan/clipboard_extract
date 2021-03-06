from configparser import SafeConfigParser
from os import path


class config_rw():
    # this functions reads the config file and returns all tools set to active in the ini file
    # check if file exists
    # if not then create it with base parameters
    def __init__(self):
        self.config = SafeConfigParser()
        home_path = path.expanduser('~')  # gets the default home folder
        tesseract_sub_folder = "AppData\\Local\\Programs\\Tesseract-OCR\\tesseract.exe"
        standard_tesseract_path = path.join(home_path, tesseract_sub_folder)  # joins default home folder and the tesseract sub folder
        self.config_file = "config.ini"
        if not path.exists(self.config_file):  # check for the file
            self.config['Settings'] = {    # default ini values
                'path': standard_tesseract_path
                                 }
            # now write the data into file
            with open(self.config_file, 'w') as configfile:  # write file
                self.config.write(configfile)

    def read_ini(self):
        self.config.read(self.config_file)
        return self.config
