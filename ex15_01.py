#Counting Organizations
#This application will read the mailbox data (mbox.txt) and count the number of
#email messages per organization (i.e. domain name of the email address) using
#a database with the following schema to maintain the counts.

import sqlite3

conn = sqlite3.connect('orgdb.sqlite')
cur = conn.cursor()

cur.execute('DROP TABLE IF EXISTS Counts')

cur.execute('''
CREATE TABLE Counts (org TEXT, count INTEGER)''')  # Counts is table name!

fname = input('Enter file name: ')
if (len(fname)<1): fname = 'mbox-short.txt'
fh = open(fname)


for line in fh:
    if not line.startswith('From: '): continue
    pieces = line.split('@')
    org = pieces[1] #grab the email part

    #Read this like a file                     #Like a dictionary:
    cur.execute('SELECT count FROM counts WHERE org = ? ', (org,))
                                #? == place holder    #(email,) == is a tuple with one item
    row = cur.fetchone() #row is the information that we get from the data base

    #if the row is empty
    if row is None:
        #insert into the table the email ?
        cur.execute('''INSERT INTO Counts (org, count)
                VALUES (?, 1)''', (org,)) #like a dictionary here~
    #if row exists, update counts
    else:
        cur.execute('UPDATE Counts SET count = count + 1 WHERE org = ?',
                    (org,))
    conn.commit()

#https://wwww.sqlite.org/lang_select.html

sqlstr = 'SELECT org, count FROM Counts ORDER BY count DESC LIMIT 10'

for row in cur.execute(sqlstr):
    print(str(row[0]), row[1])

cur.close()
