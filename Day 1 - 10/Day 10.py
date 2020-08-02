#Todo
#Busy with things
#Studied online video from tuselco
#Solve 2 problems tomorrow
#Added 2 hrs in Sunday
#Problem

# Solved From Hacker Rank
# Let's learn about list comprehensions! You are given three integers  and  representing the dimensions of a cuboid along with an integer .
# Print a list of all possible coordinates given by  on a 3D grid where the sum of  is not equal to . Here, .
# Please use list comprehensions rather than multiple loops, as a learning exercise.

    x = int(input())
    y = int(input())
    z = int(input())
    n = int(input())

    print ([[a,b,c] for a in range(x+1) for b in range(y+1) for c in range(z+1) if a + b + c != n ])
    
