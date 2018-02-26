##Compare Lists
###print different results based on the results

list_1 = [1,2,5,6,2]
list_2 = [1,2,5,6,2]
list_3 = [1,2,5,6,5,3]
list_4 = ['celery', 'carrots', 'bread', 'milk']
list_5 = ['celery', 'carrots', 'bread', 'cream']

# def compareLists(l1, l2):
#     isSame = True

#     if len(l1) != len(l2):
#         isSame = False
#     else:
#         for idx in range(0, len(l1)):
#             if l1[idx] != l2[idx]:
#                 isSame = False
    
#     if isSame == True:
#         print('The lists are the same')
#     else:
#         print('The lists are not the same')

##more succinct version
def compareLists(l1, l2):
    if l1 == l2:
        print ("The lists are the same")
    else: 
        print ("The lists are not the same")


compareLists(list_1, list_2)
compareLists(list_1, list_3)
compareLists(list_1, list_4)
compareLists(list_4, list_5)