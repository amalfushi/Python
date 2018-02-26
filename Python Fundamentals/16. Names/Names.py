users = {
 'Students': [
     {'first_name':  'Michael', 'last_name' : 'Jordan'},
     {'first_name' : 'John', 'last_name' : 'Rosales'},
     {'first_name' : 'Mark', 'last_name' : 'Guillen'},
     {'first_name' : 'KB', 'last_name' : 'Tonel'}
  ],
 'Instructors': [
     {'first_name' : 'Michael', 'last_name' : 'Choi'},
     {'first_name' : 'Martin', 'last_name' : 'Puryear'}
  ]
 }

def printDict(dictionary):
    for key in dictionary: #for each dictionary in this dictionary
        count = 1
        for people in dictionary[key]: #for each person in subcategory
            #print this string but stick these values in the{}
            print "{}- {} {} - {}".format(count,
                people["first_name"],
                people["last_name"],
               len(people["first_name"]) + len(people["last_name"]) )
            count += 1

printDict(users)