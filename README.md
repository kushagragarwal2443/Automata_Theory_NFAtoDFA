# Automata_Theory_NFAtoDFA
Converts a Non-Deterministic Finite Machine to a Deterministic Finite Machine | Automata Theory (A19)

### Refer to report.pdf for a detailed analysis ###

## Explanation ##

Replace the example file  __*input.json*__  with your NFA in a similar json format.

{

    "states" : 2,
    
    "letters" : ["a", "b"],
    
    "t_func" : [[1, "a", [1]],[0, "b", [0,1]] ],
    
    "start" : 0,
    
    "final" : [0]
    
}

Execute the script  __*mycode.py*__  to see the DFA formed in the file output.json
