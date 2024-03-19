weight = [2 ,7 , 6 , 5 ,4 , 3 ,2 ]
conv1 = ['J',  'Z',  'I' , 'H' , 'G ' ,'F' , 'E' , 'D' , 'C',  'B',  'A']
conv2 = ['X' , 'W'  ,'U' , 'T' , 'R' , 'Q' , 'P' , 'N ' ,'M' , 'L' , 'K']

def validate(x):
  if (len(x)!=9):
    return False
  if x[0] not in ['S', 'T', 'F', 'G']:
    return False
  if not x[1:8].isdigit():
    return False
  if not x[8].isalpha():
    return False
  check = 0
  for i in range(7):
    check = check + int(nric[i+1])*weight[i]
  if nric[0]=='T' or nric[0]=='G':
    check = check + 4
  check = check%11
  if nric[0]=='S' or nric[0]=='T':
    return conv1[check]==x[8]
  else:
    return conv2[check]==x[8]

nric = input('Enter an NRIC number: ')
if validate(nric):
  print("NRIC is valid.")
else:
  print("NRIC is invalid.")

