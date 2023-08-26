import aiosqlite as sq

class DBManager:
    def __init__(self):
        self.base = None
        self.cur = None

    async def start(self):
        self.base = await sq.connect('/data/database.db')
        self.cur = await self.base.cursor()
        if self.base:
            print('Подключение к базе данных выполнено успешно!')
        await self.base.commit()
        return self

    async def close(self):
        await self.base.close()

    async def user_exists(self, user_id):
            result = await (await self.cur.execute("SELECT * FROM users WHERE user_id = ?", (user_id,))).fetchmany(1)
            await self.base.commit()
            return bool(len(result))

    async def add_user(self, user_id, user_name, user_firstname, user_lastname):
            await self.cur.execute("INSERT INTO users (user_id, user_name, user_firstname, user_lastname) VALUES (?, ?, ?, ?)", (user_id, user_name, user_firstname, user_lastname,))
            await self.base.commit()

    async def get_date_ot(self, user_id):        
            return await (await self.cur.execute("SELECT OT FROM users WHERE user_id = ?", (user_id,))).fetchone()

    async def get_date_pb(self, user_id):
            return await (await self.cur.execute("SELECT PB FROM users WHERE user_id = ?", (user_id,))).fetchone()

    async def get_date_eb(self, user_id):
            return await (await self.cur.execute("SELECT EB FROM users WHERE user_id = ?", (user_id,))).fetchone()

    async def get_date_pjb(self, user_id):
            return await (await self.cur.execute("SELECT PJB FROM users WHERE user_id = ?", (user_id,))).fetchone()

    async def get_date_pjb1(self, user_id):
            return await (await self.cur.execute("SELECT PJB1 FROM users WHERE user_id = ?", (user_id,))).fetchone()

    async def get_date_opmb(self, user_id):
            return await (await self.cur.execute("SELECT OPMB FROM users WHERE user_id = ?", (user_id,))).fetchone()
    
    async def get_date_med_osm(self, user_id):
            return await (await self.cur.execute("SELECT MED_OSM FROM users WHERE user_id = ?", (user_id,))).fetchone()
    
    async def get_all_users(self):
            users = await (await self.cur.execute("SELECT user_id FROM users")).fetchall()
            return [user[0] for user in users]
