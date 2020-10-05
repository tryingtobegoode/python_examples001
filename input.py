###
### FIRST OFF, IF YOU PUT A HASHTAG, ANYTHING YOU PUT
### AFTER, WILL BE IGNORED BY THE COMPUTER
###
### THIS IS A COMMON FEATURE ACCROSS PROGRAMMING LANGUAGES
### AND IS CALLED "COMMENTING OUT"
###
### ( ALTHOUGH HOW YOU DO IT DIFFERS BY LANGUAGE )
###
### MOST PEOPLE USE IT TO MAKE NOTES, EXPLAIN HOW FUNCTIONS WORK
### OR ANYTHING THAT WOULD BE HELPFUL FOR A SAPIEN READING IT
###


### A FOUNDATIONAL CONCEPT TO LEARN IS THE 'OBJECT'
###
### OBJECTS CAN BE DATA, OR FUNCTIONS
###
### FUNCTIONS ARE PROCESSES THAT THE COMPUTER DOES
###


name = input("hey boss, what's your name?")

### NAME IS AN OBJECT
###
### input() IS A NATIVE ( COMES WITH THE LANGUAGE )
###             FUNCTION OF PYTHON
###
### HERE'S HOW THE FUNCTION WORKS IN MORE DETAIL
### https://www.w3schools.com/python/python_user_input.asp
###
### INSIDE THE PARANTHESES (), YOU CAN PUT WHATEVER THE 
### FUNCTION IS DEFINED TO ALLOW ( THIS WILL MAKE MORE SENSE LATER )
###
### FOR PYTHON'S input() IN THIS USE CASE, I JUST PUT A 
### STRING TO DISPLAY IN THE TERMINAL TO THE USER

hours = input("hellow {}. How many hours do you plan to study for?    ".format( name ))

### 
### A STRING, IS A COLLECTION OF DATA DEFINED AS A STRING
### WHICH MEANS, STRINGS CAN BE ANY CHARACTER SET PUT TOGETHER
### SO LONG AS IT IS INSIDE OF "" OR '' 
###
### SO I CREATED A STRING THAT WILL DISPLAY TO THE USER...
### BUT IN ORDER OF THE PROGRAM TO PRINT WHAT THE USER INPUTED
### I HAD TO PUT IN THE CURLY BRACES {} WHICH IS CALLED
### A REPLACEMENT FIELD
### https://realpython.com/python-formatted-output/
###
### AND THE .format() NATIVE FUNCTION ALLOWS ME TO DEFINE
### WHAT IS THE SYSTEM IS REPLACING THE {} WITH
### https://www.w3schools.com/python/ref_string_format.asp
###
### SEE WHAT I DID BEFORE WITH CREATING THE OBJECT name = input()
### TO THE USER I POPPED UP A WAY FOR THEM TO INPUT TEXT
### BUT TO THE COMPUTER, I CREATED A DATA OBJECT WHO'S VALUE
### IS WHAT THE USER ENTERED
###
### SO LATER ON, I CAN PRINT WHAT THEY ENTERED, BECASE SO LONG
### AS THE SCRIPT IS ACTIVE, THE COMPUTER HAS THAT name OBJECT
### STORED

#suggestion = hours * 2

###                 SEE HERE? I HAD TO PUT A \ BEFORE THE ', BECAUSE IF I DIDN'T, THE COMPUTER WOULD TREAT THAT CONTRACTION AS THE END OF THE STRING
print('oh wow, that\'s a lot of studying. to get a good grade, you should probably study for {} hours    '.format( int(hours) * 2))

### 
### print() IS ANOTHER NATIVE PYTHON FUNCTION
### https://www.w3schools.com/python/ref_func_print.asp
###
### PYTHON CAN DO MATH NATIVELY, BUT IN ORDER FOR THE COMPUTER
### TO PROPERLY UNDERSTAND WHAT IT'S GIVEN, I HAD TO 
### DEFINE WHAT I WAS GETTING AS A NUMBER, THEN MULTIPLY IT BY TWO
### 
### I USED THE NATIVE int() FUNCTION TO DO THAT
### https://www.programiz.com/python-programming/methods/built-in/int
###
### THERE'S NATIVE FUNCTIONS TO DEFINE ALL DATA TYPES
### INCLUDING DICTIONARIES, FLOATS, STRINGS, ETC.
###
### NORMALLY, WHAT I PUT INSIDE THE .function()
### I WOULD HAVE AS ANOTHER OBJECT DEFINED BEFORE IT ( I COMMENTED IT OUT )
### BUT TO MEET YOUR PROF'S 3 LINE REQUIREMENT, I PUT IT INSIDE THE PARENTHESIS
###
### TO GET A GOOD FOUNDATION OF PYTHON, I'D SUGGEST
### MAKING FUNCTIONS AND PLAYING AROUND WITH PYTHON
### DICTONARIES.
###
### THEN MAKING LOOPS THROUGH DICTONARIES WITH while, for, if elif else, & try except
### FUNCTIONS
###
### DICTONARIES - https://www.w3schools.com/python/python_dictionaries.asp
###
### WHILE - https://www.w3schools.com/python/python_while_loops.asp
###
### IF, ELIF, ELSE - https://www.datacamp.com/community/tutorials/elif-statements-python?utm_source=adwords_ppc&utm_campaignid=1565261270&utm_adgroupid=67750485268&utm_device=c&utm_keyword=&utm_matchtype=b&utm_network=g&utm_adpostion=&utm_creative=332661264374&utm_targetid=dsa-429603003980&utm_loc_interest_ms=&utm_loc_physical_ms=9061184&gclid=EAIaIQobChMI7O6r3eHX6wIVEvDACh1qygnkEAAYASAAEgIjsfD_BwE
###
### for - https://www.w3schools.com/python/python_for_loops.asp
###
### try | except - https://www.w3schools.com/python/python_try_except.asp
