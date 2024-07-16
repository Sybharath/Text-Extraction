from Backend.src.parser_prescription import Prescriptionparser
import pytest

@pytest.fixture()
def doc_1_maria():
    document_text = '''
Dr John Smith, M.D
2 Non-Important Street,
New York, Phone (000)-111-2222
Name: Marta Sharapova Date: 5/11/2022
Address: 9 tennis court, new Russia, DC
Prednisone 20 mg
Lialda 2.4 gram
Directions:
Prednisone, Taper 5 mg every 3 days,
Finish in 2.5 weeks -
Lialda - take 2 pill everyday for 1 month
Refill: 3 times
'''
    return Prescriptionparser(document_text)

@pytest.fixture()
def doc_2_virat():
    document_text = '''
Dr John >mith, M.D

2 Non-Important street,
New York, Phone (900)-323- ~2222

Name:  Virat Kohli Date: 2/05/2022

Address: 2 cricket blvd, New Delhi

Omeprazole 40 mg

Directions: Use two tablets daily for three months
Refill: 3 times
'''
    return Prescriptionparser(document_text)

@pytest.fixture()
def doc_3_empty():
    return Prescriptionparser('')

def test_get_name(doc_1_maria, doc_2_virat, doc_3_empty):
    assert doc_1_maria.get_feild('patient_name') == 'Marta Sharapova'
    assert doc_2_virat.get_feild('patient_name') == 'Virat Kohli'
    assert doc_3_empty.get_feild('patient_name') == None

def test_get_address(doc_1_maria, doc_2_virat, doc_3_empty):
    assert doc_1_maria.get_feild('patient_address') == '9 tennis court, new Russia, DC'
    assert doc_2_virat.get_feild('patient_address') == '2 cricket blvd, New Delhi'
    assert doc_3_empty.get_feild('patient_address') == None

def test_get_medicines(doc_1_maria, doc_2_virat, doc_3_empty):
    assert doc_1_maria.get_feild('patient_medicine') == 'Prednisone 20 mg\nLialda 2.4 gram'
    assert doc_2_virat.get_feild('patient_medicine') == 'Omeprazole 40 mg'
    assert doc_3_empty.get_feild('patient_medicine') is None

def test_get_directions(doc_1_maria, doc_2_virat, doc_3_empty):
    assert doc_1_maria.get_feild('directions') == 'Prednisone, Taper 5 mg every 3 days,\nFinish in 2.5 weeks -\nLialda - take 2 pill everyday for 1 month'
    assert doc_2_virat.get_feild('directions') == 'Use two tablets daily for three months'
    assert doc_3_empty.get_feild('directions') is None

def test_get_refill(doc_1_maria,doc_2_virat,doc_3_empty):
    assert doc_1_maria.get_feild("refill") == '3'
    assert doc_2_virat.get_feild("refill") == '3'
    assert doc_3_empty.get_feild("refill") == None

def test_parse(doc_1_maria,doc_2_virat,doc_3_empty):
    recoed_maria = doc_1_maria.parse()
    assert recoed_maria['patient_name'] == 'Marta Sharapova'
    assert recoed_maria['patient_address'] == '9 tennis court, new Russia, DC'
    assert recoed_maria['patient_medicine'] == 'Prednisone 20 mg\nLialda 2.4 gram'
    assert recoed_maria['directions'] == 'Prednisone, Taper 5 mg every 3 days,\nFinish in 2.5 weeks -\nLialda - take 2 pill everyday for 1 month'
    assert recoed_maria['refill'] == '3'

    record_virat = doc_2_virat.parse()
    assert record_virat =={
        'patient_name': 'Virat Kohli',
        'patient_address': '2 cricket blvd, New Delhi',
        'patient_medicine': 'Omeprazole 40 mg',
        'directions': 'Use two tablets daily for three months',
        'refill': '3'
    }

    record_empty = doc_3_empty.parse()
    assert record_empty == {
        'patient_name': None,
        'patient_address': None,
        'patient_medicine': None,
        'directions': None,
        'refill': None
    }


