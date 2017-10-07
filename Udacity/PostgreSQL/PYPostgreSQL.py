#!/usr/bin/env python2.7
import psycopg2


def main():
    ''' Connect to database, create cursor and call three functions
    '''
    conn = psycopg2.connect(database="news",
                            user="user1", password="password",
                            host="127.0.0.1", port="5432")
    print "Connection to database established\n"
    cur = conn.cursor()
    problemOne(cur)
    problemTwo(cur)
    problemThree(cur)
    conn.close()
    print "\nAll operations done successfully"


def problemOne(cur):
    ''' Excute the SQL statement for problem one
        Args:
            param1 (cursor): connection info to DB and execute SQL commands
    '''
    print "1. What are the most popular three articles of all time?"
    cur.execute('''SELECT title, views
                FROM articles, get_the_count
                WHERE get_the_count.slug = articles.slug
                ORDER by views DESC
                LIMIT 3;''')
    rows = cur.fetchall()
    for title, views in rows:
        print "{} - {} views".format(title, views)


def problemTwo(cur):
    ''' Excute the SQL statement for problem two
        Args:
            param1 (cursor): connection info to DB and execute SQL commands
    '''
    print "\n2. Who are the most popular article authors of all time?"
    cur.execute('''SELECT name, SUM(viewed) AS viewed
                FROM articles, authors, viewed_article
                WHERE articles.author = authors.id
                and viewed_article.slug = articles.slug
                GROUP by name
                ORDER by viewed DESC;''')
    rows = cur.fetchall()
    for row in rows:
        print row[0], '\t -', row[1], 'views'


def problemThree(cur):
    ''' Excute the SQL statement for problem three
        Args:
            param1 (cursor): connection info to DB and execute SQL commands
    '''
    print "\n3. On which days did more than 1% of requests lead to errors?"
    cur.execute('''SELECT TO_CHAR(working.date,'MONTH DD, YYYY'),
                TRUNC(errors * 100.0 / (hits + errors), 2) AS percent
                FROM nonworking, working
                WHERE nonworking.date = working.date
                AND (errors * 100.0 /(hits + errors)) >= 1.0;''')
    rows = cur.fetchall()
    for row in rows:
        print row[0], ' - ', row[1], '%'


# make sure that the code is only run when this program
# is executed directly, and not when it is imported
# as a module
if __name__ == '__main__':
    main()
else:
    print "Run code directly"
