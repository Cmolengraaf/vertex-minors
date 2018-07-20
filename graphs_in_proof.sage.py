
# This file was *autogenerated* from the file graphs_in_proof.sage
from sage.all_cmdline import *   # import sage library

_sage_const_3 = Integer(3); _sage_const_2 = Integer(2); _sage_const_1 = Integer(1); _sage_const_0 = Integer(0); _sage_const_7 = Integer(7); _sage_const_6 = Integer(6); _sage_const_5 = Integer(5); _sage_const_4 = Integer(4)# This file builds a dictionary containing all the graphs considered in the proof of Theorem 4.3 and 4.5 in https://arxiv.org/abs/1805.05306 and then checks that these are not distance-hereditary

load("GraphClasses.sage")

G_dict={}

# Theorem 4.3

G_dict43={}

# Step 2

G=SimpleGraph({_sage_const_0 :[_sage_const_4 ,_sage_const_1 ],_sage_const_1 :[_sage_const_0 ,_sage_const_4 ,_sage_const_2 ,_sage_const_3 ],_sage_const_2 :[_sage_const_3 ,_sage_const_1 ],_sage_const_3 :[_sage_const_4 ,_sage_const_2 ,_sage_const_1 ],_sage_const_4 :[_sage_const_0 ,_sage_const_1 ,_sage_const_3 ]})
G_dict43[_sage_const_2 ]=[G]

# Step 3

G_dict43[_sage_const_3 ]=[]
G=SimpleGraph({_sage_const_0 :[_sage_const_4 ,_sage_const_1 ,_sage_const_2 ],_sage_const_1 :[_sage_const_0 ,_sage_const_5 ],_sage_const_2 :[_sage_const_0 ,_sage_const_3 ],_sage_const_3 :[_sage_const_4 ,_sage_const_2 ],_sage_const_4 :[_sage_const_5 ,_sage_const_3 ,_sage_const_0 ],_sage_const_5 :[_sage_const_4 ,_sage_const_1 ]})
edges=[(_sage_const_0 ,_sage_const_3 ),(_sage_const_0 ,_sage_const_5 ),(_sage_const_3 ,_sage_const_5 )]
for es in Subsets(edges):
    Gtmp=SimpleGraph(G)
    Gtmp.add_edges(es)
    G_dict43[_sage_const_3 ].append(Gtmp)

# Step 5

G=SimpleGraph({_sage_const_0 :[_sage_const_4 ,_sage_const_1 ],_sage_const_1 :[_sage_const_0 ,_sage_const_4 ,_sage_const_2 ,_sage_const_3 ],_sage_const_2 :[_sage_const_3 ,_sage_const_1 ],_sage_const_3 :[_sage_const_4 ,_sage_const_2 ,_sage_const_1 ],_sage_const_4 :[_sage_const_0 ,_sage_const_1 ,_sage_const_3 ]})
G_dict43[_sage_const_5 ]=[G]

G_dict["Thm43"]=G_dict43

# Theorem 4.5

G_dict45={}

# Step 1

G_dict45[_sage_const_1 ]=[]
G=SimpleGraph({_sage_const_0 :[_sage_const_1 ,_sage_const_2 ,_sage_const_3 ,_sage_const_5 ,_sage_const_4 ],_sage_const_1 :[_sage_const_2 ,_sage_const_3 ,_sage_const_0 ],_sage_const_2 :[_sage_const_5 ,_sage_const_3 ,_sage_const_1 ,_sage_const_0 ],_sage_const_3 :[_sage_const_4 ,_sage_const_2 ,_sage_const_1 ,_sage_const_0 ],_sage_const_4 :[_sage_const_3 ,_sage_const_0 ],_sage_const_5 :[_sage_const_2 ,_sage_const_0 ]})
edges=[(_sage_const_4 ,_sage_const_5 )]
for es in Subsets(edges):
    Gtmp=SimpleGraph(G)
    Gtmp.add_edges(es)
    G_dict45[_sage_const_1 ].append(Gtmp)

# Step 3

# Case 1

