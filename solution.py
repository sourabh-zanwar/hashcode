import numpy as np



with open('data/a.txt') as f:
    data = f.readlines()
for i in range(len(data)):
    data[i] = data[i].split()
    for j in range(len(data[i])):
        data[i] = [int(x) for x in data[i]]        
n_books = data[0][0]
n_lib = data[0][1]
n_days = data[0][2]
del data[0]
book_value = np.array(data[0])
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


books_in_lib_score = []
for i in range(len(books_in_lib)):
    books_in_lib_score.append([])
    for j in range(len(books_in_lib[i])):
        books_in_lib_score[i].append(book_value[books_in_lib[i][j]])

book_scores = []
for i in range(len(books_in_lib)):
    book_scores.append(sum(books_in_lib_score[i]))
lib_scores = book_scores/((n_books_ship/n_books_lib)+n_signup_days)
lib_scores = lib_scores.tolist()
order_of_lib = []
for i in range(len(lib_scores)):
    order_of_lib.append((lib_scores.index(max(lib_scores))))
    lib_scores[order_of_lib[i]] = 0
    

order_books_in_lib = []
for i in range(len(books_in_lib)):
    order_books_in_lib.append([])
    for j in range(len(books_in_lib[i])):
        p = books_in_lib_score[i].index(max(books_in_lib_score[i]))
        order_books_in_lib[i].append(books_in_lib[i][p])
        books_in_lib_score[i][p] = 0
del i,j,lib_scores,books_in_lib_score,p




for i in range(1,len(order_books_in_lib)):
        order_books_in_lib[i] = 
        











