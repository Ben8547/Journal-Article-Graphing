from RetrieveData import file_path
import pickle
from numpy import zeros, save

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

    Adjacency = zeros((n,n)) # make an n by n matrix to store adjacency matrix

    # each row and column of the matrix represents a paper.
    # If entry (i,j) has a 0 that mean that paper i does not reference paper j
    # If entry (i,j) has a 1 then i does reference j

    for i in range(n): # there is probably a quicker way to do this though I am not sure what it would be
        for j in range(n):
            if papers[j] in simplifiedData[papers[i]]:
                Adjacency[i,j] = 1

    save("Adjacency.npy",Adjacency) # save the matrix to a binary file

    print("File Saved")