G=SimpleGraph({_sage_const_0 :[_sage_const_4 ,_sage_const_1 ],_sage_const_1 :[_sage_const_0 ,_sage_const_4 ,_sage_const_2 ,_sage_const_3 ],_sage_const_2 :[_sage_const_3 ,_sage_const_1 ],_sage_const_3 :[_sage_const_4 ,_sage_const_2 ,_sage_const_1 ],_sage_const_4 :[_sage_const_0 ,_sage_const_1 ,_sage_const_3 ]})
G_dict45[_sage_const_3 ]=[G]

# Case 2

# Subcase 1

G=SimpleGraph({_sage_const_0 :[_sage_const_2 ,_sage_const_1 ],_sage_const_1 :[_sage_const_4 ,_sage_const_2 ,_sage_const_0 ],_sage_const_2 :[_sage_const_1 ,_sage_const_0 ,_sage_const_3 ],_sage_const_3 :[_sage_const_2 ,_sage_const_4 ],_sage_const_4 :[_sage_const_1 ,_sage_const_3 ]})
G_dict45[_sage_const_3 ].append(G)

# Subcase 2

G=SimpleGraph({_sage_const_0 :[_sage_const_3 ,_sage_const_1 ],_sage_const_1 :[_sage_const_4 ,_sage_const_3 ,_sage_const_2 ,_sage_const_0 ],_sage_const_2 :[_sage_const_3 ,_sage_const_4 ,_sage_const_1 ],_sage_const_3 :[_sage_const_4 ,_sage_const_2 ,_sage_const_1 ,_sage_const_5 ,_sage_const_0 ],_sage_const_4 :[_sage_const_3 ,_sage_const_2 ,_sage_const_1 ,_sage_const_5 ],_sage_const_5 :[_sage_const_4 ,_sage_const_3 ]})
edges=[(_sage_const_0 ,_sage_const_5 )]
for es in Subsets(edges):
    Gtmp=SimpleGraph(G)
    Gtmp.add_edges(es)
    G_dict45[_sage_const_3 ].append(Gtmp)

# Subcase 3

# Subsubcase 1

G=SimpleGraph({_sage_const_0 :[_sage_const_2 ,_sage_const_1 ],_sage_const_1 :[_sage_const_4 ,_sage_const_2 ,_sage_const_0 ],_sage_const_2 :[_sage_const_1 ,_sage_const_0 ,_sage_const_3 ],_sage_const_3 :[_sage_const_2 ,_sage_const_4 ],_sage_const_4 :[_sage_const_1 ,_sage_const_3 ]})
G_dict45[_sage_const_3 ].append(G)

# Subsubcase 2

G=SimpleGraph({_sage_const_0 :[_sage_const_1 ,_sage_const_2 ,_sage_const_3 ,_sage_const_5 ,_sage_const_4 ,_sage_const_7 ,_sage_const_6 ],_sage_const_1 :[_sage_const_0 ,_sage_const_2 ,_sage_const_3 ,_sage_const_5 ],_sage_const_2 :[_sage_const_1 ,_sage_const_3 ,_sage_const_0 ,_sage_const_4 ],_sage_const_3 :[_sage_const_2 ,_sage_const_1 ,_sage_const_0 ,_sage_const_5 ,_sage_const_4 ],_sage_const_4 :[_sage_const_0 ,_sage_const_5 ,_sage_const_2 ,_sage_const_3 ,_sage_const_7 ],_sage_const_5 :[_sage_const_0 ,_sage_const_4 ,_sage_const_1 ,_sage_const_3 ,_sage_const_6 ],_sage_const_6 :[_sage_const_5 ,_sage_const_0 ],_sage_const_7 :[_sage_const_4 ,_sage_const_0 ]})
edges=[(_sage_const_6 ,_sage_const_7 ),(_sage_const_6 ,_sage_const_4 ),(_sage_const_6 ,_sage_const_2 ),(_sage_const_7 ,_sage_const_5 ),(_sage_const_7 ,_sage_const_1 )]
for es in Subsets(edges):
    Gtmp=SimpleGraph(G)
    Gtmp.add_edges(es)
    G_dict45[_sage_const_3 ].append(Gtmp)

