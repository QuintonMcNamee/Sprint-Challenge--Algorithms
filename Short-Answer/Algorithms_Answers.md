#### Please add your answers to the ***Analysis of  Algorithms*** exercises here.

## Exercise I

a)  This program will have a time complexity of:
    Worst/Average case: O(n)
    Best case: O(1)
    
    Justification: O(n^3) from the condition and O(n^2) from the statement cancel out to O(n). As n gets bigger the time to run the program increases at the same rate.


b)  This program will have a time complexity of:
    Worst/Average case: O(n^2)
    Best case: O(n)

    Justification: Nested loops therefore the time will increase exponentionally as n becomes larger.


c)  This program will have a time complexity of:
    Worst/Average case: O(n)
    Best case: O(1)

    Justification: 2 + bunnyEars(n - 1) simplifies to O(n). As n gets bigger the time to run the program increases at the same rate.

## Exercise II

Since we are trying to minimized the number of broken eggs. I will use a binary search approach. Therefore, the time complexity will be O(log(n)).

def egg_drop(n):
    # step 1: delcare variables
    # step 2: divide n by 2 to see if that floor breaks the eggs
    # step 3: if the egg breaks, repeat step 2
              if the egg DOESNT break, check if the floor number + 1 breaks:
                if the floor number + 1 breaks, then return the floor number
                else if the floor number + 1 DOESNT break, take the UPPER half of the n divided by 2 (from step 2) and then repeat step 2.


