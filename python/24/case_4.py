result = map(
    lambda x: x * x,
    filter(lambda x: x % 2 == 0, range(10))
)

print(result)

'''


    Approach                    Stores all results?	    Lazy?	    Extra Memory         Time
    List Comprehension	        ✅ Yes	                ❌	        O(n)                O(n)
    map()	                    ❌ No	                ✅	        O(1)                O(n)
    filter()	                ❌ No	                ✅	        O(1)                O(n)
    Generator Expression	    ❌ No	                ✅	        O(1)                O(n)

'''

