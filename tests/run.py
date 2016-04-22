import unittest
import glob
from lxml import etree

class TestPerMessages(unittest.TestCase):
  def setUp(self):
      with open("../schemas/sand_messages.xsd") as f: 
        sand_schema_doc = etree.parse(f)
        self.sand_schema = etree.XMLSchema(sand_schema_doc)

  def test_valid_messages(self):
      for message in glob.glob("../per/*-OK-*.xml"):
        sand_message = etree.parse(message)
        self.assertTrue(self.sand_schema.validate(sand_message))
        print "Test succesful : " + message
  
  def test_invalid_messages(self):
      for message in glob.glob("../per/*-KO-*.xml"):
        sand_message = etree.parse(message)
        self.assertFalse(self.sand_schema.validate(sand_message))
        print "Test succesful : " + message

class TestMetricsMessages(unittest.TestCase):
  def setUp(self):
      with open("../schemas/sand_messages.xsd") as f: 
        sand_schema_doc = etree.parse(f)
        self.sand_schema = etree.XMLSchema(sand_schema_doc)

  def test_valid_messages(self):
      for message in glob.glob("../metrics/*-OK-*.xml"):
        sand_message = etree.parse(message)
        self.assertTrue(self.sand_schema.validate(sand_message))
        print "Test succesful : " + message
  
  def test_invalid_messages(self):
      for message in glob.glob("../metrics/*-KO-*.xml"):
        sand_message = etree.parse(message)
        self.assertFalse(self.sand_schema.validate(sand_message))
        print "Test succesful : " + message
  
if __name__ == '__main__':
      unittest.main()