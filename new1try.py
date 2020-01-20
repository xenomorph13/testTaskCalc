from selenium import webdriver
import unittest
from selenium.webdriver.common.keys import Keys

class calcButton:
    def __init__(self, driver):
        self.numb1 = '//*[@id="root"]/div/div[2]/div[4]/div[1]'
        self.numb2 = '//*[@id="root"]/div/div[2]/div[4]/div[2]'
        self.numb3 = '//*[@id="root"]/div/div[2]/div[4]/div[3]'
        self.numb4 = '//*[@id="root"]/div/div[2]/div[3]/div[1]'
        self.numb5 = '//*[@id="root"]/div/div[2]/div[3]/div[2]'
        self.numb6 = '//*[@id="root"]/div/div[2]/div[3]/div[3]'
        self.numb7 = '//*[@id="root"]/div/div[2]/div[2]/div[1]'
        self.numb8 = '//*[@id="root"]/div/div[2]/div[2]/div[2]'
        self.numb9 = '//*[@id="root"]/div/div[2]/div[2]/div[3]'
        self.numb0 = '//*[@id="root"]/div/div[2]/div[5]/div[1]'
        self.sign_plus = '//*[@id="root"]/div/div[2]/div[4]/div[4]'
        self.sign_rav = '//*[@id="root"]/div/div[2]/div[5]/div[3]'
        self.sign_minus = '//*[@id="root"]/div/div[2]/div[3]/div[4]'
        self.sign_multiply = '//*[@id="root"]/div/div[2]/div[2]/div[4]'
        self.sign_division = '//*[@id="root"]/div/div[2]/div[1]/div[4]'
        self.sign_point = '//*[@id="root"]/div/div[2]/div[5]/div[2]'
        self.sign_reset = '//*[@id="root"]/div/div[2]/div[1]/div[1]'
        self.denial = '//*[@id="root"]/div/div[2]/div[1]/div[2]'
        self.sign_percent = '//*[@id="root"]/div/div[2]/div[1]/div[3]'
        self.result = "//div[contains(@class, 'component-display')]/div"
        self.driver = driver

    def click_key(self, node):
        node.click()

    def find_node(self, xpath):
        return self.driver.find_element_by_xpath(xpath)

    def do_buttons(self, buttons=[]):
        for button in buttons:
            self.click_key(self.find_node(button))


