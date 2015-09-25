# instascraper

Checks if words of n length are currently in use as usernames on instagram. It sends a GET request for the 
usernames url and if it receives a 404 error it lists the username as not in use.  
Using this method results in a reasonable number of positives as instagram has an extensive forbidden words 
list which, if queried with a GET request, will return a 404 error.

## Usage
The script can search for words of n length by supplying a positive integer as a command-line argument like so:  
```sudo python main.py 5```  
If no argument is supplied it will default to search every listing in the dictionary.
