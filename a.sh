#!/bin/bash
a=/home/tione/notebook/ChineseChess-AlphaZero/data/play_data
b=/home/tione/notebook/ChineseChess-AlphaZero/data/trained
 
for i in `ls $a`
do
echo $b/$i
# ls -l $b/$i 
rm -rf $b/$i 
done