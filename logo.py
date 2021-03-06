#!/usr/bin/python3

from termcolor import colored

blocks = [
[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
[0,0,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,0,0],
[0,0,1,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,1,0,0],
[0,0,1,1,2,2,0,0,2,2,0,0,2,2,0,0,0,0,0,0,1,1,0,0],
[0,0,1,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,1,0,0],
[0,0,1,1,0,0,2,2,2,2,0,0,2,2,2,2,0,0,0,0,1,1,0,0],
[0,0,1,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,1,0,0],
[0,0,1,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,1,0,0],
[0,0,1,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,1,0,0],
[0,0,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,0,0],
[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
[1,1,1,1,1,1,1,1,0,0,0,0,0,0,0,0,1,1,1,1,1,1,1,1],
[1,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,1],
[0,0,0,0,0,0,1,1,0,0,1,1,0,0,1,1,0,0,1,1,0,0,0,0],
[0,0,0,0,1,1,0,0,1,1,0,0,1,1,0,0,1,1,0,0,0,0,0,0],
[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
]

def get_color(num):
  if num == 0:
    return 'grey'
  
  if num == 1:
    return 'white'

  if num == 2:
    return 'green'

  return 'white'

def print_computer():
    for row in blocks:
      line = "" 
      for num in row: 
        color = get_color(num)
        line += colored('\u25A0', color)

      print(line)

def print_rules():
    print(colored('Be rigorous', 'green', 'on_grey'))
    print(colored('Strive for greatness', 'green', 'on_grey'))
    print(colored('Reflect on your progress', 'green', 'on_grey'))
    print()
    print(colored('No feigning surprise', 'green', 'on_grey'))
    print(colored('No well-actuallys', 'green', 'on_grey'))
    print(colored('No backseat driving', 'green', 'on_grey'))
    print(colored('No subtle-isms', 'green', 'on_grey'))

if __name__ == '__main__':
    print_computer()
    print()
    print_rules()

