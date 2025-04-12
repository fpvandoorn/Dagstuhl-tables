# Authors: Bernardo Subercaseaux and Floris van Doorn
from eznf import modeler
import argparse, itertools, time, math

# Maximum number of connections made on a day with N participants and K tables per day.
def max_nr_connections(N, K):
    return N // K * K * (K - 1) // 2 + (N % K) * ((N % K) - 1) // 2

# Maximum number of connections made on a day with N participants, with L table of size K, and
# all other tables smaller. Assumes N >= L * K.
def min_nr_connections(N, K, L=1):
    return L * K * (K - 1) // 2 + max_nr_connections(N - L * K, K - 1)

def stats(N, K, M, T, S, C):
    conn_needed = N * (N - 1) // 2
    conn_per_meal = max_nr_connections(N, K)
    easy_min_days = math.ceil(conn_needed / conn_per_meal)
    print(f"{conn_needed} connections needed.")
    print(f"{conn_per_meal} connections can be made per meal.")
    print(f"{easy_min_days} is an easy lower bound for the number of meals.")
    if M < easy_min_days:
        print(f"Too few days. Problem will be UNSAT.")
    if C > 0 and S > 1:
        print(f"WARNING! Positive `-c` is not currently compatible with `-s` greater than 1.")
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

    # symmetry breaking: first meal has optimal arrangement
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
    argparser.add_argument("-s", "--symmetry_break", type=int, default=1, help="Amount of symmetry breaking (0 is no symmetry breaking, meals - 1 is maximum). Set max if expected unsat, set to 0-2 if sat. It is not clear which of those will be quickest. The semantics is that if you set this to S, then this will only add constrainst for the first S days, and it will only generate clauses of length at most S.")
    argparser.add_argument("-c", "--max_connections", type=int, default=0, help="Maximum of connections that can be made each meal (0 is unlimited).")
    argparser.add_argument("-d", "--decode", action="store_true", help="Decode the model")
    argparser.add_argument("--knf", action="store_true", help="Use KNF encoding")
    args = argparser.parse_args()
    N_PEOPLE = args.n_people
    TABLE_CAPACITY = args.table_capacity
    MEALS = args.meals
    TABLECOUNT = args.table_count
    DECODE = args.decode
    SYMMETRY_BREAK = args.symmetry_break
    MAX_CONNECTIONS = args.max_connections
    KNF = args.knf
    stats(N_PEOPLE, TABLE_CAPACITY, MEALS, TABLECOUNT, SYMMETRY_BREAK, MAX_CONNECTIONS)
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

