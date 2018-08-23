# Dagstuhl's Happy Diner Problem

## The Table Assignment Assignment

**The Problem Statement**: What is the minimum number of meals so that each of the `n` conference participants can share at least one meal with every other participant when eating at tables of at most `k` persons? We call this number `T(n,k)`.

In particular, we have an unlimited number of tables, and we do not require that any two participants have a meal together exactly once, or that every table is fully occupied.

## Dagstuhl's Table Table

| n / k |  2       |   3        |   4        |   5        |   6        |   7        |  8
|:-----:|----------|------------|------------|------------|------------|------------|-------
|   1   |  **0**   |  **0**     |  **0**     |  **0**     |  **0**     |  **0**     |  **0**
|   2   |  **1**   |  1         |  1         |  1         |  1         |  1         |  1
|   3   |  3       |  **1**     |  1         |  1         |  1         |  1         |  1
|   4   |  **3**   |  3  cd     |  **1**     |  1         |  1         |  1         |  1
|   5   |  5       |  3   C     |  3  d      |  **1**     |  1         |  1         |  1
|   6   |  **5**   |  4  e      |  3         |  3  d      |  **1**     |  1         |  1
|   7   |  7       |  4         |  3         |  3         |  3   d     |  **1**     |  1
|   8   |  **7**   |  4         |  3  B      |  3         |  3         |  3 d       |  **1**
|   9   |  9       |  **4** AH  |  4  c      |  3   C     |  3         |  3         |  3 d
|   10  |  **9**   | 6-7 c      |  4  E      |  4   e     |  3         |  3         |  3 
|   11  | 11       | 6-7        |  5  e      | 4-5        |  3         |  3         |  3
|   12  | **11**   | 6-7        |  5         | 4-5 a      |  3   B     |  3         |  3
|   13  | 13       |  7  a      |  5         | 4-5        |  3-4       |  3 C       |  3
|   14  | **13**   |  7         |  5         | 4-5        |  3-4       |            |  3
|   15  | 15       | **7**  F   |  5         | 4-5        |  4   a     |            |  3
|   16  | **15**   |  9   c     |  **5**  H  |  5  c      |  4         |            |  3 B
|   17  | 17       |  9         | 6-9 a      | 5-6        |  4         |  4 a       |  
|   18  | **17**   |  9    G    | 7-9 a      | 5-6        |  4   B     |  4         |  3-4 B
|   19  | 19       |  10  a     | 7-9        | 5-6        |  5-6 a     |            |
|   20  | **19**   |  10        | 7-9        | 5-6        |  5-6       |            |  4 aB
|   21  | 21       | **10** F   | 8-9 c      |  6  a      |  5-6 B     |            |
|   22  | **21**   |  12   c    | 8-9        |  6         |  5-6       |            |
|   23  | 23       |  12        | 8-9        |  6         |  5-6       |            |
|   24  | **23**   |  12  G     | 8-9        |  6         |  5-6       | 5-6 a      |  
|   25  | 25       |  13  a     |  9  a      |  **6**  AH |  6   c     |            |
|   26  | **25**   |  13        |  9         |7-9  a      |  6-7       |            |
|   27  | 27       | **13**  AH |  9         |7-9         |  6-7       |            |  5   a
|   28  | **27**   | 15-16   c  | **9**  F   |8-9  a      |  6-7       |            |  5
|   29  | 29       | 15-16      |10-11 a     |8-11        |  6-7       |            |  5
|   30  | **29**   | 15-16   J  |  11  a G   |8-11        |  6-7 B     |            |  5   B

Legend: we use lower case `a`-`e` to justify lower bounds and upper case `A`-`J` to justify upper bounds, which are explained below.
No explanation is given when `n ≤ k` or `k = 2` or the value can be derived from the inequalities `T(n+1,k) ≥ T(n,k) ≥ T(n,k+1)`.

The bolded values indicate perfect solutions (see below).

## Terminology

* Given a table assignment for 1 or more meals. We say that this is a *valid solution* if every participant meet every other participant at least once.
* A valid solution with `n` participants and table size of at most `k` is called a `(n,k)`-*solution*.
* Given a valid solution. We say that it is an *optimal solution* if there is no valid solution (with the same `n` and `k`) with fewer days.
* Given a valid solution. We say that it is a *perfect solution* if every participant meets every other participant exactly once.
* The *Social Golfer Problem* is similar: what is the maximum possible of meals such that no two participants sit at the same table? `G(m,k)` is the maximal number with `m*k` participants and where each table contains **exactly** `k` participants.

