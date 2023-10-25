import datetime
import time
# import threading
# import random


################################################################################
#   Watchdog to stop tasks
################################################################################
# class Watchdog(threading.Thread):

# 	period = -1
# 	current_cpt = -1

#     	############################################################################
# 	def __init__(self, period):

# 		self.period = period
		
# 		threading.Thread.__init__(self)


#     	############################################################################
# 	def run(self):

# 		print(" : Starting watchdog")

# 		self.current_cpt = self.period

# 		while (1):

# 			if(self.current_cpt >= 0):

# 				self.current_cpt -= 1
# 				time.sleep(1)
				
# 			else :
# 				print("!!! Watchdog stops tasks.")
# 				global watchdog
# 				watchdog = True
# 				self.current_cpt = self.period



################################################################################
#   Handle all connections and rights for the server
################################################################################
class my_task():


	name = None
	priority = -1
	period = -1
	execution_time = -1
	last_deadline = -1
	last_execution_time = None


    	############################################################################
	def __init__(self, name, priority, period, execution_time, last_execution):

		self.name = name
		self.priority = priority
		self.period = period
		self.execution_time = execution_time
		self.last_execution_time = last_execution

	############################################################################
	# def run(self):

	# 	# Update last_execution_time
	# 	self.last_execution_time = datetime.datetime.now()

	# 	# global watchdog
		
	# 	# execution_time = random.randint(2, 30)

	# 	print(self.name + " : Starting task (" + self.last_execution_time.strftime("%H:%M:%S") + ") : execution time = " + str(execution_time))

	# 	while (timer != 44):

	# 		execution_time -= 1

	# 		time.sleep(1)

	# 		if (execution_time <= 0):
	# 			print(self.name + " : Terminating normally (" + datetime.datetime.now().strftime("%H:%M:%S") + ")")
	# 			return
		

	# 	print(self.name + " : Pre-empting task (" + datetime.datetime.now().strftime("%H:%M:%S") + ")")

	def run(self):

			# Update last_execution_time
			
			self.last_execution_time = datetime.datetime.now()

			print(self.name + " : Starting task (" + self.last_execution_time.strftime("%H:%M:%S") + ") : execution time = " + str(execution_time))

			print("\t" + self.name + " : Starting task (" + self.last_execution_time.strftime("%H:%M:%S") + ")")

			time.sleep(self.execution_time)

			print("\t" + self.name + " : Ending task (" + self.last_execution_time.strftime("%H:%M:%S") + ")")
	

####################################################################################################
#
#
#
####################################################################################################
if __name__ == '__main__':

	# Init and instanciation of watchdog

	# global watchdog
	# watchdog = False

	# my_watchdog = Watchdog(period = 10)		# Watchdog 10 seconds
	# my_watchdog.start()


	last_execution = datetime.datetime.now()
	
	# Instanciation of task objects
	task_list = []
	task_list.append(my_task(name="sensor_acquisition", priority = 1, period = 10, execution_time = 1, last_execution = last_execution))
	task_list.append(my_task(name="motors_control", priority = 1, period = 10, execution_time = 1, last_execution = last_execution))
	task_list.append(my_task(name="camera_analysis", priority = 1, period = 30, execution_time = 20, last_execution = last_execution))
	task_list.append(my_task(name="transmission_system", priority = 1, period = 60, execution_time = 20, last_execution = last_execution))

	# # Global scheduling loop
	# while(1):

	# 	print("\nScheduler tick : " + datetime.datetime.now().strftime("%H:%M:%S"))
		
	# 	# # Reinit watchdog
	# 	# watchdog = False
	# 	# my_watchdog.current_cpt = 10
	
	# 	for task_to_run in task_list :
		
	# 		# Reinit watchdog
	# 		# watchdog = False
	# 		# my_watchdog.current_cpt = 10
		
	# 		task_to_run.run()
	

	while(1):

		time_now = datetime.datetime.now()
		
		# print("\nScheduler tick : " + time_now.strftime("%H:%M:%S"))

		# Find the task with Earliest deadline

		task_to_run = None
		earliest_deadline = time_now + datetime.timedelta(hours=1)	# Init ... not perfect but will do the job

		for current_task in task_list:
		
			current_task_next_deadline = current_task.last_execution_time + datetime.timedelta(seconds=current_task.period)

			print("\tDeadline for task " + current_task.name + " : " + current_task_next_deadline.strftime("%H:%M:%S"))
				
			if (current_task_next_deadline < earliest_deadline):
				earliest_deadline = current_task_next_deadline
				task_to_run = current_task


		# Start task
		task_to_run.run()