import unittest
from logics import PostgresConnector
class TestDBLogics(unittest.TestCase):
   def Test_User(self):
       Expected=str
       Result=type(user)
       self.assertEqual(Expected, Result)

   def Test_Password(self):
       Expected = str
       Result = type(Password)
       self.assertEqual(Expected, Result)
  
if __name__ == '__main__':
    unittest.main(verbosity=2)
