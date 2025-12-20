'''
Python logical operators (and, or, not)
are special keywords that act as conjunctions in our code,
connecting and evaluating multiple conditions within a single expression
--- The Three Logical Operators
Operator           Returns True when...             Example
and                Both conditions are True         True and True → True
or                 At least one condition is True   True or False → True
not                Reverses the boolean value       not False → True

---  Short-Circuit Evaluation  - Lazy evalution
'''
# Greater than or equal 18 and hasLicense
# age=20
# hasLicense=True
# canDrive = age >=18 and hasLicense==True
# print(canDrive)


# isRaining = False or hasUmbrella
# isRaining =True
# hasUmbrella = True
# canGoOut = not isRaining or hasUmbrella
# print(canGoOut)


# False and ------  ==>False
# True or --------- ===> True

print(10 < 20 and 10/0) # True  or ----

