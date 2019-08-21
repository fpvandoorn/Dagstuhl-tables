# Dagstuhl's Happy Diner Problem

## The Table Assignment Assignment

**The Problem Statement**: What is the minimum number of meals so that each of the `n` conference participants can share at least one meal with every other participant when eating at tables of at most `k` persons? We call this number `T(n,k)`.

In particular, we have an unlimited number of tables, and we do not require that any two participants have a meal together exactly once, or that every table is fully occupied.

## Dagstuhl's Table Table
| n / k |    2     |   3        |   4        |   5        |   6        |   7        |  8         |
|:-----:|----------|------------|------------|------------|------------|------------|------------|
|   1   |  **0**   |  **0**     |  **0**     |  **0**     |  **0**     |  **0**     |  **0**     |
|   2   |  **1**   |    1       |    1       |    1       |    1       |    1       |    1       |
|   3   |    3     |  **1**     |    1       |    1       |    1       |    1       |    1       |
|   4   |  **3**   |    3   cd  |  **1**     |    1       |    1       |    1       |    1       |
|   5   |    5     |    3  `↖`  |    3   d   |  **1**     |    1       |    1       |    1       |
|   6   |  **5**   |    4   fg  |    3       |    3   d   |  **1**     |    1       |    1       |
|   7   |    7     |    4       |    3       |    3       |    3   d   |  **1**     |    1       |
|   8   |  **7**   |    4       |    3   B   |    3       |    3       |    3   d   |  **1**     |
|   9   |    9     |  **4** AH  |    4  c`↘` |    3  `↖`  |    3       |    3       |    3   d   |
|   10  |  **9**   |    6   c   |    4  `↖`  |    4   fg  |    3       |    3       |    3       |
|   11  |   11     |    6       |    5   g   |    4       |    3       |    3       |    3       |
|   12  | **11**   |    6   E   |    5       |    4   E   |    3   B   |    3       |    3       |
|   13  |   13     |    7   a   |    5       |    5   e   |    4  `↘`  |    3  `↖`  |    3       |
|   14  | **13**   |    7       |    5       |    5       |    4       |    4   f   |    3       |
|   15  |   15     |  **7** F   |    5       |    5       |    4       |    4       |    3       |
|   16  | **15**   |    9   c   |  **5** H   |    5       |    4       |    4       |    3   B   |
|   17  |   17     |    9       |   6-8  a   |    5  `↖`  |    4       |    4       |    4   f   |
|   18  | **17**   |    9   G   |   7-8  a   |   5-6      |    4   B   |    4       |    4       |
|   19  |   19     |   10   a   |   7-8      |    6   g   |    5   g   |    4  `↖`  |    4       |
|   20  | **19**   |   10       |   7-8  A   |    6       |    5       |   5-6  g   |    4   B   |
|   21  |   21     | **10** F   |   8-9  c   |    6       |    5   E   |   5-6      |   4-5      |
|   22  | **21**   |   12   c   |   8-9      |    6       |   5-6      |   5-6      |   4-5      |
|   23  |   23     |   12       |   8-9      |    6       |    6   g   |   5-6      |    5   g   |
|   24  | **23**   |   12   G   |   8-9      |    6       |    6       |   5-6      |    5       |
|   25  |   25     |   13   a   |    9   a   |  **6** AH  |    6       |   5-6      |    5       |
|   26  | **25**   |   13       |    9       |   7-9  a   |    6  `↖`  |   5-6      |    5       |
|   27  |   27     | **13** AH  |    9       |   7-9      |   6-7      |    6 g     |    5       |
|   28  | **27**   | 15-16  c   |  **9** F   |   8-9  a   |    7   g   |    6       |    5       |
|   29  |   29     | 15-16      |  10-11 a   |   8-9 `↖`  |    7       |    6       |    5       |
|   30  | **29**   | 15-16  J   |   11   a G |   8-11     |    7   B   |    6    K  |    5   B   |

