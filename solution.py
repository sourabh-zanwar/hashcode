import numpy as np

with open('data/a_example.txt') as f:
    data = f.readlines()


for i in range(len(data)):
    data[i] = data[i].split()
    for j in range(len(data[i])):
        data[i] = [int(x) for x in data[i]]
        
n_books = data[0][0]
n_lib = data[0][1]
n_days = data[0][2]
del data[0]
book_scores = np.array(data[0])
del data[0]

n_books_lib = []
n_signup_days = []
n_books_ship = []
books_in_lib = []
for i in range(n_lib):
    n_books_lib.append(data[0][0])
    n_signup_days.append(data[0][1])
    n_books_ship.append(data[0][2])
    del data[0]
    books_in_lib.append(data[0])
    del data[0]
del i,j
if not data:
    del data


n_books_lib = np.array(n_books_lib)
n_signup_days = np.array(n_signup_days)
n_books_ship = np.array(n_books_ship)