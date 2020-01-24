# IndonesianDotPuzzle : COMP 472 Project #1

## Problem definition
Problem is defined in the following document: https://moodle.concordia.ca/moodle/pluginfile.php/3793266/mod_label/intro/COMP_472_2020_Winter_Project_1.pdf
## Define the problem state space
initial state       : Some combination of 1's and 0's [i.e 0 1 1 0 0 1 1 0 0 1 0 1 1 1 0]
set of operators    : touch a token, flip the state of that token and all adjacent tokens
goal test function  : Goal state should only contains 0's [i.e 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0]
path cost function  : depth is cost
