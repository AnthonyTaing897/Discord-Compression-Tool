import random
import string

characters = string.ascii_letters + string.digits

def gen_code(length):
    return ''.join(random.choice(characters) for _ in range(length))

def gen_sessCode(length=6, database=None):       
    code = gen_code(length)

    if(database):
        database.get_all_records()
        for record in database.get_all_records():
            if record['Given Code'] == code:
                return gen_sessCode(length,database)
        
    return code
    
def gen_sessID(length=10, database=None):        
    code = gen_code(length)

    if(database):
        database.get_all_records()
        for record in database.get_all_records():
            if record['Session ID'] == code:
                return gen_sessID(length,database)
        
    return code

