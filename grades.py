from selenium import webdriver
from time import sleep
from selenium.webdriver.chrome.options import Options
from texttable import Texttable
import os
import sys
import re
sys.path.append(os.path.realpath('.'))
import inquirer

class color:
   PURPLE = '\033[95m'
   CYAN = '\033[96m'
   DARKCYAN = '\033[36m'
   BLUE = '\033[94m'
   GREEN = '\033[92m'
   YELLOW = '\033[93m'
   RED = '\033[91m'
   BOLD = '\033[1m'
   UNDERLINE = '\033[4m'
   END = '\033[0m'

opts=Options()
opts.add_argument("--headless")
driver = webdriver.Chrome(chrome_options=opts)

subjects=['OS', 'AUTOMATA', 'PROBABILITY', 'ALGO', 'DATA-ANALYSIS', 'SCIENCE' , 'EMBEDDED']
links=['1697','1698','1645','1696','1699','1727','1728']
questions = [
    inquirer.List('size',
                  message=color.BOLD+color.GREEN+"WELCOME TO MOODLE".center(40,"*"),
                  choices=['OS', 'AUTOMATA', 'PROBABILITY', 'ALGO', 'DATA-ANALYSIS', 'SCIENCE' , 'EMBEDDED'],
              ),
]

answers = inquirer.prompt(questions)
lst=(str(answers.values())).split("\'")
select=lst[1]
for i in range(7):
   if(select==subjects[i]):
      driver.get('https://moodle.iiit.ac.in/grade/report/user/index.php?id='+links[i])

sleep(1)
username_box=driver.find_element_by_id('username')
username_box.send_keys('email')
password_box=driver.find_element_by_id('password')
password_box.send_keys('passkey')
login_box=driver.find_element_by_class_name('btn-submit')
login_box.click()

result=driver.find_element_by_class_name("boxaligncenter")

trs=result.find_elements_by_tag_name("tr")
th=result.find_elements_by_tag_name("th")
lst1=[]
finallist=[]
lst1=[]
c=1

for tr in trs:

  teh=tr.find_elements_by_tag_name("th")
  for ele in teh:
    lst1.append(ele.text)
  
  ted=tr.find_elements_by_tag_name("td")
  for ele in ted:
    lst1.append(ele.text)
  
  if len(lst1)>2:
    finallist.append(lst1)
  
  lst1=[]

# print(finallist)
# for x in :
#   for y in x:
#     print(y.text)
#   print("lolololo----------------------------")  


# for table printing
# for i in range(len(lis)):
# 	a=lis[i].split(" ")
# 	finallist.append(a)


t = Texttable()
t.add_rows(finallist)
print(t.draw())


driver.close()


