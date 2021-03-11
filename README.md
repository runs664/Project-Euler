# Project Euler 💻💡
<p style='text-align: justify;'><b>Project Euler</b> (named after <i>Leonhard Euler</i>) is a website dedicated to a series of computational problems intended to be solved with computer programs. The project attracts adults and students interested in mathematics and computer programming. Since its creation in 2001 by Colin Hughes, Project Euler has gained notability and popularity worldwide. It includes over 700 problems, with a new one added once every one or two weeks. Problems are of varying difficulty, but each is solvable in less than a minute of CPU time using an efficient algorithm on a modestly powered computer. As of 5 April 2020, Project Euler has more than 1,000,000 users, from all over the world, who have solved at least one problem.<p>

## ※Example problem and solutions

### The first Project Euler problem is:

><p style='text-align: justify;'>If we list all the natural numbers below 10 that are multiples of 3 or 5, we get 3, 5, 6 and 9. The sum of these multiples is 23.</p>

><p style='text-align: justify;'>Find the sum of all the multiples of 3 or 5 below 1000.</p>

<p style='text-align: justify;'>Though this problem is much simpler than the typical problem, it serves to illustrate the potential difference that an efficient algorithm makes. The brute-force algorithm examines every natural number less than 1000 and keeps a running sum of those meeting the criteria. This method is simple to implement, as shown by the following pseudocode:</p>

```pascal
total := 0
for NUM from 1 through 999 do
    if NUM mod 3 = 0 or NUM mod 5 = 0 then
        total := total + NUM
return total
```