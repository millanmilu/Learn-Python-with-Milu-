names = ['milu', 'Misan', 'millan', 'Babloo', 'anil']
print("It delete items from end of the list ")
names.pop()
print(names)
print("pop(0) returns the head (start), pop() or pop(-1) returns the tail(end)")
print(names.pop(0))

print(" LIFO -LAST IN ,FIRST OUT ;FIFO - FIRST IN ,FIRST OUT")
"""It’s computing jargon time! Don’t worry, these
won’t be on the final exam. If you use append() to
add new items to the end and pop() to remove
them from the same end, you’ve implemented a
data structure known as a LIFO (last in, first out)
queue. This is more commonly known as a stack.
pop(0) would create a FIFO (first in, first out)
queue. These are useful when you want to collect
data as they arrive and work with either the oldest
first (FIFO) or the newest first (LIFO)."""