#Rode-Tornado VS. Rode-Vulkaan
import time #Imports a module to add a pause

#Figuring out how users might respond
answer_A = ["A", "a"]
answer_B = ["B", "b"]

#Grabbing objects
boat = 0
car = 0

required = ("\nUse only A, B\n") #Cutting down on duplication

#The story is broken into sections, starting with "intro"
def intro():
  print (" Rode Tornado werkte voor tientallen jaren al voor de justice league deze keer is die mentor van de young justice league. "
  " Deze league zijn de tiener versies van de justice league. Samen met deze helden is Rode Tornado de teamleider van de young justice. " 
  " Op een dag wilde Rode Tornado d’r schepper ontmoeten. Hierbij kwam een groot obstakel: Rode Vulkaan, de laatste creatie van Tio Morrow, de jonge versie van rode tornado. "
  " Rode vulkaan was sneller, sterker maar ook meedogenlozer."
  " Rode vulkaan doodde Tio Morrow en voerde Tio’s plan uit: "
  " een grote vulkaan eruptie totdat mensen niet meer kunnen ademen. " 
  " Beide vechten tot het einde. ")
  
  print ("""  A. Gebruik je tornado om een auto te gooien op rode vulkaan
  B. Gebruik je tornado om een boot te gooien op rode vulkaan""")
  choice = input(">>> ") #Here is your first choice.
  if choice in answer_A:
    option_damage()
  elif choice in answer_B:
    print ("\nWelp, that was quick.\n")
    print (required)
    intro()

def option_damage(): 
  print ("\nRode Vulkaan vecht hard terug, Niet veel schade. Nu een tegen-aanval "
  "rode vulkaan vecht en pakt een boom gooit:")
  time.sleep(1)
  print ("""  A. Counter Twin-Tornado
  B. ontwijk""")
  choice = input(">>> ")
  if choice in answer_A:
    option_run()
  elif choice in answer_B:
    print ("\n AH!!!!!, 2 stadium van vulkaan\n")
  else:
    print (required)
    option_run()


def option_run():
  print ("\nGet help from the Justice League\n")
  time.sleep(1)
  print ("""  A. Create GIANT Tornado
  B. Call the Justice League and WIN!""")
  choice = input(">>> ")
  if choice in answer_A:
    print ("\nRode vulkaan overlijd\n")
  elif choice in answer_B:
    print ("\n Door samen te werken versla je het kwaad.\n")
    option_gameover()
  else:
    print (required)
    option_gameover()
intro()