'''
author = Marek Fraj
'''
TEXTS = ['''
Situated about 10 miles west of Kemmerer, 
Fossil Butte is a ruggedly impressive 
topographic feature that rises sharply 
some 1000 feet above Twin Creek Valley 
to an elevation of more than 7500 feet 
above sea level. The butte is located just 
north of US 30N and the Union Pacific Railroad, 
which traverse the valley. ''',

'''At the base of Fossil Butte are the bright 
red, purple, yellow and gray beds of the Wasatch 
Formation. Eroded portions of these horizontal 
beds slope gradually upward from the valley floor 
and steepen abruptly. Overlying them and extending 
to the top of the butte are the much steeper 
buff-to-white beds of the Green River Formation, 
which are about 300 feet thick.''',

'''The monument contains 8198 acres and protects 
a portion of the largest deposit of freshwater fish 
fossils in the world. The richest fossil fish deposits 
are found in multiple limestone layers, which lie some 
100 feet below the top of the butte. The fossils 
represent several varieties of perch, as well as 
other freshwater genera and herring similar to those 
in modern oceans. Other fish such as paddlefish, 
garpike and stingray are also present.'''
]

import copy

credentials = {
'bob': '123',
'ann': 'pass123',
'mike': 'password123',
'liz': 'pass123'
}
#1
print('Hello and welcome to my program!')
#2
user_name = input('To gain further access, please enter your user name: ')
password = input('Thank You. Now please enter your password: ')
#3
if credentials.get(user_name) != password:
    print('Password or username is wrong')
    quit()

elif credentials.get(user_name) == password:
    print('Permission granted')
print('-'*50)
#4
text_choice = input('Please choose a text to work with(type text 1, text2 or text 3): ')
if text_choice == 'text 1':
    text = (TEXTS[0:1])
    print(text)

elif text_choice == 'text 2':
    text = TEXTS[1:2]
    print(text)

elif text_choice == 'text 3':
    text = TEXTS[2:3]
    print(text)

else:
    print('You have entered an invalid value')
    quit()
print('-'*50)
#5
text_to_words = str(text).split()
text_to_words_deep_copy1 = copy.deepcopy(text_to_words)
text_to_words_deep_copy2 = copy.deepcopy(text_to_words)
text_to_words_deep_copy3 = copy.deepcopy(text_to_words)
text_to_words_deep_copy4 = copy.deepcopy(text_to_words)
text_to_words_deep_copy5 = copy.deepcopy(text_to_words)
text_to_words_deep_copy6 = copy.deepcopy(text_to_words)

number_of_words = 0
while text_to_words_deep_copy1:
    text_to_words_deep_copy1.pop()
    number_of_words += 1
print('The number of words in this text is: ', number_of_words)

words_starting_with_capital = 0
while text_to_words_deep_copy2:
    popped_word_capital = text_to_words_deep_copy2.pop()
    if popped_word_capital[0].istitle() == True:
        words_starting_with_capital += 1
print('The number of title cased words in this text is: ', words_starting_with_capital)

words_upper = 0
while text_to_words_deep_copy3:
    popped_word_upper = text_to_words_deep_copy3.pop()
    if popped_word_upper[0:-1].isupper():
        words_upper += 1
print('The number of upper case words in this text is: ', words_upper)

words_lower = 0
while text_to_words_deep_copy4:
    popped_word_lower = text_to_words_deep_copy4.pop()
    if popped_word_lower[0:-1].islower():
        words_lower += 1
print('The number of lower case words in this text is: ', words_lower)

words_numeric = 0
list_of_numerics = []
while text_to_words_deep_copy5:
    numeric_word = text_to_words_deep_copy5.pop()
    if numeric_word.isnumeric() == True:
        words_numeric += 1
        list_of_numerics.append(int(numeric_word))
print('The number of words in this text, that are purely numeric is: ', words_numeric)
print('-'*50)
#6
dict = {}

while text_to_words_deep_copy6:
  word = text_to_words_deep_copy6.pop()
  length = len(word)
  if length in dict:
    dict[length] += 1
  else:
    new = {length : 1}
    dict.update(new)

print(dict.items())

print('One letter words: ', dict.get(1))
print('Two letter words: ', dict.get(2))
print('Three letter words: ', dict.get(3))
print('Four letter words: ', dict.get(4))
print('Five letter words: ', dict.get(5))
print('Six letter words: ', dict.get(6))
print('Seven letter words: ', dict.get(7))
print('Eight letter words: ', dict.get(8))
print('Nine letter words: ', dict.get(9))
print('Ten letter words: ', dict.get(10))
print('Eleven letter words: ', dict.get(11))
print('Twelve letter words: ', dict.get(12))
print('Thirteen letter words: ', dict.get(13))

print('-'*50)
#7
sum_of_numerics = sum(list_of_numerics)
print('If we summed all the numbers in this text, we would get: ', sum_of_numerics)