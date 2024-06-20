import cookbook

conn = cookbook.connect()
cursor = conn.cursor()

score = input('Enter the value: ')
if score == 'None' or score == '':
    score = None
operator = 'IS' if score is None else '=' # for equality

# operator = 'IS NOT' is score is None else '<>' # for inequality

cursor.execute("SELECT * FROM expt WHERE score {} %s".format(operator), (score,))

print(cursor.fetchall())

cursor.close()
