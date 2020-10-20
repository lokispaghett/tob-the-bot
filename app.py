print("Title of program: tob the bot :]")
print()
while True:
  description = input("So, how are you feeling today?")

  list_of_words = description.split()

  feelings_list = []
  encouragement_list = []
  counter = 0
  
  for each_word in list_of_words:
    
    if each_word == "sad":
      feelings_list.append("sad")
      encouragement_list.append("i hope you feel better!")
      counter += 1
    if each_word == "happy":
      feelings_list.append("happy")
      encouragement_list.append("good job! keep going!")
      counter += 1
    if each_word == "tired":
      feelings_list.append("tired")
      encouragement_list.append("it's ok to take a break, i hope you are ok!")
      counter += 1
    if each_word == "bad":
      feelings_list.append("bad")
      encouragement_list.append("oh no, i hope you are alright!")
      counter += 1
    if each_word == "bored":
      feelings_list.append("bored")
      encouragement_list.append("why not take a walk?")
      counter += 1
    if each_word == "annoyed":
      feelings_list.append("annoyed")
      encouragement_list.append("drink some water and try to relax, i hope you feel ok now!")
      counter += 1
    if each_word == "angry":
      feelings_list.append("angry")
      encouragement_list.append("drink some water and try to relax, i hope you feel ok now!")
      counter += 1

  if counter == 0:
    
      output = "Sorry I don't really understand, can you express yourself another way?"

  elif counter == 1:
    
      output = "It seems that you are feeling quite " + feelings_list[0] +".  "+  encouragement_list[0] + " Remember that I'm always here for you :)"  

  else:

    feelings = ""    
    for i in range(len(feelings_list)-1):
      feelings += feelings_list[i] + ", "
    feelings += "and " + feelings_list[-1]
    
    encouragement = ""    
    for j in range(len(encouragement_list)-1):
      encouragement += encouragement_list[i] + ", "
    encouragement += "and " + encouragement_list[-1]

    output = "It seems that you are feeling quite " + feelings + ". Please always remember "+ encouragement + "! Hope you feel better :)"

  print()
  print(output)
  print()
