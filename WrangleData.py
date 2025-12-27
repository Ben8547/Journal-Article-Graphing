

'''
General Idea:

1. Use Alex to grab all papers published since 1971 - date of Chua paper

2. Use ["referenced_works"] key to find all of the works referenced by each paper.

3. Create a graph of the data.

4. Take the subgraph including the Chua paper (only those papers referencing it in some path)

5. Find the most "impactful" papers - i.e. most densly connected in the subgraph
'''