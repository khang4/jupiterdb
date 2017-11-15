import mysql.connector;

class _jupiter:
    #construct by giving name of database to connect to
    def __init__(self,database):
        self.connection=mysql.connector.connect(user="root",password="",host="127.0.0.1",database=database);
        self.cursor=self.connection.cursor();

    #GENERAL sql add function
    #add to give table all values in give array of values
    def add(self,table,values):
        valuestring="";
        for i,x in enumerate(values):
            valuestring+='''"{}"'''.format(x);

            if not i==len(values)-1:
                valuestring+=",";

        try:
            self.cursor.execute('''insert into {} values ({})'''.format(table,valuestring));
            self.connection.commit();

        except mysql.connector.Error as err:
            print(err);

    def update(self,table,key,id,col,value):
        try:
            self.cursor.execute('''update {} set {}="{}" where {}="{}"'''.format(
                table,col,value,key,id
            ));
            self.connection.commit();

        except mysql.connector.Error as err:
            print(err);