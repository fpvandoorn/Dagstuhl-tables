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
|   4   |  **3**   |    3   c   |  **1**     |    1       |    1       |    1       |    1       |
|   5   |    5     |    3   `↖` |    3   di  |  **1**     |    1       |    1       |    1       |
|   6   |  **5**   |    4   fg  |    3       |    3   di  |  **1**     |    1       |    1       |
|   7   |    7     |    4       |    3       |    3       |    3   d   |  **1**     |    1       |
|   8   |  **7**   |    4       |    3     B |    3       |    3       |    3   d   |  **1**     |
|   9   |    9     |  **4**  AH |    4   `↘` |    3   `↖` |    3       |    3       |    3   d   |
|   10  |  **9**   |    6   c   |    4   `↖` |    4   fg  |    3       |    3       |    3       |
|   11  |   11     |    6       |    5   g   |    4       |    3       |    3       |    3       |
|   12  | **11**   |    6     E |    5       |    4       |    3     B |    3       |    3       |
|   13  |   13     |    7   a   |    5       |    4     E |    4  `↘`  |    3   `↖` |    3       |
|   14  | **13**   |    7       |    5       |    5   g   |    4       |    4 fg    |    3       |
|   15  |   15     |  **7**   F |    5       |    5       |    4       |    4       |    3       |
|   16  | **15**   |    9   c   |  **5**   H |    5       |    4       |    4       |    3     B |
|   17  |   17     |    9       |    7   i   |    5   `↖` |    4       |    4       |    4  `↘`  |
|   18  | **17**   |    9     G |    7       |    6   j   |    4     B |    4       |    4       |
|   19  |   19     |   10   a   |    7       |    6       |    5 gi`↘` |    4   `↖` |    4       |
|   20  | **19**   |   10       |    7     X |    6       |    5       |    5 g     |    4       |
|   21  |   21     | **10**   F |    8   c   |    6       |    5       |    5       |    4       |
|   22  | **21**   |   12   c   |    8       |    6       |    5     L |    5       |    4     E |
|   23  |   23     |   12       |    8       |    6       |    6   g   |    5       |    5   g   |
|   24  | **23**   |   12     J |    8     J |    6       |    6       |    5       |    5       |
|   25  |   25     |   13   a   |    9   a   |  **6**  AH |    6       |    5     E |    5       |
|   26  | **25**   |   13       |    9       |   7-8  a E |    6   `↖` |    6  j    |    5       |
|   27  |   27     | **13**  AH |    9       |   8-9  i   |   6-7      |    6       |    5       |
|   28  | **27**   |   15   c   |  **9**   F |   8-9      |    7   g   |    6       |    5       |
|   29  |   29     |   15       |   11   i   |   8-9      |    7       |    6       |    5       |
|   30  | **29**   |   15     J |   11     G |   8-9    X |    7   B   |    6     E |    5     B |

