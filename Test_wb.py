from unittest import TestCase, main
from wb import fizzbuzz

class TestFizzBuzz(TestCase):

  def test_div_by_15(self):
    result_1 = fizzbuzz(15)
    self.assertEqual(result_1, 'FizzBuzz')
    result_2 = fizzbuzz(30)
    self.assertEqual(result_2, 'FizzBuzz')
    self.assertEqual(fizzbuzz(60), 'FizzBuzz')

  def test_div_by_10(self):
    self.assertNotEqual(fizzbuzz(10),'Fizz')
    # self.assertNotEqual(fizzbuzz(10),'Buzz')
    self.assertFalse(fizzbuzz(20))
  def test_div_by_5(self):
    self.assertEqual(fizzbuzz(60), 'FizzBuzz')
    self.assertEqual(fizzbuzz(60), 'FizzBuzz')

#   def test_negative(self):
#     self.assertTrue()


if __name__ == '__main__':
  main()