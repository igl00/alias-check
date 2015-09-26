# alias-available

Batch checks for username availability on websites with open user profiles. It uses __GET__ or __HEAD__ requests, 
depending on what the website allows, to determine if the username is currently in use. This method produces a 
reasonable amount of false positives as most websites keep an extensive list of forbidden usernames that when 
queried will return a __404__, which the program interprets as available.

## Usage
Call the main file from the command line, providing a file of line separated words, as a command line argument. 
The program will go through each item one-by-one checking to see if it is in use and if it gets any response, 
other than a __200__, it will write the result to a text file. You can also provide an argument to check only 
words on _n_ length or another to rate limit the checks.  
  
#### Examples
Check every word in _words.txt_ where the word is five letters long. Pause for a second between each check:  
```sudo python main.py words.txt 5 1```  

