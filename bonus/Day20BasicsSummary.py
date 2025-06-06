'''
Objects can be stored in variables
    ex:
        name = "John"
        last_name = "Smith"
        id = "10221"        (these are all strings)

        members = 5         (this is an integer)
        height = 1.75       (this is a float
'''
'''
Objects can also be produced by functions
    ex:
        name = input("What is your name?")
        print(name) would return "What is your name" and the input
'''
'''
Converting one type, to another type
    ex:
        name = float(input("What is your name?"))       This would return "What is your name" and the float of the input
'''
'''
Not all functions return a value
    ex:
        print functions
        x = print("Hello)       Would return Hello
        but just typing x into the console would be blank.
'''
'''
Methods:
    ex: 
        "hello".upper()
        "hello".capitalize()
        "hello".title()
        
Can get a list of methods by using dir(str), dir(float) dir(list)
'''

'''
lists []
tuples ()
cannot append a tuple

indexing will give you the corresponding item in a list or tuple [0], 
negative indexing will give you a character in an array[-2]

dictionaries should be used when data is more heterogeneous 
'''

'''
While loops
    Use while true to always start
    use an actual while field == "..." to have a real requirement
    
for loops are designed to run as many times as needed to in order to get through each line in a sequence

match case, is a controlled flow code block
    match "...":
        case "...":
            xxxx
        case "...":
            xxxx

If elif else are used for more complex comparisons and conditional blocks

f strings are used to create a string where we can enter dynamic values 
    f"...{variable.method()} ..."
'''

'''
Errors
    Syntax errors
        usually when the parenthesis does not match or are absent, message is not always clear
    Exceptions
        NameError
        AttributeError
        ValueError
        usually invalid syntax as in not defined or no attribute
    Try Except does not catch
        Usually syntax errors
    When to use try except or if else
        try except always catches syntax errors but not logical ones,

Comments and doc strings
    These text blocks are in a doc string
    # defines a comment
    
Modules
    Imported things in your python file
    contains standard libraries
    Can install 3rd party libraries using pip install
    webapps through streamlit
    simple desktop app through pysimplegui
'''