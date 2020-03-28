import json
import numpy as np

#=========Read json input=========
f=open("input.json","r").read()
nfa=json.loads(f)
f.close()

#=========Reading the input NFA==========

nfa_states=nfa["states"]
nfa_letters=nfa["letters"]
nfa_start=nfa["start"]
nfa_final=nfa["final"]
nfa_t_func=nfa["t_func"]



#===============Making a DFA from the read NFA===============
dfa_states = 2**n_states
dfa_letters = nfa["letters"]
dfa_start = nfa["start"]
dfa_final = []



#=========Initialising transition functions for both NFA and DFA==========

nfa_updatedt_func=np.zeros(nfa_letters +1, nfa_states+1)
dfa_t_func=np.zeros(dfa_letters+1, dfa_states+1)


# ===========Powerset====================
powerset=[]
states = [i for i in range(nfa_states)]
for i in range(2**nfa_states):
    powerset.append([states[j] for j in range(nfa_states) if (i & (2**j))])

# ===========Final States==========

for finalstate in nfa_final:
    for i in powerset:
        if(i!=[]): 
            for elements in i:
                if(finalstate == elements):
                    dfa_final.append(i)
dfa_finalstates=[]
for sets in dfa_final:
    if sets not in dfa_finalstates:
        dfa_finalstates.append(sets)
     
dfa_final = dfa_finalstates

# ===========NFA TFunc==========
   
for transition in nfa_t_func:
    nfa_updatedt_func[transition[0]+1][nfa_letters.index(transition[1])+1] = transition[2]

counter=1

for i in range(nfa_states):
    nfa_t_func[i+1][0] = i

for i in nfa_letters:
    nfa_t_func[0][counter] = i
    counterw = counter + 1

# ===========DFA TFunc==========
counter=1

for i in dfa_letters:
    dfa_t_func.append([[], i, []])

for subset in powerset:
    if(subset != []):
        for letters in d_letters:
            answer = set([])
            for state in subset:
                answer = answer.union(set(nfa_t_func[state+1][dfa_letters.index(letters)+1]))
            if(len(x) == 0): 
                answer = []
            dfa_t_func.append([subset,letters, list(answer)])
        counter = counter + 1

finalanswer={'states':dfa_states, "letters":dfa_letters, "t_func":dfa_t_func, "start": dfa_start, "final":dfa_final}
f=open("output.json","w").write()
json.dumps(finalanswer, f)

