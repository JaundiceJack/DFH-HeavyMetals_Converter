import sys
from PyQt5.QtWidgets import QDialog, QApplication
from PyQt5.QtGui import QIntValidator, QDoubleValidator
from PyQt5.QtCore import QCoreApplication
from Interface import Ui_Dialog

#convert_to_double takes a string
#if the string is a float, the text is returned as a float.
#if the string was not a number, an exception is raised.
#if the string was empty, 0 is returned.
def convert_to_double(text):
    if text != '':
        try:
            return float(text)
        except ValueError:
            print("Unable to convert entry.")
            pass
        except Exception as ex:
            print(ex)
    else:
        return 0
    
#get_conversion takes two Q-input fields
#the text is converted to a double
#the serving is multiplied by 0.001  
def get_conversion(field, serving):
    value1 = convert_to_double(field.text())
    value2 = convert_to_double(serving.text())
    return str(value1 * (value2 * 0.001))

class Converter(QDialog):
    """BasicDialog sets up a dialog box with the supplied user interface.
    Extracts basic functionality into an inheritable class"""    
    def __init__(self):
        #Run setup on the given user interface
        super().__init__()
        self.ui = Ui_Dialog()
        self.ui.setupUi(self)
        self.double_validator = QDoubleValidator()
        self.input = {'convert from': self.ui.fromCombo,
                      'convert to': self.ui.toCombo,
                      'serving': self.ui.servingLE,
                      'arsenic entry': self.ui.asLE,
                      'cadmium entry': self.ui.cdLE,
                      'lead entry': self.ui.pbLE,
                      'mercury entry': self.ui.hgLE,
                      'arsenic result': self.ui.asL,
                      'cadmium result': self.ui.cdL,
                      'lead result': self.ui.pbL,
                      'mercury result': self.ui.hgL}
        self.restrict_input()
        self.arsenic = None
        self.cadmium = None
        self.lead = None
        self.mercury = None
        self.input['arsenic entry'].textChanged.connect(self.display_conversion)
        self.input['cadmium entry'].textChanged.connect(self.display_conversion)
        self.input['lead entry'].textChanged.connect(self.display_conversion)
        self.input['mercury entry'].textChanged.connect(self.display_conversion)
        self.show()
        
    def display_conversion(self):
        self.calculate_it()
        self.input['arsenic result'].setText(self.arsenic)
        self.input['cadmium result'].setText(self.cadmium)
        self.input['lead result'].setText(self.lead)
        self.input['mercury result'].setText(self.mercury)

    def calculate_it(self):
        self.arsenic = get_conversion(self.input['arsenic entry'],
                                      self.input['serving'])
        self.cadmium = get_conversion(self.input['cadmium entry'],
                                      self.input['serving'])
        self.lead = get_conversion(self.input['lead entry'],
                                   self.input['serving'])
        self.mercury = get_conversion(self.input['mercury entry'],
                                      self.input['serving'])

    def restrict_input(self):
        self.input['serving'].setValidator(self.double_validator) 
        self.input['arsenic entry'].setValidator(self.double_validator) 
        self.input['cadmium entry'].setValidator(self.double_validator) 
        self.input['lead entry'].setValidator(self.double_validator) 
        self.input['mercury entry'].setValidator(self.double_validator) 

            
if __name__ == '__main__':
    app = QCoreApplication.instance()
    if app is None:
        app = QApplication(sys.argv)
        
    prog = Converter()
    
    sys.exit(app.exec_())