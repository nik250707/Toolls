#import
import time

#functions
def fat():

	try:
		while True:
			answer = input("Ты жирная? Д/н \n(Quit чтобы выйти.):")
			if answer.lower() == "д":
				print("Правильно!")
				break
			elif answer.lower() == "н":
				print("А вот и да!")
				break
			elif answer.lower() == "quit":
				print("\nЛадно")
				time.sleep(1)
				print("Пока!")
				exit(0)
			else:
				print("\nНе понятно")
				time.sleep(1)
	except KeyboardInterrupt:
		print("\nЗачем ты меня выключил?")
		time.sleep(1)
		exit(0)

#run
fat()

