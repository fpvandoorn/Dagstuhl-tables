# Authors: Bernardo Subercaseaux and Floris van Doorn
from eznf import modeler
import argparse, itertools, time, math

def tr(N):
    """The N-th triangle number"""
    return N * (N - 1) // 2

def sort_by(l, f):
  """Sort l using f. This probably already exists."""
  s = list(zip(map(lambda x:f(x), l),l))
  s.sort()
  return list(map(lambda x: x[1], s))

def max_nr_connections(N, K):
    """Maximum number of connections made on a day with N participants and K tables per day."""
    return N // K * tr(K) + tr(N % K)

def evenly_nr_connections(N, T):
    """If we spread N evenly over N tables, how many connections are formed?"""
    return ((N - 1) % T + 1) * tr(math.ceil(N / T)) + (T - ((N - 1) % T + 1)) * tr(N // T)

def min_nr_connections(N, K, L=1):
    """Maximum number of connections made on a day with N participants, with L tables of size K, and
    all other tables smaller. Assumes N >= L * K."""
    return L * tr(K) + max_nr_connections(N - L * K, K - 1)

def configs_aux(N, K, M, acc, pre):
    """Collection of non-increasing lists with sum N, max M and the sum of the lowest two elements is at least K.
    Result is collected in acc, and results are prepended by pre."""
    if N == 0:
        return acc + [pre]
    if N <= K:
        acc += [] if N + pre[-1] <= K or N > pre[-1] else [pre + [N]]
        return acc
    for k in range(M, K // 2, -1):
        acc = configs_aux(N - k, K, k, acc, pre + [k])
    return acc

def configs(N, K):
    """List of non-dominated configurations."""
    return configs_aux(N, K, K, [], [])

def size(conf):
    """The number of connections of a configuration."""
    return sum(map(tr, conf))

def overlap_table(conf, t, k=0):
    """Minimal overlap between configuration conf (minus k on each table) and a table with t people.
    Overlap means that connections that were formed twice."""
    people_left = t
    tables_left = len(conf)
    acc = 0
    for i in conf[::-1]:
        overlap = max(min(i - k, people_left // tables_left), 0)
        acc += tr(overlap)
        people_left -= overlap
        tables_left -= 1
    return acc

def overlap_aux(conf1, conf2):
    """(lower bound for) Minimal overlap between two configurations. Not optimal."""
    # k indicates the number of tables `t` we've seen so far with `t >= len(conf2)`.
    # we may assume that such tables (when evaluating them in decreasing order) overlaps with at
    # least 1 person from each table of conf2.
    # Note: we may not assume that such tables overlap with at least `t // len(conf2)` with
    # each table from conf2.
    # Counterexample: `conf1 = conf2 = [9,9,2]`
    k = 0
    sum_so_far = 0
    for t in conf1:
        sum_so_far += overlap_table(conf2, t, k)
        if t >= len(conf2) or conf2[t] <= k:
            k += 1
    return sum_so_far
    # return sum(map(lambda t: overlap_table(conf2, t), conf1))

def overlap(conf1, conf2):
    """(lower bound for) Minimal overlap between two configurations. Not optimal."""
    i = overlap_aux(conf1, conf2)
    j = overlap_aux(conf2, conf1)
    # i != j  is possible for e.g. [5, 5, 5, 5] and [5, 3, 3, 3, 3, 3]
    return max(i, j)

def min_days(N, conf, confs, K, M):
    """(lower bound for) minimum number of days needed when day 1 uses conf, and later days can use
    configurations from confs (`M` is the previous max found, only used for optimization)"""
    conn = tr(N) - size(conf)
    max_remainder = max(map(lambda c: size(c) - overlap(conf, c), confs))
    days = math.ceil(conn / max_remainder)
    # check for lower bound `j`
    if (M - 1) * max_remainder < conn:
        print(f"{conf} cannot be the best configuration for a solution with {M} days. It forms at most {size(conf)} + {M - 1} * {max_remainder} = {(M - 1) * max_remainder + size(conf)} connections.")
        return 1 + days
    str = f"({(M - 1) * max_remainder - conn} more than needed)" if (M - 1) * max_remainder > conn else "(precisely what is needed)"
    print(f"{conf} on day 1 forms at most {size(conf)} + {M - 1} * {max_remainder} = {(M - 1) * max_remainder + size(conf)} connections in {M} days {str}.")
    possible_configs = [c for c in confs if size(c) - overlap(conf, c) + (M - 2) * max_remainder >= conn]
    possible_configs.reverse()
    conns = [size(c) - overlap(conf, c) for c in possible_configs]
    all_conns = [c * (M - 1) + size(conf) for c in conns]
    if len(possible_configs) > 1:
        print(f"Days 2+ use configs {possible_configs} which can make at most {conns} connections per day, and can make at most {all_conns} connections when used exclusively after day 1.")
        return 1 + days
    c = possible_configs[0]
    print(f"Days 2+ must use config {c} which can make at most {conns[0]} connections per day (total {all_conns[0]}).")
    if conn < days * max_remainder:
        return 1 + days
    pairs = overlap(conf, c)
    maxes = len([i for i in c if i == K])
    conn_per_day = evenly_nr_connections(pairs, maxes)
    if pairs < maxes * (maxes + 2) and len(conf) * 2 <= K and (days + 1) * conn_per_day < tr(pairs) and days > 2 and c == conf:
        print(f"There are {pairs} pairs that could only meet {(days + 1) * conn_per_day} < {tr(pairs)} times (argument `j`), so we need at least {days + 2} days.\n")
        return 2 + days
    print(f"Unsure whether it is possible in {days + 1} days ({pairs} pairs need to meet {tr(pairs)} times, computed {(days + 1) * conn_per_day} possible meetings ({(days + 1) * (pairs - maxes)} naive meetings?)).\n")
    return 1 + days



def better_lower_bound(N, K, M):
    """A lower bound based of the number of meals needed. (`g` in `README.md`)
    Methodology:
    * compute all non-dominated first days
    * count how many new connections later days can make after that first day, assuming that the
      first day is the best day (w.r.t. some ordering)."""
    confs = configs(N, K)
    confs = sort_by(confs, size)
    if len(confs) < 20:
        print(f"non-dominated configurations: {confs[::-1]}")
    else:
        print(f"{len(confs)} non-dominated configurations. The first 10 are {confs[:-11:-1]}")
    min_so_far = N + 2
    while confs:
        conf = confs.pop()
        if size(conf) * M < tr(N):
            print("remaining configurations cannot possibly create enough connections in fewer days")
            break
        min_so_far = min(min_so_far, min_days(N, conf, confs + [conf], K, M))
    return min_so_far

def stats(N, K, M, T, S, C):
    """Print some statistics about the given problem."""
    conn_needed = tr(N)
    conn_per_meal = max_nr_connections(N, K)
    easy_min_days = math.ceil(conn_needed / conn_per_meal)
    min_days = easy_min_days
    # maximum number of tables possible in a non-dominated configuration
    max_nondominated_tables = 1 if N <= K else (N + 1) // (K // 2 + 1) if K % 2 == 0 else (2 * N) // (K + 1)
    print(f"{conn_needed} connections needed.")
    print(f"{conn_per_meal} connections can be made per meal.")
    print(f"{easy_min_days} is an easy lower bound for the number of meals.")
    print(f"Optimal solutions have between {math.ceil(N / K)} and {max_nondominated_tables} tables.")
    if N <= K**2 - 2:
        min_days = better_lower_bound(N, K, easy_min_days)
        if min_days != easy_min_days:
            print(f"{min_days} is a better lower bound for the number of meals.")
    if M < min_days:
        print(f"Too few days. Problem will be UNSAT.")
    if C > 0 and C * M < conn_needed:
        print(f"Too few connections per meal. Problem will be UNSAT.")





def encode(N, K, M, T, S, C, knf=False):
    enc = modeler.Modeler()

    # note: if S > 0, we could remove all constraints of meal 0.

    for p1 in range(N):
        for p2 in range(p1+1, N):
            for m in range(M):
                enc.add_var(f"p_{p1}_{p2}_{m}", description=f"p_{p1} meets p_{p2} at meal {m}")

    # any two participants meet
    for p1 in range(N):
        for p2 in range(p1+1, N):
            enc.add_clause([f"p_{p1}_{p2}_{m}" for m in range(M)])

    # transitivity of the meet-relation
    for p1 in range(N):
        for p2 in range(p1+1, N):
            for p3 in range(p2+1, N):
                for m in range(M):
                    enc.add_clause([f"-p_{p1}_{p2}_{m}", f"-p_{p2}_{p3}_{m}", f"p_{p1}_{p3}_{m}"])
                    enc.add_clause([f"-p_{p1}_{p2}_{m}", f"p_{p2}_{p3}_{m}", f"-p_{p1}_{p3}_{m}"])
                    enc.add_clause([f"p_{p1}_{p2}_{m}", f"-p_{p2}_{p3}_{m}", f"-p_{p1}_{p3}_{m}"])

    # enforce maximal table size
    if knf:
        print("Using KNF encoding")
    for p1 in range(N): # we could make this range(N - K), if that is convenient.
        for m in range(M):
            if knf:
                enc.add_kconstraint_le(K-1, [f"p_{p1}_{p2}_{m}" for p2 in range(p1+1, N)])
            else:
                enc.at_most_k([f"p_{p1}_{p2}_{m}" for p2 in range(p1+1, N)], K-1)

    # TABLE COUNT (0 = unlimited)
    if T > 0:
        for m in range(M):
            for s4 in itertools.combinations(range(N), T+1):
                enc.add_clause([f"p_{p1}_{p2}_{m}" for (p1, p2) in itertools.combinations(s4, 2)])

    # enforce maximal connections per meal
    if C > 0:
        for m in range(M):
            if knf:
                enc.add_kconstraint_le(C, [f"p_{p1}_{p2}_{m}" for p1 in range(N) for p2 in range(p1+1, N)])
            else:
                enc.at_most_k([f"p_{p1}_{p2}_{m}" for p1 in range(N) for p2 in range(p1+1, N)], C)

    # "symmetry breaking": first meal has optimal arrangement.
    # This is not sound, and a separate argument has to be given in case that the optimal arrangement is never used.
    max_table_size = K
    # number of tables that have `max_table_size` people in them
    nr_max_tables = N // K
    nr_submax_tables = 0
    optimal_arrangement = {}
    if S > 0 and C <= 0:
        # first person that sits at table i
        first_person = {}
        for j in range(nr_max_tables):
            first_person[j] = j * K
        for p in range(N):
            optimal_arrangement[p] = p // K
        for p1 in range(N):
            for p2 in range(p1+1, N):
                if optimal_arrangement[p1] == optimal_arrangement[p2]:
                    enc.add_clause([f"p_{p1}_{p2}_{0}"])
                else:
                    enc.add_clause([f"-p_{p1}_{p2}_{0}"])
    if S > 0 and C > 0:
        # We will create a configuration [M, M, ..., M, M-1, M-1, ..., M-1, x] with the maximal connections <= C.
        while min_nr_connections(N, max_table_size) > C:
            max_table_size -= 1
        nr_max_tables = N // max_table_size
        while min_nr_connections(N, max_table_size, nr_max_tables) > C:
            nr_max_tables -= 1
        remainder = N - max_table_size * nr_max_tables
        nr_submax_tables = remainder // (max_table_size - 1)
        remainder -= nr_submax_tables * (max_table_size - 1)
        print(f"The first meal will have {nr_max_tables} tables of size {max_table_size}, \
{nr_submax_tables} tables of size {max_table_size - 1}{', and one table of size ' + str(remainder) if remainder > 0 else ''}.")
        current_table = 0
        current_table_count = 0
        first_person = {}
        first_person[0] = 0 # probably unused
        for p in range(N):
            if current_table_count >= max_table_size - (0 if current_table < nr_max_tables else 1):
                current_table += 1
                current_table_count = 0
                first_person[current_table] = p
            optimal_arrangement[p] = current_table
            current_table_count += 1
        # print(optimal_arrangement) # debug
        for p1 in range(N):
            for p2 in range(p1+1, N):
                if optimal_arrangement[p1] == optimal_arrangement[p2]:
                    enc.add_clause([f"p_{p1}_{p2}_{0}"])
                else:
                    enc.add_clause([f"-p_{p1}_{p2}_{0}"])


    # more symmetry breaking: participant 0 meets participant lK+i not later than lK+i+1 if 0<=i<K-1
    # and 0 < l. (because we can permute the elements at table l on meal 0)
    # furthermore, 0 meets lK no later than (l+1)K (because we can permute the tables on meal 0)
    # furtermore, K meets i no later than i+1 (for 0<i<K-1)
    # we only require this for S-1 days after day 0, the later days have longer clauses.
    if S > 1 and N > K and M > 1:
        for l in range(1, nr_max_tables + nr_submax_tables + 1):
            if l < nr_max_tables - 1:
                # symmetry breaking between tables on meal 0 of size max_table_size (except table 0)
                for m in range(1,min(M - 1, S)):
                    enc.add_clause([f"p_{0}_{first_person[l]}_{m2}" for m2 in range(1,m+1)] + [f"-p_{0}_{first_person[l+1]}_{m}"])
            if l < nr_max_tables:
                # symmetry breaking between people on a table of size max_table_size (on meal 0, except table 0)
                for i in range(max_table_size - 1):
                    for m in range(1,min(M - 1, S)):
                        enc.add_clause([f"p_{0}_{first_person[l] + i}_{m2}" for m2 in range(1,m+1)] + [f"-p_{0}_{first_person[l] + i + 1}_{m}"])
            if nr_max_tables <= l < nr_max_tables + nr_submax_tables - 1:
                # symmetry breaking between tables on meal 0 of size max_table_size - 1
                for m in range(1,min(M - 1, S)):
                    enc.add_clause([f"p_{0}_{first_person[l]}_{m2}" for m2 in range(1,m+1)] + [f"-p_{0}_{first_person[l+1]}_{m}"])
            if nr_max_tables <= l < nr_max_tables + nr_submax_tables:
                # symmetry breaking between people on a table of size < max_table_size (on meal 0)
                for i in range(max_table_size - 2):
                    for m in range(1,min(M - 1, S)):
                        enc.add_clause([f"p_{0}_{first_person[l] + i}_{m2}" for m2 in range(1,m+1)] + [f"-p_{0}_{first_person[l] + i + 1}_{m}"])
        # symmetry breaking between people on a table 0 (on meal 0, except person 0)
        for i in range(1, max_table_size - 1):
            for m in range(1,min(M - 1, S)):
                enc.add_clause([f"p_{i}_{K}_{m2}" for m2 in range(1,m+1)] + [f"-p_{i+1}_{K}_{m}"])
    # print(enc._clauses)
    return enc


def decode(model, N, M):
    ans = []
    for m in range(M):
        table_to_people = {}
        person_to_table = {}
        for p1 in range(N):
            if p1 in person_to_table:
                continue
            person_to_table[p1] = len(table_to_people) + 1
            table_to_people[person_to_table[p1]] = [p1]
            for p2 in range(p1+1, N):
                if model[f"p_{p1}_{p2}_{m}"]:
                    person_to_table[p2] = person_to_table[p1]
                    table_to_people[person_to_table[p1]].append(p2)
        print(f"Meal {m}: {table_to_people}")
        ans.append(list(table_to_people.values()))
    print(ans)
    return ans

# todo
def check(result, N):
    M = len(result)

def short_output(result):
    M = len(result)
    for m in range(M):
        print(' '.join(map(lambda s: ''.join(map(lambda x: chr(x + (49 if x < 9 else 56)), s)), result[m])))


if __name__ == "__main__":
    argparser = argparse.ArgumentParser()
    argparser.add_argument("-n", "--n_people", type=int, default=8, help="Number of people")
    argparser.add_argument("-k", "--table_capacity", type=int, default=5, help="Table capacity")
    argparser.add_argument("-m", "--meals", type=int, default=5, help="Number of meals")
    argparser.add_argument("-t", "--table_count", type=int, default=0, help="Number of tables (0 is unlimited)")
    argparser.add_argument("-s", "--symmetry_break", type=int, default=1, help="Amount of symmetry breaking (0 is no symmetry breaking, meals - 1 is maximum). Set max if expected unsat, set to 0-2 if expected sat. It is not clear which of those will be quickest. The semantics is that if you set this to S, then this will only add constrainst for the first S days, and it will only generate clauses of length at most S. Note: when set to S > 0, this does assume that at least one day uses the optimal configuration, which is not known to always be true.")
    argparser.add_argument("-c", "--max_connections", type=int, default=0, help="Maximum of connections that can be made each meal (0 is unlimited).")
    argparser.add_argument("-d", "--decode", action="store_true", help="Decode the model")
    argparser.add_argument("--knf", action="store_true", help="Use KNF encoding")
    argparser.add_argument("--stats_only", action="store_true", help="Don't compute the SAT-encoding")
    argparser.add_argument("--no_stats", action="store_true", help="Don't compute the stats")
    args = argparser.parse_args()
    N_PEOPLE = args.n_people
    TABLE_CAPACITY = args.table_capacity
    MEALS = args.meals
    TABLECOUNT = args.table_count
    DECODE = args.decode
    SYMMETRY_BREAK = args.symmetry_break
    MAX_CONNECTIONS = args.max_connections
    KNF = args.knf
    STATS_ONLY = args.stats_only
    NO_STATS = args.no_stats
    if not NO_STATS:
        stats(N_PEOPLE, TABLE_CAPACITY, MEALS, TABLECOUNT, SYMMETRY_BREAK, MAX_CONNECTIONS)
    if STATS_ONLY:
        exit()
    encoding = encode(N_PEOPLE, TABLE_CAPACITY, MEALS, TABLECOUNT, SYMMETRY_BREAK, MAX_CONNECTIONS, knf=KNF)
    filename = f"formulas/dagstuhl_{N_PEOPLE}_{TABLE_CAPACITY}_{MEALS}{'_' + str(TABLECOUNT) if TABLECOUNT > 0 else ''}{'_c' + str(MAX_CONNECTIONS) if MAX_CONNECTIONS > 0 else ''}.{'knf' if KNF else 'cnf'}"
    encoding.serialize(filename)
    print(f"Wrote encoding file to {filename}")
    if DECODE:
        t0 = time.time()
        a, b, result = encoding.solve_and_decode(lambda model: decode(model, N_PEOPLE, MEALS))  # Decode the model
        t1 = time.time()
        print(f"took {round(t1 - t0, 5)} seconds")
        if N_PEOPLE < 36:
            short_output(result)
        else:
            print("36+ people; need better implementation to print short output.")

