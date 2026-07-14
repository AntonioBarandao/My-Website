def conflict_brute_force(classes):
 # TODO: Compare every pair of classes
 pass


def conflict_presorting(classes):
 # TODO: Sort classes by starting time
 # TODO: Compare neighboring classes
 pass


def gcd(a, b):
 # TODO: Implement Euclid's algorithm
 pass


def lcm(a, b):
 # TODO: Reduce LCM to the GCD problem
 pass

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