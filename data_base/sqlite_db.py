import sqlite3 as sq


async def sql_start():
    global base, cur
    base = sq.connect('./data/database.db')
    cur = base.cursor()
    if base:
        print('Data base connect OK!')
    base.commit()


async def user_exists(user_id):
    with base:
        result = cur.execute("SELECT * FROM users WHERE user_id = ?", (user_id,)).fetchmany(1)
        base.commit()
        return bool(len(result))
        

async def add_user(user_id, user_name, user_firstname, user_lastname):
    with base:
        cur.execute("INSERT INTO users (user_id, user_name, user_firstname, user_lastname) VALUES (?, ?, ?, ?)", (user_id, user_name, user_firstname, user_lastname,))
        

async def get_date_ot(user_id):
    with base:
        return cur.execute("SELECT OT FROM users WHERE user_id = ?", (user_id,)).fetchone()
        

async def get_date_pb(user_id):
    with base:
        return cur.execute("SELECT PB FROM users WHERE user_id = ?", (user_id,)).fetchone()

async def get_date_eb(user_id):
    with base:
        return cur.execute("SELECT EB FROM users WHERE user_id = ?", (user_id,)).fetchone()

async def get_date_pjb(user_id):
    with base:
        return cur.execute("SELECT PJB FROM users WHERE user_id = ?", (user_id,)).fetchone()

async def get_date_pjb1(user_id):
    with base:
        return cur.execute("SELECT PJB1 FROM users WHERE user_id = ?", (user_id,)).fetchone()

async def get_date_opmb(user_id):
    with base:
        return cur.execute("SELECT OPMB FROM users WHERE user_id = ?", (user_id,)).fetchone()
    
async def get_date_med_osm(user_id):
    with base:
        return cur.execute("SELECT MED_OSM FROM users WHERE user_id = ?", (user_id,)).fetchone()
    
async def get_all_users():
    with base:
        users = cur.execute("SELECT user_id FROM users").fetchall()
        return [user[0] for user in users]
