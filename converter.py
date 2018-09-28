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

#restrict_input takes a dict of line_edits and a QValidator. It applies the validator to each field.
def restrict_input(input_fields, validator):
    for name, field in input_fields.items():
      field.setValidator(validator)


class Converter(QDialog):
    """BasicDialog sets up a dialog box with the supplied user interface.
    Extracts basic functionality into an inheritable class"""    
    def __init__(self):
        #Run setup on the given user interface
        super().__init__()
        self.ui = Ui_Dialog()
        self.ui.setupUi(self)
        self.setup_interaction()
        #place the UI onscreen
        self.show()

    def setup_interaction(self):
        self.setup_dropdowns()
        self.setup_text_entry()
        self.setup_displays()
        self.validate_entry()
        self.update_on_entry()
     
    def setup_dropdowns(self):
      #define dropdown selectors
      self.dropdown_fields = {
        'from': self.ui.from_combo,             #given units
        'to':   self.ui.to_combo,               #desired units
        'weight_units': self.ui.weight_combo}   #serving size/tab/capsule weight units

    def setup_text_entry(self):
      #define text entry fields
      self.text_entry_fields = {
        'weight_entry': self.ui.weight_entry,       #serving/capsule weight value
        'as_entry':     self.ui.given_as_entry,     #arsenic value
        'cd_entry':     self.ui.given_cd_entry,     #cadmium value
        'pb_entry':     self.ui.given_pb_entry,     #lead value
        'hg_entry':     self.ui.given_hg_entry}     #mercury value

    def setup_displays(self):
      #define display fields
      self.given_units = {
        'as_unit': self.ui.given_as_unit,
        'cd_unit': self.ui.given_cd_unit,
        'pb_unit': self.ui.given_pb_unit,
        'hg_unit': self.ui.given_hg_unit}
      self.calc_units = {
        'as_unit': self.ui.calc_as_unit,
        'cd_unit': self.ui.calc_cd_unit,
        'pb_unit': self.ui.calc_pb_unit,
        'hg_unit': self.ui.calc_hg_unit}
      self.calc_values = {
        'as_value': self.ui.calc_as_value,
        'cd_value': self.ui.calc_cd_value,
        'pb_value': self.ui.calc_pb_value,
        'hg_value': self.ui.calc_hg_value}

    def validate_entry(self):
      #create a QValidator to inhibit text entry
      self.double_validator = QDoubleValidator()
      #apply the validator to the relevant input fields
      restrict_input(self.text_entry_fields, self.double_validator) 

    def update_on_entry(self):
      #upon text entry, update the display to show the converted values
      for key, field in self.text_entry_fields.items():
        field.textChanged.connect(self.display_conversion)
      self.dropdown_fields['from'].currentIndexChanged.connect(self.update_given_units)
      self.dropdown_fields['to'].currentIndexChanged.connect(self.update_calc_units)
    
    def update_given_units(self):
      for key, field in self.given_units.items():
        field.setText(self.dropdown_fields['from'].currentText())

    def update_calc_units(self):
      for key, field in self.calc_units.items():
        field.setText(self.dropdown_fields['to'].currentText())








    #calculate the converted values and set the display to the value  
    def display_conversion(self):
        self.calculate_conversion()
        self.calc_values['as_value'].setText(self.arsenic)
        self.calc_values['cd_value'].setText(self.cadmium)
        self.calc_values['pb_value'].setText(self.lead)
        self.calc_values['hg_value'].setText(self.mercury)

    #use the entered values to store
    def calculate_conversion(self):
        self.arsenic = get_conversion(self.text_entry_fields['arsenic entry'],
                                      self.text_entry_fields['serving'])
        self.cadmium = get_conversion(self.text_entry_fields['cadmium entry'],
                                      self.text_entry_fields['serving'])
        self.lead = get_conversion(self.text_entry_fields['lead entry'],
                                   self.text_entry_fields['serving'])
        self.mercury = get_conversion(self.text_entry_fields['mercury entry'],
                                      self.text_entry_fields['serving'])

            
if __name__ == '__main__':
    app = QCoreApplication.instance()
    if app is None:
        app = QApplication(sys.argv)
        
    prog = Converter()
    
    sys.exit(app.exec_())