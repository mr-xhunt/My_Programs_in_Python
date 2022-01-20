import re

str = '''
CodeWithHarry
Home
Courses
Blog
Contact
LoginSignup

Course: Python Tutorials For Absolute Beginners
Python Tutorials Teaser
What Is Programming and Why Python?
Downloading Python and Pycharm Installation
Using Modules & Pip In Python
Writing Our First Python Program
Using Python As A Calculator
Comments, Escape Sequences & Print Statement
Variables, Datatypes and Typecasting
String Slicing And Other Functions In Python
Python Lists And List Functions
Dictionary & Its Functions Explained
Python Exercise 1 - Apni Dictionary
Sets In Python
If Else & Elif Conditionals In Python
Exercise 1 - Solution And Your Answers
Python Exercise 2 - Faulty Calculator
For Loops In Python
While Loops In Python
Break & Continue Statements In Python
Python Exercise 2: Faulty Calculator Solution
Python Exercise 3 - Guess The Number
Operators In Python
Short Hand If Else Notation In Python
Functions And Docstrings
Try Except Exception Handling In Python
Python File IO Basics
Open(), Read() & Readline() For Reading File
Python Exercise 3: Solution
Writing And Appending To A File
Python Exercise 4: Astrologer's Stars
Seek(), tell() & More On Python Files
Using With Block To Open Python Files
Exercise 5: Health Management System
Scope, Global Variables and Global Keyword
Recursions: Recursive Vs Iterative Approach
Exercise 4: Solution And First Solver
Anonymous/Lambda Functions In Python
Exercise 5: Solution And First Solver
Using Python External & Built In Modules
F-Strings & String Formatting In Python
Exercise 6: Game Development: Snake Water Gun
*args and **kwargs In Python
Time Module In Python
Virtual Environment & Requirements.txt
Enumerate Function
How Import Works In Python?
If __name__==__main__ usage & necessity
Join Function In Python
Map, Filter & Reduce
Exercise 6 Solution & First Solver
Exercise 7: Healthy Programmer
Decorators In Python
Classes & Objects (OOPS)
Creating Our First Class In Python
Instance & Class Variables | Python Tutorials For Absolute Beginners In Hindi #54
Self & __init__() (Constructors) | Python Tutorials For Absolute Beginners In Hindi #55
Class Methods In Python | Python Tutorials For Absolute Beginners In Hindi #56
Class Methods As Alternative Constructors | Python Tutorials For Absolute Beginners In Hindi #57
Static Methods In Python | Python Tutorials For Absolute Beginners In Hindi #58
Abstraction & Encapsulation | Python Tutorials For Absolute Beginners In Hindi #59
Single Inheritance | Python Tutorials For Absolute Beginners In Hindi #60
Multiple Inheritance | Python Tutorials For Absolute Beginners In Hindi #61
Multilevel Inheritance | Python Tutorials For Absolute Beginners In Hindi #62
Public, Private & Protected Access Specifiers | Python Tutorials For Absolute Beginners In Hindi #63
Polymorphism In Python | Python Tutorials For Absolute Beginners In Hindi #64
Super() and Overriding In Classes | Python Tutorials For Absolute Beginners In Hindi #65
Diamond Shape Problem In Multiple Inheritance | Python Tutorials For Absolute Beginners In Hindi #66
Operator Overloading & Dunder Methods | Python Tutorials For Absolute Beginners In Hindi #67
Abstract Base Class & @abstractmethod | Python Tutorials For Absolute Beginners In Hindi #68
Setters & Property Decorators | Python Tutorials For Absolute Beginners In Hindi #69
Object Introspection | Python Tutorials For Absolute Beginners In Hindi #70 hunter@hotmail.com
ziva23@yahoo.com sheroo@gmail.com miga@gmail.com sahara23@hotmail.com
Python Mini Project #1 | Python Tutorials For Absolute Beginners In Hindi #71
Generators In Python | Python Tutorials For Absolute Beginners In Hindi #72
Python Comprehensions | Python Tutorials For Absolute Beginners In Hindi #73
Using Else With For Loops | Python Tutorials For Absolute Beginners In Hindi #74
Function Caching In Python | Python Tutorials For Absolute Beginners In Hindi #75
Else & Finally In Try Except | Python Tutorials For Absolute Beginners In Hindi #76
Coroutines In Python | Python Tutorials For Absolute Beginners In Hindi #77
Exercise 7: Solution & First Solver | Python Tutorials For Absolute Beginners In Hindi #78
Os Module | Python Tutorials For Absolute Beginners In Hindi #79
Exercise 8: Oh Soldier Prettify My Folder| Python Tutorials For Absolute Beginners In Hindi #80
Requests Module For HTTP Requests | Python Tutorials For Absolute Beginners In Hindi #81
Json Module | Python Tutorials For Absolute Beginners In Hindi #82
Exercise 9: Akhbaar Padhke Sunaao | Python Tutorials For Absolute Beginners In Hindi #83
Pickle Module | Python Tutorials For Absolute Beginners In Hindi #84
Exercise 10: Pickling Iris | Python Tutorials For Absolute Beginners In Hindi #85
Regular Expressions | Python Tutorials For Absolute Beginners In Hindi #86
Converting .py to .exe | Python Tutorials For Absolute Beginners In Hindi #87
Python Exercise 8: Solution + Tips | Python Tutorials For Absolute Beginners In Hindi #88
Raise In Python + Examples | Python Tutorials For Absolute Beginners In Hindi #89
Python 'is' vs '==': What's The Difference? | Python Tutorials For Absolute Beginners In Hindi #90
Python 2.x Vs Python 3.x | Python Tutorials For Absolute Beginners In Hindi #91
Python Exercise 9 Solution + Shoutouts | Python Tutorials For Absolute Beginners In Hindi #92
Creating a Command Line Utility In Python | Python Tutorials For Absolute Beginners In Hindi #93
Exercise 10: Solution + Shoutouts | Python Tutorials For Absolute Beginners In Hindi #94
Creating a Python Package Using Setuptools | Python Tutorials For Absolute Beginners In Hindi #95
Python Exercise 11: Regex Email Extractor | Python Tutorials For Absolute Beginners In Hindi #96
Learning Path For Python Web Development | Python Tutorials For Absolute Beginners In Hindi #97
Python GUI Development - Learning Path | Python Tutorials For Absolute Beginners In Hindi #98
Machine Learning & Data Science Learning Path | Python Tutorials For Absolute Beginners In Hindi #99
Overview
Q&A
Downloads
Announcements
Python Exercise 11: Regex Email Extractor | Python Tutorials For Absolute Beginners In Hindi #96
Problem Statement:-
The task you have to perform is "Email Extractor."

Suppose you are a student and want to get an internship. You have to contact your professors and some companies to get an internship. For that, you need their email so that you can contact them. 

The task you have to do is to extract the email from text data using Regex Expressions. 

When you go to a website and click on the contact section, by pressing CTRL+A, all the website's content gets added to the clipboard. Paste the data in your python file or in a string. Extract an email from the above data, and after extracting the email, write it into a file with a new line character. Your text file after writing data should look similar to this:

abc123@gmail.com

cdf456@gmail.com
mayankcho@gmail.com
 


You are advised to participate in solving this problem. This task will help you become a good problem solver and help you accept the challenge and acquire new skills.

Have you solved this task? If yes, then it is time to check your solution. The solution is discussed in tutorial#100.

 

Code as described/written in the video

Previous
Next

CodeWithHarry
Copyright © 2022 CodeWithHarry.com
mayankcho23@gmail.com
mayank@gmail.edu.in
Python Exercise 11: Regex Email Extractor | Python Tutorials For Absolute Beginners In Hindi #96 | CodeWithHarry
'''



email = re.findall(r"[0-9a-zA-Z._]+@[0-9a-zA-Z._]+[.][[0-9a-zA-Z]+", str)


with open("email_lists.txt", "w") as get_email:
    for email in email:
        get_email.write(email + "\n")

