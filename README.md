# Dagstuhl's Happy Diner Problem

## The Table Assignment Assignment

What is the minimum number of meals so that each of the `n` conference participants can share at least one meal with every other participant when eating at tables of at most `k` persons? We call this number `T(n,k)`

In particular, we have an unlimited number of tables, and we do not require that any two participants have a meal together exactly once, or that every table is fully occupied.

## Dagstuhl's Table Table

| n / k |  2  |  3    |  4    |  5    |  6    |  7    |  8
|-------|-----|-------|-------|-------|-------|-------|-------
|   1   |  0  |  0    |  0    |  0    |  0    |  0    |  0 
|   2   |  1  |  1    |  1    |  1    |  1    |  1    |  1
|   3   |  3  |  1    |  1    |  1    |  1    |  1    |  1
|   4   |  3  |  3  cd|  1    |  1    |  1    |  1    |  1
|   5   |  5  |  3   E|  3  d |  1    |  1    |  1    |  1
|   6   |  5  |  4  e |  3    |  3  d |  1    |  1    |  1
|   7   |  7  |  4    |  3    |  3    |  3   d|  1    |  1
|   8   |  7  |  4    |  3   B|  3    |  3    |  3    |  1
|   9   |  9  |  4   A|  4  c |  3   C|  3    |       |  3
|   10  |  9  | 6-7 c |  4-5  | 3-5   |  3    |       |
|   11  | 11  | 6-7   |  4-5  | 3-5   |  3    |       |
|   12  | 11  | 6-7   |  4-5  | 4-5 a |  3   B|       |
|   13  | 13  | 7   a |  5  a | 4-5   |  3-4  |       |
|   14  | 13  | 7     |  5    | 4-5   |  3-4  |       |
|   15  | 15  | 7    F|  5    | 4-5   |  4   a|       |
|   16  | 15  | 9   c |  5   F|  5  c |  4    |       |
|   17  | 17  | 9     | 6-9 a | 5-9   |  4    |       |
|   18  | 17  | 9    G| 7-9 a | 5-9   |  4   B|       |
|   19  | 19  | 10  a | 7-9   |5-10   |  5-7 a|       |
|   20  | 19  | 10    | 7-9 B |5-10   |  5-7  |       |
|   21  | 21  | 10   F|8-10 c |6-10 a |  5-7 B|       |

Legend: we use lowercase `a`-`e` to justify lower bounds and upper case `A`-`E` to justify upper bounds, which are explained below. 
No explanation is given when `n <= k` or `k = 2` or the value can be derived from the inequalities `T(n+1,k) >= T(n,k) >= T(n,k+1)`.

## Properties

### Known Values
* `T(n,2) = n` if `n` is odd, `T(n,2)=n-1` if `n` is even.
  * The lower bound is given by `c`, see below. 
  * The upper bound can be obtained as follows.
    * Suppose `n = 4m`: split it up in 2 groups of size 2m, first do those groups independently in 2m-1 days, then in the next 2m days on day i let person j in group 1 sit with person i+j (mod 2m) in group 2.
    * Suppose `n = 2m` with m odd:
      the first m days on day i let person i sit with i+m and person i+j with i-j.
      the next 2k:=m-1 days, on day 2k-1 and 2k let person i sit with person i+2k-1 and i-(2k-1). If i is even it will sit with i+2k-1 first, and if i is odd it will sit with i-(2k-1) first.
    * Suppose `n` is odd, then we can use the solution for `n+1` participants, dropping 1 participant.
* `T(n,k) = 1` if `n <= k`.
* If `k < n <= (3/2)k` then `T(n,k) = 3`.
  * `d`: It cannot be done in 2 days, because on day 1 there are at least 2 tables. All participants on table 1 need to be sit with all participants not on table 1 on day 2, but that means that everyone needs to sit together on day 2. Contradiction.
  * `D`: It can be done in 3 days. Suppose `2k-n >= Ceil(k/2)`, i.e. `2k-n >= k/2`, i.e. `3k >= 2n`.
    Then 3 sets of size `k` can cover all pairs: 
    On day 1 sit participants `1--k` together.
    On day 2 sit `(k+1)--n` and participants `1--Ceil(k/2)` together.
    On day 3 sit `Ceil(k/2)+1 -- n` together.

