from selenium import selenium
import unittest, time, re

class sel(unittest.TestCase):
    def setUp(self):
        self.verificationErrors = []
        self.selenium = selenium("localhost", 4444, "*chrome", "http://127.0.0.1:8000/")
        self.selenium.start()
    
    def test_sel(self):
        sel = self.selenium
        sel.open("/polls/")
        try: self.failUnless(sel.is_text_present("exact:Best football team?"))
        except AssertionError, e: self.verificationErrors.append(str(e))
        sel.click("link=exact:Best football team?")
        sel.wait_for_page_to_load("30000")
        try: self.failUnless(sel.is_text_present("FC Barcelona"))
        except AssertionError, e: self.verificationErrors.append(str(e))
        sel.click("css=input[type=submit]")
        sel.wait_for_page_to_load("30000")
        sel.click("choice1")
        sel.click("css=input[type=submit]")
        sel.wait_for_page_to_load("30000")
        try: self.failUnless(sel.is_text_present("exact:Vote again?"))
        except AssertionError, e: self.verificationErrors.append(str(e))
    
    def tearDown(self):
        self.selenium.stop()
        self.assertEqual([], self.verificationErrors)

if __name__ == "__main__":
    unittest.main()
