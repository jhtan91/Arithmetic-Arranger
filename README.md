# Arithmetic-Arranger
***************************************************************************************************************
This program is written for FCC certification under the curriculum "Scientific Computing with Python Projects".

This repository is created for viewing purpose only.
Please do not copy the code for cheating at the FCC certification.

I will make more changes in the future when my programming skill improved.
This is sufficient for the test_modules for now.
***************************************************************************************************************

***************************************************************************************************************
A few conditions to be met:
1. Problems cannot be more than 5.
2. Numbers cannot have more than 4 digits.
3. Problems can only contains digits.
4. Operator must be "+" or "-" only.
5. 2 spaces must be placed in front of the longest operands.
6. 4 spaces must be placed between each problems.
7. The lines must be the length of longest operands +2.
8. All problems must be right-aligned.
9. Must be able to accept optional argument that will show answers if "True".
***************************************************************************************************************

************
My solution
************
The input problems are in the form of string : (['3200 - 698', '1 - 3801', '4512 - 4', '1230 - 49', '988 + 400'])
To rearrange the problems, every problem will be split into 5 parts:

  3200    <<< upper_problems
-  698    <<< expression_problems (- or +) + lower_problems
------    <<< lines "-"
  2502    <<< total
  
join() and .append() are used to join the spaces and the strings without the bracket([]) and comma(,). The rest are if else statements.
