import time
import threading


def do_something():
	print('Sleeping 1 second...')
	time.sleep(1)
	print('Done Sleeping...')



def Main():
	start = time.perf_counter()
###############Traditional Maneual method of threading ##########
	# create two threads for each function, pass through target function (unexecuted)
#	t1 = threading.Thread(target=do_something)
#	t2 = threading.Thread(target=do_something)

	# apply start method to each thread

#	t1.start()
#	t2.start()

	# run join methods to ensure completion

#	t1.join()
#	t2.join()


###################Using a loop########################
	
	# create a list of threads
#	threads = []


	# Underscore is a throw away variable to loop over 10 items
#	for _ in range(10):
#		t = threading.Thread(target=do_something)
#		t.start()
#
	# loop through the list and join the threads
#	for thread in threads:
#		thread.join()

#	finish = time.perf_counter()
#	print(f'Finished in {round(finish-start, 2)} seconds')

################################Pass in arguments########################

# Function requireing an argument
	def do_something_specific(second):
		print(f'Sleeping {second}second(s)...')
		time.sleep(second)
		print('Done Sleeping...')

# create a list of threads
	threads = []

# create new threads accepting arguments
	for _ in range(10):
		# pass in arguments through a list
		t = threading.Thread(target=do_something_specific, args=[1.5])
		t.start()
		threads.append(t)


	for thread in threads:
		thread.join()
	

	finish = time.perf_counter()
	print(f'Finished in {round(finish-start, 2)} seconds')


if __name__ == '__main__':
	Main()