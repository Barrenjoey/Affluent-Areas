import psycopg2


# def Content():
#     TOPIC_DICT = {"Basics":[[]]}
#     return TOPIC_DICT

try:
    conn = psycopg2.connect("dbname='template1' user='dbuser' host='localhost' password='dbpass'")
except:
    print("I am unable to connect to the database")