from configparser import SafeConfigParser
from os import path


class config_rw():
    # this functions reads the config file and returns all tools set to active in the ini file
    # check if file exists
    # if not then create it with base parameters
    def __init__(self):
        self.config = SafeConfigParser()
        self.config_file = "config.ini"
        if not path.exists(self.config_file):  # check for the file
            self.config['Settings'] = {    # default ini values
                'path': ''
                                 }
            # now write the data into file
            with open(self.config_file, 'w') as configfile:  # write file
                self.config.write(configfile)

    def read_ini(self):
        self.config.read(self.config_file)
        return self.config
