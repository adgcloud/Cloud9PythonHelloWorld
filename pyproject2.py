#!/usr/bin/env python3.7
from random import *

def uniqueNames(deptchars, instanceprompt):
    deptchars = input("What is the name of your department? : ")
    deptprompt = deptchars.lower()
print(deptprompt)
if deptprompt not in ["accounting", "finops","marketing"]:
    print("You are in the " + deptprompt + " department. Only members of FinOps, Marketing or Accounting should enter this information")
    raise SystemExit
else:
    instanceprompt = int(input("How many EC2 instances do you want? : "))
    print("Number of instances:", instanceprompt)
for i in range(instanceprompt):
    char = random()
    print("Unique instance name:", deptprompt + str(char))

if __name__ == "__uniqueNames__":
    uniqueNames()