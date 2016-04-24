#!/bin/sh
a=0
while [ $a -ne 209 ]
do
  echo "${a}"
  python edge.py png/out-${a}.png
  a=`expr $a + 1`
done
