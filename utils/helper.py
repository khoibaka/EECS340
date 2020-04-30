
def find_id_from_name(rows, name):
    for row in rows:
        if(row[1] == name):
            return row[0]
    return -1

def check_name_pk(rows,name):
    for row in rows:
        if(row[0] == name):
            return True
    return False