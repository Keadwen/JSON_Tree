# Module json_collector - locate the data inside JSON in the easier way.
import os
import re
import json

__author__ = 'Jakub Mlynarczyk (jkbmlynarczyk@gmail.com)'


class JsonCollector(object):
  """Search inside JSON files for a requested subtrees values.

  JsonCollector module provides more flexible way to find a data inside
  any JSON file. While creating the object it is mandatory to specify 
  the location of file(s) and the tree from which we want to collect data.

  Args:
    json_location (str): a location of the JSON file.
    tree_word (string): an object with values to search for.
    json_data (dict): an object contains all data from json.
    json_search_result (dict): an object with requested key and it's value.
  """

  def __init__(self):
    self.json_location = None
    self.tree_word = None
    self.json_data = {}
    self.json_search_result = {}

  def GetData(self, json_location, tree_word):
    """Search for a key in a JSON file.

    Returns the dict with only one key:value pair if requested key exists.
    If the key not in a file, then returns empty dict. 
    """
    self.json_location = json_location
    self.tree_word = tree_word
    self._OpenJson()
    self.json_search_result = self._FindTree(self.json_data, {})
    return self.json_search_result

  def _OpenJson(self):
    """Checks the location of JSONs file and reads all of them."""
    try:
      json_file = open(self.json_location)
      self.json_data = json.load(json_file)
      json_file.close()
    except IOError:
      return {}

  def _FindTree(self, dict_in, dict_out):
    """Return dict value under requested subtrees.

    Method provides recursive search to collect all key:value pairs inside
    a nested dict that can contain list and dicts as values.

    Args:
      dict_in (dict): an object with a dict to scan.
      dict_out (dict): an object with all key:values that where nested

    Returns the value of the key that has been requested by a user.
    If a key does not exist in the JSON file, returns an empty dict object.
    """
    for key, value in dict_in.iteritems():
      dict_out[key] = value             # Append the dict with a nested k:v
      if isinstance(value, dict):       
        self._FindTree(value, dict_out)  # Dict as a value, recursive search.
      elif isinstance(value, list):     # List as a value.
        for i in value:
          self._FindTree(i, dict_out)    # Recursive search for each element.

    return dict_out.get(self.tree_word, {})  # Return only requested key.
