"""
some docstring
password=hello
no issue
"""
from Crypto.Cipher import AES
import base64
import os

import mysql.connector
import pymysql
import psycopg2
import pgdb
import pg

from flask import Flask


secret_key = '1234567890123456'
something = something()
def getDecrypted(encodedtext):
    cipher = AES.new(secret_key, AES.MODE_ECB)
    return cipher.decrypt(base64.b64decode(encodedtext))

class A:
    """
    password=azerty123
    OK
    """
    passed = "passed"
    password = "azerty123" 
    password = "azerty123" 
    fieldNameWithPasswordInIt = "password" 
    fieldNameWithPasswordInIt = "" 
    user, password = get_credentials()
    (a, b) = ("some", "thing")

    def __init__(self):
        """
        password=azerty123
        OK
        """
        self.passed = "passed"
        fieldNameWithPasswordInIt = "azerty123"            
        fieldNameWithPasswordInIt = os.getenv("password", "")  
        self.fieldNameWithPasswordInIt = "azerty123"            
        self.fieldNameWithPasswordInIt = os.getenv("password", "")  

    def a(self,pwd="azerty123", other=None):  

        var1 = 'admin'
        var1 = 'user=admin&password=Azerty123'        
        var1 = 'user=admin&passwd=Azerty123'          
        var1 = 'user=admin&pwd=Azerty123'             
        var1 = 'user=admin&password='                   
        var1 = 'user=admin&password= '                  
        var1 = "user=%s&password=%s" % "Password123"    
        var1 = "user=%s&password=%s" % pwd              
        var1 = f"&password={pwd}"                       
        var1 = f"&password='{pwd}'"                     
        var1 = "&password=?"                            
        var1 = "&password=:password"                    
        var1 = "&password=:param"                       
        var1 = "&password='"+pwd+"'"                    
        var1 = f"&password={pwd}"                       
        var1 = "&password={something}"                  

        url = "http://user:azerty123@domain.com"      
        url = "https://user:azerty123@domain.com"      
        url = "ftp://user:azerty123@domain.com"      
        url = "http://user:@domain.com"               
        url = "http://user@domain.com:80"             
        url = "http://user@domain.com"                
        url = "http://domain.com/user:azerty123"      
        url = "ssh://domain.com/user:azerty123"      
        url = "unknown://domain.com/user:azerty123"      

        username = 'admin'        
        password = pwd
        password = 'azerty123'                                    
        password = "azerty123"                                    
        password = '''azerty123'''                                
        password = """azerty123"""                                
        password = u'azerty123'                                   
        password = f"azerty123"                                   
        password = b"azerty123"                                   
        password = "?"                                            
        variableNameWithPasswordInIt = 'azerty123'                
        variableNameWithPassphraseInIt = 'azerty123'              
        variableNameWithPasswdInIt ='azerty123'                   
        variableNameWithPwdInIt ='azerty123'                      
        variableNameWithPasswordInItEmpty = ""                    

        
        
        json_password = "password"                                
        pwd = "pwd"                                               
        PASSWORD = "Password"                                     
        PASSWORD_INPUT = "[id='password']"                        
        PASSWORD_PROPERTY = "custom.password"                     
        TRUSTSTORE_PASSWORD = "trustStorePassword"                
        CONNECTION_PASSWORD = "connection.password"               
        RESETPWD = "/users/resetUserPassword"                     

        if password == 'Azerty123': 
            pass
        elif password.__eq__('Azerty123'): 
            pass
        elif 'Azerty123'.__eq__(password): 
            pass

        hash_map = { 'password': "azerty123"} 
        hash_map = { ("a", "b") : "c"} 
        hash_map = { something : "c"} 
        hash_map = {'admin_form' : adminForm, **self.admin.context(request),} 
        hash_map = { 'password': pwd} 
        hash_map = { 'password': "password"} 
        hash_map['db_password'] = "azerty123" 
        hash_map['db_password'] = pwd 
        hash_map['something'] = "azerty123" 
        hash_map[something] = "something" 
        hash_map['password'] = 'password' 

        encoded_user = 'gUhd9TxpnQppnZVAf7cv9pa5sgRo2sFmShrr/NK9dz0='
        encoded_password = 'gUhd9TxpnQppnZVAf7cv9uVnoE28Vq0bR2Cx6Ku1UQA=' 
        username = getDecrypted(encoded_user)                       
        password = getDecrypted(encoded_password)                   
    
    def db(self, pwd):
        mysql.connector.connect(host='localhost', user='root', password='Azerty123')  
        mysql.connector.connection.MySQLConnection(host='localhost', user='root', password='password')  
        mysql.connector.connect(host='localhost', user='root', password=pwd)  
        mysql.connector.connection.MySQLConnection(host='localhost', user='root', password=pwd)  
        mysql.connector.connection.MySQLConnection(host='localhost', user='root', password='')  
        mysql.connector.connection.MySQLConnection(host='localhost', user='root', "")  

        pymysql.connect(host='localhost', user='root', password='Azerty123') 
        pymysql.connect('localhost', 'root', 'password') 
        pymysql.connections.Connection(host='localhost', user='root', password='password') 
        pymysql.connections.Connection('localhost', 'root', 'password') 
        pymysql.connect(host='localhost', user='root', password=pwd) 
        pymysql.connect('localhost', 'root', pwd) 
        pymysql.connections.Connection(host='localhost', user='root', password=pwd) 
        pymysql.connections.Connection('localhost', 'root', pwd) 
        pymysql.connect('localhost', 'root', '') 
        pymysql.connect(host='localhost', user='root', password='') 
        pymysql.connections.Connection(host='localhost', user='root', password='') 
        pymysql.connections.Connection('localhost', 'root', '') 

        psycopg2.connect(host='localhost', user='postgres', password='Azerty123') 
        psycopg2.connect(host='localhost', user='postgres', password=pwd,) 

        pgdb.connect(host='localhost', user='postgres', password='Azerty123') 
        pgdb.connect('localhost', 'postgres', 'password') 
        pgdb.connect(host='localhost', user='postgres', password=pwd) 
        pgdb.connect('localhost', 'postgres', pwd) 

        pg.DB(host='localhost', user='postgres', passwd='Azerty123') 
        pg.DB(None, 'localhost', 5432, None, 'postgres', 'password') 
        pg.DB(host='localhost', user='postgres', passwd=pwd) 
        pg.DB(None, 'localhost', 5432, None, 'postgres', pwd) 

        pg.connect(host='localhost', user='postgres', passwd='Azerty123') 
        pg.connect(None, 'localhost', 5432, None, 'postgres', 'password') 
        pg.connect(host='localhost', user='postgres', passwd=pwd) 
        pg.connect(None, 'localhost', 5432, None, 'postgres', pwd) 
        pg.connect(host='localhost', user='postgres', passwd='') 
        pg.connect(None, 'localhost', 5432, None, 'postgres', '') 

        random.call(None, password = 42) 
        random.call(None, password = "hello") 
        random.call(None, password = "") 
        pg.connect(*unpack, 'localhost', 5432, None, 'postgres', pwd) 

    

