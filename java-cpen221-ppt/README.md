Questions taken from CPEN 221 in 2016.

My solutions :)

"
## Question 1: Find the Fibonacci Numbers

Given an array of integers, find the elements in the array that are also Fibonacci numbers and return all such numbers as a list sorted in ascending order. If the array contains duplicates that are also Fibonacci numbers then the list returned should have only one entry for such numbers (i.e., the list should not contain duplicates).

The Fibonacci sequence is 1, 1, 2, 3, 5, 8, ... (0 is not part of the Fibonacci sequence.)

## Question 2: Fully Parenthesized Expressions

Let us define an expression to be any String. `Expression` is therefore a datatype with a String as its internal representation. A fully parenthesized expression is one where every opening parenthesis, '(', has a matching closing parenthesis, ')'. An expression that contains no parentheses is, trivially, a fully parenthesized expression. The datatype `FPExpression` is a subtype of `Expression` (and also has recursive structure). Implement the key methods for `FPExpression`.

Note that your implementation should support these different types of brackets/parentheses: `()`, `[]`, `{}`. The usual rules apply: `{` is closed by `}`, etc.

Responses to potential doubts:
+ Whitespace can be ignored irrespective of where it occurs.
+ An empty String "" is not a valid expression and hence not a valid fully parenthesized expression as well.

## Question 3: Prime Factorization

Given an integer n, this method returns a string that represents the prime factorization of n.
	 
The prime numbers that are factors of n must appear in ascending order in the returned string.

#### Examples
1. **n = 8.** The returned string should be "2^3" where "^" refers to exponentiation.
1. **n = 12.** The returned string should be "2^2 * 3" where "*" represents multiplication.
1. **n = 7.** The returned string should be "7".
1. **n = 1764.** The returned string should be "2^2 * 3^2 * 7^2”.
1. **n = 210.** The returned string should be "2 * 3 * 5 * 7".
1. **n = 1.** The returned string should be "1". Note that 1 is a special case because 1 is not considered a prime number.

## Question 4: Zip Zap Zoom

Consider the following game: Given two integers M and N (N >= M), you start saying out the numbers except that if the number is divisible by 3 you say “zip”, if it is divisible by 5 you say “zap”. For a number that is divisible by 15, you would say “zipzap”.

A `Triple` is a datatype that contains three public integers, `a`, `b` and `c`.

You have to implement a method that takes integers A and B as input and returns a `Triple` where `a` corresponds to the number of times one would say “zip”, `b` corresponds to the number of times one would say “zap”, and `c` corresponds to the number of times one would say “zipzap”.

#### Examples

1. **m = 1, n = 4**. The `Triple` returned would have `a=1`, `b=0`, `c=0` because the game would result in the sequence 1, 2, zip, 4.
1. **m = 2, n = 6**. The `Triple` returned would have `a=2`, `b=1`, `c=0` because the game would result in the sequence 2, zip, 4, zap, zip.
1. **m = 150, n = 165**. The `Triple` returned would have `a=4`, `b=2`, `c=2`.
1. **m = 474747, n = 747474**. The `Triple` returned would have `a=72728`, `b=36363` and `c=18182`.

## What Should You Implement / Guidelines

+ You should implement all the methods that are indicated with `TODO`.
+ Passing the provided tests is the minimum requirement. Use the tests to identify cases that need to be handled.
+ You can implement additional helper methods if you need to but you should keep these methods `private` to the appropriate classes.
+ You do not need to implement new classes.
+ You can use additional standard Java libraries by importing them.
+ Do not throw new exceptions unless the specification for the method permits exceptions.\
"
