# A * alphabet maze walker

Walks a maze using A* and prints out solved path using alphabet letters

## Requirements
Python 3

## Sample usage

### Use case 1
run in your terminal:

`python3 maze.py`
Paste any legitimate puzzle, such as this:
~~~~
###_#########
#___________#
#_##_______##
#_##________#
#_###########
#_###########
~~~~
Press `Ctrl+D`

### Use case 2
Save your maze in a text file.
Cat your text file and pipe it to the script

`cat maze.txt | python3 maze.py`

## Output

If the script is able to find a solution, it will print it out, as follows:
~~~~
###a#########
#dcb________#
#e##_______##
#f##________#
#g###########
#h###########
~~~~
