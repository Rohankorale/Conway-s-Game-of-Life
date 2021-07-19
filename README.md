# Conway-s-Game-of-Life
## A project for simulating/playing the beautiful 'Game of Life!'


The '*Game of Life*' or '*Life*' is a **cellular Automata** formulated by the british mathematician John Conway. In simple words an automata is a machine/algorithm which 
is self-moving. Once an input is given, it keeps working automatically based on some pre-defined set of rules. On the same lines, cellular automata is an automata 
consisting of cellular grid where each cell is designated with a state (alive/dead), at a time(say t=0). Based on the rules, these cells change their states as 
time passes on. DIfferent set of reule produce differeent patterns. Jon Conway wanted to create an unpredictable automation such that some cells would live for a 
long time beforedying while other would go on living for forever (stable configurations). And he came up with the '*Game of Life*'.

### Rules
The universe of *Game of Life* is an infinite 2-D grid of square cells. Each cell is either alive or dead at a given time. Every cell interacts with its eight neighbours :
horizotally, vertically and diagonally adjacent cells. The outcome of an interaction is based on the numbers of alive/dead cells as :

1. A live cell with less than 2 neighbours would die
2. A live cell with more than 3 neighbours would also die
3. A live cell with 2-3 neigbours would survive
4. A dead cell with exctly 3 neighbours would become alive

Interestingly, thses rules for the automation **express the rules applicable in the real life** :

1. A live cell with neighbours less than 2 or more than 3, dies, by ***isolation*** and ***overpopulation*** respectively.
2. A live cell with 2-3 neighbous would survive as it is in a ***stabilized colony***
3. A dead cell with exactly 3 neighbours would become alive by ***reproduction***

The first generation(t=0) goes on creating different generations as time passes and these new generations are pure functions of the preceding one, as identical patterns
are produced from identical parent patterns
