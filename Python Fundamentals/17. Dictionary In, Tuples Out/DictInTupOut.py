# function input
my_dict = {
  "Speros": "(555) 555-5555",
  "Michael": "(999) 999-9999",
  "Jay": "(777) 777-7777"
}

def dictToTups(dictionary):
  newList = []
  for key in dictionary:
    newList.append(
      (key, dictionary[key])
      )
  return newList

print dictToTups(my_dict)