# Step 5

# Case 1

G_dict45[_sage_const_5 ]=[]
G=SimpleGraph({_sage_const_0 :[_sage_const_3 ,_sage_const_1 ],_sage_const_1 :[_sage_const_4 ,_sage_const_3 ,_sage_const_2 ,_sage_const_0 ],_sage_const_2 :[_sage_const_3 ,_sage_const_4 ,_sage_const_1 ],_sage_const_3 :[_sage_const_4 ,_sage_const_2 ,_sage_const_1 ,_sage_const_5 ,_sage_const_0 ],_sage_const_4 :[_sage_const_3 ,_sage_const_2 ,_sage_const_1 ,_sage_const_5 ],_sage_const_5 :[_sage_const_4 ,_sage_const_3 ]})
edges=[(_sage_const_0 ,_sage_const_5 )]
for es in Subsets(edges):
    Gtmp=SimpleGraph(G)
    Gtmp.add_edges(es)
    G_dict45[_sage_const_5 ].append(Gtmp)

# Case 2

# Subcase 1

G=SimpleGraph({_sage_const_0 :[_sage_const_1 ,_sage_const_2 ,_sage_const_3 ,_sage_const_5 ,_sage_const_4 ],_sage_const_1 :[_sage_const_2 ,_sage_const_3 ,_sage_const_0 ],_sage_const_2 :[_sage_const_5 ,_sage_const_3 ,_sage_const_1 ,_sage_const_0 ],_sage_const_3 :[_sage_const_4 ,_sage_const_2 ,_sage_const_1 ,_sage_const_0 ],_sage_const_4 :[_sage_const_3 ,_sage_const_0 ],_sage_const_5 :[_sage_const_2 ,_sage_const_0 ]})
edges=[(_sage_const_4 ,_sage_const_5 )]
for es in Subsets(edges):
    Gtmp=SimpleGraph(G)
    Gtmp.add_edges(es)
    G_dict45[_sage_const_5 ].append(Gtmp)

# Subcase 2

G=SimpleGraph({_sage_const_0 :[_sage_const_1 ,_sage_const_2 ,_sage_const_3 ,_sage_const_4 ,_sage_const_5 ,_sage_const_6 ,_sage_const_7 ],_sage_const_1 :[_sage_const_0 ,_sage_const_2 ,_sage_const_3 ,_sage_const_5 ,_sage_const_4 ,_sage_const_7 ],_sage_const_2 :[_sage_const_0 ,_sage_const_1 ,_sage_const_3 ,_sage_const_4 ],_sage_const_3 :[_sage_const_0 ,_sage_const_1 ,_sage_const_2 ,_sage_const_4 ,_sage_const_5 ],_sage_const_4 :[_sage_const_0 ,_sage_const_2 ,_sage_const_3 ,_sage_const_7 ,_sage_const_1 ],_sage_const_5 :[_sage_const_0 ,_sage_const_1 ,_sage_const_3 ,_sage_const_6 ],_sage_const_6 :[_sage_const_0 ,_sage_const_5 ],_sage_const_7 :[_sage_const_0 ,_sage_const_4 ,_sage_const_1 ]})
edges=[(_sage_const_6 ,_sage_const_7 ),(_sage_const_6 ,_sage_const_4 ),(_sage_const_6 ,_sage_const_2 ),(_sage_const_7 ,_sage_const_5 ),(_sage_const_4 ,_sage_const_5 )]
for es in Subsets(edges):
    Gtmp=SimpleGraph(G)
    Gtmp.add_edges(es)
    G_dict45[_sage_const_5 ].append(Gtmp)

G_dict["Thm45"]=G_dict45


####################################################
# Check that all graphs are not distance-hereditary
####################################################


fail=False
for Thm_dict in G_dict.values():
    for G_list in Thm_dict.values():
        for G in G_list:
            if G.is_DH():
                print("Graph for {} at step {} is distance-hereditary!")
                fail=True
if not fail:
    print("All graphs in Theorems 4.3 and 4.5 are not distance-hereditary.")