Legend:
* We use lower-case letters `a`-`z` (or `↘`) to justify lower bounds and upper-case letters `A`-`Z` (or `↖`) to justify upper bounds. These bounds are explained under [Lower Bounds](#lower-bounds) and [Upper Bounds](#upper-bounds).
* No explanation is given when `n ≤ k` or `k = 2` or the value can be derived from the inequality `T(n,k) ≤ T(n+1,k)`.
* We have the relation `T(n+1,k+1) ≤ T(n,k)` (see [Relations](#relations)). If we use this as an upper bound we write `↖` (the value in this cell is at most the value to the top-left of this cell) and as a lower bound we write `↘` (this value is at least the value to the bottom-right).
* The bolded values indicate perfect solutions (see [Terminology](#terminology)).
* The upper bound `J` has not been verified by the authors of this table.

## Dual table
<!-- Todo: update lower bounds in columns 10+ -->
| T \ k |  2       |   3         |   4         |   5         |    6        |    7        |   8         |    9        |   10        |   11        |   12        |
|:-----:|----------|-------------|-------------|-------------|-------------|-------------|-------------|-------------|-------------|-------------|-------------|
|   1   |  **2**   |  **3**      |  **4**      |  **5**      |  **6**      |  **7**      |  **8**      | **9**       | **10**      | **11**      | **12**      |
|   2   |    2     |    3     c  |    4     di |    5     di |    6     d  |    7      d |    8      d |   9       d |  10       d |  11       d |  12       d |
|   3   |  **4**   |    5 `←` fg |    8 B c`→` |    9 `←` fg |   12  B `→` |   13 `←` fg |   16    B`→`|  17  `←` fg |  20     B`→`|  21  `←` fg |  24     B`→`|
|   4   |    4     |  **9** AH   |   10  `←` g |   13    E g |   18 B gi`→`|   19  `←` g |   22    E g |  27     B i |  28    `←`g | 29-31 `←` g |             |
|   5   |  **6**   |    9      c | **16**  H   |   17  `←` j |   22    L g |   25    E j |   32   B gi |  33   `←` j |  38     L g | 39-41 `←` j |             |
|   6   |    6     |   12    E a |   16      i | **25** AH a | 26-27 `←` g | 31-32   E g | 32-37     g | 41-42   E g |  50     B g | 51-52 `←` g |             |
|   7   |  **8**   | **15**  F   |   20    X c | 25-26     i | 30-34   B h | 31-38  `←`j | 32-44     j | 45-50   B j |  50-56    j | 51-63     g |             |
|   8   |    8     |   15      c |   24    J a | 26-30   E i | 36-38   E i | **49** AH a | 50-52 `←` g | 54-59   K g |  55-66 `←`g | 56-73 `←` g |             |
|   9   | **10**   |   18    G a | **28**  F   | 30-35   X c | 36-42     i | 49-51     i | **64**  H a | 65-68 `←` g |  66-75 `←`j | 67-84 `←` g |             |
|   10  |   10     | **21**  F   |   28      i | 35-40   A a | 42-48  AB i | 49-57     i | 64-67     i | **81**  H a |  82-86 `←`g | 83-94 `←` g |             |
|   11  | **12**   |   21      c |   32    G a | 35-45     a | 42-54     c | 49-63     i | 64-73     i | 81-85     i |             |             |             |
|   12  |   12     |   24    J a |   36    J a | 37-46 `←` i | 48-60   B a | 49-70     i | 64-80     i | 81-92     i |             |**121** AH a |             |
|   13  | **14**   | **27** AH   | **40**  F   | 41-50 `←` i |             |             | 72-88   B i | 81-100    i |             |             |             |
|   14  |   14     |   27      c |   40      i |             | 66-68   A i | 77-84   A a | 88-96   A i | 99-108  A i |             |             |             |
|   15  | **16**   |   30    J a |             | 55-60   A a | 66-72     i |             |             | 99-117    i |             |             |             |
|   16  |   16     | **33**  J   |   48    J a | **65**  F a | 66-78     i | 91-93   A i | 104-112 A a | 117-126 A i |             |             |             |
|   17  | **18**   |   33      c | **52**  F   | 65-66     i | 78-84   A c | 91-99     i |             |             |             |             |             |
|   18  |   18     |   36    J a |   52      i | 65-70     i |             | 91-105    i | 104-123   i |             |             |             |             |
|   19  | **20**   | **39**  J   |             |             |             | 91-112    i | 104-129   i |             |             |             |             |
|   20  |   20     |   39      c |   60    J a |             | 78-98     i |             | 104-136   i | 153-157 A i |             |             |             |
|   21  | **22**   |   42    J a | **64**  H   | **85**  J a |   102   A i | 119-126 A a | 136-144 A i | 153-164   i |             |             |             |
|   22  |   22     | **45**  A   |   64      i | 85-86     i | 102-108   i |             | 136-152   i | 153-172   i |             |             |             |
|   23  | **24**   |   45      c |             | 85-90     i |             | 133-135 A i | 152-160 A c | 171-180 A i |             |             |             |
|   24  |   24     |   48    J a |   72    J a |             |             | 133-141   i |             | 171-189   i |             |             |             |
|   25  | **26**   | **51**  J   | **76**  J   | 95-100  A a | 114-126 A a | 133-147   i |             | 171-198   i |             |             |             |
|   26  |   26     |   51      c |   76      i | **105** J a | 114-128   i | 133-154   i | 152-179   i |             |             |             |             |
|   27  | **28**   |   54    J a |             | 105-106   i | 114-132   i |             | 152-185   i | 207-216 A a |             |             |             |
|   28  |   28     | **57**  J   |             | 105-110   i | 114-138   i |             | 184-192 A i |             |             |             |             |
|   29  | **30**   |   57      c | **88**  J   |  115    A c | 138-144 A c | 161-175 A a | 184-200   i | 207-229   i |             |             |             |
|   30  |   30     |   60    J a |   88      i |             |             | 161-177   i | 184-208   i | 207-236   i |             |             |             |
|   31  | **32**   | **63**  A   |             |**125** AH a |             | 161-183   i |             | 207-244   i |             |             |             |

* **Dual problem statement**: What is the maximum number of conference participants so that each participant can share at least one of the `T` meals with any other participant when eating at tables of at most `k` participants?
* This is the maximal `n = n(T,k)` such that `T(n,k) ≤ T`.
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
* The upper bound `J` has not been verified by the authors of this table.

## Terminology

* Given a table assignment for 1 or more meals. We say that this is a *valid solution* if every participant meet every other participant at least once.
* A valid solution with `n` participants and table size of at most `k` is called a `(n,k)`-*solution*.
* Given a valid solution. We say that it is an *optimal solution* if there is no valid solution (with the same `n` and `k`) with fewer days.
* Given a valid solution. We say that it is a *perfect solution* if every participant meets every other participant exactly once and all tables have `k` participants every meal.
* A *distribution* is a seating assignment for a single meal.
* A *configuration* is an assignment for the *number* of participants to each table for a single meal (but not stating which participant goes where).
* We say that a configuration `C` is dominated if it has two tables with `a` and `b` participants and `a + b ≤ k`.
  * In this case, we can merge these two tables and still have a valid solution, so we may assume we have a solution without dominated configurations.
* A *connection* is a pair of people sitting at the same table. A *new connection* is a connection that was not yet formed on a previous day. The number of connections a table of size `l` makes is `s(l) = l(l-1)/2`, not all of which might be new connections. The number of new connections `s(c)` of a configuration `c` is the sum.
* The *optimal configuration* `opt` is the configuration with the most connections. It has `⌊ n / k ⌋` tables of size `k` and one table of size `n mod k`, and it is unique.
* If `k < n ≤ k^2 - 1` then it is not possible to create `2 * s(opt)` new connections after two days, since at least one pair of participants has to sit at the same table on both days, or a configuration other than the optimal configuration has to be used. Let `s(c1,c2)` the maximum number of new connections `c2` can make on day 2 is `c1` was used on day 1.

## Properties

### Relations
* `T(n+1,k) ≥ T(n,k) ≥ T(n+1,k+1) ≥ T(n,k+1)`.
  * If a value in the table can be derived from the first inequality, no other explanation is given.
  * The second inequality follows by treating two of the `n+1` people as a single person (always seating them together), and then applying a `(n,k)`-solution.
* `T(n,k) ≤ T(n,m) * T(m,k)`.
  * If we have a seating arrangement for `n` participants at table size `m`, then we can give a seating arrangement for table size `k` by simulating tables of size `m` over `T(m,k)` meals.
  * This subsumes the relation `T(n+1,k) ≥ T(n,k) ≥ T(n,k+1)` above since `T(k,k+1)=1`.
  * If there is a perfect `(n,m)`-solution and a perfect `(m,k)`-solution then there is a perfect `(n,k)`-solution.

### Perfect Solutions
* Necessarily, every perfect solution is optimal.
* Necessary requirements for a perfect `(n,k)`-solution to exist are `k - 1 | n - 1` and `k | n` (or `n = 1`), i.e. `n ≡ k (mod k(k-1))`.
* A perfect `(n,k)`-solution exists iff `T(n,k) = (n-1)/(k-1)`.
* The perfect solutions are in boldface in the tables above.
* Perfect solutions are also called *Kirkman Systems* in the literature.
* Perfect solutions are also characterized by [the Social Golfer Problem](#relation-to-the-social-golfer-problem) or [resolvable 2-designs](#relation-to-block-designs).
* We give various explicit perfect solutions in [literature.md](literature.md)
* The upper bounds `F`, `H` and (some of) `J` all give families of perfect solutions.

### Special Cases
* `T(n,k) = 1` if `n ≤ k` trivially.
* `T(n,2) = n` if `n` is odd, `T(n,2)=n-1` if `n` is even.
  * The lower bound is given by `a`.
  * The upper bound can be obtained as follows.
    * Suppose `n = 4m`: split it up in 2 groups of size `2m`, first do those groups independently in `2m-1` days, then in the next `2m` days on day `i` let person `j` in group 1 sit with person `i+j (mod 2m)` in group 2.
      * This also follows from upper bound `A`.
    * Suppose `n = 2m` with `m` odd:
      * For the first `m` days: on day `i` let person `i` sit with `i+m` and person `i+j` with `i-j`.
      * For the next `m-1` days, on day `2k-1` and `2k` let person `i` sit with the persons `i+2k-1` and `i-(2k-1)`. If `i` is even it will sit with `i+2k-1` first, and if `i` is odd it will sit with `i-(2k-1)` first.
    * Suppose `n` is odd, then we can use the solution for `n+1` participants.
* If `k` is even and `k < n ≤ 2k` then `T(n,k) = 3`. Also, if `k` is odd and `k < n < 2k` then `T(n,k) = 3`. These are *all* the values for `(n,k)` where `T(n,k) = 3`.
  * If `n > k` then `T(n,k) ≥ 3` is explained by the lower bound `d`.
  * If `k` is even and `n ≤ 2k` then `T(n,k) ≤ 3` is explained by the upper bound `B`.
  * If `k` is odd and `n < 2k` then `T(n,k) ≤ 3` is explained by `T(n,k) ≤ T(n-1,k-1) ≤ 3`, using the previous bullet point.
  * For smaller `n` we have `T(n,k) = 1` trivially and for larger `n` we have `T(n,k) ≥ 4` by lower bound `f`.

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
* `e`: proven for this special case, see below.
* `f`: If `k` is odd then `T(2k,k) ≥ 4`.
  * This is likely a special case of `g`.
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
  <!-- Double check: Did we compute reason about this correctly, also considering the possibility that the optimal distribution is never used? -->
  <!-- * Let `d(c1,c2) = sum_{l ∈ c2} s(l) - max(l - |c1|, 0)`. Then `s(c1,c2) ≤ d(c1,c2) ≤ s(c2)`.
  * Conjecture: `s(c1, c2) ≤ d(opt,opt)` whenever `s(c2) ≤ s(c1)` and `c1` and `c2` are non-dominated. (this is true, but I haven't figured out the precise argument yet) -->
  * This means that after `T+1` days at most `s(opt) + T * s` connections can be made, which gives a lower bound for the number of days.
  * The Python program that is part of `dagstuhl.py` tries to compute a better lower bound (an older, worse Mathematica function computing this is given in `lowerbound.txt`.)
* `h`: If there is no perfect `(n,k)`-solution but `k | n` and `k - 1 | n - 1`, then `T(n-1, k) > (n - 1) / (k - 1)`.
  * To see this, first notice that `T(n-1, k) ≥ (n - 1) / (k - 1)` is given by the lower bound `a`.
  * The only way equality can hold is if all but 1 table has size `k` every meal, and seating every participant exactly once with every other participant.
  * This means that every participant sits at a table of size `k - 1` exactly once.
  * We can add a participant at the empty seat every meal, and then we get a perfect `(n, k)`-solution, which contradicts the assumption.
  * For `(n,k) = (36,6)` there is no perfect solution, see [Latin Squares](#latin-squares).
* `i`: Let `n = mk + l`, and let `d` be the lower bound given by `a`. Suppose that `(d-1)(k-1) + (l-1) < n-1`, then there is no solution in `d` days with an optimal configuration.
  * The reason is as follows: Let `A` be any participant sitting at the smallest table in the optimal configuration: it can meet at most `l-1` participants that meal, and at most `k-1` participants every other meal, which is not enough.
  * This means that for any solution in `d` days, the smallest table size is `(n-1)-(d-1)(k-1)`.
  * We can now check whether it is possible to create at least `n(n-1) / 2d` connections in a single day, with this extra condition on the smallest table size. If not, then `T(n,k) > d`.
  * We don't use `i` if `a` or `c` applies. This bound is always at least as strong as `a` or `c`. When `n < k^2` most of the time `g` is stronger.
* `j`:
  * If `k < n ≤ k^2 - 2` and the lower bound by `g` gives a number of days where `s(opt) + T * s = n(n-1)/2`, then all connections starting at day 2 have to be optimal.
  * This is is usually impossible, so that 1 more day is needed.
  * If every day uses the same configuration (which is usually/always the case under the assumption above), then this means that participants that sat together on both days 1 and 2 will sit together every day. The reason is that every day requires the least number of duplicated connections, and the duplicated connections between day 2 and n must be a subset of the duplicated connections between day 1 and n (otherwise day `n` will form fewer new connections than required, because there is distinct overlap with day 1 and day 2). This means that those groups sit together every day.
  * When we quotient by the groups (i.e. consider the groups as single participants) we get an `(n', k')`-solution for `n' < n` and `k' < k`. We get a contradiction if such a solution doesn't exist. We can also compute how often groups of a particular size will meet, or how often a group that sat at a particular table on day 1 will meet other groups of a certain size. This often leads to contradictions, which are described below.
  * We can also replace all groups of size `l` by groups of size `l'`, which leads to a contradiction for e.g. `T(42, 11)`.
  * For `T(18,5)` we work out this argument in detail:
    * There are 153 connections to be made, and the only configurations with at least 30 connections are `s(5553)=33` and `s(5544)=32`.
    * If `5553` is never used, then since `s(5544,5544) = 30`, the maximum number of connections is `32+4*30<153`, so this is impossible
    * So assume day 1 is `5553` and note that `s(5553,5553)=30>s(5553, 5544)`. This means that every day must be `5553`, and every table with 5 participants must create 9 new connections after day 1.
    * Given a table of size 5 on day 5, then for every previous day, 2 people already sat together. Since 9 new connections must be formed, this means that 2 people sat together for all 5 meals. Hence there must be 3 pairs of people that sat together every day.
    * There must be a table where 2 such pairs meet. If this is not on day 1, such a table creates at most 8 new connections, which is a contradiction. Hence there is a table on day 1 without any of the pairs. This table must contain 2 people that also sit together on day 5, contradiction.
    * SAT-solvers can do this with quite some effort (~2 minutes assuming the configuration `5553` exists?).
  * For `T(26,7)`, the only way we can form the required 325 connection in 5 days is to use the optimal configuration `7775` every day, and to form 73 connections on day 1 and 63 connections on days 2-5 (there must be at least 10 duplicate connections). This means that 10 pairs must always sit together, and 3 tables must contain always 3 pairs, and 1 table always 1 pair. This means that 5 pairs only sit on tables with 2 other pairs and 1 single participant, so they will meet 10 pairs and 5 single participants, but they need to meet 9 pairs and 7 single participants. So it's impossible in 5 days.
  * `T(34,9) > 5`, because otherwise the configuration `9997` must always be used and there must be 3 triples that always sit together on a table of size 9, but the different triples can never meet
  * `T(39,7) > 7` because otherwise we need configuration `777774` every day, with 6 pairs always sitting together spread over the 5 tables of size 7. These pairs can only have 7 meetings, while 15 are required.
  * `T(45,8) > 7`, because otherwise we need configuration `888885` every day, with 10 pairs always sitting together. These pairs only have 35 meetings, while 45 are required.
  * `T(51,9) > 7`, because otherwise we need configuration `999996` every day, with 15 pairs always sitting together. If we collapse these 15 pairs to single participants, we would get a solution to `T(36,6)=7` which doesn't exist. This argument also works for `T(57,10) > 7`.
  * `T(76,10) > 9`, because otherwise we need configuration `10,10,10,10,10,10,10,6` every day, with 15 pairs always sitting together. These pairs only have 81 meetings, while 105 are required.
  * `T(42,11) > 5`, because otherwise we need configuration `11,11,11,9` every day, and the groups consist of 10 triples and 6 pairs. Reducing the size of each group by 1, this would lead to a `(26, 7)`-solution, which is impossible.
  * On the other hand, `T(38,10) = 5` and `T(22,6) = 5` are possible (see `L`).
* `k` (currently unused): If `k < n ≤ k^2 - 2` and the lower bound by `g` gives a number of days where `d := d(n, k) := s(opt) + T * s - n(n-1)/2` is only slightly larger than 0, we can hopefully still sometimes derive a contradiction.
  * Promising candidates are `d(27, 6) = 2`, `d(32, 7) = 4`, `d(37, 8) = 6`, `d(42, 9) = 8`, `d(59, 9) = 6`, `d(86, 10) = 5`.

  <!-- same argument likely holds for T(26,7), T(34,6), T(39,7), T(45,8), T(34,9), T(51,9) -->
  <!-- `T+1 > 2` and for any possible configuration starting at day 2, there are at least two tables with `k` participants and less than `k` tables. -->
  <!-- No! consider T(50,10) FIXME -->
* Priority of labels: nothing (it follows from the cell above), then `↘`/`→`, then `a`/`c`, then `d`/`f`/`h`/`i`, then `g`/`j`, then `e`
  * If a label with earlier (higher) priority applies, we don't write this label. We do write multiple labels with the same priority.

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
* `F`, `G`, `X`: a solution has been elsewhere, usually in articles. An explicit solution is given in [literature.md](literature.md).
  * See [Relation to the Social Golfer Problem](#relation-to-the-social-golfer-problem).
  * See [Relation to Block Designs](#relation-to-block-designs).
  * `X`: Some solutions were given on Stack Exchange.
* `H`: If `k` is a prime power and `n` is a power of `k`, then there is a perfect `(n,k)`-solution.
  * Consider the field `F` of order `k`, and a vector field `V` with cardinality `n` over `F`.
  * For every 1-dimensional subspace `L` of `V` the sets of 1-dimensional affine spaces parallel to `L` forms a partition of `V`. This defines a table assignment for a single meal.
  * The set of all table assignments determined by all 1-dimensional subspaces in this way forms a perfect `(n,k)`-solution. The reason that it is perfect follows from the fact that 1-dimensional affine spaces stand in bijective correspondence to pairs of points in `V`.
  * This idea is due to Neil Strickland.
  * If `k` is prime (not just a prime power) and `n` is a power of `k`, then the existence of a perfect `(n,k)`-solution also follows from upper bound `A`.
* `J`: see [Kirkman Systems](#kirkman-systems) and [Relation to Block Designs](#relation-to-block-designs).
* `L`:
  * Given an `(n,k)`-solution in `T` days and a subset `A ⊆ n` of participants. We say that `A` is `i`-*good* if no `i+1` participants from `A` sit at the same table during the same meal.
  * Given an `i`-good set `A` with `m` elements, and `b ≥ 1`, `c ≥ 0`, then there is a `(bn+cm,bk+ci)`-solution in `T` days, by replacing everyone not in `A` by `b` people and everyone in `A` with `b + c` people, that always sit together.
  * For `c = 0` this gives back upper bound `B`.
  * There is a `(16,4)`-solution with a 6-element 2 good set (take the solution to `T(22,6)` given explicitly below and let `A` be the set of 6 pairs that always sit together). Therefore (taking `c = 1`) we have `T(16b+6,4b+2) ≤ 5`.
* `K`: From a perfect solution, we can get new solutions with the table size two larger.
  * If we start with a perfect `(n,k)`-solution (with `k > 2`) and a 2-good set `A` (see upper bound `L`) such that `|A|+(k-2)|A|(|A|-1)/2 < n`, then we can find a 2-good set with one more participant. The reason is that every pair of people in `A` sit at the same table exactly once, with `k-2` other people. Therefore, at most `|A|+(k-2)|A|(|A|-1)/2` other people cannot be added to `A` while keeping `A` 2-good, which means that there is someone we can add to `A` so that the new set is 2-good.
<!-- * `X`: unverified solutions from [the Social Golfer Problem](#relation-to-the-social-golfer-problem). -->
* Priority of labels: nothing (it follows from the cell below), then `↖`/`←`, then `A`/`B`/`H`/`K`, then `L`, then `F`/`G`, then `E`/`X`, then `J`.
  * If a label with earlier (higher) priority applies, we don't write this label. We do write multiple labels with the same priority.

<!-- TODO: refactor next 4 sections into "Literature", maybe separate sections for perfect solutions -->

### Literature

#### Relation to the Social Golfer Problem
* The *Social Golfer Problem* is a problem similar to Dagstuhl's Happy Diner Problem: given a group of `m*k` golfers playing in `m` groups of `k` golfers each day. No two golfers play together more than once. What is the maximum possible of days they can play? Call this number `G(m,k)`.
* From a good solution `G(m,k)` of the Social Golfer Problem we can retrieve a `(m*k,k)`-solution to the Happy Diner Problem.
* `F`: There is a perfect `(m*k,k)`-solution iff `G(m,k) = (m*k - 1) / (k - 1)` iff `T(m*k,k) = (m*k - 1) / (k - 1)`.
* `G`: If `G(m,k)*(k-1) = m*k - 2` then `T(m*k,k) = G(m,k) + 1`. This is a lower bound by `a` and a upper bound using the solution to `G(m,k)`: take the solution to `G(m,k)` for the first `G(m,k)` meals. Then everyone has seen all other participants, but 1. For the last meal, have one table for each of the pair of participants which still need to see each other.
* `G`: If `G(m,k)*(k-1) = m*k - 3` (and `k ≥ 3`) then `T(m*k,k) ≤ G(m,k) + 2`. After the solution to `G(m,k)` every participant still needs to meet 2 other participants, which can be easily achieved in two days, by splitting everyone up in group of 2 or 3 people.
* We only use the letters `F` and `G` if we could find an explicit, valid solution.
* A trivial upper bound is `G(m,k) ≤ (mk-1)/(k-1)`. We call a solution to the Social Golfer Problem *good* if it is close to this trivial upper bound.
* See [External Links](#external-links) for more sources on the Social Golfer Problem. In particular many solutions of the Social Golfer Problem can be found in this [Mathematica Demonstration](http://demonstrations.wolfram.com/SocialGolferProblem/).
  * The external links contain the following good solutions (only solutions that give new results for the Dagstuhl Happy Dinner Problem are included here). Explicit solutions are given in [literature.md](literature.md).
    * `G(5,3) = 7` gives `T(15,3) = 7` ([MD](http://demonstrations.wolfram.com/SocialGolferProblem/)).
    * `G(6,3) = 8` gives `T(18,3) = 9` ([MD](http://demonstrations.wolfram.com/SocialGolferProblem/)).
    * `G(7,3) = 10` gives `T(21,3) = 10` ([MD](http://demonstrations.wolfram.com/SocialGolferProblem/)).
    * `G(11,3) = 16` gives `T(33,3) = 16` ([Survey](https://www.jstor.org/stable/1402466)).
    * `G(7,4) = 9` gives `T(28,4) = 9` ([MD](http://demonstrations.wolfram.com/SocialGolferProblem/)).
    * `G(8,4) = 10` gives `T(32,4) = 11` ([MD](http://demonstrations.wolfram.com/SocialGolferProblem/)).
    * `G(10,4) = 13` gives `T(40,4) = 13` ([Survey](https://www.jstor.org/stable/1402466)).
    * `G(13,4) = 17` gives `T(52,4) = 17` ([CRCB](https://www.sciencedirect.com/science/article/pii/S0097316598929247)).
    * `G(13,5) = 16` gives `T(65,5) = 16` ([Survey](https://www.jstor.org/stable/1402466)).
  * Many of these solutions are also found in the literature, see `J`.
<!-- * `X`: A reasonable claim about the Social Golfer Problem has been made, but without an explicit solution.
  * On [Math Stack Exchange](https://math.stackexchange.com/questions/69325/social-golfer-problem-quintets) the claims `G(10,3) = 14` and `G(12,3) = 17` are made, but without giving explicit solutions. These solutions give `T(30,3) = 15` and `T(36,3) = 18`.
  * ([MD](http://demonstrations.wolfram.com/SocialGolferProblem/) and [MG](http://www.mathpuzzle.com/MAA/54-Golf%20Tournaments/mathgames_08_14_07.html) claim that `G(8,3) = 11`, but don't give a valid solution. -->

#### Kirkman Systems

* `J`: A perfect `(n,3)`-solution for `n ≥ 3` is called a *Kirkman Triple System* and is possible iff `n ≡ 3 mod 6`.
  * This is proven in *Solution of Kirkman's schoolgirl problem*, Ray-Chaudhuri and Wilson (1971).
  * This shows that `G(2k+1,3) = 3k+1`.
  * Together with lower bound `a`, this gives that `T(6k+1,3) = T(6k+2,3) = T(6k+3,3) = 3k+1`.
* `J`: The optimal `(6m,3)`-solution for `m > 1` has `3m` days.
  * This follows from the study of *Nearly Kirkman Triple Systems*.
  * A Nearly Kirkman Triple System is a `(6m,3)`-solution in `3m` days where on the first `3m-1` days, all tables have 3 participants, and on the last day every table has 2 participants. In such a solution, all participants meet all other participants exactly once.
  * A Nearly Kirkman Triple Systems exists for `6m ≥ 18`.
    * [ANKS](http://engine.scichina.com/publisher/scp/journal/Math%20A1/37/5/10.1360/ya1994-37-5-555?slug=abstract) states this and gives references.
  * For `6m = 12` there is a optimal `(12,3)`-solution in 6 days which is not a Nearly Kirkman Triple System. (see `E`)
* `J`: A *Kirkman System* is an alternative name for an optimal solution.
  * According to [On resolvable designs](https://www.sciencedirect.com/journal/discrete-mathematics/vol/3/issue/4) they exist for all `(n,4)` with `n ≡ 4 mod 12`.
  * [ANKS](http://engine.scichina.com/publisher/scp/journal/Math%20A1/37/5/10.1360/ya1994-37-5-555?slug=abstract) cites papers that show that for every `k` there is a Kirkman System for all but finitely many `n ≡ k mod k(k-1)`.
* `J`: A *Nearly Kirkman System* is an `(n,k)`-solution where all participants meet each other exactly once, on all but 1 days all tables contain `k` participants and on the last day all tables contain `k-1` participants.
  * A necessary condition for a Nearly Kirkman System is that `n ≡ 0 mod k(k-1)`.
  * If a Nearly Kirkman System exists for `(n,k)` then `T(n,k) = n / (k-1)`
  * [ANKS](http://engine.scichina.com/publisher/scp/journal/Math%20A1/37/5/10.1360/ya1994-37-5-555?slug=abstract) proves that for every `k` there is a Nearly Kirkman System for all but finitely many `n ≡ 0 mod k(k-1)`.
  * It also states that for `k = 4` and `n ≡ 0 mod 12` there is a Nearly Kirkman System for all `n`, except possibly for `n` in `{12, 84, 132, 264, 372, 456, 552, 660, 804, 852}`

#### Latin Squares
* The Social Golfer Problem `G(n,n)` is related to finding [mutually orthogonal Latin squares](https://en.wikipedia.org/wiki/Graeco-Latin_square).
  * Let `L(n)` is the maximal number of mutually orthogonal Latin squares of order `n`, that is [`L(n) = A001438(n)`](https://oeis.org/A001438).
  * The relation is `G(n,n) = L(n) + 2`.
    * The reason is that the first two days specify a bijection between the participants and the squares in a `n × n` grid (the cell `(i,j)` corresponds to the participant `p(i,j)` that was in group `i` on day 1 and in group `j` on day 2.)
    * Every day `d ≥ 3` produces a Latin square by putting `k` in cell `(i,j)` if participant `p(i,j)` was in group `k`.
    * The fact that this is a Latin square follows from the fact that no pair of participants was in the same group on day `d`, `1` and `2`.
    * Days `d₁, d₂ ≥ 3` have no pair of participants in the same group iff the corresponding Latin Squares are orthogonal.
  * There is no pair of mutually orthogonal squares of order 6, so `L(6) = 1` and `G(6,6) = 3` ([OEIS](https://oeis.org/A001438)). In particular there is no perfect `(36,6)`-solution, so `T(36,6) > 7`.
  * `L(10)` is the smallest unknown value. According to [this Math Stack Exchange answer](https://math.stackexchange.com/q/649893) `L(10) < 9`. This implies that there is no perfect `(100,10)`-solution, so `T(100,10) > 11`.

#### Relation to Block Designs
* A [resolvable 2-`(n,k,1)` design](https://en.wikipedia.org/wiki/Block_design#Resolvable_2-designs) is an equivalent characterization of a perfect `(n,k)`-solution. This is also called a `(n,k,1)`-RBIBD (resolvable balanced incomplete block design).
  * It is a special case of a [BIBD (or 2-design)](https://en.wikipedia.org/wiki/Block_design#Definition_of_a_BIBD_(or_2-design)) with `(v,b,r,k,λ) = (n,b,r,k,1)` (where `b = n(n-1)/(k(k-1))` and `r = (n-1)/(k-1)`).
    * This 2-design is equivalently characterized as the [Steiner System](https://en.wikipedia.org/wiki/Steiner_system) `S(2,k,n)`.
  * `J`: In [RBIBD5](http://ajc.maths.uq.edu.au/pdf/15/ajc-v15-p177.pdf) it is shown that a `(n,5,1)`-RBIBD exists for all `n ≡ 5 mod 20`, except possibly for `n` in `{45, 185, 225, 345, 465, 645}`.
* A `(K,λ)`-RGDD (resolvable group divisible design) is a generalization, where the participants are partitioned in groups, and every pair of participants from two different groups meet exactly `λ` times and every pair of distinct participants from the same group never meet. The table sizes must all be in the set `K`.
  * Dagstuhl's Happy diner problem asks to find a `({1,...,k},1)`-GDD but where participants can meet each other multiple times.
  * Many solutions to `(K,1)`-RGDDs will give solutions to Dagstuhl's Happy Diner problem.
    * If all groups have size 1, then the solution is immediate.
    * If all groups are size `≤ k` then we get an solution by adding 1 day where all participants meet everyone in their group.

### Solutions for Individual Cases

* The solution `T(6,3) ≥ 4` is very detailed. Other solutions with the same techniques will have much less explanation. So if you don't understand the reasoning, read `T(6,3) ≥ 4` first (See [Examples](#examples)).
* See [here](sat.md) for instructions/information about the SAT-solvers used in this project. The indicated time is the fastest time we found (always produced by the most efficient script).

#### `T(12,3) ≤ 6`
* Solution found by SAT-solvers:
```
159 278 3AC 46B
12C 345 8AB 679
12B 348 79A 56C
168 25A 39B 47C
14A 236 57B 89C
137 249 BC 58 6A
```
* kissat took 0.1s on a laptop
<!--
0.2s for s = 5
0.4s for s = 4
0.2s for s = 3
0.1s for s = 2
0.4s for s = 1
0.2s for s = 0
-->
* It is impossible to do his with only 4 tables for each meal. This was verified by a SAT-solver (after aggressive symmetry breaking can be done in 134 seconds on a laptop).
<!--
134s for s = 5
s for s = 4
s for s = 3
s for s = 2
s for s = 1
s for s = 0
-->

#### `T(17,4) ≤ 7`
* Solution found by SAT-solvers:
```
1234 5678 9ABC DEFG H
1469 28EH 7ACG B 35DF
7 48CD 26BF 1AEG 359H
1BDH 8A 6CF 379E 245G
1 45BE 67GH 89DF 23AC
29 CEH 56AD 38BG 147F
36E 158C 9G 27BD 4AFH
```
* kissat took 1.4s on a laptop
<!--
12.9s for s = 3
1.4s for s = 2
4.2s for s = 1
4.4s for s = 0
-->

#### `T(13,5) ≤ 4`
* Solution found with kissat (<0.1s):
```
12345 6789A BCD
19AB 2367C 458D
18C 239AD 4567B
167D 238B 459AC
```
<!-- s = 0, but it's always fast. -->

#### `T(26,5) ≤ 8`
* Solution found by Adam Zsolt Wagner using AlphaEvolve:
```
5 9 11 16 20 | 2 10 14 22 25 | 4 12 15 18 21 | 0 1 17 19 23 | 3 6 7 8 13 | 24
8 13 14 15 19 | 0 2 5 6 18 | 11 21 22 23 24 | 3 4 16 17 25 | 1 7 9 10 12 | 20
1 4 14 17 24 | 5 7 8 21 25 | 6 10 15 16 23 | 2 3 11 12 20 | 9 13 18 19 22 | 0
2 5 15 17 21 | 0 4 10 11 13 | 7 14 18 20 23 | 1 6 9 19 25 | 8 12 16 22 24 | 3
1 8 10 11 20 | 0 3 9 14 21 | 2 12 13 16 19 | 4 5 7 17 22 | 6 15 18 24 25 | 23
3 6 18 22 23 | 0 8 10 12 21 | 7 11 15 19 25 | 9 13 17 20 24 | 1 2 5 14 16 | 4
6 11 12 14 17 | 0 15 20 22 25 | 2 4 8 9 23 | 1 13 16 18 21 | 3 5 10 19 24 | 7
8 10 11 17 18 | 1 3 9 15 22 | 4 6 19 20 21 | 0 2 7 16 24 | 5 12 13 23 25 | 14
```

#### `T(22,6) ≤ 5`
* Solution found by SAT-solvers:
```
123456 789ABC DEFGHI JKLM
458FIM 26ABDK 379GHL 1CEJ
3ABFIJ 45CGHK 18DL 2679EM
45ABEL 3CDM 268GHJ 179FIK
38EK 4579DJ 1ABGHM 26CFIL
```
* kissat took 7.4s on a laptop
* This is a special case of `L`
<!--
200s for s = 4
>240s for s = 3
32.5s for s = 2
33.7s for s = 1
7.5s for s = 0
-->

#### `T(36,6) ≤ 8`
* Solution found by an annealing algorithm (to be committed):
```
22  4  7 28  9  1  |  8 21  6 29 15  2  | 27 32 19 17 30 16  |  0 11 13 10  5 14  | 31 12 20 18 25 34  | 23 33 26 24 35  3  |
12 30 29 31  0 33  | 26 22 11 24 17  6  | 35 20 14  7 21  2  | 23 19 15  1 28 18  | 32  9 34 10 16  8  | 27  3 13  4  5 25  |
11 20 15  3 32 34  | 16  6 27 33  7 12  |  4  8 30  1 14 24  |  9  2  5  0 18 26  | 19 13 25 22 29 21  | 17 35 10 31 28 23  |
25 26 15 30  7 10  |  6 14 31 19  9  3  |  1  5 34 17 21 33  | 32 13 24 12 28  2  | 23 22  8 20  0 27  | 11 18  4 16 29 35  |
33 32 22 18 14 15  | 30  6 13 23  4 34  | 19  8 35 26  5 12  | 28  0 10 16 21  3  | 20  9 17 24 25 29  | 31  1 27  7 11  2  |
33  8 25 11 28 19  | 31  1 26 13 20 16  | 23 29  9  5 32  7  | 21  6 24 10 18 27  |  0 12 17  4 14 15  | 22 30 34 35  2  3  |
34 19  0 11  7 24  | 22  1  3 29 10 12  | 18  5 28  6 20 30  | 31 26 32  4  8 21  |  2 17 25 16 14 23  |  9 35 15 27 33 13  |
19 33 20 10  2  4  | 34 29 28 14 27 26  |  9 11 21 23 12 30  |  3  7 17  8 18 13  | 24 16 31  5 22 15  |  1 35 25  6  0 32  |
```

#### `T(25,7) ≤ 5`
* Solution found by Mathematica SAT-solver:
```
235KLP 78BHJM 16ADEG 49CFINO
25EGIJO 1348BFL 6CMNP 79ADHK
47EFGHP 25689B 3ACDJLN 1IKMO
46FJK 8ABDIOP 1257CHN 39EGLM
367HILO 19JP 245ADFM 8BCEGKN
```
* kissat took 1.7s on a laptop
<!-- 1.7s for s = 0 -->
<!-- 26.6s for s = 1 -->

#### `T(31,7) ≤ 6`
* Solution found by Adam Zsolt Wagner using AlphaEvolve:
```
3 4 5 6 10 14 15 | 9 11 13 23 26 | 0 17 21 22 24 27 | 1 2 7 16 20 29 | 8 12 18 19 25 28 30
7 8 13 14 19 22 29 | 0 2 10 15 24 25 26 | 6 11 12 | 4 5 16 17 23 27 28 | 1 3 9 18 20 21 30
2 11 14 17 18 27 30 | 0 6 7 9 24 28 29 | 1 4 5 8 19 20 26 | 10 12 13 15 16 21 | 3 22 23 25
2 6 8 19 21 23 | 9 14 16 25 | 1 10 11 15 20 22 28 | 3 7 12 17 26 27 29 | 0 4 5 13 18 24 30
0 3 8 11 16 19 24 | 14 21 26 28 | 2 4 5 9 12 22 | 1 6 13 17 20 25 27 | 7 10 15 18 23 29 30
8 9 10 15 17 19 27 | 0 1 12 14 20 23 24 | 2 3 13 28 | 6 16 18 22 26 30 | 4 5 7 11 21 25 29
```


#### `T(22,8) ≤ 4`
* Solution found by Mathematica SAT-solver:
```
12345678 9ABCDEFG HIJKLM
47ACIK 1369BDHM 258EFGJL
258ACHM 136EFGIK 479BDJL
47EFGHM 136ACJL 2589BDIK
```
* kissat took 0.8s on a laptop
<!-- 0.8s for s = 0 -->
<!-- 1.1s for s = 1 -->

#### `T(41,9) ≤ 6`
* Solution found with the help of Adam Zsolt Wagner using AlphaEvolve:
```
1 3 8 24 27 36 | 10 13 18 28 29 30 31 33 | 0 6 7 11 20 26 34 39 40 | 2 4 5 9 12 17 22 23 38 | 14 15 16 19 21 25 32 35 37
3 5 18 19 21 27 33 34 40 | 20 22 26 31 36 37 38 | 6 11 12 13 23 24 25 28 32 | 2 4 7 8 16 29 30 35 | 0 1 9 10 14 15 17 39
0 19 21 22 24 29 30 38 39 | 1 2 4 13 28 34 37 40 | 5 6 8 11 14 15 31 | 7 9 17 18 25 32 33 36 | 3 10 12 16 20 23 26 27 35
12 14 15 23 29 30 34 36 40 | 8 9 13 17 19 20 21 26 28 | 5 7 10 24 37 | 1 6 11 16 18 22 33 35 38 | 0 2 3 4 25 27 31 32 39
9 16 17 24 31 34 35 40 | 2 4 6 10 11 19 21 36 | 1 5 20 25 26 29 30 32 | 3 7 13 14 15 22 27 28 38 | 0 8 12 18 23 33 37 39
0 5 13 16 28 35 36 39 | 2 4 14 15 18 20 24 26 33 | 1 7 12 19 21 23 31 | 8 10 22 25 32 34 38 40 | 3 6 9 11 17 27 29 30 37
```
<!-- annealing gets quite reliably to 8 violations for T(42,9), so that might be impossible. -->

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

#### `T(14,5) ≥ 5`
* This also follows from `g`.
* UNSAT found with kissat (<0.1s).
<!--
<0.1s for s = 3
0.2s for s = 2
3.4s for s = 1
>40s for s = 0
-->

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
* The condition `n ≡ k mod k(k-1)` is necessary for a perfect `(n,k)`-solution to exist. To what extent is it sufficient?
  * It is true when `k` is a prime power and `n` is a power of `k`, see `H`.
  * In the smallest case where `k` is not a prime power, the first non-trivial example is immediately a counterexample. There is no perfect `(36,6)`-solution (see [Latin Squares](#latin-squares)).
  * It is true for `k = 2` and `k = 3`.
  * For `k = 4` it's true according to [On resolvable designs](https://www.sciencedirect.com/journal/discrete-mathematics/vol/3/issue/4).
  * According to [ANKS](http://engine.scichina.com/publisher/scp/journal/Math%20A1/37/5/10.1360/ya1994-37-5-555?slug=abstract) for every `k` this is true for all but finitely many `n` (Theorem 1, citing *The existence of resolvable block designs. Survey of combinatorial theory*, D Ray-Chaudhuri, R Wilson - 1973).
    * This shows that for a fixed `k` the asymptotic behavior of `T(n,k)` is `T(n,k) ≤ (n-1)/(k-1) + O(1)`, i.e. `T(n,k) - (n-1)/(k-1)` is bounded by a constant (possibly depending on `k`).
* For every `n` and `k` is there an optimal `(n,k)`-solution in which, during every meal, at most one table is not completely occupied?
  * This is false. All optimal `(8,5)`-solutions have at least one day with two tables of four participants. This was found by brute force, but is quite easy to see by hand (to do).
  * It is also false that there always is an optimal `(n,k)`-solution where there are `⌈ n/k ⌉` tables each day (where `⌈ x ⌉` is the smallest integer which is at least `x`).
    The Mathematica SAT-solver easily found a [solution](#solutions-for-individual-cases) that `T(12,3) ≤ 6`. With the help of other SAT-solvers Bernardo Subercaseaux showed that the problem was unsatisfiable under the additional condition that only 4 tables could be used per day.
* In all cases we know the following holds: if there is a perfect `(n,k)` solution, then `T(n+1,k) = T(n,k) + 2`.
  * Does this always hold? Or maybe `T(n+1,k) ≥ T(n,k) + 2`?

## External Links / References

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
* Kirkman System:
  * [Wolfram Mathworld](http://mathworld.wolfram.com/KirkmanTripleSystem.html),
  * [Dutch dissertation by Pieter Mulder (1917)](https://babel.hathitrust.org/cgi/pt?id=njp.32101065911230;view=1up;seq=19).
  * *Solution of Kirkman's schoolgirl problem*, Ray-Chaudhuri and Wilson, 1971. In [Proc. of Symp. in Pure Math, Vol 19](http://www.ams.org/books/pspum/019/).
  * *Kirkman triple systems and their generalizations: A survey*, Rees and Wallis, 2002. [Springer](https://link.springer.com/chapter/10.1007/978-1-4613-0245-2_13)
  * [*Asymptotic Existence of Nearly Kirkman Systems*, Hao Chen, Wen-Song Chu](http://engine.scichina.com/publisher/scp/journal/Math%20A1/37/5/10.1360/ya1994-37-5-555?slug=abstract)
* Block Designs:
  * *A Survey of Resolvable Solutions of Balanced Incomplete Block Designs*, Sanpei Kageyama, Rev. Inst. Internat. Statist., 40, 269–273. [JSTOR](https://www.jstor.org/stable/1402466)
  * *On Cyclically Resolvable Cyclic Steiner 2-Designs*, Clement Lam and Ying Miao, Journal of Combinatorial Theory, Series A, Volume 85, Issue 2, February 1999, Pages 194-207. [ScienceDirect](https://www.sciencedirect.com/science/article/pii/S0097316598929247)
  * [*On resolvable designs*, Haim Hanani, D.K. Ray-Chaudhuri, Richard M. Wilson](https://www.sciencedirect.com/journal/discrete-mathematics/vol/3/issue/4) Discrete Mathematics, 1972, 3:343-357.
* Oberwolfach Problem: [Sarah's Oberwolfach Problem Page](http://facultyweb.kennesaw.edu/shollid4/oberwolfach.php).

## Contributing

* Contributions are welcome! Feel free to add any information. Please provide links or justifications of claims you make.

## Errata

* 2025.06.13: argument `j` was incorrect.
* 2025.04.10: `T(13,5)` was incorrectly listed to be 5.