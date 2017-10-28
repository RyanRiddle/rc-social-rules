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
    print(colored('No', 'green', 'on_grey'), colored('feigning surprise', 'grey', 'on_white'))
    print(colored('No', 'green', 'on_grey'), colored('well-actuallys', 'grey', 'on_white'))
    print(colored('No', 'green', 'on_grey'), colored('backseat driving', 'grey', 'on_white'))
    print(colored('No', 'green', 'on_grey'), colored('subtle-isms', 'grey', 'on_white'))

print_computer()
print()
print_rules()

