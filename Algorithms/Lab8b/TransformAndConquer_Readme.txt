What transformation is used in the schedule-conflict problem?
instead of comparing each class with each other the algorithm first sorts the classes
by the start time then sorts the neiboring classes.

Why does sorting make conflict detection easier?
it reduces the number of comparions needed since the algorithm only has to compare classes
that are directly after it.

Compare the O(n²) and O(n log n) solutions. Which grows faster?
the O(n^2) grows faster since it compares every class with every other class but  O(n log n)
first sorts the classes so it uses less comparions and grows slower.

What problem is the LCM problem reduced to?
the LCM problem is reduced to the GCD problem. that function first finds/uses the GCD function
(using Euclid's algorithm to find GCD) then can find the LCM from there.

Which conflict-detection solution is more appropriate for 100,000 classes? Explain.
the presorting solution since the time complexity is O(n log n ) and would require less comparsions
then the O(n^2). That solution would need a large amount of comparions and would not be efficent.

When could the brute-force solution still be acceptable?
it is acceptable when the number of classes is small since the number of comparsions will also 
be small. 