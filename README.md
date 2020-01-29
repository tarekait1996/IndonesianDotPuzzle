# IndonesianDotPuzzle : COMP 472 Project #1

## Problem definition
Problem is defined in the following [document](https://moodle.concordia.ca/moodle/pluginfile.php/3793266/mod_label/intro/COMP_472_2020_Winter_Project_1.pdf) on Moodle.


## Define the problem state space
__initial state__       : Some combination of 1's and 0's [i.e 0 1 1 0 0 1 1 0 0 1 0 1 1 1 0]

__set of operators__    : touch a token, flip the state of that token and all adjacent tokens

__goal test function__  : Goal state should only contains 0's [i.e 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0]

__path cost function__  : depth is cost
