import unittest
from unittest.mock import patch

from tmc import points
from tmc.utils import load, load_module, reload_module, get_stdout, check_source
from functools import reduce
import os
import textwrap

exercise = 'src.parilliset'
function = 'parilliset'

def get_correct(test_case: list) -> list:
    pass


@points('4.parilliset')
class ParillisetTest(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        with patch('builtins.input', side_effect=[AssertionError("Syötteen pyytämistä ei odotettu")]):
           cls.module = load_module(exercise, 'fi')

    def test_0_paaohjelma_kunnossa(self):
        ok, line = check_source(self.module)
        message = """Funktioita testaava koodi tulee sijoittaa lohkon
if __name__ == "__main__":
sisälle. Seuraava rivi tulee siirtää:
"""
        self.assertTrue(ok, message+line)

    def test_1_funktio_olemassa(self):
        try:
            from src.parilliset import parilliset
        except:
            self.assertTrue(False, 'Koodistasi pitäisi löytyä funktio nimeltä parilliset(lista: list)')
        try:
            from src.parilliset import parilliset
            parilliset([1,2])
        except:
            self.assertTrue(False, 'Toimiihan funktiokutsu\nparilliset([1,2])')

    def test_2_paluuarvon_tyyppi(self):
        parilliset = load(exercise, function, 'fi')
        val = parilliset([1,2])
        self.assertTrue(type(val) == list, f"Funktio {function} ei palauta listaa parametrin arvolla [1,2].")
    
    def test_3_lukuja_1(self):
        test_cases = {(1,2,3,4,5,6): [2,4,6], 
                      (1,2,3,4,8,9,10,12,14,15): [2,4,8,10,12,14],
                      (1,3,5,7,9,2,4,6,8,10): [2,4,6,8,10]}
        for test_case in test_cases:
            with patch('builtins.input', side_effect=[AssertionError("Syötteen pyytämistä ei odotettu")]):
                reload_module(self.module)
                output_alussa = get_stdout()
                pisimmat = load(exercise, function, 'fi')
                
                correct = test_cases[test_case]
                test_case2 = test_case[:]
                test_result = pisimmat(list(test_case))

                self.assertEqual(sorted(correct), sorted(test_result), f"Tulos {test_result} ei vastaa odotettua {correct} kutsuttaessa parilliset({test_case2})")
                self.assertEqual(test_case, test_case2, f"Funktio ei saa muuttaa alkuperäistä listaa. Arvon pitäisi olla {list(test_case2)} mutta se on {list(test_case)}.")

    def test_4_lukuja_2(self):
        test_cases = {(99,100,101,100,99,100,101): [100,100,100], 
                      (6,6,6,6,5,6,6,6,6,6,5): [6,6,6,6,6,6,6,6,6],
                      (1,1,2,2,1,1,2,2): [2,2,2,2]}
        for test_case in test_cases:
            with patch('builtins.input', side_effect=[AssertionError("Syötteen pyytämistä ei odotettu")]):
                reload_module(self.module)
                output_alussa = get_stdout()
                pisimmat = load(exercise, function, 'fi')
                
                correct = test_cases[test_case]
                test_case2 = test_case[:]
                test_result = pisimmat(list(test_case))

                self.assertEqual(sorted(correct), sorted(test_result), f"Tulos {test_result} ei vastaa odotettua {correct} parilliset({test_case2})")
                self.assertEqual(test_case, test_case2, f"Funktio ei saa muuttaa alkuperäistä listaa. Arvon pitäisi olla {list(test_case2)} mutta se on {list(test_case)}.")

    

    

    

    

   
    

    
              
if __name__ == '__main__':
    unittest.main()
