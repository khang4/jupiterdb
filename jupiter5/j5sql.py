import mysql.connector;

class _jupiter:
    #construct by giving name of database to connect to
    def __init__(self,database):
        self.connection=mysql.connector.connect(user="root",password="",host="127.0.0.1",database=database);
        self.cursor=self.connection.cursor();

    #GENERAL sql add function
    #give it table name to add to and array of arrays of values, it will add each
    #array in values as a seperate row
    def add(self,table,values):
        valuestring="";
        for iy,y in enumerate(values):
            valuestring+="(";

            for ix,x in enumerate(y):
                valuestring+='''"{}"'''.format(x);

                if not ix==len(y)-1:
                    valuestring+=",";

            valuestring+=")";

            if not iy==len(values)-1:
                valuestring+=",";

        try:
            self.cursor.execute('''insert into {} values {}'''.format(table,valuestring));
            self.connection.commit();

        except mysql.connector.Error as err:
            print(err);

    #GENERAL sql update function
    #give it table name, primary key to match with id, col to change and new value to put in
    def update(self,table,key,id,col,value):
        try:
            self.cursor.execute('''update {} set {}="{}" where {}="{}"'''.format(
                table,col,value,key,id
            ));
            self.connection.commit();

        except mysql.connector.Error as err:
            print(err);

    #return the highest id value of the given table and correct
    #primary key for that table, only applicable FOR TABLES that
    #HAVE INTEGER IDS FOR PRIMARY KEY!!!!!
    def getLastId(self,table,primaryKey):
        try:
            self.cursor.execute("select max({}) from {}".format(primaryKey,table));

            for x in self.cursor:
                return x[0];

        except mysql.connector.Error as err:
            print(err);
            return -1;