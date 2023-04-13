#!python3

"""
Strings are iterable.  Use for loops to iterate through both strings to create a list to represent a deck of cards. Note: We can also use list comprehension as strings are still iterable!
"""

ranks = "A23456789TJQK"
suits = "CDHS"



def createDeck():
  deck = []
  for r in range(0,13) :
    for s in range(0,4):
      x = [f'{ranks[r]}{suits[s]}']
      deck.append(x)
  return deck



#Also cant get assert to work
def main():
  deck = createDeck()
  print(deck)
  assert "AS" in deck
  assert "KC" in deck
  assert deck.count("TC") == 1


if __name__ == "__main__":
  main()
