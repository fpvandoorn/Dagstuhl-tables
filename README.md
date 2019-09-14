# Dagstuhl's Happy Diner Problem

## The Table Assignment Assignment

**The Problem Statement**: What is the minimum number of meals so that each of the `n` conference participants can share at least one meal with every other participant when eating at tables of at most `k` persons? We call this number `T(n,k)`.

In particular, we have an unlimited number of tables, and we do not require that any two participants have a meal together exactly once, or that every table is fully occupied.

## Dagstuhl's Table Table
| n \ k |    2     |   3        |   4        |   5        |   6        |   7        |  8         |
|:-----:|----------|------------|------------|------------|------------|------------|------------|
|   1   |  **0**   |  **0**     |  **0**     |  **0**     |  **0**     |  **0**     |  **0**     |
|   2   |  **1**   |    1       |    1       |    1       |    1       |    1       |    1       |
|   3   |    3     |  **1**     |    1       |    1       |    1       |    1       |    1       |
|   4   |  **3**   |    3   cd  |  **1**     |    1       |    1       |    1       |    1       |
|   5   |    5     |    3   `↖` |    3   di  |  **1**     |    1       |    1       |    1       |
|   6   |  **5**   |    4   fg  |    3       |    3   di  |  **1**     |    1       |    1       |
|   7   |    7     |    4       |    3       |    3       |    3   d   |  **1**     |    1       |
|   8   |  **7**   |    4       |    3     B |    3       |    3       |    3   d   |  **1**     |
|   9   |    9     |  **4**  AH |    4  c`↘` |    3   `↖` |    3       |    3       |    3   d   |
|   10  |  **9**   |    6   c   |    4   `↖` |    4   fg  |    3       |    3       |    3       |
|   11  |   11     |    6       |    5   g   |    4       |    3       |    3       |    3       |
|   12  | **11**   |    6     E |    5       |    4     E |    3     B |    3       |    3       |
|   13  |   13     |    7   a   |    5       |    5   e   |    4  `↘`  |    3   `↖` |    3       |
|   14  | **13**   |    7       |    5       |    5       |    4       |    4 f     |    3       |
|   15  |   15     |  **7**   F |    5       |    5       |    4       |    4       |    3       |
|   16  | **15**   |    9   c   |  **5**   H |    5       |    4       |    4       |    3     B |
|   17  |   17     |    9       |    7   i E |    5   `↖` |    4       |    4       |    4   f   |
|   18  | **17**   |    9     G |   7-8      |   5-6      |    4     B |    4       |    4       |
|   19  |   19     |   10   a   |   7-8      |    6   g   |    5 gi`↘` |    4   `↖` |    4       |
|   20  | **19**   |   10       |   7-8    A |    6       |    5       |    5 g     |    4       |
|   21  |   21     | **10**   F |   8-9  c   |    6       |    5       |    5       |    4       |
|   22  | **21**   |   12   c   |   8-9      |    6       |    5     E |    5       |    4     E |
|   23  |   23     |   12       |   8-9      |    6       |    6   g   |    5       |    5   g   |
|   24  | **23**   |   12     G |   8-9      |    6       |    6       |    5       |    5       |
|   25  |   25     |   13   a   |    9   a   |  **6**  AH |    6       |    5     E |    5       |
|   26  | **25**   |   13       |    9       |   7-9  a   |    6   `↖` |   5-6      |    5       |
|   27  |   27     | **13**  AH |    9       |   8-9  i   |   6-7      |    6 g     |    5       |
|   28  | **27**   | 15-16  c   |  **9**   F |   8-9      |    7   g   |    6       |    5       |
|   29  |   29     | 15-16      |   11   i   |   8-9  `↖` |    7       |    6       |    5       |
|   30  | **29**   | 15-16    J |   11     G |   8-11     |    7   B   |    6     K |    5     B |

