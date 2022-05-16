"""
Uses the dictionary API. (https://dictionaryapi.dev/) 

This Class takes in a word and then the get() method returns a random synonym of that word. If there is no synonym, it simply returns the original word passed in.
"""

import requests
import random

class SynonymsAPI:

  """
  Takes in a word and the stitches into the dictionary API url.
  """
  def __init__(self,word="good"):
    self.api_url = f'https://api.dictionaryapi.dev/api/v2/entries/en/{word}'
    self.word = word


  """
  Takes the word passed into the constructor and returns a random synonym. If there are no synonyms in the dictionary, then it just returns the original word.
  """
  def get(self):
    r = requests.get(self.api_url)
    response = r.json()

    #this if statement catches if it's a weird word that has limited information in it. ex: sometimes a word will only have information about its pronunciation.__doc__
    if (type(response) is list):
      
      #this is necessary because to get to the synonyms, I actually have to parse through many embedded lists / dictionaries
      diction = response[0]
      meanings = diction['meanings']
      lyst = meanings[0]
      syn = lyst["synonyms"]

      #This part just determines whether we can actually find a random synonym, or if there is only 1 synonym, or if there are no synonyms.
      if (len(syn) > 1):
        return syn[random.randint(0,len(syn)-1)]
      elif (len(syn) == 1):
        return syn[0]
      else:
        return self.word

    #failsafe in case the word is not in the dictionary / doesn't have any information on its meaning in the dictionary
    else:
      print("word could not be found")
      return self.word