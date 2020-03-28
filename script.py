import json
import numpy as np

f=open("input.json","r")
r=f.read()
nfa=json.loads(r)
f.close()

nfa["states"]=nfa["states"]
nfa["letters"]=nfa["letters"]
nfa_start=nfa["start"]
nfa_final=nfa["final"]
nfa_t_func=nfa["t_func"]

nfa_updatedt_func=[[[] for i in range(len(nfa["letters"])+1)] for j in range(nfa["states"]+1)]
dfa_t_func=[[[] for i in range(len(dfa["letters"])+1)] for j in range(dfa_states+1)]

superset=[]
dfa_states = 2**nfa["states"]
dfa["letters"] = nfa["letters"]
dfa_start = nfa["start"]
dfa_final = []
states = [i for i in range(nfa["states"])]
for i in range(2**nfa["states"]):
    superset.append([states[j] for j in range(nfa["states"]) if (i & (2**j))])

for finalstate in nfa_final:
    for i in superset:
        if(i!=[]): 
            for elements in i:
                if(finalstate == elements):
                    dfa_final.append(i)
dfa_finalstates=[]
for sets in dfa_final:
    if sets not in dfa_finalstates:
        dfa_finalstates.append(sets)
     
dfa_final = dfa_finalstates
   
for transition in nfa_t_func:
    nfa_updatedt_func[transition[0]+1][nfa["letters"].index(transition[1])+1] = transition[2]

counter=1

for i in range(nfa["states"]):
    nfa_updatedt_func[i+1][0] = i

for i in nfa["letters"]:
    nfa_updatedt_func[0][counter] = i
    counter = counter + 1

counter=1
dfa_t_func=[]

for i in dfa["letters"]:
    dfa_t_func.append([[], i, []])

for ss in superset:
    if(ss != []):
        for letters in dfa["letters"]:
            answer = set([])
            for state in ss:
                answer = answer.union(set(nfa_updatedt_func[state+1][dfa["letters"].index(letters)+1]))
            if(len(answer) == 0): 
                answer = []
            dfa_t_func.append([ss,letters, list(answer)])
        counter = counter + 1

finalanswer={'states':dfa_states, "letters":dfa["letters"], "t_func":dfa_t_func, "start": dfa_start, "final":dfa_final}
jso=json.dumps(finalanswer)
f=open("output.json","w")
h=f.write(jso)
f.close()