## Properties

### Perfect Solutions
* Necessarily, every perfect solution is optimal.
* Necessary requirements for a perfect `(n,k)`-solution to exist are `k - 1 | n - 1` and `k | n` (or `n = 1`). 
* A perfect `(n,k)`-solution exists iff `T(n,k) = (n-1)/(k-1)`.

### Known Values
* `T(n,2) = n` if `n` is odd, `T(n,2)=n-1` if `n` is even.
  * The lower bound is given by `c`, see below. 
  * The upper bound can be obtained as follows.
    * Suppose `n = 4m`: split it up in 2 groups of size `2m`, first do those groups independently in `2m-1` days, then in the next `2m` days on day `i` let person `j` in group 1 sit with person `i+j (mod 2m)` in group 2.
    * Suppose `n = 2m` with `m` odd:
      * For the first `m` days: on day `i` let person `i` sit with `i+m` and person `i+j` with `i-j`.
      * For the next `m-1` days, on day `2k-1` and `2k` let person `i` sit with the persons `i+2k-1` and `i-(2k-1)`. If `i` is even it will sit with `i+2k-1` first, and if `i` is odd it will sit with `i-(2k-1)` first.
    * Suppose `n` is odd, then we can use the solution for `n+1` participants, dropping 1 participant.
* `T(n,k) = 1` if `n ≤ k`.
* If `k < n ≤ (3/2)k` then `T(n,k) = 3`.
  * `d`: It cannot be done in 2 days, because on day 1 there are at least 2 tables. All participants on table 1 need to be sit with all participants not on table 1 on day 2, but that means that everyone needs to sit together on day 2. Contradiction.
  * `D`: It can be done in 3 days. Suppose `2k-n ≥ Ceil(k/2)`, i.e. `2k-n ≥ k/2`, i.e. `3k ≥ 2n`.
    Then 3 sets of size `k` can cover all pairs: 
    On day 1 sit participants `1--k` together.
    On day 2 sit `(k+1)--n` and participants `1--Ceil(k/2)` together.
    On day 3 sit `Ceil(k/2)+1 -- n` together.
* If `k` is prime and `n` is a power of `k`, then there is a perfect `(n,k)`-solution. This follows from upper bound `A` (by induction) or from the next bullet point.
* `H`: If `k` is a prime power and `n` is a power of `k`, then there is a perfect `(n,k)`-solution. 
  * Consider the field `F` of order `k`, and a vector field `V` with cardinality `n` over `F`.
  * For every 1-dimensional subspace `L` of `V` the sets of 1-dimensional affine spaces parallel to `L` forms a partition of `V`. This defines a table assignment for a single meal.
  * The set of all table assignments determined by all 1-dimensional subspaces in this way forms a perfect `(n,k)`-solution. The reason that it is perfect follows from the fact that 1-dimensional affine spaces stand in bijective correspondence to pairs of points in `V`.
  * This idea is due to Neil Strickland.
* `J`: A perfect `(n,3)`-solution for `n ≥ 3` is called a *Kirkman Triple System* and is possible iff `n ≡ 3 mod 6`.
  * This is (supposed to be) proven in *Solution of Kirkman's schoolgirl problem*, Ray-Chaudhuri and Wilson (1971). We couldn't find a copy of this paper.
  * Together with lower bound `a`, this gives that `T(6k+1,3) = T(6k+2,3) = T(6k+3,3) = 3k+1`.
* Other known specific values. 
  * `T(32,4)=11` is a perfect solution. This follows from `G`.

### Relations:
* `T(n+1,k) ≥ T(n,k) ≥ T(n,k+1)`. If a value in the table can be derived from these inequalities, they are no other explanation is given.


### Lower Bounds:
* `T(n,k) ≥ (n-1)/(k-1)` (special case of `a`). Every participant can see only `k-1` participants per meal, and needs to see `n-1` participants.
* `a`: Suppose `n = m*k+l` with `0 ≤ l < k`.
  There are `n(n-1)/2` pairs. 
  At most `m*k*(k-1)/2+l*(l-1)/2` pairs can be formed per meal.
  So `T(n,k)` is at least equal to the quotient of these 2.
