##Johannah Cushing
##February 27, 2019
##Artificial Intelligence 1, Spring 2019
##Machine Problem 1: Course Planning using a Constraint Satisfaction Problem Formulation

import numpy as np
import pandas as pd

from constraint import*

problem = problem()

#There are 14 terms
#Each number is a term, 1 is fall1year1.... 14 is fall2year3, etc
#0 means not taken
possible_times=[0,1,2,3,4,5,6,7,8,9,10,11,12,13,14]


problem.addVariable("CPSC-50100",[0,1,2,3,5,7,8,9,11,13,14])
problem.addVariable("MATH-51000",[0,1,3,5,7,9,11,13])
problem.addVariable("MATH-51100",[0,2,4,8,10,14])
problem.addVariable("MATH-51200",[0,4,10])
problem.addVariable("CPSC-51000",[0,1,5,7,11,13])
problem.addVariable("CPSC-51100",[0,1,3,5,7,9,11,13])
problem.addVariable("CPSC-53000",[0,2,5,8,11,14])
problem.addVariable("CPSC-54000",[0,2,3,8,9,14])
problem.addVariable("CPSC-55000",[0,1,5,7,12,13])
problem.addVariable("CPSC-50600",[0,1,3,5,7,9,11,13])
problem.addVariable("CPSC-51700",[0,2,8,14])
problem.addVariable("CPSC-52500",[0,2,4,6,8,10,12,14])
problem.addVariable("CPSC-55200",[0,2,8,14])
problem.addVariable("CPSC-55500",[0,1,4,7,10,13])
problem.addVariable("CPSC-57100",[0,3,9])
problem.addVariable("CPSC-57200",[0,5,11])
problem.addVariable("CPSC-57400",[0,4,10])
problem.addVariable("CPSC-59000",[0,2,4,5,8,10,11,14])

#Values of all given variables are different-- i.e. one different class per term
#Or if they are 0, they can be the same (not taken)
#can't use AllDifferent Constraint as multiple classes will be 0 i.e. not taken
def allDiffOrZero(*args):
    unique=set(args)
    for s in unique:
        if s==0:
            continue
        else:
            count=len([x for x in args if x==s])
            if count>1:
                return False
    return True

problem.addConstraint(allDiffOrZero,['CPSC-59000','CPSC-57400','CPSC-57200','CPSC-57100','CPSC-55500','CPSC-55200','CPSC-52500',
                                     'CPSC-51700','CPSC-50600','CPSC-55000','CPSC-54000','CPSC-53000','CPSC-51100','CPSC-51000',
                                     'MATH-51200','MATH-51100','MATH-51000','CPSC-50100'])


#these are the the requirements, so they must be taken
#remember if a=0, it means not taken...any number from 1-14 is the semester it is taken
def allTaken(*args):
    for a in args:
        if a==0:
            return False
    return True

problem.addConstraint(allTaken,["CPSC-50100","MATH-51000","MATH-51100","MATH-51200","CPSC-51000",
                                      "CPSC-51100","CPSC-53000","CPSC-54000","CPSC-55000","CPSC-59000"])

#this function add constraints for prerequisites  
def func(a,b):
    return a > b
problem.addConstraint(func,["CPSC-51100","CPSC-50100"])
problem.addConstraint(func,["CPSC-55200","CPSC-50100"])
problem.addConstraint(func,["CPSC-51000","CPSC-50100"])
problem.addConstraint(func,["CPSC-53000","CPSC-50100"])
problem.addConstraint(func,["CPSC-54000","CPSC-50100"])
problem.addConstraint(func,["CPSC-55000","CPSC-50100"])
problem.addConstraint(func,["CPSC-51700","CPSC-50100"])
problem.addConstraint(func,["CPSC-55200","CPSC-50100"])
problem.addConstraint(func,["CPSC-55500","CPSC-50100"])
problem.addConstraint(func,["CPSC-57100","CPSC-50100"])
problem.addConstraint(func,["CPSC-57200","CPSC-57100"])
problem.addConstraint(func,["CPSC-57400","CPSC-57100"])
problem.addConstraint(func,["MATH-51200","MATH-51100"])
problem.addConstraint(func,["CPSC-59000","MATH-51000"])
problem.addConstraint(func,["CPSC-59000","MATH-51100"])
problem.addConstraint(func,["CPSC-59000","MATH-51200"])
problem.addConstraint(func,["CPSC-59000","CPSC-51100"])
problem.addConstraint(func,["CPSC-59000","CPSC-53000"])
problem.addConstraint(func,["CPSC-59000","CPSC-54000"])
problem.addConstraint(func,["CPSC-59000","CPSC-55000"])

sols=problem.getSolutions()
s=pd.Series(sols[0]) #want one posible solution

print("CLASS: Artificial Intelligence, Lewis University")
print("NAME: Johannah Cushing")
print("")
print("START TERM: Year 1 Fall 1")
print("Number of Possible Degree Plans is"+ len(sols))
print("")
print("Sample Degree Plan"+ s.to_string())
