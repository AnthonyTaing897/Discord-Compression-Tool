import random
import string

characters = string.ascii_letters + string.digits

def gen_sessCode(length=6, connection=None):       
    code = gen_code(length)

    if(connection):
        cursor = connection.cursor()
        cursor.execute("SELECT session_code FROM sessions WHERE session_code = ?", (code,))

        if(cursor.fetchone()):
            return gen_sessCode(length,connection)
        
    return code
    
def gen_sessID(length=10, connection=None):        
    code = gen_code(length)

    if(connection):
        cursor = connection.cursor()
        cursor.execute("SELECT session_id FROM sessions WHERE session_id = ?", (code,))

        if(cursor.fetchone()):
            return gen_sessID(length,connection)
        
    return code

def gen_code(length):
    



    return ''.join(random.choice(characters) for _ in range(length))