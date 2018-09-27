import sys
from PyQt5.QtWidgets import QDialog, QApplication
from PyQt5.QtGui import QIntValidator, QDoubleValidator
from PyQt5.QtCore import QCoreApplication
from Interface import Ui_Dialog

#convert the serving size or capsule weight to grams
#

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
        #create a QValidator to inhibit text entry
        self.double_validator = QDoubleValidator()
        #define input fields
        self.input = {'convert from': self.ui.fromCombo,  #given units
                      'convert to': self.ui.toCombo,      #desired units
                      'serving': self.ui.servingLE,       #serving/capsule weight
                      'arsenic entry': self.ui.asLE,      #arsenic value
                      'cadmium entry': self.ui.cdLE,      #cadmium value
                      'lead entry': self.ui.pbLE,         #lead value
                      'mercury entry': self.ui.hgLE}      #mercury value
        #define display fields
        self.display = {'arsenic result': self.ui.asL,      
                        'cadmium result': self.ui.cdL,
                        'lead result': self.ui.pbL,
                        'mercury result': self.ui.hgL}
        self.arsenic = None
        self.cadmium = None
        self.lead = None
        self.mercury = None
        #apply validators to the relevant input fields
        self.restrict_input()        
        #upon text entry, update the display to show the converted values
        self.input['serving'].textChanged.connect(self.display_conversion)
        self.input['arsenic entry'].textChanged.connect(self.display_conversion)
        self.input['cadmium entry'].textChanged.connect(self.display_conversion)
        self.input['lead entry'].textChanged.connect(self.display_conversion)
        self.input['mercury entry'].textChanged.connect(self.display_conversion)
        #place the UI onscreen
        self.show()
        
    def display_conversion(self):
        self.calculate_it()
        self.display['arsenic result'].setText(self.arsenic)
        self.display['cadmium result'].setText(self.cadmium)
        self.display['lead result'].setText(self.lead)
        self.display['mercury result'].setText(self.mercury)

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