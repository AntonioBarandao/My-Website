def conflict_brute_force(classes):
 
 #compares every class with every other class
 for i in range(len(classes)):
  for j in range(i + 1, len(classes)):
   
   #unpack the classes
   name1, start1, end1 = classes[i]
   name2, start2, end2 = classes[j]

   #checks if the two classes overlap
   if start1 < end2 and start2 < end1:
    return classes[i],classes[j]

def conflict_presorting(classes):
 
 #sorts the tuples by the start time
 sortedClasses = sorted(classes, key=lambda x: x[1])

 #compares each class with the next class 
 for i in range(len(sortedClasses)- 1):
   current_class = sortedClasses[i]
   next_class = sortedClasses[i + 1]
   
   #unpack the class
   name1, start1, end1 = current_class
   name2, start2, end2 = next_class

   #compares the end of the current class with the start of the next class
   if end1 > start2:
    return current_class, next_class


def gcd(a, b):
    
    
    while b != 0:
        remainder = a % b

        a = b
        
        b = remainder
    
    return a


def lcm(a, b):
    
    greatestCommonDivisor = gcd(a, b)
    
    leastCommonMultiple = (a * b) // greatestCommonDivisor

    return leastCommonMultiple

classes = [
 ("Algorithms", 9.00, 10.50),
 ("Database", 11.00, 12.00),
 ("Artificial Intelligence", 10.25, 11.25),
 ("Networks", 13.00, 14.00)
]


print("Brute-force result:")
print(conflict_brute_force(classes))
print("\nPresorting result:")
print(conflict_presorting(classes))
print("\nOrganizations meeting every 6 and 8 days:")
print("They will meet together after", lcm(6, 8), "days.")