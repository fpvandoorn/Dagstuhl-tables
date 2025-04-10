from pysat.formula import CNF, IDPool
from pysat.solvers import Cadical195
from pysat.card import *
import itertools, time

def encode_tables(meals, people, size, tableCount):
  cnf = CNF() # create a new formula
  vpool = IDPool(start_from=1)
  e = lambda m, p, j: vpool.id(f'e_{m, p, j}') # meal m, person p, table j
  f = lambda m, p1, p2, j: vpool.id(f'f_{m, p1, p2, j}') # meal m, person p1 and p2, table j, p2 < p1.
  # r = lambda m, p, j1, j2: vpool.id(f'r_{m, p, j1, j2}') # j2 < j1.

  # q is the conjunction of two p's
  for m in range(meals):
    for p1 in range(people):
      for p2 in range(p1):
        for j in range(tableCount):
          cnf.append([-e(m, p1, j), -e(m, p2, j), f(m, p1, p2, j)]) # optional
          cnf.append([e(m, p1, j), -f(m, p1, p2, j)])
          cnf.append([e(m, p2, j), -f(m, p1, p2, j)])

  # at least at one meal and at one table person p1 and p2 are present
  for p1 in range(people):
    for p2 in range(p1):
      cnf.append([f(m, p1, p2, j) for j in range(tableCount) for m in range(meals)])

  # at each meal every person can only be at one table
  for m in range(meals):
    for p in range(people):
      for j1 in range(tableCount):
        for j2 in range(j1):
          cnf.append([-e(m, p, j1), -e(m, p, j2)])

  # never are k+1 persons on a table that holds k people
  for m in range(meals):
    for j in range(tableCount):
      cnf.extend(CardEnc.atmost([e(m, p, j) for p in range(people)], bound=size, vpool=vpool))
      # for potential_clique in itertools.combinations(range(people), size+1):
      #   cnf.append([-e(m, p, j) for p in potential_clique])

  # every person p sits at some table <= p (some symmetry breaking)
  for m in range(meals):
    for p in range(people):
      cnf.append([e(m, p, j) for j in range(min(p+1, tableCount))])

  # on meal 1, use the "optimal" seating arrangement (symmetry breaking)
  for p in range(people):
      cnf.append([e(0, p, p // size)])

  return cnf, e, f

# additional possibility for symmetry breaking: if person i sits at table t, at every table s < t there sits a person j < i. 
# If encoded naively, this could slow down solving the problem

def format(model, e, meals, people, tableCount):
  table = [None] * meals
  for m in range(meals):
    table[m] = [None] * tableCount
    for j in range(tableCount):
      table[m][j] = [p for p in range(people) if model[e(m,p,j)-1] > 0]
  print(table)

meals=5
people=25
size=7
tableCount=4

# For finding SAT problems, then `tableCount = math.ceil(people / size)` usually works, 
# and `tableCount = people // size + 1` works in all known cases 
# For a guaranteed UNSAT proof, then choosing `tableCount` to be the maximal number such that 
# `people // tableCount + (people + 1) // tableCount > size` (which is roughly `2 * people / size`)
# is guaranteed to be enough. There might be reasons why we can make the value a little smaller.

problems, e, f = encode_tables(meals, people, size, tableCount)

print(f"Number of variables: {problems.nv}")
print(f"Number of clauses: {len(problems.clauses)}")

problems.to_file('problem.cnf')

# solver = Cadical195()
# solver.append_formula(problems)
# t0 = time.time()
# result = solver.solve()
# t1 = time.time()
# print(result)
# print(f"took {round(t1 - t0, 5)} seconds")

# if result: # if satisfiable, it has a model
#   model = solver.get_model() # get the solution
#   format(model, e, meals, people, tableCount)