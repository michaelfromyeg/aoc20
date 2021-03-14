#!/bin/bash
for i in 1 2 3
do
   echo "=== DAY $i ==="
   cd $i
   python3 $i.py
   cd ..
   echo ""
done