Legend:
* We use lower-case letters `a`-`z` (or `↘`) to justify lower bounds and upper-case letters `A`-`Z` (or `↖`) to justify upper bounds. These bounds are explained under [Lower Bounds](#lower-bounds) and [Upper Bounds](#upper-bounds).
* No explanation is given when `n ≤ k` or `k = 2` or the value can be derived from the inequality `T(n,k) ≤ T(n+1,k)`.
* We have the relation `T(n+1,k+1) ≤ T(n,k)` (see [Relations](#relations)). If we use this as an upper bound we write `↖` (the value in this cell is at most the value to the top-left of this cell) and as a lower bound we write `↘` (this value is at least the value to the bottom-right).
* The bolded values indicate perfect solutions (see [Terminology](#terminology)).

## Dual table

| T \ k |  2       |   3         |   4         |   5         |   6         |   7         |  8          |     9       |
|:-----:|----------|-------------|-------------|-------------|-------------|-------------|-------------|-------------|
|   1   |  **2**   |  **3**      |  **4**      |  **5**      |  **6**      |  **7**      |  **8**      | **9**       |
|   2   |    2     |    3     cd |    4     di |    5     di |    6     d  |    7      d |    8      d |   9         |
|   3   |  **4**   |    5 `←` fg |    8 B c`→` |    9 `←` fg |   12  B `→` |   13  `←` f |   16    B`→`|  17   `←` f |
|   4   |    4     |  **9** AH   |   10  `←` g |   12    E e |   18 B gi`→`|   19  `←` g |   22    E g |  27     B i |
|   5   |  **6**   |    9      c | **16**  H a | 17-18 `←` g |   22    E g | 25-26   E g |   32   B gi | 33-34 `←` g |
|   6   |    6     |   12    E a |   16      i | **25** AH a | 26-27 `←` g | 30-32   K g | 32-37     g | 36-42   B g |
|   7   |  **8**   | **15**  F   | 17-20   E c | 25-26     i | 30-34   B h | 31-39  `←`g | 32-45     g | 45-51   B g |
|   8   |    8     |   15      c | 20-24   A a | 25-30     i | 30-38     i | **49** AH a | 50-53 `←` g | 54-59   K g |
|   9   | **10**   |   18    G a | **28**  F a | 29-35 `←` c | 36-42   B i | 49-51     i | **64**  H a | 65-69 `←` g |
|   10  |   10     | **21**  F   |   28      i | 35-40   A a | 42-48  AB i | 49-57     i | 64-67     i | **81**  H a |
|   11  | **12**   |   21      c |   32    G a | 35-45     a | 42-54     c | 49-63     i | 64-73     i | 81-85     i |
|   12  |   12     |   24    G a | 32-36     a | 35-46     i | 48-60   B a | 49-70     i | 64-80     i | 81-92     i |
|   13  | **14**   | **27** AH   | 36-40   G a | 37-50 `←` i |             |             | 72-88   B i | 81-100    i |
|   14  |   14     |   27      c | 36-40     i |             | 66-68   A i | 77-84   A a | 88-96   A i | 99-108  A i |
|   15  | **16**   | 27-30     a |             | 55-60   A a | 66-72     i |             |             | 99-117    i |
|   16  |   16     | **33**  F   | 44-48   A a |             | 66-78     i | 91-93   A i | 104-112 A a | 117-126 A i |
|   17  | **18**   |   33      c |             | 55-66     i | 78-84   A c | 91-99     i |             |             |
|   18  |   18     | 33-36     a |   52    A i | 65-70   A i |             | 91-105    i | 104-123   i |             |
|   19  | **20**   | **39**  F   |             |             |             | 91-112    i | 104-129   i |             |
|   20  |   20     |   39      c |             |             | 78-98     i |             | 104-136   i | 153-157 A i |
|   21  | **22**   | 39-42     a | **64**  H a |             |   102   A i | 119-126 A a | 136-144 A i | 153-164   i |
|   22  |   22     | **45**  A   |   64      i | 85-86   A i | 102-108   i |             | 136-152   i | 153-172   i |
|   23  | **24**   |   45      c |             | 85-90     i |             | 133-135 A i | 152-160 A c | 171-180 A i |
|   24  |   24     | 45-48     a |             |             |             | 133-141   i |             | 171-189   i |
|   25  | **26**   | **51**  J   | 68-76   A   | 95-100  A a | 114-126 A a | 133-147   i |             | 171-198   i |
|   26  |   26     |   51      c | 68-76     i |             | 114-128   i | 133-154   i | 152-179   i |             |
|   27  | **28**   | 51-54     a | 76-80   A a | 95-106    i | 114-132   i |             | 152-185   i | 207-216 A a |
|   28  |   28     | **57**  J   |             | 95-110    i | 114-138   i |             | 184-192 A i |             |
|   29  | **30**   |   57      c |             |  115    A c | 138-144 A c | 161-175 A a | 184-200   i | 207-229   i |
|   30  |   30     | 57-60     a |             |             |             | 161-177   i | 184-208   i | 207-236   i |
|   31  | **32**   | **63**  A   | 76-88     i |**125** AH a |             | 161-183   i |             | 207-244   i |

* An entry in this table shows the maximal `n` such that `T(n,k) ≤ T`. We call this value `n(T,k)`.
* This table has the same information as the previous one, organized differently.
* This table is harder to read, but much more informationally dense.
* If you want to read a value of `T(n,k)` from this table:
  * Look at the `k`-th column.
  * Find the smallest `T` that possibly satisfies `n(T,k) ≥ n`. Then `T(n,k) ≥ T`.
  * Find the smallest `T'` that definitely satisfies `n(T',k) ≥ n`. Then `T(n,k) ≤ T'`.
  * For example, to find `T(14,3)` we see that `T = 7` is the first value where `n(T,3) ≥ 14` (since `n(7,3) = 15`), so `T(14,3) = 7`.
  * For example, to find `T(24,6)`, as of August 2019 we see that `n(5,6)` is in the range `18-24` and `n(6,6)` is in the range `26-30`. We see that `n(5,6) ≥ 24` is possible but not guaranteed and that `n(6,6) ≥ 24` is guaranteed. So `T(24,6)` is either 5 or 6.
  * Using similar logic we can conclude that `T(25,6) = T(26,6) = 6`. Even though the exact values in the table are not known, we do know that `T = 6` is the smallest value where `n(T,6)` is at least `n` (when `n` is 25 or 26).
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
* A *distribution* is a seating assignment for a single meal.
* A *configuration* is an assignment for the *number* of participants to each table for a single meal (but not stating which participant goes where).
* We say that a configuration `C` is dominated if it has two tables with `a` and `b` participants and `a + b ≤ k`.
  * In this case, we can merge these two tables and still have a valid solution, so we may assume we have a solution without dominated configurations.
* A *connection* is a pair of people sitting at the same table. A *new connection* is a connection that was not yet formed on a previous day. The number of connections a table of size `l` makes is `s(l) = l(l-1)/2`, not all of which might be new connections. The number of new connections `s(c)` of a configuration `c` is the sum.
* The *optimal configuration* `opt` is the configuration with the most connections. It has `⌊ n / k ⌋` tables of size `k` and one table of size `n mod k`, and it is unique.
* If `k < n ≤ k^2 - 1` then it is not possible to create `2 * s(opt)` new connections after two days, since at least one pair of participants has to sit at the same table on both days, or a configuration other than the optimal configuration has to be used. Let `s(c1,c2)` the maximum number of new connections `c2` can make on day 2 is `c1` was used on day 1.

## Properties

### Perfect Solutions
* Necessarily, every perfect solution is optimal.
* Necessary requirements for a perfect `(n,k)`-solution to exist are `k - 1 | n - 1` and `k | n` (or `n = 1`).
* A perfect `(n,k)`-solution exists iff `T(n,k) = (n-1)/(k-1)`.
* See [Known Values](#known-values) for some known perfect solutions

### Relations
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
  * If `k` is odd and `n < 2k` then `T(n,k) ≤ 3` is explained by `T(n,k) ≤ T(n-1,k-1) ≤ 3`, using the previous bullet point.
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
* For the other known values, see the tables.

### Lower Bounds
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
  <!-- * For the proof we will use the terminology given under [Solutions for Individual Cases/New terminology](#new-terminology).  -->
  * Note that all non-dominated distributions use 2 or 3 tables.
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
* `g`: Improvement of `a` when `k < n ≤ k^2 - 2`
  * The idea for this lower bound is that every day after the first day many connections are already present on day 1. This means that the number of connections you can make on most (all but one) days is much less than calculated at `a`.
  <!-- * For the explanation we will use the terminology given under [Solutions for Individual Cases/New terminology](#new-terminology). -->
  * On day 1 at most `s(opt)` connections can be added
  * On subsequent days fewer connections can be added. We can give an upper bound, and run through all (sensible) pairs of non-dominated configurations to find the maximal number `s` of connections that can
    be added on day 2 (where we can choose the configuration of day 1 to be as optimal as possible).
  <!-- * Let `d(c1,c2) = sum_{l ∈ c2} s(l) - max(l - |c1|, 0)`. Then `s(c1,c2) ≤ d(c1,c2) ≤ s(c2)`.
  * Conjecture: `s(c1, c2) ≤ d(opt,opt)` whenever `s(c2) ≤ s(c1)` and `c1` and `c2` are non-dominated. (this is true, but I haven't figured out the precise argument yet) -->
  * This means that after `T+1` days at most `s(opt) + T * s` connections can be made, which gives a lower bound for the number of days.
  * The Mathematica function doing this is given in `lowerbound.txt`. It is not optimal, and is not necessarily increasing in `n`. In some cases we can probably increase the lower bound by 1 using a similar but more precise argument.
* `h`: If there is no perfect `(n,k)`-solution but `k | n` and `k - 1 | n - 1`, then `T(n-1, k) > (n - 1) / (k - 1)`.
  * The reason is that if `T(n-1, k) = (n - 1) / (k - 1)` is also given by the lower bound `a`.
  * The only way this solution can work is by making all but 1 table size `k` every meal, and seating every participant exactly once with every other participant.
  * This means that every participant sits at a table of size `k - 1` exactly once.
  * We can add a participant at the empty seat every meal, and then we get a perfect `(n, k)`-solution.
* `i`: Let `n = mk + l`, and let `d` be the lower bound given by `a`. Suppose that `(d-1)(k-1) + (l-1) < n-1`, then there is no solution in `d` days with an optimal configuration.
  * The reason is as follows: Let `A` be any participant sitting at the smallest table in the optimal configuration: it can meet at most `l-1` participants that meal, and at most `k-1` participants every other meal, which is not enough.
  * This means that for any solution in `d` days, the smallest table size is `(n-1)-(d-1)(k-1)`.
  * We can now check whether it is possible to create at least `n(n-1) / 2d` connections in a single day, with this extra condition on the smallest table size. If not, then `T(n,k) > d`.
  * We don't use `i` if `a` or `c` applies. This bound is always at least as strong as `a` or `c`. When `n < k^2` most of the time `g` is stronger.

### Upper Bounds
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
* `F`, `G`, see [Relation to the Social Golfer Problem](#relation-to-the-social-golfer-problem). (We don't use `F` and `G` if another letter applies.)
* `H`, `J`: see [Known Values](#known-values).
* `K`: From a perfect solution, we can get new solutions with the table size two larger.
  * Given an `(n,k)`-solution in `T` days and a subset `A ⊆ n` of participants such that no `i+1` participants from `A` sit at the same table during the same meal (let's say that `A` is `i`-*good* in this case), then there is a `(n+|A|,k+i)`-solution in `T` days, by replacing everyone in `A` with a pair of people.
  * If we start with a perfect `(n,k)`-solution (with `k > 2`) and a 2-good set `A` such that `|A|+(k-2)|A|(|A|-1)/2 < n`, then we can find a 2-good set with one more participant. The reason is that every pair of people in `A` sit at the same table exactly once, with `k-2` other people. Therefore, at most `|A|+(k-2)|A|(|A|-1)/2` other people cannot be added to `A` while keeping `A` 2-good, which means that there is someone we can add to `A` so that the new set is 2-good.


### Relation to the Social Golfer Problem
* The *Social Golfer Problem* is a problem similar to Dagstuhl's Happy Diner Problem: given a group of `m*k` golfers playing in `m` groups of `k` golfers each day. No two golfers play together more than once. What is the maximum possible of days they can play? Call this number `G(m,k)`.
* From a good solution `G(m,k)` of the Social Golfer Problem we can retrieve a `(m*k,k)`-solution to the Happy Diner Problem.
* `F`: There is a perfect `(m*k,k)`-solution iff `G(m,k) = (m*k - 1) / (k - 1)` iff `T(m*k,k) = (m*k - 1) / (k - 1)`.
* `G`: If `G(m,k)*(k-1) = m*k - 2` then `T(m*k,k) = G(m,k) + 1`. This is a lower bound by `a` and a upper bound using the solution to `G(m,k)`: take the solution to `G(m,k)` for the first `G(m,k)` meals. Then everyone has seen all other participants, but 1. For the last meal, have one table for each of the pair of participants which still need to see each other.
* `G`: If `G(m,k)*(k-1) = m*k - 3` then `T(m*k,k) ≤ G(m,k) + 2` (if `k ≥ 3`). After the solution to `G(m,k)` every participant still needs to meet 2 other participants, which can be easily achieved in two days, by splitting everyone up in group of 2 or 3 people.
* A trivial upper bound is `G(m,k) ≤ (mk-1)/(k-1)`. We call a solution to the Social Golfer Problem *good* if it is close to this trivial upper bound.
* See [External Links](#external-links) for more sources on the Social Golfer Problem. In particular many solutions of the Social Golfer Problem can be found in this [Mathematica Demonstration](http://demonstrations.wolfram.com/SocialGolferProblem/).
  * The external links contain the following good solutions: `G(m,k)` is : `G(8,3) = 11` and `G(7,4) = 9` and `G(8,4) = 10` and `G(9,4) = 11`.
  * From this, we conclude `T(24,3) = 12` and `T(28,4) = 9` and `T(32,4)=11` and `12 ≤ T(36,4) ≤ 13`.
* On [Math Stack Exchange](https://math.stackexchange.com/questions/69325/social-golfer-problem-quintets) the following claims are made, but without giving explicit solutions.
  * `G(10,3) = 14` and `G(11,3) = 16` and `G(12,3) = 17`. These solutions would give `T(30,3) = 15` and `T(36,3) = 18`.
  * `G(10,4) = 13` and `G(11,4) = 13` and `G(12,4) ≥ 14` and `G(13,4) = 17`. These solutions would give the two perfect solutions `T(40,4) = 13` and `T(52,4) = 17`.
  * `9 ≤ G(9,5) ≤ 11`.

#### Latin Squares
* The Social Golfer Problem `G(n,n)` is related to finding [mutually orthogonal Latin squares](https://en.wikipedia.org/wiki/Graeco-Latin_square).
  * Let `L(n)` is the maximal number of mutually orthogonal Latin squares of order `n`, that is [`L(n) = A001438(n)`](https://oeis.org/A001438).
  * The relation is `G(n,n) = L(n) + 2`.
    * The reason is that the first two days specify a bijection between the participants and the squares in a `n × n` grid (the cell `(i,j)` corresponds to the participant `p(i,j)` that was in group `i` on day 1 and in group `j` on day 2.)
    * Every day `d ≥ 3` produces a Latin square by putting `k` in cell `(i,j)` if participant `p(i,j)` was in group `k`.
    * The fact that this is a Latin square follows from the fact that no pair of participants was in the same group on day `d`, `1` and `2`.
    * Days `d₁, d₂ ≥ 3` have no pair of participants in the same group iff the corresponding Latin Squares are orthogonal.
  * There is no pair of mutually orthogonal squares of order 6, so `L(6) = 1` and `G(6,6) = 3`. In particular there is no perfect `(36,6)`-solution, so `T(36,6) > 7`.
  * `L(10)` is the smallest unknown value. According to [this Math Stack Exchange answer](https://math.stackexchange.com/q/649893) `L(10) < 9`. This implies that there is no perfect `(100,10)`-solution, so `T(100,10) > 11`.

### Solutions for Individual Cases

* The solution `T(6,3) ≥ 4` is very detailed. Other solutions with the same techniques will have much less explanation. So if you don't understand the reasoning, read `T(6,3) ≥ 4` first (See [Examples](#examples)).
* The code using the Mathematica SAT-solver was written by Michael Trott and optimized by Floris van Doorn.
* If the SAT-solver took longer than ~10s, we write the time as an indication for its difficulty.

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

#### `T(17,4) ≤ 7`
* Solution found by Mathematica SAT-solver:
```
1234 5678 9ABC DEFG H
1469 28EH 7ACG B 35DF
7 48CD 26BF 1AEG 359H
1BDH 8A 6CF 379E 245G
1 45BE 67GH 89DF 23AC
29 CEH 56AD 38BG 147F
36E 158C 9G 27BD 4AFH
```

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
* From then on, at most 19 connections are possible, which has to occur at least once, so day 2 is `(5,5,3)` with `8+8+3` new connections. This can be done in 1 way (up to renaming participants)
* Then there are 8 ways for day 3 to have 18 connections (and more is impossible), possibly counting things twice. We found this number by brute force.
* For none of those 8 ways, there is a valid 4th day.

### `T(22,6) ≤ 5`
* Solution found by Mathematica SAT-solver:
```
123456 789ABC DEFGHI JKLM
458FIM 26ABDK 379GHL 1CEJ
3ABFIJ 45CGHK 18DL 2679EM
45ABEL 3CDM 268GHJ 179FIK
38EK 4579DJ 1ABGHM 26CFIL
```

### `T(25,7) ≤ 5`
* Solution found by Mathematica SAT-solver:
```
235KLP 78BHJM 16ADEG 49CFINO
25EGIJO 1348BFL 6CMNP 79ADHK
47EFGHP 25689B 3ACDJLN 1IKMO
46FJK 8ABDIOP 1257CHN 39EGLM
367HILO 19JP 245ADFM 8BCEGKN
```

### `T(22,8) ≤ 4`
* Solution found by Mathematica SAT-solver:
```
12345678 9ABCDEFG HIJKLM
47ACIK 1369BDHM 258EFGJL
258ACHM 136EFGIK 479BDJL
47EFGHM 136ACJL 2589BDIK
```

### Examples

* Examples of specific upper and lower bounds.
* These all follow from other values or a general principle.
* These were found before we had these general principles, and we did them individually.
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

* This also follows from `T(10,4) ≤ T(9,3) = 4`. ([Relations](#relations) and either `A` or `H`)
* Solution found by hand:
```
1234 5678 90
1259 3670 48
1280 4679 35
045 1267 389
```

#### `T(11,4) ≥ 5`

* This also follows from `g`.
* Suppose there is a solution in 4 days.
* The only configurations which are not dominated are `(4,4,3)` and `(3,3,3,2)`. The first adds at most 15 connections, the second at most 10.
* Therefore, on at least 3 days we need a `(4,4,3)` configuration, WLOG on day 1.
* For the other days any table of size 4 has 1 pair in common with day 1, so adds at most 5 new connections. Therefore, at most 13 new connections can be added during each day.
* This means we cannot get 55 connections, therefore we get a contradiction.

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
* This also follows from `g`.
* Suppose there is a valid solution in 4 days.
* 181 connections have to be made, and at most 45 connections can be made per day, with configuration `(6,6,6,1)`. Every other configuration has at most 41 connections.
* This means that `(6,6,6,1)` has to appear, WLOG on day 1. Now on every other day, the configuration `(6,6,6,1)` can give at most `13+12+12=37` connections, which means that there is no way to get 181 connections in 4 days.

#### `T(21,6) ≤ 5`
* This was found by manually modifying `T(16,4) = 5`, using the same method as `K`.
* `K` only shows that `T(20,6) ≤ 5`.
* If you replace `1H`, `2I`, `5J`, `6K` and `9L` by single participants, you get a perfect `(16,4)`-solution
```
1234HI 5678JK 9ABCL DEFG
179DHL 26AFIK 38CE 45BGJ
18BFH 25CDIJ 37AG 469EKL
15AEHJ 289GIL 36BDK 47CF
16CGHK 27BEI 359FJL 48AD
```

#### `T(14,7) ≥ 4`
* This is a special case of `f`.
* Suppose there is a valid solution in 3 days.
* The configuration `(7,7)` has to occur, since there is no way to make at least 61 connections in 2 days otherwise.
* After `(7,7)` at most 24 connections can be made per day. So there are at most `42 + 24 + 24 = 90 < 91` connections, which is not enough.

#### `T(21,7) ≥ 5`
* This also follows from `T(21,7) ≥ T(20,7) ≥ 5` where the second inequality follows from `g`.
* Suppose there is a valid solution in 4 days.
* 210 connections have to be made, and at most 63 connections can be made per day, with configuration `(7,7,7)`.
* It is impossible to have a non-dominated solution where 5 tables are used every day.
* If `(7,7,7)` appears, WLOG on day 1, then at most 48 connections can be made every other day, but `63+48+48+48=207<210` is not enough.
* If `(7,7,7)` doesn't appear, then every day has 4 tables. Then at most 57 connections can be made on day 1, and at most 49 connections on future days (since all 7s lose at least 3 and all 6s lose at least 2 connections). This is also not enough, since `57+49+49+49=204<210`.

## Questions
* If `n ≡ k mod k(k-1)` and `n` is a prime power, is there always a perfect `(n,k)`-solution? There is no reason to believe this, but it is true for all values where the answer is known.
  * It is false when `n` is not a prime power, where the smallest example is immediately a counterexample: there is no perfect `(36,6)`-solution.
  * It is true for `k = 2` and `k = 3`.
  * For `k = 4` it's true when `n ≤ 28`. If the data on [this Math Stack Exchange page](https://math.stackexchange.com/questions/69325/social-golfer-problem-quintets) is accurate, it is also true `n ≤ 64`.
* For every `n` and `k` is there an optimal `(n,k)`-solution in which, during every meal, at most one table is not completely occupied?
  * This is false. All optimal `(8,5)`-solutions have at least one day with two tables of four participants. This was found by brute force, but is quite easy to see by hand (to do).
  * It is probably even false that there always is an optimal `(n,k)`-solution where there are `⌈ n/k ⌉` tables each day (where `⌈ x ⌉` is the smallest integer which is at least `x`).
    The Mathematica SAT-solver easily found a solution that `T(12,3) ≤ 6`, but didn't terminate within reasonable time when the additional condition was imposed that only 4 tables could be used per day.
* In all cases we know the following holds: if there is a perfect `(n,k)` solution, then `T(n+1,k) = T(n,k) + 2`.
  * Does this always hold? Or maybe `T(n+1,k) ≥ T(n,k) + 2`?

### Conjectures
* `T(n,k) ≤ n/(k-1) + O(1) * log(n)`. This should follow from an inductive argument using `A`.
* For all `k`, `T(n,k) - n/(k-1)` is bounded by a constant (independent of `n`, possibly dependent on `k`).
  * This is true for `k = 3`. In fact, the optimal `(n,3)`-solution is at most 1 higher than the value obtained from the lower bound `c`.
    The reason for this is that for every `m` there is a perfect `(6m+3,3)`-solution (see [Known Values](#known-values)), and the lower bound for `6m-2` given by `c` is only 1 lower than the value for `6m+3`.

## External Links

* Dagstuhl's Happy Diner Problem:
  * We submitted two sequences to the OEIS: [A318240](https://oeis.org/A318240) and [A318241](https://oeis.org/A318241).
  * The problem is stated on [Sarah's Oberwolfach Problem Page](http://facultyweb.kennesaw.edu/shollid4/oberwolfach.php). Finding the perfect `(n,3)`-solutions is a special case of the Oberwolfach Problem.
  * Someone asked the value of `T(18,4) - 1` on [Math Stack Exchange](https://math.stackexchange.com/questions/455459/combinatorics-group-rotation)
* Social Golfer Problem:
  * [Wolfram Mathworld](http://mathworld.wolfram.com/SocialGolferProblem.html)
  * [Warwick's result page (2002)](http://web.archive.org/web/20050308115423/http://www.icparc.ic.ac.uk/~wh/golf/)
  * [Markus Triska's master thesis (2008)](https://www.metalevel.at/sgp/)
  * [Edd Pegg Jr.'s Math Game page (2007)](http://www.mathpuzzle.com/MAA/54-Golf%20Tournaments/mathgames_08_14_07.html)
  * [A107431](https://oeis.org/A107431).
  * [Mathematica Demonstration](http://demonstrations.wolfram.com/SocialGolferProblem/)
  * [Math Stack Exchange](https://math.stackexchange.com/questions/69325/social-golfer-problem-quintets)
  * [This page](https://sci.op-research.narkive.com/48AXUzIj/the-social-golfer-problem-40-golfers-in-groups-of-5-for-8-weeks) contains a solution that `G(8,5) ≥ 8`.
* Kirkman Triple System:
  * [Wolfram Mathworld](http://mathworld.wolfram.com/KirkmanTripleSystem.html),
  * [Dutch dissertation by Pieter Mulder (1917)](https://babel.hathitrust.org/cgi/pt?id=njp.32101065911230;view=1up;seq=19).
  * *Solution of Kirkman's schoolgirl problem*, Ray-Chaudhuri and Wilson, 1971. In [Proc. of Symp. in Pure Math, Vol 19](http://www.ams.org/books/pspum/019/).
  * *Kirkman triple systems and their generalizations: A survey*, Rees and Wallis, 2002. [Springer](https://link.springer.com/chapter/10.1007/978-1-4613-0245-2_13)
* Oberwolfach Problem: [Sarah's Oberwolfach Problem Page](http://facultyweb.kennesaw.edu/shollid4/oberwolfach.php).


## Contributing

* Contributions are welcome! Feel free to add any information. Please provide links or justifications of claims you make.