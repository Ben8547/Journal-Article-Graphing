from RetrieveData import file_path
import pickle
from numpy import ones
from scipy.sparse import csr_matrix, save_npz

'''
General Idea:

1. Use Alex to grab all papers published since 1971 - date of Chua paper - import the pickle file

3. Create a graph of the data.
    - construct an adjacency matrix: should be for a directed graph

4. Take the subgraph including the Chua paper (only those papers referencing it in some path)

5. Find the most "impactful" papers - i.e. most densly connected in the subgraph
'''
with open(file_path, 'rb') as file: # use context manager to load the dictionary safely
    simplifiedData  = pickle.load(file)

if __name__ == "__main__":
    print('file loaded')

# make a list of all of the loaded papers

papers = list(simplifiedData) # list(dict) makes a list of the keys
n = len(simplifiedData) # number of papers

if __name__ == "__main__":

    # each row and column of the matrix represents a paper.
    # If entry (i,j) has a 0 that mean that paper i does not reference paper j
    # If entry (i,j) has a 1 then i does reference j

    rows = []
    cols = []

    paper_index = {paper: i for i, paper in enumerate(papers)}

    for i, paper in enumerate(papers):
        for cited in simplifiedData[paper]:
            if cited in paper_index:
                rows.append(i)
                cols.append(paper_index[cited])

    data = ones(len(rows), dtype=bool)

    Adjacency = csr_matrix(
        (data, (rows, cols)), shape=(n, n)
    ) # make an n by n matrix to store adjacency matrix; bool decreases each entry from 8 bits to 1. The matrix is sparse so by using a scipy sparse matrix we can decrease the size as well.
    # storing as a boolean sparse matix decreased the size about 3000 fold (~700 MB -> 248 KB )

    save_npz("Adjacency.npz",Adjacency) # save the matrix to a binary file

    print("File Saved")
