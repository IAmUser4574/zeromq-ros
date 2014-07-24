
import rethinkdb as r


class Db(object):

    def __init__(self, host="localhost", port=28015, db_name="zmqros"):
        self.host = host
        self.port = port
        self.db_name = db_name
        self.primary_key = "id"
        self.secondary_index = "name"
        self.config_table_name = "configuration"
        self.create()

    def create(self):
        conn = self.connect()

        db_list = r.db_list().run(conn)

        db_created = False
        table_created = False

        if not self.db_name in db_list:
            r.db_create(self.db_name).run(conn)
            db_created = True

        table_list = r.db(self.db_name).table_list().run(conn)

        if not self.config_table_name in table_list:
            r.db(self.db_name).table_create(
                self.config_table_name, primary_key=self.primary_key
            ).run(conn)

            r.db(self.db_name).table(self.config_table_name)\
                .index_create(self.secondary_index).run(conn)

            table_created = True

        return {"db": db_created, "table": table_created}

    def connect(self):
        return r.connect(host=self.host, port=self.port)

    def put_config(self, config):
        conn = self.connect()
        db_out = self.get_table(self.config_table_name)\
            .insert(config).run(conn)
        return db_out

    def get_table(self, table_name):
        return r.db(self.db_name).table(table_name)

    def get_config(self):
        ret_list = list()
        conn = self.connect()
        config_data = self.get_table(self.config_table_name).run(conn)

        for document in config_data:
            ret_list.append(document)

        return ret_list

    def get_address(self, name):
        conn = self.connect()
        addr_data = self.get_table(self.config_table_name)\
            .get_all(name, index=self.secondary_index).nth(0).run(conn)

        return addr_data
