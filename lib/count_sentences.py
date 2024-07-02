#!/usr/bin/env python3

class MyString:
  def __init__(self, value = ""):
    self.value = value
  
  @property
  def value(self):
    return self._value
  
  @value.setter
  def value(self, value):
    if type(value) == str:
      self._value = value
    else:
      print("The value must be a string.")
  
  # def is_sentence(self, value):
  #   if type(value) == str and value[-1] == ".":
  #     self._value = value
  #     return True
  #   else:
  #     return False
