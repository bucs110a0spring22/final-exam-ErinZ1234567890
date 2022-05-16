"""
Uses the Penguin Publishing API to look up the isbns. The primary purpose of this class is to return the title of the book.
"""

import requests
import json

class BookAPI:

  """
  Parameter takes in a isbn number and then stitches it into the Penguin House API url. This url will then be used in the get() method.
  """
  def __init__(self, isbn=9780147514011):
    self.url = f'https://reststop.randomhouse.com/resources/titles/{isbn}/'

  """
  takes the url passed in to get the XML response from the Penguin Publishing API. It then converts that into a string and finds the title of the book amongst the information. It then returns the title of the book as a string.
  """
  def get(self):
    
    r = requests.get(self.url)
    response = r.content

    #converts the xml response into a string and then finds the indices that the title starts and ends at.
    respString = str(response)
    titleStringStart = respString.find("<titleweb>")+10
    titleStringEnd = respString.find("</titleweb>")

    #returns the title of the book using the indices found in the previous step
    return respString[titleStringStart:titleStringEnd]