#!/usr/bin/env python3.7
from random import *

instanceprompt = int(input("How many EC2 instances do you want? : "))
deptprompt = input("What is the name of your department? : ")
print("Number of instances:", instanceprompt)
for i in range(instanceprompt):
    char = random()
    
    print("Unique instance name:", deptprompt + str(char))