* `c`: If `n = m*k+1` then this bound is `n(n-1)/(m*k*(k-1)) = n/(k-1)`. 
  Suppose `k - 1 | n` (i.e. `n ≡ -(k-1) mod k(k-1)`). Then
  `T(n,k) ≥ n/(k-1)+1`, because if it's possible after `n/(k-1)` days, we need to form `m*k*(k-1)/2` new connections every meal. This means that
  * Every table needs to be size `k`, except for 1 table of size 1 every meal.
  * Nobody can meet the same person twice.
  This means that after every meal, the number of participants participant A has met is divisible by `k-1`, so it can never equal `n-1`.
* `d`: see *Known Values*.
* `e`: proven by hand for this special case. (We don't use `e` if another letter applies.)

### Upper Bounds:
* `A`: `T(km,k) ≤ T(m,k) + m` if `m` is coprime with `(k-1)!`.
  * Divide the participants into `k` groups of `m` people. On the first `T(m,k)` days, everyone meets every participant of their group.
  * Number the participants in each group using the remainder classes modulo `m`.
  * On the `m` days after that, on day `i` (`0≤i<m`) make a table with participant `j` from the first group, `j+i` from the second group, `j+2i` from the third group, and so on. If `m` has no divisor smaller than `k`, then every participant will meet every participant from another group this way.
  * In particular, this shows that if there is a perfect `(m,k)`-solution and `m` is coprime with `(k-1)!` then there is a perfect `(km,k)`-solution. In particular, if `p` is prime there is a perfect `(p^k,p)`-solution.
* `B`: `T(nl,kl) ≤ T(n,k)`. This can be seen by making `n` groups of `l` people each and always seating all people in a single group together.
* `C`: `T(nl+1,kl+1) ≤ T(n,k)`. Same as `B`, but make one group size `l+1`.
* `D`: see *Known Values*.
* `E`: found solution by hand for this special case, see below. (We don't use `E` if another letter applies.)
* From a good solution of the social golfer's problem (see External Links) we can retrieve a solution to the Happy Diner Problem. 
  * Denote the solution to the social golfer's problem with `m` groups and `k` golfers per group (so `m*k` golfers total) by `G(m,k)`.
  * `F`: If `G(m,k)*(k-1) = m*k - 1` then `T(m*k,k) = G(m,k)`, because this gives a perfect `(m*k,k)`-solution.
  * `G`: If `G(m,k)*(k-1) = m*k - 2` then `T(m*k,k) = G(m,k) + 1`. This is a lower bound by `a` and a upper bound using the solution to `G(m,k)`: take the solution to `G(m,k)` for the first `G(m,k)` meals. Then everyone has seen all other participants, but 1. For the last meal, have one table for each of the pair of participants which still need to see each other.
  * The solutions of the social golfer's problem, can be found at the following links:
    * [Warwick's result page (2002)](http://web.archive.org/web/20050308115423/http://www.icparc.ic.ac.uk/~wh/golf/) has various perfect solutions with a small number of participants. 
    * [Markus Triska's master thesis (2008)](https://www.metalevel.at/sgp/) has `G(8,4) = 10`.
    * [Edd Pegg Jr.'s Math Game page (2007)](http://www.mathpuzzle.com/MAA/54-Golf%20Tournaments/mathgames_08_14_07.html) has `G(8,3) = 11` and `G(7,4) = 9` and `G(9,4) = 11`.
  * (We don't use `F` and `G` if another letter applies.)
* `H`, `J`: see *Known Values*.
* `K`: If `k ≤ m` then `T(n,k) ≤ T(n,m) * T(m,k)`. If we have a seating arrangement for `n` participants at table size `m`, then we can give a seating arrangement for table size `k` by simulating tables of size `m` over `T(m,k)` meals.

### Solutions computed by hand

#### `T(6,3) ≥ 4`

* TODO
* A similar argument *might* show that `T(12,3) ≥ 7`. (but `T(18,3) = 9`, so it is not generally true that `T(6k,3) > 3k`.)
  * `G(4,3) = 4`, i.e. there is no solution where 12 participants sit with different people for 5 days with a table size of 3 which might indicate that `T(12,3) ≥ 7`.

#### `T(10,4) ≤ 4`

* Solution:
```
1234 5678 90
1259 3670 48
1280 4679 35
045 1267 389
```

#### `T(11,4) ≥ 5`

* Suppose there is a solution in 4 days. 
* The only configurations which are not dominated are `(4,4,3)` and `(3,3,3,2)`. The first adds at most 15 connections, the second at most 10.
* Therefore, on at least 3 days we need a (4,4,3) configuration. WLOG day 1 is distributed `1234 5678 ABC`. 
* For the other days any table of size 4 has 1 pair in common with day 1, so adds at most 5 new connections. Therefore, at lost 13 new connections can be added during each day.
* This means we cannot get 55 connections, therefore we get a contradiction.

#### `T(10,5) ≥ 4`
* Suppose there is a valid solution in 3 days. 
* The only configurations which are not dominated are `(5,5)` (<= 20 conns), `(4,4,2)` (<= 13 conns) and `(4,3,3)` (<= 12 conns).
* Therefore, we need (5,5) at least once. WLOG day 1 is distributed `01234 56789`. 
* From now on `(5,5)` has at most 12 new conns, `(4,4,2)` has at most 9 new conns and `(4,3,3)` has at most 8 new conns.
* This means we cannot get 45 connections, therefore we have no valid solution in 3 days.


## Questions
* For every `n` and `k` is there an optimal `(n,k)`-solution in which, during every meal, at most one table is not completely occupied?
* If `n ≡ k mod k(k-1)` is there always a perfect `(n,k)`-solution? Is it true if we assume `k` is a prime power or a prime number? There is no reason to believe this, but it is true for all values where the answer is known.
  * It is true for `k = 3`. For `k = 4` it's true when `n ≤ 28`.
  
### Conjectures
* `T(n,k) ≤ n/(k-1) + O(1) * log(n)`. This should follow from an inductive argument using `A`.
* For all `k`, `T(n,k) - n/(k-1)` is bounded by a constant (independent of `n`, possibly dependent on `k`).
  * This is true for `k = 3`. In fact, the optimal `(n,3)`-solution is at most 1 higher than the value obtained from the lower bound `c`. 
    The reason for this is that for every `m` there is a perfect `(6m+3,3)`-solution (see *Known values*), and the lower bound for `6m-2` given by `c` is only 1 lower than the value for `6m+3`.

## External Links

* Dagstuhl's Happy Diner Problem: we are currently writing draft sequences [A318240](https://oeis.org/draft/A318240) and [A318241](https://oeis.org/draft/A318241).
  * We couldn't find any other place where partial solutions of this problem has been given.
  * On [Sarah's Oberwolfach Problem Page](http://facultyweb.kennesaw.edu/shollid4/oberwolfach.php) the problem has been stated and finding the perfect `(n,3)`-solutions is a special case of the Oberwolfach Problem.
* Social Golfer Problem: 
  * [Wolfram Mathworld](http://mathworld.wolfram.com/SocialGolferProblem.html) 
  * [Warwick's result page (2002)](http://web.archive.org/web/20050308115423/http://www.icparc.ic.ac.uk/~wh/golf/)
  * [Markus Triska's master thesis (2008)](https://www.metalevel.at/sgp/)
  * [Edd Pegg Jr.'s Math Game page (2007)](http://www.mathpuzzle.com/MAA/54-Golf%20Tournaments/mathgames_08_14_07.html)
  * [A107431](https://oeis.org/A107431).
* Kirkman Triple System: 
  * [Wolfram Mathworld](http://mathworld.wolfram.com/KirkmanTripleSystem.html), 
  * [Dutch dissertation by Pieter Mulder (1917)](https://babel.hathitrust.org/cgi/pt?id=njp.32101065911230;view=1up;seq=19) (pdf available on request).
  * *Solution of Kirkman's schoolgirl problem*, Ray-Chaudhuri and Wilson, 1971. In [Proc. of Symp. in Pure Math, Vol 19](http://www.ams.org/books/pspum/019/). (please send pdf if you can access it.)
  * *Kirkman triple systems and their generalizations: A survey*, Rees and Wallis, 2002. (please send pdf if you can access it.) [Springer](https://link.springer.com/chapter/10.1007/978-1-4613-0245-2_13)
* Oberwolfach Problem: [Sarah's Oberwolfach Problem Page](http://facultyweb.kennesaw.edu/shollid4/oberwolfach.php).


## Contributing

* Contributions are welcome! Feel free to add any information. Please provide links or justifications of claims you make.
