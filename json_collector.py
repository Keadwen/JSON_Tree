# Module json_collector - locate the data inside JSON in a faster and easier way.
from json import *
from os import *
from re import match

__author__ = 'Jakub Mlynarczyk (jkbmlynarczyk@gmail.com)'


class JsonCollector(object):
  """Search inside JSON files for a requested subtrees values.

  JsonCollector module provides more flexible way to find a data inside
  any JSON file. While creating the object it is mandatory to specify 
  the location of file(s) and the tree from which we want to collect data.

  Args:
    json_location (str): a location of the JSON file(s).
    tree_word (tuple): an object with values to search for.
    json_files (dict): contains all open JSON files (k: filename, v: object)
  """
  def __init__(self, json_location, tree_word):
    self.json_location = json_location
    self.tree_word = tree_word
    self.json_files = dict()

  def OpenJson(self):
  """Checks the location of JSONs file and opens all of them."""
  try:
    os.chdir(json_location)  # Change to requested location and get files list.
    f_list = os.listdir('./')
  except OSError:
    return {}

  # Open only json files.
  for f in f_list:  
    if re.match('.*\.json$', f):
      self.json_files[f] = open('./'+f)


  # create a dict of objects (key: file_name, value: open_object)
  # return the dict
  self.json_files = json_files


  def FindTree(self):
  """Return dict all values under requested location."""
