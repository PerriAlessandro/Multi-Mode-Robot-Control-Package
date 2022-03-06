#!/usr/bin/python3
import rospy
import os
from std_msgs.msg import Int32, Bool
isTimeout=False #variable that'll be set to true if the timeout expires

class colors:
	PINK = '\033[95m'
	BLUE = '\033[94m'
	CYAN = '\033[96m'
	GREEN = '\033[92m'
	YELLOW = '\033[93m' 
	RED = '\033[91m'
	ORANGE = '\033[33m' 
	PURPLE  = '\033[35m'

	ENDC = '\033[0m'
	BOLD = '\033[1m'
	UNDERLINE = '\033[4m'

def timeout_callback(data): #callback function for the timer
	global isTimeout
	isTimeout=True
	

def main():
	global isTimeout
	rospy.init_node('user_interface')
	pubModality=rospy.Publisher('mode',Int32,queue_size=10) #publisher of 'mode' topic, sends user choice to other nodes
	subTimeout=rospy.Subscriber('timeout', Bool,timeout_callback) #subscriber of 'timeout' topic to receive timeout notification from goal_reaching node
	print(colors.GREEN + colors.UNDERLINE + colors.BOLD + "\nIdle status. Waiting for a command from user..."+colors.ENDC)
	while not rospy.is_shutdown():

		try:
			command = int(input(colors.BLUE + colors.UNDERLINE + colors.BOLD +'\nChoose the modality:\n - [0] Idle,\n - [1] Goal Reaching,\n - [2] Not Assisted Driving,\n - [3] Assisted Driving,\n - [4] Quit \n'+colors.ENDC))

		except ValueError:
			command = -1

		os.system('cls||clear') #clear the console



		if command == 0: #idle status
			
			currentmode=0
			pubModality.publish(currentmode) #publish the value on 'mode' topic 
			print(colors.GREEN + colors.UNDERLINE + colors.BOLD + "\nIdle status. Waiting for a command from user..."+colors.ENDC)


		elif command == 1: #first modality (Goal Reaching)

			print(colors.BOLD + colors.UNDERLINE +colors.PINK+ "\nModality 1 - Goal Reaching"+ colors.ENDC)
			print( colors.BOLD + "(press '0' during the execution to cancel the target)" + colors.ENDC)
			currentmode=1
			pubModality.publish(currentmode) #publish the value on 'mode' topic 
			

		elif command == 2: #second modality (Not Assisted Driving)
			
			currentmode=2
			pubModality.publish(currentmode) #publish the value on 'mode' topic 
			print(colors.PURPLE + colors.UNDERLINE + colors.BOLD +"\nModality 2 - Not Assisted Driving\n"+colors.ENDC)
			
			
		elif command == 3: #third modality (Assisted Driving)
			
			currentmode=3
			pubModality.publish(currentmode) #publish the value on 'mode' topic 
			print(colors.CYAN + colors.UNDERLINE + colors.BOLD +"\nModality 3 - Assisted Driving\n"+colors.ENDC)
			
		elif command == 4:
			exit()
			
		else:
			print(colors.RED + colors.UNDERLINE + colors.BOLD +"Wrong key"+colors.ENDC)


main()
