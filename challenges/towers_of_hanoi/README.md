## Whiteboard challenge 14

### Towers of Hanoi

- whiteboard photo available in assets folder.

- The Towers of Hanoi is a mathematical puzzle where you have 3 towers and N disks of different sizes.
The puzzle starts with the disks sorted (i.e. smaller disks sits on top of larger disks) on the left-most tower, and the objective of the puzzle is to move the disks to the right-most tower with the following restrictions:
Only one disk can be moved at a given time.
A disk is moved from the top of a tower to the top of another tower.
A disk can’t be placed on top of a smaller disk.

- as the introduction to recursion I started by writing a simple countdown ```recursive_function()``` to illustrate what whas happening in recursion.  Call the function with an integer n ```recursive_function(n)``` 

- next I solved the Tower of Hanoi puzzle using recursion.  I used a second ```visual()``` function to print what was happening during recursion.  Watch in your terminal my calling with integer n ```tower(n)```