Legend:
* We use lower-case letters `a`-`z` (or `↘`) to justify lower bounds and upper-case letters `A`-`Z` (or `↖`) to justify upper bounds, which are explained below.
* No explanation is given when `n ≤ k` or `k = 2` or the value can be derived from the inequalities `T(n+1,k) ≥ T(n,k) ≥ T(n,k+1)`.
* We have the relation `T(n+1,k+1) ≤ T(n,k)` (see [Relations](#relations)). If we use this as an upper bound we write `↖` (the value in this cell is at most the value to the top-right of this cell) and as a lower bound we write `↘` (this value is at least the value to the bottom-left).
* The bolded values indicate perfect solutions (see below).

## Dual table

| T / k |  2       |   3         |   4         |   5         |   6         |   7         |  8          |     9       |
|:-----:|----------|-------------|-------------|-------------|-------------|-------------|-------------|-------------|
|   1   |  **2**   |  **3**      |  **4**      |  **5**      |  **6**      |  **7**      |  **8**      | **9**       |
|   2   |    2     |    3     cd |    4      d |    5      d |    6     d  |    7      d |    8      d |   9         |
|   3   |  **4**   |    5  `←`fg |    8 B c`→` |    9   `←`fg|   12   B`→` |   13   `←`f |   16    B`→`|  17    `←`f |
|   4   |    4     |  **9** AH   |   10   `←`g |   12    E e |   18   B g  |   19   `←`g | 20-22   B g | 27-28   B g |
|   5   |  **6**   |    9     c  | **16**  H a | 17-18  `←`g | 21-22  E g  | 19-26     g |   32    B g | 33-34  `←`g |
|   6   |    6     |   12   E a  | 16-17     a | **25** AH a | 26-27 `←`g  | 30-32   K g | 32-37     a | 36-42   B g |
|   7   |  **8**   | **15** F    | 16-20     c | 25-27     a | 30-36  B a  | 31-39  `←`g | 32-45     g | 45-51   B g |
|   8   |    8     |   15     c  | 20-24   A a | 25-31     a | 30-39    a  | **49** AH a | 50-53  `←`g | 54-59   K g |
|   9   | **10**   |   18   G a  | **28**  F a | 29-35  `←`c | 36-44  B a  | 49-52     a | **64**  H a | 65-69  `←`g |
|   10  |   10     | **21** F    | 28-29     a | 35-40   A a | 42-49 AB a  | 49-58     a | 64-68     a | **81**  H a |
|   11  | **12**   |   21     c  |   32    G a | 35-45     a | 42-54    c  | 49-65     a | 64-75     a | 81-86     a |
|   12  |   12     |   24   G a  | 32-36     a | 35-47     a | 48-60  B a  | 49-71     a | 64-82     a | 81-94     a |
|   13  | **14**   | **27** AH   |             |             |             |             |             |             |
|   14  |   14     |   27     c  |             |             | 66-69  A a  | 77-84   A a | 88-97   A a | 99-110  A a |
|   15  | **16**   | 27-30    a  |             | 55-60   A a |             |             |             |             |
|   16  |   16     | **33** F    | 44-48   A a |             |             | 91-94   A a | 104-112 A a | 117-127 A a |
|   17  | **18**   |   33     c  |             |             | 78-84  A c  |             |             |             |
|   18  |   18     | 33-36    a  | 52-53   A a | 65-71   A a |             |             |             |             |
|   19  | **20**   | **39** F    |             |             |             |             |             |             |
|   20  |   20     |   39     c  |             |             |             |             |             | 153-158 A a |
|   21  | **22**   | 39-42    a  | **64**  H a |             | 102-104 A a | 119-126 A a | 136-146 A a |             |
|   22  |   22     | **45** A    |             | 85-87   A a |             |             |             |             |
|   23  | **24**   |   45     c  |             |             |             | 133-136 A a | 152-160 A c | 171-182 A a |
|   24  |   24     | 45-48    a  |             |             |             |             |             |             |
|   25  | **26**   | **51** J    | 68-76   A a | 95-100  A a | 114-126 A a |             |             |             |
|   26  |   26     |   51     c  |             |             |             |             |             |             |
|   27  | **28**   | 51-54    a  | 76-80   A a |             |             |             |             | 207-216 A a |
|   28  |   28     | **57** J    |             |             |             |             | 184-194 A a |             |
|   29  | **30**   |   57     c  |             |  115    A c | 138-144 A c | 161-175 A a |             |             |
|   30  |   30     | 57-60    a  |             |             |             |             |             |             |
|   31  | **32**   | **63** A    |             |**125** AH a |             |             |             |             |

* An entry in this table shows the maximal `n` such that `T(n,k) ≤ T`. We call this value `n(T,k)`.
* This table has the same information as the previous one, organized differently.
* This table is harder to read, but much more informationally dense.
* If you want to read a value of `T(n,k)` from this table:
  * Look at the `k`-th column.
  * Find the smallest `T` that possibly satisfies `n(T,k) ≥ n`. Then `T(n,k) ≥ T`.
  * Find the smallest `T'` that definitely satisfies `n(T',k) ≥ n`. Then `T(n,k) ≤ T'`.
  * For example, to find `T(14,3)` we see that `T = 7` is the first value where `n(T,3) ≥ 14` (since `n(T,3) = 15`), so `T(14,3) = 7`.
  * For example, to find `T(24,6)`, as of August 2019 we see that `n(5,6)` is in the range `18-24` and `n(6,6)` is in the range `26-30`. We see that `n(5,6) ≥ 24` is possible but not guaranteed and that `n(6,6) ≥ 24` is guaranteed. So `T(24,6)` is either 5 or 6.
  * Using similar logic we can conclude that `T(25,6) = T(26,6) = 6`. Even though the exact values in the table are not known, we do know that `T = 6` is the smallest value where `n(T,6)` is at least `n` (for `n` is 25 or 26).
  * With only this information it is possible that `T(27,6) > 6`.
* In this table the upper-case (or `←`) letters show why the entry is not smaller (why it is possible to have a solution with this number of participants) and the lower-case (or `→`) letters show why the entry is not larger (why it is not possible to have a solution with one more partipant).
* The use of `T(n+1,k+1) ≤ T(n,k)` is indicated with `←` and `→`. `←` means that this cell strictly greater than the cell to the left, while `→` means that this cell is strictly smaller than the cell to the right.
* Sometimes two cells point at each other (e.g. `(T,k) = (4,4)` and `(T,k) = (4,5)`). This looks circular, but it is not. It means that the upper bound of the left cell follows from the upper bound of the right cell and the lower bound of the right cell follows from the lower bound of the left cell.
* For `k > 3` and `T > 12` we only put values where either the lower bound or the upper bound is nontrivial (not obtained by `← → a c B`)

## Terminology

* Given a table assignment for 1 or more meals. We say that this is a *valid solution* if every participant meet every other participant at least once.
* A valid solution with `n` participants and table size of at most `k` is called a `(n,k)`-*solution*.
* Given a valid solution. We say that it is an *optimal solution* if there is no valid solution (with the same `n` and `k`) with fewer days.
* Given a valid solution. We say that it is a *perfect solution* if every participant meets every other participant exactly once and all tables have `k` every meal.
* The *Social Golfer Problem* is similar: what is the maximum possible of meals such that no two participants sit at the same table? `G(m,k)` is the maximal number with `m*k` participants and where each table contains **exactly** `k` participants.

## Properties

### Perfect Solutions
* Necessarily, every perfect solution is optimal.
* Necessary requirements for a perfect `(n,k)`-solution to exist are `k - 1 | n - 1` and `k | n` (or `n = 1`).
* A perfect `(n,k)`-solution exists iff `T(n,k) = (n-1)/(k-1)`.
* See [Known Values](#known-values) for some known perfect solutions

### Relations:
* `T(n+1,k) ≥ T(n,k) ≥ T(n+1,k+1) ≥ T(n,k+1)`.
  * If a value in the table can be derived from the first inequality, no other explanation is given.
  * The second inequality follows by treating two of the `n+1` people as a single person (always seating them together), and then applying a `(n,k)`-solution.
* `T(n,k) ≤ T(n,m) * T(m,k)`.
  * If we have a seating arrangement for `n` participants at table size `m`, then we can give a seating arrangement for table size `k` by simulating tables of size `m` over `T(m,k)` meals.
  * This subsumes the relation `T(n+1,k) ≥ T(n,k) ≥ T(n,k+1)` above since `T(k,k+1)=1`.
  * If there is a perfect `(n,m)`-solution and a perfect `(m,k)`-solution then there is a perfect `(n,k)`-solution.

### Known Values
* `T(n,k) = 1` if `n ≤ k` trivially.
* `T(n,2) = n` if `n` is odd, `T(n,2)=n-1` if `n` is even.
  * The lower bound is given by `a`, see below.
  * The upper bound can be obtained as follows.
    * Suppose `n = 4m`: split it up in 2 groups of size `2m`, first do those groups independently in `2m-1` days, then in the next `2m` days on day `i` let person `j` in group 1 sit with person `i+j (mod 2m)` in group 2.
    * Suppose `n = 2m` with `m` odd:
      * For the first `m` days: on day `i` let person `i` sit with `i+m` and person `i+j` with `i-j`.
      * For the next `m-1` days, on day `2k-1` and `2k` let person `i` sit with the persons `i+2k-1` and `i-(2k-1)`. If `i` is even it will sit with `i+2k-1` first, and if `i` is odd it will sit with `i-(2k-1)` first.
    * Suppose `n` is odd, then we can use the solution for `n+1` participants, dropping 1 participant.
* If `k` is even and `k < n ≤ 2k` then `T(n,k) = 3`. Also, if `k` is odd and `k < n < 2k` then `T(n,k) = 3`. These are *all* the values for `(n,k)` where `T(n,k) = 3`.
  * If `n > k` then `T(n,k) ≥ 3` is explained by the lower bound `d`.
  * If `k` is even and `n ≤ 2k` then `T(n,k) ≤ 3` is explained by the upper bound `B`.
  * If `k` is odd and `n < 2k` then `T(n,k) ≤ 3` is explained by `T(n,k) ≤ T(n-1,k-1) ≤ 3` by the previous bullet point.
  * For smaller `n` we have `T(n,k) = 1` trivially and for larger `n` we have `T(n,k) ≥ 4` by lower bound `f`.
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
  * `T(32,4)=11` is an optimal solution. This follows from `G`.
  * There are more known values, see tables.

### Lower Bounds:
* `↘`/`→`: The relation `T(n,k) ≥ T(n+1,k+1)` can sometimes be used as a lower bound. See [Relations](#relations).
* `T(n,k) ≥ (n-1)/(k-1)` (special case of `a`). Every participant can see only `k-1` participants per meal, and needs to see `n-1` participants.
* `a`: Suppose `n = m*k+l` with `0 ≤ l < k`.
  There are `n(n-1)/2` pairs.
  At most `m*k*(k-1)/2+l*(l-1)/2` pairs can be formed per meal.
  So `T(n,k)` is at least equal to the quotient of these 2.
* `b`: *obsolete*.
* `c`: If `n = m*k+1` then the bound from `a` is `n(n-1)/(m*k*(k-1)) = n/(k-1)`.
  Suppose `k - 1 | n` (i.e. `n ≡ -(k-1) mod k(k-1)`) and `k > 2`. Then
  `T(n,k) ≥ n/(k-1)+1`, because if it's possible after `n/(k-1)` days, we need to form `m*k*(k-1)/2` new connections every meal. This means that
  * Every table needs to be size `k`, except for 1 table of size 1 every meal.
  * Nobody can meet the same person twice.
  This means that after every meal, the number of participants participant A has met is divisible by `k-1`, so it can never equal `n-1`.
* `d`: If `n > k` then `T(n,k) ≥ 3`.
  * It cannot be done in 2 days, because on day 1 there are at least 2 tables. All participants on table 1 need to be sit with all participants not on table 1 on day 2, but that means that everyone needs to sit together on day 2. Contradiction.
* `e`: proven for this special case, see below. (We don't use `e` if another letter applies.)
* `f`: If `k` is odd then `T(2k,k) ≥ 4`.
  * This also implies that for even `k` we have `T(2k+1,k) ≥ T(2(k+1),k+1) ≥ 4`
  * For the proof we will use the terminology given under [Solutions for Individual Cases/New terminology](#new-terminology). Note that all non-dominated distributions use 2 or 3 tables.
  * Suppose this can be done in 3 days.
  * Suppose the assignment for day 1 is `{a, b, c}` with `k ≥ |a| ≥ |b| ≥ |c| ≥ 0`. We may assume that `|a|` is the largest among all table sizes on all days.
  * Let `x ∈ a` and let `x ∈ a₂ ⊆ a`, `b₂ ⊆ b` and `c₂ ⊆ c` be the participants of the table containing `x` on day 2. We may assume that `b₂ ≠ ∅` (by interchanging day 2 and 3), and from this we can conclude that `a₂ ≠ a` (otherwise `|a|` was not largest).
  * Now on day 3, all of the following must be true
    * Everyone in `a₂` has to meet everyone in `b \ b₂` and `c \ c₂`, so they must all be at the same table.
    * Everyone in `a \ a₂` has to meet everyone in `b₂` and `c₂`.
    * Everyone in `b₂` has to additionally meet everyone in `c \ c₂`.
  * Since not everyone can be at the same table, this means that `c₂ = c`.
  * The table assignment on day 3 must be `{ a₂ ∪ (b \ b₂), (a \ a₂) ∪ b₂ ∪ c }`.
  * `b₂ ≠ b`, since otherwise `|a₂ ∪ b₂ ∪ c₂| > k`.
  * Everyone in `b \ b₂` has never seen anyone in `c`, which means that `c = ∅`.
  * This means that `|a| = |b| = k`
  * Everyone in `a \ a₂` and everyone in `b \ b₂` must have seen each other on day 2, so the table assignment on day 2 was `{ a₂ ∪ b₂ (a \ a₂) ∪ (b \ b₂) }`.
  * Since `k` is odd, we have `max(|a₂|, |a \ a₂|) > k / 2` and `max(|b₂|, |b \ a₂|) > k / 2`, which means that on either day 2 or day 3 there was a table with more that `k` participants. Contradiction!
* Note: For `n < k^2` (and especially for `n < k^2/2`) the bound obtained by `a` and `c` are not very good. The reason is that although on day 1 you might be able to make the caculated number of new connections, every other day many connections were already present on day 1. This means that the number of connections you can make on most (all but one) days is much less, so you need more days to do it. In [Solutions for Individual Cases](#solutions-for-individual-cases) we give many arguments of this form, but it is quite hard to generalize is rigorously (since having a distribution with fewer connections on day 1 might lead to more connections on subsequent days).
* `g`: Improvement of `a` and `c` when `k < n ≤ k^2 - 2`
  * For the explanation we will use the terminology given under [Solutions for Individual Cases/New terminology](#new-terminology).
  * On day 1 at most `s(opt)` connections can be added
  * On subsequent days fewer connections can be added. We can give an upper bound, and run through all (sensible) pairs of non-dominated configurations to find the maximal number `s` of connections that can
    be added on day 2 (where we can choose the configuration of day 1 to be as optimal as possible).
  <!-- * Let `d(c1,c2) = sum_{l ∈ c2} s(l) - max(l - |c1|, 0)`. Then `s(c1,c2) ≤ d(c1,c2) ≤ s(c2)`.
  * Conjecture: `s(c1, c2) ≤ d(opt,opt)` whenever `s(c2) ≤ s(c1)` and `c1` and `c2` are non-dominated. (this is true, but I haven't figured out the precise argument yet) -->
  * This means that after `T+1` days at most `s(opt) + T * s` connections can be made, which gives a lower bound for the number of days.
  * The Mathematica function doing this is given in `lowerbound.txt`. It is not optimal, and is not necessarily increasing in `n`. I'm quite sure it is correct though.

### Upper Bounds:
* `↖`/`←`: The relation `T(n+1,k+1) ≤ T(n,k)` can be used as an upper bound. See [Relations](#relations).
* `A`: `T(km,k) ≤ T(m,k) + m` if `m` is coprime with `(k-1)!`.
  * Divide the participants into `k` groups of `m` people. On the first `T(m,k)` days, everyone meets every participant of their group.
  * Number the participants in each group using the remainder classes modulo `m`.
  * On the `m` days after that, on day `i` (`0≤i<m`) make a table with participant `j` from the first group, `j+i` from the second group, `j+2i` from the third group, and so on. If `m` has no divisor smaller than `k`, then every participant will meet every participant from another group this way.
  * In particular, this shows that if there is a perfect `(m,k)`-solution and `m` is coprime with `(k-1)!` then there is a perfect `(km,k)`-solution. In particular, if `p` is prime there is a perfect `(p^k,p)`-solution.
* `B`: `T(nl,kl) ≤ T(n,k)`. This can be seen by making `n` groups of `l` people each and always seating all people in a single group together.
* `C`: *obsolete*.
* `D`: *obsolete*.
* `E`: found solution for this special case, see below. (We don't use `E` if another letter applies.)
* From a good solution of the social golfer's problem (see *External Links*) we can retrieve a solution to the Happy Diner Problem.
  * Denote the solution to the social golfer's problem with `m` groups and `k` golfers per group (so `m*k` golfers total) by `G(m,k)`.
  * `F`: If `G(m,k)*(k-1) = m*k - 1` then `T(m*k,k) = G(m,k)`, because this gives a perfect `(m*k,k)`-solution.
  * `G`: If `G(m,k)*(k-1) = m*k - 2` then `T(m*k,k) = G(m,k) + 1`. This is a lower bound by `a` and a upper bound using the solution to `G(m,k)`: take the solution to `G(m,k)` for the first `G(m,k)` meals. Then everyone has seen all other participants, but 1. For the last meal, have one table for each of the pair of participants which still need to see each other.
  * The solutions of the social golfer's problem, can be found at the following links:
    * [Warwick's result page (2002)](http://web.archive.org/web/20050308115423/http://www.icparc.ic.ac.uk/~wh/golf/) has various perfect solutions with a small number of participants.
    * [Markus Triska's master thesis (2008)](https://www.metalevel.at/sgp/) has `G(8,4) = 10`.
    * [Edd Pegg Jr.'s Math Game page (2007)](http://www.mathpuzzle.com/MAA/54-Golf%20Tournaments/mathgames_08_14_07.html) has `G(8,3) = 11` and `G(7,4) = 9` and `G(9,4) = 11`.
  * (We don't use `F` and `G` if another letter applies.)
* `H`, `J`: see [Known Values](#known-values).
* `K`: From a perfect solution, we can get new solutions with the table size two larger.
  * Given an `(n,k)`-solution in `T` days and a subset `A ⊆ n` of participants such that no `i+1` participants from `A` sit at the same table during the same meal (let's say that `A` is `i`-*good* in this case), then there is a `(n+|A|,k+i)`-solution in `T` days, by replacing everyone in `A` with a pair of people.
  * If we start with a perfect `(n,k)`-solution (with `k > 2`) and a 2-good set `A` such that `|A|+(k-2)|A|(|A|-1)/2 < n`, then we can find a 2-good set with one more participant. The reason is that every pair of people in `A` sit at the same table exactly once, with `k-2` other people. Therefore, at most `|A|+(k-2)|A|(|A|-1)/2` other people cannot be added to `A` while keeping `A` 2-good, which means that there is someone we can add to `A` so that the new set is 2-good.


### Solutions for Individual Cases

* The solution `T(6,3) ≥ 4` is very detailed. Other solutions with the same techniques will have much less explanation. So if you don't understand the reasoning, read `T(6,3) ≥ 4` first (See [Examples](#examples)).
* The code using the Mathematica SAT-solver was written by Michael Trott and optimized by Floris van Doorn.

#### New terminology

* A *distribution* is a seating assignment for a single meal.
* A *configuration* is an assignment for the *number* of participants to each table for a single meal (but not stating which participant goes where).
* We say that a configuration `C` is dominated if it has two tables with `a` and `b` participants and `a + b ≤ k`.
  * In this case, we can merge these two tables and still have a valid solution, so we may assume we have a solution without dominated configurations.
* A *connection* is a pair of people sitting at the same table. A *new connection* is a connection that was not yet formed on a previous day. The number of connections a table of size `l` makes is `s(l) = l(l-1)/2`, not all of which might be new connections. The number of new connections `s(c)` of a configuration `c` is the sum.
* The *optimal configuration* `opt` is the configuration with the most connections. It has `⌊ n / k ⌋` tables of size `k` and one table of size `n mod k`, and it is unique.
* If `k < n ≤ k^2 - 1` then it is not possible to create `2 * s(opt)` new connections after two days, since at least one pair of participants has to sit at the same table on both days, or a configuration other than the optimal configuration has to be used. Let `s(c1,c2)` the maximum number of new connections `c2` can make on day 2 is `c1` was used on day 1.

#### `T(12,3) ≤ 6`
* Solution found by Mathematica SAT-solver:
```
159 278 3AC 46B
12C 345 8AB 679
12B 348 79A 56C
168 25A 39B 47C
14A 236 57B 89C
137 249 BC 58 6A
```

#### `T(11,4) ≥ 5`

* Suppose there is a solution in 4 days.
* The only configurations which are not dominated are `(4,4,3)` and `(3,3,3,2)`. The first adds at most 15 connections, the second at most 10.
* Therefore, on at least 3 days we need a `(4,4,3)` configuration, WLOG on day 1.
* For the other days any table of size 4 has 1 pair in common with day 1, so adds at most 5 new connections. Therefore, at most 13 new connections can be added during each day.
* This means we cannot get 55 connections, therefore we get a contradiction.

#### `T(12,5) ≤ 4`
* Solution found by Mathematica SAT-solver:
```
12345 6789A BC
1279 38B 456AC
128C 4579B 36A
126AB 379C 458
```

#### `T(13,5) ≥ 5`
* This solution was found part by hand, part by computer brute-force.
* Suppose there is a valid solution in 4 days.
* `(5,5,3)` or `(5,4,4)` has to occur at least once.
* If `(5,5,3)` never occurs, then from day 2 on at most 18 connections are possible. Contradiction.
* So day 1 is `(5,5,3)` (23 connections).
* From then on, at most 19 connections are possible, which has to occur at least once, so day 2 is (5,5,3) with 8+8+3 new connections. This can be done in 1 way (up to renaming participants)
* Then there are 8 ways for day 3 to have 18 connections (and more is impossible), possibly counting things twice. We found this number by brute force.
* For none of those 8 ways, there is a valid 4th day.

#### `T(21,6) ≤ 5`
* This was found by modifying `T(16,4) = 5`, using the same method as `K`.
* `K` only shows that `T(20,6) ≤ 5`.
```
1234HI 5678JK 9ABCL DEFG
179DHL 26AFIK 38CE 45BGJ
18BFH 25CDIJ 37AG 469EKL
15AEHJ 289GIL 36BDK 47CF
```

### Examples

* Examples of specific upper and lower bounds.
* These now all follow from other values or a general principle.
* Often they were cases we had to do individually previously.
* Examples that do not follow from other principles are listed under [Solutions for Individual Cases](#solutions-for-individual-cases).

#### `T(6,3) ≥ 4`

* This is a special case of `f`.
* Suppose there is a solution in 3 days.
* At least 2 days need configuration `(3,3)`.
  * The reason is that we need to establish 15 connections between participants over 3 days.
  * We can establish at most 6 connections during a single day by configuration `(3,3)`.
  * Configuration `(2,2,2)` is not dominated, but establishes only 3 connections
  * Any other configuration is dominated by either `(3,3)` or `(2,2,2)`.
  * If there is at most 1 day with configuration `(3,3)`, then the maximum number of established connections is `6 + 3 + 3 = 12 < 15`, which is not enough.
* Without loss of generality we can assume that the first day has configuration `(3,3)`, distributed as `123 456` (i.e. `1`, `2` and `3` sit together and `4`, `5` and `6` sit together).
* Now on the other days, we can establish at most 4 connections.
  * The reason is that if we use configuration `(3,3)`, then 2 participants on the first table already sat together on table 1, and the same for the second table.
  * Therefore, configuration `(3,3)` gives at most 4 new connections.
  * We already saw that the only other non-dominated configuration gives at most 3 new connections.
* Therefore, the maximal number of connections we can establish is `6 + 4 + 4 = 14 < 15`, which is not enough.
* So there is no valid `(6,3)`-solution with 3 days.

#### `T(10,4) ≤ 4`

* This also follows from `T(10,4) ≤ T(9,3) = 4`.
* Alternative solution found by hand:
```
1234 5678 90
1259 3670 48
1280 4679 35
045 1267 389
```

#### `T(10,5) ≥ 4`
* This is a special case of `f`.
* Suppose there is a valid solution in 3 days.
* The only configurations which are not dominated are `(5,5)` (<= 20 conns), `(4,4,2)` (<= 13 conns) and `(4,3,3)` (<= 12 conns).
* Therefore, we need `(5,5)` at least once. WLOG day 1 is distributed `01234 56789`.
* From now on `(5,5)` has at most 12 new conns, `(4,4,2)` has at most 9 new conns and `(4,3,3)` has at most 8 new conns.
* This means we cannot get 45 connections, therefore we have no valid solution in 3 days.

#### `T(13,6) ≥ 4`
* This is a special case of `f`.
* Suppose there is a valid solution in 3 days.
* The configurations with at least 26 connections which are not dominated are `(6,6,1)` and `(6,5,2)`, one of which has to occur at least once.
  * Suppose day 1 is `(6,6,1)`. Then no other day can have more than 20 connections. Day 2 has
    * `(6,6,1)` at most 11+9 = 20 connections
    * `(6,5,2)` at most 11+8+1 = 20 connections (actually, less)
    * `(6,4,3)` and `(5,5,3)` and `(5,4,4)` also have less than 20 connections, all other configurations are dominated.
  * Suppose no day is `(6,6,1)`. Then every day needs 26 connections exactly, which is impossible.
* Alternatively, this can be derived from `T(13,6) ≥ T(14,7) ≥ 4`

#### `T(19,6) ≥ 5`
* Suppose there is a valid solution in 4 days.
* 181 connections have to be made, and at most 45 connections can be made per day, with configuration `(6,6,6,1)`. Every other configuration has at most 41 connections.
* This means that `(6,6,6,1)` has to appear, WLOG on day 1. Now on every other day, the configuration `(6,6,6,1)` can give at most `13+12+12=37` connections, which means that there is no way to get 181 connections in 4 days.

#### `T(14,7) ≥ 4`
* This is a special case of `f`.
* Suppose there is a valid solution in 3 days.
* The configuration `(7,7)` has to occur, since there is no way to make at least 61 connections in 2 days otherwise.
* After `(7,7)` at most 24 connections can be made per day. So there are at most `42 + 24 + 24 = 90 < 91` connections, which is not enough.

#### `T(21,7) ≥ 5`
* Suppose there is a valid solution in 4 days.
* 210 connections have to be made, and at most 63 connections can be made per day, with configuration `(7,7,7)`.
* It is impossible to have a non-dominated solution where 5 tables are used every day.
* If `(7,7,7)` appears, WLOG on day 1, then at most 48 connections can be made every other day, but `63+48+48+48=207<210` is not enough.
* If `(7,7,7)` doesn't appear, then every day has 4 tables. Then at most 57 connections can be made on day 1, and at most 49 connections on future days (since all 7s lose at least 3 and all 6s lose at least 2 connections). This is also not enough, since `57+49+49+49=204<210`.

## Questions
* If `n ≡ k mod k(k-1)` is there always a perfect `(n,k)`-solution? Is it true if we assume `k` is a prime power or a prime number? There is no reason to believe this, but it is true for all values where the answer is known.
  * It is true for `k = 3`. For `k = 4` it's true when `n ≤ 28`.
* For every `n` and `k` is there an optimal `(n,k)`-solution in which, during every meal, at most one table is not completely occupied?
  * This is false. All optimal `(8,5)`-solutions have at least one day with two tables of four participants. This was found by brute force, but is quite easy to see by hand (to do).
  * It is probably even false that there always is an optimal `(n,k)`-solution where there are `⌈ n/k ⌉` tables each day (where `⌈ x ⌉` is the smallest integer which is at least `x`).
    The Mathematica SAT-solver easily found a solution that `T(12,3) ≤ 6`, but didn't terminate within reasonable time when the additional condition was imposed that only 4 tables could be used per day.

### Conjectures
* `T(n,k) ≤ n/(k-1) + O(1) * log(n)`. This should follow from an inductive argument using `A`.
* For all `k`, `T(n,k) - n/(k-1)` is bounded by a constant (independent of `n`, possibly dependent on `k`).
  * This is true for `k = 3`. In fact, the optimal `(n,3)`-solution is at most 1 higher than the value obtained from the lower bound `c`.
    The reason for this is that for every `m` there is a perfect `(6m+3,3)`-solution (see [Known Values](#known-values)), and the lower bound for `6m-2` given by `c` is only 1 lower than the value for `6m+3`.

## External Links

* Dagstuhl's Happy Diner Problem:
  * We submitted two sequences to the OEIS: [A318240](https://oeis.org/A318240) and [A318241](https://oeis.org/A318241).
  * The problem is stated on [Sarah's Oberwolfach Problem Page](http://facultyweb.kennesaw.edu/shollid4/oberwolfach.php). Finding the perfect `(n,3)`-solutions is a special case of the Oberwolfach Problem.
* Social Golfer Problem:
  * [Wolfram Mathworld](http://mathworld.wolfram.com/SocialGolferProblem.html)
  * [Warwick's result page (2002)](http://web.archive.org/web/20050308115423/http://www.icparc.ic.ac.uk/~wh/golf/)
  * [Markus Triska's master thesis (2008)](https://www.metalevel.at/sgp/)
  * [Edd Pegg Jr.'s Math Game page (2007)](http://www.mathpuzzle.com/MAA/54-Golf%20Tournaments/mathgames_08_14_07.html)
  * [A107431](https://oeis.org/A107431).
* Kirkman Triple System:
  * [Wolfram Mathworld](http://mathworld.wolfram.com/KirkmanTripleSystem.html),
  * [Dutch dissertation by Pieter Mulder (1917)](https://babel.hathitrust.org/cgi/pt?id=njp.32101065911230;view=1up;seq=19).
  * *Solution of Kirkman's schoolgirl problem*, Ray-Chaudhuri and Wilson, 1971. In [Proc. of Symp. in Pure Math, Vol 19](http://www.ams.org/books/pspum/019/). (please send pdf if you can access it.)
  * *Kirkman triple systems and their generalizations: A survey*, Rees and Wallis, 2002. (please send pdf if you can access it.) [Springer](https://link.springer.com/chapter/10.1007/978-1-4613-0245-2_13)
* Oberwolfach Problem: [Sarah's Oberwolfach Problem Page](http://facultyweb.kennesaw.edu/shollid4/oberwolfach.php).


## Contributing

* Contributions are welcome! Feel free to add any information. Please provide links or justifications of claims you make.