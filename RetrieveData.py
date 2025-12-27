import pickle
from pyalex import Works, Authors, Sources, Institutions, Topics, Publishers, Funders
import pyalex as alex

email = "example@gmail.com" # remove before publishing

alex.config.email = email # The polite pool has much faster and more consistent response times

# note that the original Leon Chua paper on Memristors is given by https://doi.org/10.1109/TCT.1971.1083337

'''
General Idea:

1. Use Alex to grab all papers published since 1971 - date of Chua paper
    - Electrical engineering is a "concept" in Alex. We can sort by concepts

2. Store the relevant information - Alex ID and Referenced IDs to a file (pickle file since it can just be loaded by python again)

'''

ee_works_query = Works().filter(
    #concepts={"id": "C119599485"},
    publication_year = "1971-2025",
    title_and_abstract={"search": "memristor"}
) # This does not fetch results yet—it defines the query called ee_works.

#ee_works = ee_works_query.get() # returns a list of dictionaries - each dictionary contains the information of an entire work

#n = len(ee_works) # number of works
#print("%i works found"%n)

simplified_data = [] # empty list

for work in ee_works_query.paginate(per_page=200): # paginate allows us to view all of the hits, not just the first n like .get()
    # work is a list - it stores the dictionaries of a sungle page
    for i in range(len(work)):
        simplified_data.append({
            work[i]["id"]: work[i]["referenced_works"] # appends a dictionary with the work and its references
        })

file_path = './article_dependancy_dictionary'
with open(file_path, 'wb') as file: # context reader opens and closes file
    pickle.dump(simplified_data, file)

print('saved to file')