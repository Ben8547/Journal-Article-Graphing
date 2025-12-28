# Journal-Article-Graphing

Here we use the OpenAlex API to graph the dependencies of journal articles referencing Leon Chua's seminal work on memristor theory. This will provide structure on which to base a literature review for an upcoming presentation I need to give.

We query all papers with the word memristor in their title or abstract and save the paper ID as well as citation IDs. Then we track save the connection structure in a sparse matrix and create a directed graph from the adhacency matrix. The graph and matrix can be visualized.
