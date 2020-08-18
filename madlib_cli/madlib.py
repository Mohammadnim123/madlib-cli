
def wlcome():
    print(f"""
    hello in the Madlib Game ....
    in this game i will ask you to enter some thing
    after that you will be surprized
    lets go .....
    """)
    
 

def inputs():
    name = input("Enter your name ...")
    name2 = input("Enter any inanimate name ....")
    adjective = input("Enter adjective ....")
    verb = input("Enter present verb ....")
    return [name,name2,adjective,verb]
   

def read():
    valList = inputs()
    with open('assets/template.txt') as f:
        contents = f.read()
    yourContent = contents %(valList[0],valList[1],valList[2],valList[3])
    return yourContent

    

def write():
    yourContent = read()
    with open('assets/your_answer.txt', 'w') as f2:
        f2.write(yourContent)
    print("  *****************************************************  ")
    print("  also you can find your answer iside your_answer.txt")
    print("  *****************************************************  ")
    print(yourContent)


def read_template(val):
  x = val.strip()
  return x

def merge(templateString,exList):
  yourContent = templateString %(exList[0],exList[1],exList[2],exList[3])
  return yourContent

def parse(temStr):
  newStr = ""
  newList = []
  i = 0
  while i<len(temStr):
    if temStr[i] == '%':
      newStr = newStr + ''
      i += 1

    else:
      newStr = newStr + temStr[i]  
    i += 1

  for i in range(temStr.count('%s')):
    newList.append('%s')
  return [newStr,newList]


if __name__ == "__main__":
    wlcome()
    write()
    

