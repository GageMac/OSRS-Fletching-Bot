import pyautogui
import time

import keyboard as kb
from pynput import keyboard

import random
import threading

import sys
import trace

#from pynput.mouse import Button as MouseButton
#from pynput.mouse import Controller as MouseController
#mouse = MouseController()

#Sources
#https://www.youtube.com/watch?v=YRAIUA-Oc1Y&t=145s
#https://stackoverflow.com/questions/2905965/creating-threads-in-python
#https://stackoverflow.com/questions/24604685/start-new-thread-of-a-class-inside-start-new-thread

logs = pyautogui.locateCenterOnScreen('images/logs.png', confidence = 0.75)
knife = pyautogui.locateCenterOnScreen('images/knife.png', confidence = 0.75)
bank = pyautogui.locateCenterOnScreen('images/bank.png', confidence = 0.9)

#thread_with_trace constructor and functions found here https://stackoverflow.com/questions/24604685/start-new-thread-of-a-class-inside-start-new-thread

threads = []

class thread_with_trace(threading.Thread): 
  def __init__(self, *args, **keywords): 
    threading.Thread.__init__(self, *args, **keywords) 
    self.killed = False

  def start(self): 
    self.__run_backup = self.run        
    threading.Thread.start(self) 

  def kill(self): 
    self.killed = True

#Random time between actions so bot is less detectable
rand = random.randint(1, 2)
#Random time between 25 and 30 seconds for the logs to be cut
logCut = random.randint(25, 30)

#Key to be pressed to exit bank
escape = "esc"
space = "space" 

def on_press(key):
	try:
		k = key.char
	except:
		k = key.name
	if k in ['1']:
		print('Key pressed: ' + k)
		fletch_thread = thread_with_trace(target=fletchThread)
		fletch_thread.start()
		threads.append(fletch_thread)
	if k in ['2']:
		print('Key pressed: ' + k)
		for thread in threads:
			if thread.is_alive() is True:
				thread.kill()
				threads.append(fletch_thread)

def fletchThread():
    while True:
      pyautogui.click(pyautogui.locateCenterOnScreen('images/knife.png', confidence = 0.75))
      time.sleep(rand)
      pyautogui.click(pyautogui.locateCenterOnScreen('images/logs.png', confidence = 0.75))
      time.sleep(rand)
      kb.press_and_release(escape)
      time.sleep(rand)
      pyautogui.click(pyautogui.locateCenterOnScreen('images/knife.png', confidence = 0.75))
      time.sleep(rand)
      pyautogui.click(pyautogui.locateCenterOnScreen('images/logs.png', confidence = 0.75))
      time.sleep(rand)
      pyautogui.click(pyautogui.locateCenterOnScreen('images/yewLog.png', confidence = 0.75))
      time.sleep(15)
      pyautogui.moveTo(720, 280)
      time.sleep(rand)
      pyautogui.click() 
      time.sleep(rand)
      pyautogui.click(pyautogui.locateCenterOnScreen('images/deposit.png', confidence = 0.75)) 
      time.sleep(rand)

#Listener Documentation
listener = keyboard.Listener(on_press=on_press)
listener.start()
listener.join()

#def mouse_button_left_click(click_hold_delay):
    #mouse.press(MouseButton.left)
    #time.sleep(click_hold_delay)
    #mouse.release(MouseButton.left)
    
#def move_mouse(end_x, end_y):
	#current_x = mouse.position[0]
	#current_y = mouse.position[1]

	#x_distance = end_x - current_x
	#y_distance = end_y - current_y

	#if x_distance < 0:
		#x_move = -1
	#if x_distance > 0:
		#x_move = 1
	#if x_distance == 0:
		#x_move = 0

	#if y_distance < 0:
		#y_move = -1
	#if y_distance > 0:
		#y_move = 1
	#if y_distance == 0:
		#y_move = 0

	#offset = (abs(x_distance)-abs(y_distance))

	#if abs(x_distance) > abs(y_distance):
		#for index in range(abs(x_distance)):
			#if abs(y_distance) != 0:
				#offset_chance = random.randint(0,int(abs(x_distance)/abs(y_distance)))
				
				#if offset_chance == 0:
					#if mouse.position[1] != end_y:
						#mouse.move(0, y_move)

				#if abs(end_y - mouse.position[1]) == (abs(x_distance) - index):
					#mouse.move(0, y_move)

				#if abs(end_x - mouse.position[0]) == abs(end_y - mouse.position[1]):
					#mouse.move(x_move, y_move)
					#index = index + 1

				#if mouse.position[0] != end_x:
					#mouse.move(x_move, 0)
			#else:
				#if mouse.position[0] != end_x:
					#mouse.move(x_move, 0)

	#if abs(y_distance) > abs(x_distance):
		#for index in range(abs(y_distance)):
			#if abs(x_distance) != 0:
				#offset_chance = random.randint(0,int(abs(y_distance)/abs(x_distance)))
				
				#if offset_chance == 0:
					#if mouse.position[0] != end_x:
						#mouse.move(x_move, 0)

				#if abs(end_x - mouse.position[0]) == (abs(y_distance) - index):
					#mouse.move(x_move, 0)

				#if abs(end_x - mouse.position[0]) == abs(end_y - mouse.position[1]):
					#mouse.move(x_move, y_move)
					#index = index + 1

				#if mouse.position[1] != end_y:
					#mouse.move(0, y_move)
			#else:
				#if mouse.position[1] != end_y:
					#mouse.move(0, y_move)

	#if abs(x_distance) == abs(y_distance):
		#for index in range(x_distance):
			#mouse.move(x_move, y_move)
