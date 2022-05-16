"""
This code takes in a penguin random house isbn (13 digits, no hyphens) and prints out the title. It then replaces the words in the title with synonyms.
"""
import BookAPI
import SynonymsAPI

def main():
  isbn = input("Please input a Penguin Random House 13 digit isbn without the hyphen: (ex: 9781400064625) ")
  bookTest = BookAPI.BookAPI(isbn)
  title = bookTest.get()
  print(f'This is the title of the book: {title}')
  print("and this is a new title generated using synonyms:" + generateNewTitle(str(title)))
  #synoTest = SynonymsAPI.SynonymsAPI("CHRISTMAS")
  #synoTest.get()
  

def generateNewTitle(bookTitle):
  titleList = bookTitle.split()
  newTitle= " "
  #synoTest = SynonymsAPI.SynonymsAPI()
  for i in titleList:
    #print(i)
    synoTest = SynonymsAPI.SynonymsAPI(i)
    #syno = synoTest.get()
    newTitle = newTitle + " " + str(synoTest.get())
  return newTitle

main()