class CalcucatorTest(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.get('https://algont.github.io/react-calculator/')
        self.calculator = calcButton(self.driver)

    #проверка нажатия доступных кнопок чисел 0+1+2+3+4+5+6+7+8+9
    def test_00(self):
        do_buttons = [self.calculator.numb0, self.calculator.numb1, self.calculator.numb2, self.calculator.numb3, self.calculator.numb4, self.calculator.numb5 ,self.calculator.numb6, self.calculator.numb7, self.calculator.numb8, self.calculator.numb9]
        right_res = '0123456789'
        try:
            self.calculator.do_buttons(do_buttons)
            print(self.calculator.find_node(self.calculator.result).text) 
            print(right_res) 
            assert self.calculator.find_node(self.calculator.result).text == right_res
            print('Тест: test_00 пройден')
        except Exception:
            print('Тест: test_00 не пройден')
            
    #проверка операции сложения 1+2
    def test_01(self):
        do_buttons = [self.calculator.numb1, self.calculator.sign_plus, self.calculator.numb2, self.calculator.sign_rav]
        right_res = '3'
        try:
            self.calculator.do_buttons(do_buttons)
            print(self.calculator.find_node(self.calculator.result).text) 
            print(right_res) 
            assert self.calculator.find_node(self.calculator.result).text == right_res
            print('Тест: test_01 пройден')
        except Exception:
            print('Тест: test_01 не пройден')

      #проверка операции вычетания 9-5
    def test_02(self):
        do_buttons = [self.calculator.numb9, self.calculator.sign_minus, self.calculator.numb5, self.calculator.sign_rav]
        right_res = '4'
        try:
            self.calculator.do_buttons(do_buttons)
            print(self.calculator.find_node(self.calculator.result).text) 
            print(right_res) 
            assert self.calculator.find_node(self.calculator.result).text == right_res
            print('Тест: test_02 пройден')
        except Exception:
            print('Тест: test_02 не пройден')

    #проверка вывода дробного числа 56.9
    def test_03(self):
        do_buttons = [self.calculator.numb5, self.calculator.numb6, self.calculator.sign_point, self.calculator.numb9]
        right_res = '56.9'
        try:
            self.calculator.do_buttons(do_buttons)
            print(self.calculator.find_node(self.calculator.result).text) 
            print(right_res) 
            assert self.calculator.find_node(self.calculator.result).text == right_res
            print('Тест: test_03 пройден')
        except Exception:
            print('Тест: test_03 не пройден')
            
    #проверка операции очищения поля 2+4= С
    def test_04(self):
        do_buttons = [self.calculator.numb2, self.calculator.sign_plus, self.calculator.numb4, self.calculator.sign_rav, self.calculator.sign_reset]
        right_res = '0'
        try:
            self.calculator.do_buttons(do_buttons)
            print(self.calculator.find_node(self.calculator.result).text) 
            print(right_res) 
            assert self.calculator.find_node(self.calculator.result).text == right_res
            print('Тест: test_04 пройден')
        except Exception:
            print('Тест: test_04 не пройден')

    #проверка операции деления 37/8
    def test_05(self):
        do_buttons = [self.calculator.numb3, self.calculator.numb7, self.calculator.sign_division, self.calculator.numb8, self.calculator.sign_rav]
        right_res = '4.625'
        try:
            self.calculator.do_buttons(do_buttons)
            print(self.calculator.find_node(self.calculator.result).text) 
            print(right_res) 
            assert self.calculator.find_node(self.calculator.result).text == right_res
            print('Тест: test_05 пройден')
        except Exception:
            print('Тест: test_05 не пройден')
            
    #проверка операции умножения 9*2
    def test_06(self):
        do_buttons = [self.calculator.numb9, self.calculator.sign_multiply, self.calculator.numb2, self.calculator.sign_rav]
        right_res = '18'
        try:
            self.calculator.do_buttons(do_buttons)
            print(self.calculator.find_node(self.calculator.result).text) 
            print(right_res) 
            assert self.calculator.find_node(self.calculator.result).text == right_res
            print('Тест: test_06 пройден')
        except Exception:
            print('Тест: test_06 не пройден')
            
    #проверка операции с одним отрицательным,вторым дробным -6+1.1
    def test_07(self):
        do_buttons = [self.calculator.numb6, self.calculator.denial, self.calculator.sign_plus, self.calculator.numb1, self.calculator.sign_point, self.calculator.numb1, self.calculator.sign_rav]
        right_res = '-4.9'
        try:
            self.calculator.do_buttons(do_buttons)
            print(self.calculator.find_node(self.calculator.result).text) 
            print(right_res) 
            assert self.calculator.find_node(self.calculator.result).text == right_res
            print('Тест: test_07 пройден')
        except Exception:
            print('Тест: test_07 не пройден')
            
      #проверка операции сложение+умножение 1+4*7
    def test_08(self):
        do_buttons = [self.calculator.numb1, self.calculator.sign_plus, self.calculator.numb4, self.calculator.sign_multiply, self.calculator.numb7, self.calculator.sign_rav]
        right_res = '29'
        try:
            self.calculator.do_buttons(do_buttons)
            print(self.calculator.find_node(self.calculator.result).text) 
            print(right_res) 
            assert self.calculator.find_node(self.calculator.result).text == right_res
            print('Тест: test_08 пройден')
        except Exception:
            print('Тест: test_08 не пройден')

         #проверка операции умножение+сложение 2*2+1   
    def test_09(self):
        do_buttons = [self.calculator.numb2, self.calculator.sign_multiply, self.calculator.numb2, self.calculator.sign_plus, self.calculator.numb1, self.calculator.sign_rav]
        right_res = '5'
        try:
            self.calculator.do_buttons(do_buttons)
            print(self.calculator.find_node(self.calculator.result).text) 
            print(right_res) 
            assert self.calculator.find_node(self.calculator.result).text == right_res
            print('Тест: test_09 пройден')
        except Exception:
            print('Тест: test_09 не пройден')         

     #проверка операции вычисления 10% от 20. 20*10%
    def test_10(self):
        do_buttons = [self.calculator.numb2, self.calculator.numb0, self.calculator.sign_multiply, self.calculator.numb1, self.calculator.numb0, self.calculator.sign_percent]
        right_res = '2'
        try:
            self.calculator.do_buttons(do_buttons)
            print(self.calculator.find_node(self.calculator.result).text) 
            print(right_res) 
            assert self.calculator.find_node(self.calculator.result).text == right_res
            print('Тест: test_02 пройден')
        except Exception:
            print('Тест: test_02 не пройден')       
            
    def tearDown(self):  #После каждого теста закрываем браузер
       self.driver.quit() 

if __name__ == '__main__':
    testLoad = unittest.TestLoader()
    runner = unittest.TextTestRunner(verbosity=2)
    unittest.main()

  
