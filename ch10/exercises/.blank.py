import timeit
def while_loop(n=100_000_000):
   i = 0
   s = 0
   while i < n:
       s += i
       i += 1
   return s
def for_loop(n=100_000_000):
   s = 0
   for i in range(n):
       s += i
   return s
def main():
   print('while loop\t\t', timeit.timeit(while_loop, number=1))
   print('for loop\t\t', timeit.timeit(for_loop, number=1))
if __name__ == '__main__':
   main()



#second one
from __future__ import print_function

import random

name = raw_input("Hi, I'm PyVa. What is your name: ")

print('Hi',name, end='.')

yesorno = raw_input(' Would you like to play Rock, Paper, Scissors?: ')

yesorno = str(yesorno)

if yesorno == str('Yes'):

  choices = ['Rock', 'Paper', 'Scissors']

print('Ok')

your_choice = raw_input('Choose Rock, Paper or Scissors: ')

print('My turn...')

my_choice = random.choice(choices)

print('I choose,', my_choice)

if your_choice == my_choice:

  print('We both choose the same, it is a draw.')

elif your_choice == 'Rock' and my_choice == 'Paper':

  print('I win!')

elif your_choice == 'Scissors' and my_choice == 'Paper':

  print('You win!')

elif your_choice == 'Paper' and my_choice == 'Rock':

  print('You win!')

elif your_choice == 'Paper' and my_choice == 'Scissors':

  print('I win!')

elif your_choice == 'Rock' and my_choice == 'Scissors':

  print('You win!')

elif your_choice == 'Scissors' and my_choice == 'Rock':

  print('I win!')

again = raw_input('Would you like to play again?:')

#this is where I would like to loop to the start depending on input.

else:

      print('Ok, maybe we can play later, bye.')




