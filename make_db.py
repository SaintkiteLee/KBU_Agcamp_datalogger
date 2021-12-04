import sqlite3

conn = sqlite3.connect('database.sqlite3')

conn.execute(
'''
create table test_log (date text, time text, temp_a real, temp_b real, humidity_a integer , humidity_b int, co2 int )
'''
)