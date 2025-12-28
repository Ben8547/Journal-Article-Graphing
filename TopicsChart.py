import pandas as pd
from pyalex import Works
import pyalex as alex
import os

file_name = "Topic_Counts.csv"

if not os.path.exists("./"+file_name): # get the data if it is not already stored
    print("Fetching Data")

    email = "example@gmail.com" # remove before publishing

    alex.config.email = email # The polite pool has much faster and more consistent response times

    file_path = './article_dependancy_dictionary'

    ee_works_query = Works().filter(
        #concepts={"id": "C119599485"},
        publication_year = "1971-2025",
        title_and_abstract={"search": "memristor"}
    ) # This does not fetch results yet—it defines the query called ee_works.

    #ee_works = ee_works_query.get() # returns a list of dictionaries - each dictionary contains the information of an entire work

    #n = len(ee_works) # number of works
    #print("%i works found"%n)

    Topics_counts = {} # empty dictionary

    #print(Works()["W2016922062"]["primary_topic"]) - a dictionary; want to extract "display_name" key
    #print(Works()["W2016922062"]["topics"]) - a list of dictionaries

    for work in ee_works_query.paginate(per_page=200): # paginate allows us to view all of the hits, not just the first n like .get()
        # work is a list - it stores the dictionaries of a sungle page
        for i in range(len(work)):
            if work[i]["primary_topic"] is not None: # in case a paper does not have a primary type
                if work[i]["primary_topic"]["display_name"] in Topics_counts.keys():
                    Topics_counts[work[i]["primary_topic"]["display_name"]] += 1
                else: # because the topic is new
                    Topics_counts[work[i]["primary_topic"]["display_name"]] = 1

            for j in range(len(work[i]["topics"])):
                if work[i]["topics"][j]["display_name"] in Topics_counts.keys():
                    Topics_counts[work[i]["topics"][j]["display_name"]] += 1
                else:
                    Topics_counts[work[i]["topics"][j]["display_name"]] = 1


    Topics_counts_data = pd.DataFrame(
        Topics_counts.items(),
        columns=["topic", "count"]
    )

    Topics_counts_data.sort_values(by="count")

    Topics_counts_data.to_csv("./" + file_name, index=False)

else: # the data is already saved
    print("Loading Data")
    Topics_counts_data = pd.read_csv("./" + file_name)

# plot a bar graph

import matplotlib.pyplot as plt

Topics_counts_data = Topics_counts_data[ Topics_counts_data["count"] >= 100 ]

plt.figure(figsize=(12,6))
plt.bar(Topics_counts_data["topic"], Topics_counts_data["count"],width=0.9)
plt.ylabel("Counts")
plt.xlabel("Topics")
plt.title("Topics of Memristor Papers")

plt.xticks(rotation=45, fontsize=8, ha='right')  # rotate labels 90 degrees

plt.tight_layout()  # adjust layout so labels fit

plt.show()
