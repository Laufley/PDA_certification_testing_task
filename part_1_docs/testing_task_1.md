### Testing task 1:

# Carry out static testing on the code below.
# Comment on any errors that you see below.

Note that we are only looking for errors here.

**Not** any issues with, i.e.: 
Thinking that methods should be renamed or should be class level, or using string interpolation etc. 

These aren't errors but rather standards that vary from developer to developer. 

Only comment on errors that would stop the tests running.

```python

class CardGame:
#The class is not defined. It needs a constructor and attributes. 
  # Suggestion:
#     def __init__(self):
#     self.deck = []
 

  def check_for_ace(self, card):
    if card.value = 1:
      return True
    else
      return False
# the if statement has to contain double equals instead of one. 
# the else statement needs to be follwed by a colon.
# SUGGESTION: 
# def check_for_ace(self, card):
#     if card.value == 1:
#       return True
#     else:
#       return False

  dif highest_card(self, card1 card2):
  if card1.value > card2.value:
    return card
  else:
    return card2

# the arguments card1 card2 are not separated. They need a comma in between.
# dif is a syntax error. Should be def.
#the first return should be returning card1 instead of card.
# SUGGESTION:
# def highest_card(self, card1, card2):
#   if card1.value > card2.value:
#     return card1
#   else:
#     return card2
  

def cards_total(self, cards):
  total
  for card in cards:
    total += card.value
    return "You have a total of" + total
  
# total doesn't have any value. We can solve it by writing total = 0
# the return should be one indentation shorter, at the same level as the for loop.
# since we had set the total variable to 0 it is now an integrer, so when we try to concadenate it with a string in the return, it will give an error.
# one way to solve this will be to transform the int into a str by: str(total)
# to make it cleaner, the final string should add a space before ending.
# SUGGESTION
# def cards_total(self, cards):
#   total = 0
#   for card in cards:
#     total += card.value
#   return "You have a total of " + str(total)
```
