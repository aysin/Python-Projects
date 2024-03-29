# learning dictinaries

def new(num_buckets = 256):
	'''Initializes a map with the given number of buckets.'''
	aMap = []
	for i in range(0, num_buckets):
		aMap.append([])
	return aMap

def hash_key(aMap, key):
	'''Given a key this will create a number and then conver 
	ot to an index for the aMap's buckets'''
	return hash(key) %len(aMap)

def get_bucket(aMap, key):
	'''Given a key, find the bucket where it would go.'''
	bucket_id = hash_key(aMap, key)
	return aMap[bucket_id]

def get_slot(aMap, key, default=None):
	'''
	REturns the index, key, and the value of a slot found in a bucket.
	Returns -1, key, and default (none if not set) when not found.
	'''
	bucket = get_bucket(aMap, key)

	for i, kv in enumerate(bucket):
		k, v = kv
		if key == k:
			return i, k, v
	return -1, key, default

def get(aMap, key, default=None):
	'''Gets the value in a bucket for the given key, or the default.'''
	i, k, v = get_slot(aMap, key, default = default)
	return v
	
def set(aMap, key, value):
	'''sets the key to the value, replacing any exiting value.'''
	bucket = get_bucket(aMap, key)
	i, k, v = get_slot(aMap, key)

	if i >= 0:
		#the key exists, replace it
		bucket[i] = (key, value)
	else:
		#the key doesnt, append to create it
		bucket.append((key,value))

def delete(aMap, key):
	'''Deletes the given key from the Map'''
	bucket = get_bucket(aMap, key)

	for i in xrange(len(bucket)):
		k, v = bucket[i]
		if key == k:
			del bucket[i]
			break


def list(aMap):
	'''Prints out whats in the map '''
	for bucket in aMap:
		if bucket:
			for k,v in bucket:
				assert ("Flamenco Sketches")
				print k, v