class PASSWORD(A):
    def getPassword(self, password):
        pass
    def somePassword(self, password=42):  
        pass
    def somePassword(self, password=""):  
        pass
    def somePassword(self, *, password="hello"): 
        pass

instance = A()
instance.db('password')

DATABASES = {
    'postgresql_db': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'quickdb',
        'USER': 'sonarsource',
        'PASSWORD': 'azerty123',                    
        'PASSWORD': os.getenv('DB_PASSWORD'),       
        'HOST': 'localhost',
        'PORT': '5432'
    },
    'any_other_key': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'quickdb',
        'USER': 'sonarsource',
        'PASSWORD': 'azerty123',                    
        'PASSWORD': os.getenv('DB_PASSWORD'),       
        'HOST': 'localhost',
        'PORT': '5432'
    }
}

dict1 = {'password': ''} 
dict2 = dict(password='AZURE_PASSWORD') 
dict3 = {'password': 'password'} 
dict4 = {"login_password": "password"} 
module.fail_json(msg="Password parameter is missing."
                                     " Please specify this parameter in task or"
                                     " export environment variable like 'export VMWARE_PASSWORD=ESXI_PASSWORD'") 
jim = User(username='jimcarry',password="password88") 
conn = pymssql.connect(server='yourserver', user='yourusername@yourserver',
             password='yourpassword', database='yourdatabase') 

def test_flask():
    app = Flask(__name__)
    app.config["SECRET_KEY"] = "foo"  
    app.config["SECURITY_PASSWORD_HASH"] = "sha512_crypt"  
    a, app.config["SECRET_KEY"] = "foo", "foo"  
    app.config["SECURITY_PASSWORD_HASH"], app.config["SECRET_KEY"] = "foo", "foo"  
