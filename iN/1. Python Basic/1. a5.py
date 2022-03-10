#1. What does an empty dictionary's code look like?
	{}
#2. What is the value of a dictionary value with the key 'foo' and the value 42?
	42

#3. What is the most significant distinction between a dictionary and a list?
	the main difference is that items in dictionaries are accessed via keys and not via their index.
	
#4. What happens if you try to access spam['foo'] if spam is {'bar': 100}?
	KeyError: 'foo'

#5. If a dictionary is stored in spam, what is the difference between the expressions 'cat' in spam and 'cat' in spam.keys()?
	There is no difference. 

#6. If a dictionary is stored in spam, what is the difference between the expressions 'cat' in spam and 'cat' in spam.values()?
	'cat' in spam checks whether there is a 'cat' key in the dictionary, 
	while 'cat' in spam.values() checks whether there is a value 'cat' for one of the keys in spam.

#7. What is a shortcut for the following code?
#   if 'color' not in spam:
#       spam['color'] = 'black'
	
	spam.setdefault('color','Black')

#8. How do you "pretty print" dictionary values using which module and function?
	pprint.pprint()