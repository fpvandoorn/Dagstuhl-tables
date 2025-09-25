Some solutions are found by SAT-solvers.

* There is a very naive Mathematica SAT-encoding, that is really bad in [here](SAT.nb) (or [here](SAT.txt) in plain text). This was written by Michael Trott and optimized by Floris van Doorn (it is included in this repo).
* There is a slightly better SAT encoding [here](tables.py) in Python.
* The most efficient SAT encoder is here [here](dagstuhl.py), also in Python (mostly written by Bernardo Anibal Subercaseaux Roa).

To use the python SAT encoders, run e.g.
```
python3 dagstuhl.py -n 14 -k 5 -m 4 -s 4
python3 dagstuhl.py -n 22 -k 6 -m 5 -s 0
```
The `s` flag should be `m - 1` (or higher) when you try to prove UNSAT. It should be set to 0-2 when you try to prove SAT.
You can use e.g. [kissat](https://github.com/arminbiere/kissat) to prove SAT/UNSAT. Follow the build instructions there (requires `gcc`) and (optionally) add `kissat` to your path (e.g. by copying it to `/usr/bin/`). Then run e.g.
```
kissat formulas/dagstuhl_14_5_4.cnf
```
You can use the `-t` option to limit the number of tables.