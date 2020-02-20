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





nb_days = [n_days]
for i in range(n_lib):
    nb_days.append(nb_days[i] - n_signup_days[order_of_lib[i]])
del nb_days[0]

nb_books = []
for i in range(n_lib):
    nb_books.append(int(nb_days[i]*n_books_ship[order_of_lib[i]]))




for i in range(len(order_books_in_lib)):
    order_books_in_lib[i] = order_books_in_lib[i][0:nb_books[i]]
    
    

for i in range(1,len(order_books_in_lib)):
    for j in range(0,i):
        order_books_in_lib[i] = [x for x in order_books_in_lib[i] if x not in order_books_in_lib[j]]



order_books_in_lib = [x for x in order_books_in_lib if x != []]
nb_lib = len(order_books_in_lib)

op = []
for i in range(len(order_of_lib)):
    op.append([order_of_lib[i],len(books_in_lib[i])])
    

out = []
for i in range(len(order_books_in_lib)):
    out.append([op[i], order_books_in_lib[i]])

for i in range(len(out)):
    for j in range(len(out[i])):
        for k in range(len(out[i][j])):
            out[i][j][k] = str(out[i][j][k])
        out[i][j] = [' '.join(out[i][j])]



with open('data/output/cout.txt','w') as f:
    f.write(str('{}\n'.format(nb_lib)))
    for i in range(len(out)):
        f.write('{}\n{}\n'.format(out[i][0][0],out[i][1][0]))
