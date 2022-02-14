#1. What exactly is []?
	List.

#2. In a list of values stored in a variable called spam, how would you assign the value 'hello' as the third value? 
(Assume [2, 4, 6, 8, 10] are in spam.) 
	spam = [2, 4, 6, 8, 10]
	spam.insert(3, 'hello')

#3. Let's pretend the spam includes the list ['a', 'b', 'c', 'd'] for the next three queries.
What is the value of spam[int(int('3' * 2) / 11)]?
	'd'

#4. What is the value of spam[-1]?
	'd'

#5. What is the value of spam[:2]?
	['a', 'b']

Let's pretend bacon has the list [3.14, 'cat', 11, 'cat', True] for the next three questions.
#6. What is the value of bacon.index('cat')?
	1

#7. How does bacon.append(99) change the look of the list value in bacon?
	[3.14, 'cat', 11, 'cat', True, 99]

#8. How does bacon.remove('cat') change the look of the list in bacon?
	[3.14, 11, 'cat', True, 99, 99]

#9. What are the list concatenation and list replication operators?
	The operator for list concatenation is +, while the operator for replication is *
	
#10. What is difference between the list methods append() and insert()?
	using append, a new entry at the end of the list can be added.
	using insert(position, new_entry), It is possible to create a new entry in exactly that position.

#11. What are the two methods for removing items from a list?
	remove() and pop()

#12. Describe how list values and string values are identical.
	string is ordered collections of only characters,
	but the elements of list can have any type.

#13. What's the difference between tuples and lists?
	lists are mutable while tuples are immutable.
	A list has a variable size while a tuple has a fixed size.	

#14. How do you type a tuple value that only contains the integer 42?
	(42,)

#15. How do you get a list value's tuple form? How do you get a tuple value's list form?
	tuple() and list()

#16. Variables that "contain" list values are not necessarily lists themselves. Instead, what do they contain?
	Variables will contain references to list values rather than list values themselves.

#17. How do you distinguish between copy.copy() and copy.deepcopy()?
	In some cases, a user wants copies he can modify without affecting the original,
	to do that he need to use copy.copy()
	but using copy.deepcopy() will automatically modify the original following the copy one.

# importing copy module
import copy
  
# initializing list 1 
li1 = [1, 2, [3,5], 4]

li5= li1
  
# using copy for shallow copy  
li2 = copy.copy(li1) 
  
# using deepcopy for deepcopy  
li3 = copy.deepcopy(li1)

print(li1)
li2[2]=333
print(li1)

li3[2]=333
print(li3)
print(li1)

li5[2]=666
print(li1)

"""
the output will be 
"""
[1, 2, [3, 5], 4]
[1, 2, [3, 5], 4]
[1, 2, 333, 4]
[1, 2, [3, 5], 4]
[1, 2, 666, 4]