### Relations:
* `T(n+1,k) >= T(n,k) >= T(n,k+1)`. If a value in the table can be derived from these inequalities, they are no other explanation is given.


### Lower Bounds:
* `T(n,k) >= (n-1)/(k-1)` (special case of `a`). Every participant can see only `k-1` participants per meal, and needs to see `n-1` participants.
* `a`: Suppose `n = m*k+l` with `0 <= l < k`.
  There are `n(n-1)/2` pairs. 
  At most `m*k*(k-1)/2+l*(l-1)/2` pairs can be formed per meal.
  So `T(n,k)` is at least equal to the quotient of these 2.
* `c`: If `n = m*k+1` then this bound is `n(n-1)/(m*k*(k-1)) = n/(k-1)`. 
  Suppose `k - 1 | n` (i.e. `n == -(k-1) mod k(k-1)`). Then
  `T(n,k) >= n/(k-1)+1`, because if it's possible after `n/(k-1)` days, we need to form `m*k*(k-1)/2` new connections every meal. This means that
  * Every table needs to be size `k`, except for 1 table of size 1 every meal.
  * Nobody can meet the same person twice.
  This means that after every meal, the number of participants participant A has met is divisible by `k-1`, so it can never equal `n-1`.
  * A special case is `T(6m+1,3) >= 3m+1`.
* `d`: see Known Values.
* `e`: proven by hand for this special case.

### Upper Bounds:
* `A`: `T(km,k) <= T(m,k) + m` if `m` is coprime with `(k-1)!`.
  * Divide the participants into `k` groups of `m` people. On the first `T(m,k)` days, everyone meets every participant of their group.
  * Number the participants in each group using the remainder classes modulo `m`.
  * On the `m` days after that, on day `i` (`0<=i<m`) make a table with participant `j` from the first group, `j+i` from the second group, `j+2i` from the third group, and so on. If `m` has no divisor smaller than `k`, then every participant will meet every participant from another group this way.
* `B`: `T(nl,kl) <= T(n,k)`. This can be seen by making `n` groups of `l` people each and always seating all people in a single group together.
* `C`: `T(nl+1,kl+1) <= T(n,k)`. Same as `B`, but make one group size `l+1`.
* `D`: see Known Values.
* `E`: found solution by hand for this special case.
* From a good solution of the social golfer's problem (see External Links) we can retrieve a solution to the Happy Diner Problem. 
  * Denote the solution to tha social golfer's problem with `m` groups and `k` golfers per group (so `m*k` golfers total) by `G(m,k)`.
  * `F`: If `G(m,k)*(k-1) = m*k - 1` then `T(m*k,k) = G(m,k)`.
  * `G`: If `G(m,k)*(k-1) = m*k - 2` then `T(m*k,k) = G(m,k) + 1`.
this follows from the solution of the social golfer's problem, found [here](http://web.archive.org/web/20050308115423/http://www.icparc.ic.ac.uk/~wh/golf/).
* if `n <= 3^{m+1}` then `T(n,3) <= n/2 + (5/2)m`. So `T(n,3)` is only logarithmically above the easiest lower bound `(n-1)/(k-1)`.


## Conjectures

* Weak: `T(n,k) <= n/(k-1) + O(1) * log(n)`
* Strong: For all `k`, `T(n,k) - n/(k-1)` is bounded by a constant (independent of `n`, possibly dependent on `k`).
* There always exists an optimal solution in which, during every meal, at most one table is not completely occupied.


## External Links

* OEIS: [A318240](https://oeis.org/draft/A318240) and [A318241](https://oeis.org/draft/A318241) (needs more information).
* Social Golfer Problem: [Wolfram Mathworld](http://mathworld.wolfram.com/SocialGolferProblem.html), [2008 master thesis](https://www.metalevel.at/sgp/), [Warwick's old result page](http://web.archive.org/web/20050308115423/http://www.icparc.ic.ac.uk/~wh/golf/), [A107431](https://oeis.org/A107431).
* [Oberwolfach Problem](http://facultyweb.kennesaw.edu/shollid4/oberwolfach.php).



