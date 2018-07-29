import psycopg2
from datetime import datetime
from password_pi import password, public_ip

def testDB():
    try:
        
        # conn = psycopg2.connect(database="test", user="pi", password=password, host=public_ip,
        #                         port="50850")
        conn = psycopg2.connect(database="test", user="pi", password=password, host="127.0.0.1",
                                port="5432")
    except Exception as e:
        print(e)
    else:
        cur = conn.cursor()
        sql = "SELECT * from people;"
        cur.execute(sql)
        for record in cur:
            print(record)
        conn.commit()
        conn.close()
        cur.close()
def store_viewers_to_table(streamer_name, viewers):
    try:
        conn = psycopg2.connect(database="twitch", user="pi", password=password, host="127.0.0.1",
                                port="5432")
        #conn = psycopg2.connect(database="twitch", user="pi", password=password, host=public_ip,
        #    port="50850")
    except:
        print("I am unable to connect to the database")
    else:
        cur = conn.cursor()
        try:
            table_name = str(streamer_name) + "_" + str(datetime.now().strftime('%Y%m%d%H%M%S'))
            print("CREATE TABLE " + str(table_name) + " (name varchar PRIMARY KEY);")
            cur.execute("CREATE TABLE " + str(table_name) + " (name varchar PRIMARY KEY);")
            try:
                sql = "INSERT INTO " + table_name + " (name) VALUES \n"
                for viewer in viewers[0:-2]:
                    sql += "('" + str(viewer) + "'), \n"
                sql += "('" + str(viewers[-1]) + "');"
                # print(sql)
                cur.execute(sql)

            except:
                print("I can't insert!")
        except:
            print("I can't drop our test database!")

        conn.commit()  # <--- makes sure the change is shown in the database
        conn.close()
        cur.close()
def store_viewers_to_table_array(streamer_name, viewers):
    try:
        conn = psycopg2.connect(database="twitch_new", user="pi", password=password, host="127.0.0.1",
                                port="5432")
        #conn = psycopg2.connect(database="twitch", user="pi", password=password, host=public_ip,
        #    port="50850")
    except:
        print("I am unable to connect to the database")
    else:
        cur = conn.cursor()
        try:
            table_name = str(streamer_name)
            print("CREATE TABLE IF NOT EXISTS " + str(table_name) + " (datetime timestamp PRIMARY KEY, viewers varchar[]);")
            cur.execute("CREATE TABLE IF NOT EXISTS " + str(table_name) + " (datetime timestamp PRIMARY KEY, viewers varchar[]);")
            try:
                sql = "INSERT INTO " + table_name + " (datetime, viewers) VALUES (%s, %s)"
                dt = datetime.now()
                cur.execute(sql, (dt, viewers))
            except Exception as e:
                print("I can't insert!", e)
        except Exception as e:
            print("I can't drop our test database!", e)

        conn.commit()  # <--- makes sure the change is shown in the database
        conn.close()
        cur.close()
def get_viewer_table_for_streamer(streamer_name, limit=1):
    try:
        conn = psycopg2.connect(database="twitch_new", user="pi", password=password, host="127.0.0.1",
                                port="5432")
        #conn = psycopg2.connect(database="twitch", user="pi", password=password, host=public_ip,
        #    port="50850")
    except:
        print("I am unable to connect to the database")
    else:
        cur = conn.cursor()
        try:
            table_name = str(streamer_name)

            sql = "SELECT * FROM " + str(table_name) + " ORDER BY datetime DESC LIMIT " + str(limit) + ";"
            cur.execute(sql)
            for record in cur:
                print(record[1][0:10])
        except Exception as e:
            print("I can't read", e)
        conn.commit()  # <--- makes sure the change is shown in the database
        conn.close()
        cur.close()


if __name__ == '__main__':
    # testDB()
    # store_viewers_to_table_array('test_streamer_name', ['mydude', 'wow_such_viewer_name'])
    get_viewer_table_for_streamer('asmongold')