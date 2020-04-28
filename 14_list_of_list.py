small_bird = ['hummingbird','finch','Verdin']
extinct_bird =['dodo','pigeon','great auk']
carol_bird = [3,'French hens',2,'turtledoves']
#now add all list
all_bird = [small_bird,extinct_bird,'macaw',carol_bird]
#print(all_bird)
"""The first item is a list: in fact, it’s small_birds, the
first item we specified when creating all_birds. You
should be able to guess what the second item is """
print(all_bird[1])
#['dodo', 'passenger pigeon', 'Norwegian Blue']
"""It’s the second item we specified, extinct_birds. If
we want the first item of extinct_birds, we can
extract it from all_birds by specifying two indexes"""

print(all_bird[1][0])
""" The [1] refers to the list that’s the second item in
all_birds, whereas the [0] refers to the first item in
that inner list"""
