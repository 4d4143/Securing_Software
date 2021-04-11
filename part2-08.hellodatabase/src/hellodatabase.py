#!/usr/bin/env python3
import sys
import sqlite3


def read_database(conn):

	# output should be a list of pairs
	# agents = [(id1, name1), (id2, name2), (id3, name3), ...] ordered by id
	queryStatement = "SELECT id, name FROM Agent"
	query = conn.execute(queryStatement).fetchall()
	query.sort()

	# write code here

	return query



def main(argv):
	name = sys.argv[1]
	conn = sqlite3.connect(name)
	agents = read_database(conn)
	for agent in agents:
		print(agent[0], agent[1])

# This makes sure the main function is not called immediatedly
# when TMC imports this module
if __name__ == "__main__": 
	if len(sys.argv) != 2:
		print('usage: python %s database' % sys.argv[0])
	else:
		main(sys.argv)
