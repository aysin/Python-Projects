import hashmap

#create a mapping of state to abbreviation
states = hashmap.new()
hashmap.set(states, 'Oregon', 'OR')
hashmap.set(states, 'Florida', 'FL')
hashmap.set(states, 'California', 'CA')
hashmap.set(states, 'New York', 'NY')
hashmap.set(states, 'Michigan', 'MI')

#create a basic set of states and some cities in them
cities = hashmap.new()
hashmap.set(cities, 'CA', 'San Francisco')
hashmap.set(cities, 'MI', 'Detroit')
hashmap.set(cities, 'FL', 'Jacksonville')

#add some more cities
hashmap.set(cities, 'NY', 'New York')
hashmap.set(cities, 'OR', 'Portland')

#print out some cities
print '-' * 15
print "NY State has: %s " %hashmap.get(cities, 'NY')
print "OR State has: %s " %hashmap.get(cities, 'OR')


#print some states
print '-' * 15
print "Michigan's abbreviation is: %s " %hashmap.get(states, 'Michigan')
print "Florida's abbreviation is: %s " %hashmap.get(states, 'Florida')


#do it by using the state then cities dict
print '-' * 15
print "Michigan has: %s" % hashmap.get(cities, hashmap.get(states, 'Michigan'))
print "Florida has: %s" % hashmap.get(cities, hashmap.get(states, 'Florida'))

#print every state abbreviation
print '-' * 15
hashmap.list(states)

#print every city abbreviation
print '-' * 15
hashmap.list(cities)

print '-' * 15
state = hashmap.get(states, 'Texas')

if not state:
	print "Sorry, no Texas"


city = hashmap.get(cities, 'TX', 'Does not exist')
print "The city for the state 'TX' is: %s" %city


