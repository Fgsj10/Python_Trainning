"""
Author = francisco Junior
"""

#Input and data received user

sumAnswerYes = 0


#Questions for detective
questions = ('Voce telefonou para a vitima? ',
             'Voce esteve no local do crime? ',
             'Voce mora perto da vitima? ',
             'Voce devia para a vitima? ',
             'Voce trabalhou para a vitima? ')


#Creating list for adding answer

answer = []


for question in questions:
    answer.append(input(question).upper())

