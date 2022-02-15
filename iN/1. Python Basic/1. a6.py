#1. What are escape characters, and how do you use them?
	\t, \n

#2. What do the escape characters n and t stand for?
	\n is a newline, \t is a tab

#3. What is the way to include backslash characters in a string?
	If you want an actual backslash in the string or regex, you have to write two backslash before it: \\ 
	
#4. The string "Howl's Moving Castle" is a correct value. 
#Why isn't the single quote character in the word Howl's not escaped a problem?
	because its wraped under double quotation.
	but if we had wraped it under single quotes, we should have used \'	

#5. How do you write a string of newlines if you don't want to use the n character?
	use multiple string instead.
	- Multiline strings allow you to use newlines in strings without the \n escape character.

#6. What are the values of the given expressions?
#'Hello, world!'[1]
#'Hello, world!'[0:5]
#'Hello, world!'[:5]
#'Hello, world!'[3:]
	e
	Hello,
	Hello,
	lo, world!

#7. What are the values of the following expressions?
#'Hello'.upper()
#'Hello'.upper().isupper()
#'Hello'.upper().lower()
	'HELLO'
	True
	'hello'

#8. What are the values of the following expressions?
#'Remember, remember, the fifth of July.'.split()
#'-'.join('There can only one.'.split())
	['Remember,', 'remember,', 'the', 'fifth', 'of', 'July.']
	'There-can-only-one.'

#9. What are the methods for right-justifying, left-justifying, and centering a string?
	rjust(), ljust(), and center() string methods, respectively

#10. What is the best way to remove whitespace characters from the start or end?
	using replace
	sentence = ' hello  apple'
	sentence.replace(" ", "")
	the output will be 'helloapple'












