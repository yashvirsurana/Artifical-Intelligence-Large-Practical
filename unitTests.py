#####################################################
# UNIT TESTS FOR CAES-READER
# Copyright (C) 2015, Yashvir Surana, s1368177
# Author: Yashvir Surana <yashvirsurana@gmail.com>
# TEST Extension for: reader.py
#####################################################

import unittest as ut
import reader

class test_cases(ut.TestCase):
    
    def test_case1(self):
        c=reader.Read()
        self.assertFalse(c.readFile('case1.json','fraud')) #lawyer is not a fraud lawyer 

    def test_case2(self):
        d=reader.Read()
        self.assertTrue(d.readFile('case2.json','wikiReliable')) #wikipedia is reliable

    def test_case3(self):
        e=reader.Read()
        self.assertTrue(e.readFile('case3.json','stoleCash')) #culprit stole cash

    def test_case4(self):
        f=reader.Read()
        with self.assertRaises(ValueError):
            f.readFile('case4.json','stoleCash') #improper argument
    
    def test_case5(self):
        g=reader.Read()
        with self.assertRaises(ValueError):
            g.readFile('case5.json','stoleCash') #Incorrect JSON input

tests = ut.TestLoader().loadTestsFromTestCase(test_cases)
ut.TextTestRunner(verbosity=2).run(tests)



