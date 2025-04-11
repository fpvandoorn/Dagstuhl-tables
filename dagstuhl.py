# Authors: Bernardo Subercaseaux and Floris van Doorn
from eznf import modeler
import argparse, itertools, time

def stats(N, K, M, T):
    conn_needed = N * (N - 1) // 2
    conn_per_meal = N // K * K * (K - 1) // 2 + (N % K) * ((N % K) - 1) // 2
    print(f"{conn_needed} connections needed")
    print(f"{conn_per_meal} connections can be made per meal")
    print(f"{conn_needed // conn_per_meal} is an easy lower bound for the number of meals")

def encode(N, K, M, T, S, knf=False):
    enc = modeler.Modeler()

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

    if knf:
        print("Using KNF encoding")
    for p1 in range(N):
        for m in range(0, M):
            if knf:
                enc.add_kconstraint_le(K-1, [f"p_{p1}_{p2}_{m}" for p2 in range(p1+1, N)])
            else:
                enc.at_most_k([f"p_{p1}_{p2}_{m}" for p2 in range(p1+1, N)], K-1)

    # TABLE COUNT (0 = unlimited)
    if T > 0:
        for m in range(0, M):
            for s4 in itertools.combinations(range(N), T+1):
                enc.add_clause([f"p_{p1}_{p2}_{m}" for (p1, p2) in itertools.combinations(s4, 2)])

    # symmetry breaking: first meal has optimal arrangement
    if S >= 0:
        optimal_arrangement = {}
        for p in range(N):
            optimal_arrangement[p] = p // K
        for p1 in range(N):
            for p2 in range(p1+1, N):
                if optimal_arrangement[p1] == optimal_arrangement[p2]:
                    enc.add_clause([f"p_{p1}_{p2}_{0}"])
                else:
                    enc.add_clause([f"-p_{p1}_{p2}_{0}"])

    # more symmetry breaking: second meal, how much can we add?
    # if N > K and M > 1:
    #     enc.add_clause([f"p_{0}_{K}_{1}"])
    #     if K >= M:
    #         enc.add_clause([f"p_{0}_{K+1}_{1}"])
    #     else if N // K >= M:
    #         enc.add_clause([f"p_{0}_{2*K}_{1}"])

    # more symmetry breaking: participant 0 meets participant lK+i not later than lK+i+1 if 0<=i<K-1
    # and 0 < l. (because we can permute the elements at table l on meal 0)
    # furthermore, 0 meets lK no later than (l+1)K (because we can permute the tables on meal 0)
    # furtermore, K meets i no later than i+1 (for 0<i<K-1)
    # we only require this for S days after day 0, because otherwise the new clauses get too complicated.
    if N > K and M > 1:
        for l in range(1, N // K + 1):
            if l < N // K - 1:
                for m in range(1,min(M - 1, S+1)):
                    enc.add_clause([f"p_{0}_{l * K}_{m2}" for m2 in range(1,m+1)] + [f"-p_{0}_{(l + 1) * K}_{m}"])
            for i in range(K - 1):
                if l * K + i + 1 < N:
                    for m in range(1,min(M - 1, S+1)):
                        enc.add_clause([f"p_{0}_{l * K + i}_{m2}" for m2 in range(1,m+1)] + [f"-p_{0}_{l * K + i + 1}_{m}"])
        for i in range(1, K - 1):
            for m in range(1,min(M - 1, S+1)):
                enc.add_clause([f"p_{i}_{K}_{m2}" for m2 in range(1,m+1)] + [f"-p_{i+1}_{K}_{m}"])

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
    argparser.add_argument("-s", "--symmetry_break", type=int, default=0, help="Amount of symmetry breaking (-1 is minimum, meals - 2 is maximum). Set max if expected unsat, set to -1,0,1 if sat(?)")
    argparser.add_argument("-d", "--decode", action="store_true", help="Decode the model")
    argparser.add_argument("--knf", action="store_true", help="Use KNF encoding")
    args = argparser.parse_args()
    N_PEOPLE = args.n_people
    TABLE_CAPACITY = args.table_capacity
    MEALS = args.meals
    TABLECOUNT = args.table_count
    DECODE = args.decode
    SYMMETRY_BREAK = args.symmetry_break
    KNF = args.knf
    stats(N_PEOPLE, TABLE_CAPACITY, MEALS, TABLECOUNT)
    encoding = encode(N_PEOPLE, TABLE_CAPACITY, MEALS, TABLECOUNT, SYMMETRY_BREAK, knf=KNF)
    encoding.serialize(f"formulas/dagstuhl_{N_PEOPLE}_{TABLE_CAPACITY}_{MEALS}{'_' + str(TABLECOUNT) if TABLECOUNT > 0 else ''}.{'knf' if KNF else 'cnf'}")
    if DECODE:
        t0 = time.time()
        a, b, result = encoding.solve_and_decode(lambda model: decode(model, N_PEOPLE, MEALS))  # Decode the model
        t1 = time.time()
        print(f"took {round(t1 - t0, 5)} seconds")
        if N_PEOPLE < 36:
            short_output(result)
        else:
            print("36+ people, need better short output.")

