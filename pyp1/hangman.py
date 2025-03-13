import random
# قائمة كلمة التخمين
words=("hangman", "chairs", "backpack", "bodywash", "clothing",
                 "computer", "python", "program", "glasses", "sweatshirt",
                 "sweatpants", "mattress", "friends", "clocks", "biology",
                 "algebra", "suitcase", "knives", "ninjas", "shampoo")
# قائمة hangman
hangman= ['''
  +---+
  |   |
      |
      |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
      |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
  |   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========''']
# طباعة اسم اللعبه
print("""
 _                                             
| |                                            
| |__   __ _ _ __   __ _ _ __ ___   __ _ _ __  
| '_ \ / _` | '_ \ / _` | '_ ` _ \ / _` | '_ \ 
| | | | (_| | | | | (_| | | | | | | (_| | | | |
|_| |_|\__,_|_| |_|\__, |_| |_| |_|\__,_|_| |_|
                    __/ |                      
                   |___/                       """)
# fun الرئيسيه
def play():
  # اختيار كلمه للكمبيوتر
  computer_choose=random.choice(words)
    # معرفة طول الكلمه وتبديل الحروف ب علامة ناقص
  display=['-']* len(computer_choose)
    # بعد تبديل حروف الكلمه نضيف مسافه بعد كل علامة ناقص باستخدام 
    # " ".join( الجزء المطلوب التعديل عليه )
  print(" ".join(display))
    # طباعة اول شكل للعبة
  print(hangman[0])
    # عمل متغير بعدد الحاولات
  x=6 
    # عمل لوب بعدد حرف الكلمة ويجب ان تكون المحاولات اكبر من 0
  while "-" in display and (x > 0):
      # عمل متغير للحرف اللي المستخدم هيقوم بادخاله
    guessed=input("Please guess a letter:").lower()
        # عمل شرط لو الحرف مش موجود هنقلل المحاولات واحد
    if guessed not in computer_choose:
      x-=1
        # عمل لوب بعدد حروف الكلمة
    for i in range(len(computer_choose)):
            # لو الحرف اللي المستخدم كتبه صح هنبدله الناقص بالحرف 
            # اللي هي في السطر 73
      if computer_choose[i]==guessed:
        display[i]=guessed
          # ونطبع متغير display line 73
        print(display)
          # ونطبع عدد المحاولات المتاحه
        print(f"You have {x} more tries")
          # هذا الجزء مختص عند خسارة محوله تتم طباعة جزء من شخصية اللعبه من 1 الي 6 وليس من اول 0
          # حيث اول شكل تم استخدامه في بداية اللعبه
    if x == 5:
      print(hangman[1])
      print(f"You have {x} more tries")
    elif x== 4:
      print(hangman[2])
      print(f"You have {x} more tries")
    elif x== 3:
      print(hangman[3])
      print(f"You have {x} more tries")
    elif x== 2:
      print(hangman[4])
      print(f"You have {x} more tries")
    elif x== 1:
      print(hangman[5])
      print(f"You have {x} more tries")
    if x ==0:
      print(hangman[6])
      print(f"You have {x} more tries")
    # بعد الانتهاء من المحاولات يتم الوصول الي نهاية اللعبة 
  else:
    print("""
      **********
       You Win
      ********** """)  


play()