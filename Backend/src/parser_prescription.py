import re

from Backend.src.parser_generic import MedicalDocParser

import abc
class Prescriptionparser(MedicalDocParser):
    def __init__(self,text):
        MedicalDocParser.__init__(self, text)

    def parse(self):
        return {
            'patient_name': self.get_feild('patient_name'),
            'patient_address': self.get_feild('patient_address'),
            'patient_medicine': self.get_feild('patient_medicine'),
            'directions': self.get_feild('directions'),
            'refill': self.get_feild('refill')
        }

    def get_feild(self,feild_name):
        pattern =''
        flags = None

        pattern_dict = {
            'patient_name': {'pattern': "Name:(.*)Date",'flags': 0},
            'patient_address': {'pattern': "Address:(.*)\n", 'flags': 0},
            'patient_medicine': {'pattern': "Address[^\n]*(.*)Directions", 'flags': re.DOTALL},
            'directions': {'pattern': "Directions:(.*)Refill", 'flags': re.DOTALL},
            'refill': {'pattern': 'Refill:(.*)times', 'flags': re.DOTALL}
        }

        pattern_object = pattern_dict.get(feild_name)
        if pattern_object:
            matches = re.findall(pattern_object['pattern'], self.text,flags=pattern_object['flags'])
            if len(matches) > 0:
                return matches[0].strip()


    # def get_name(self):
    #     pattern = "Name:(.*)Date"
    #     matches = re.findall(pattern,self.text)
    #     if len(matches)>0:
    #         return matches[0].strip()
    #
    # def get_address(self):
    #     pattern = "Address:(.*)\n"
    #     matches = re.findall(pattern,self.text)
    #     if len(matches)>0:
    #         return matches[0].strip()
    #
    # def get_medicine(self):
    #     pattern = "Address[^\n]*(.*)Directions"
    #     matches = re.findall(pattern,self.text,re.DOTALL)
    #     if len(matches)>0:
    #         return matches[0].strip()
    #
    # def get_directions(self):
    #     pattern = "Directions:(.*)Refill"
    #     matches = re.findall(pattern,self.text,re.DOTALL)
    #     if len(matches)>0:
    #         return matches[0].strip()
    #
    # def get_refill(self):
    #     pattern = 'Refill:(.*)times'
    #     matches = re.findall(pattern,self.text,re.DOTALL)
    #     if len(matches)>0:
    #         return matches[0].strip()

if __name__ == '__main__':
    document_text = '''
Name: Marta Sharapova Date: 5/11/2022

Address: 9 tennis court, new Russia, DC
Prednisone 20 mg
Lialda 2.4 gram
Directions:

Prednisone, Taper 5 mg every 3 days,
Finish in 2.5 weeks a
Lialda - take 2 pill everyday for 1 month

Refill: 2 times
'''
    pp = Prescriptionparser(document_text)
    print(pp.parse())

