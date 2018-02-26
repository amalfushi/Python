name = ["Anna", "Eli", "Pariece", "Brendan", "Amy", "Shane", "Oscar"]
favorite_animal = ["horse", "cat", "spider", "giraffe", "ticks", "dolphins", "llamas"]

def make_dict(arr1, arr2):
    if len(arr1) >= len(arr2):
        dictionary = dict(zip(arr1, arr2))
    else:
        dictionary = dict(zip(arr2, arr1))
    return dictionary

print make_dict(name, favorite_animal)