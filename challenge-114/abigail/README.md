# Solutions by Abigail
## [Next Palindrome Number](https://perlweeklychallenge.org/blog/perl-weekly-challenge-114/#TASK1)

> You are given a positive integer `$N`.
>
> Write a script to find out the next Palindrome Number higher than
> the given integer `$N`.

### Example
~~~~
Input: $N = 1234
Output: 1331

Input: $N = 999
Output: 1001
~~~~

### Solutions
* [AWK](awk/ch-1.awk)
* [Bash](bash/ch-1.sh)
* [C](c/ch-1.c)
* [Perl](perl/ch-1.pl)

### Blog
[Next Palindrome Number](https://abigail.github.io/HTML/Perl-Weekly-Challenge/week-114-1.html)

## [Higher Integer Set Bits](https://perlweeklychallenge.org/blog/perl-weekly-challenge-114/#TASK2)

> You are given a positive integer `$N`.
> 
> Write a script to find the next higher integer having the same number of
> `1` bits in binary representation as `$N`.

### Examples
~~~~
Input: $N = 3
Output: 5
~~~~

Binary representation of `$N` is `011`. There are two `1` bits. So the next
higher integer is `5` having the same the number of `1` bits i.e. `101`.

~~~~
Input: $N = 12
Output: 17
~~~~

Binary representation of `$N` is `1100`. There are two `1` bits. So the next
higher integer is `17` having the same number of `1` bits i.e. `10001`.

### Solutions
* [GNU AWK](awk/ch-2.gawk)
* [Bash](bash/ch-2.sh)
* [C](c/ch-2.c)
* [Perl](perl/ch-2.pl)

### Blog
[Higher Integet Set Bits](https://abigail.github.io/HTML/Perl-Weekly-Challenge/week-114-2.html)
