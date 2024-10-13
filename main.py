questions = ["Which country has the highest life expectancy? : " , 'A',
    "What is the most common surname in the United States? : " , 'C'
      ,"Who was the Ancient Greek God of the Sun? : "  , 'B'
       ,"How many minutes are in a full week? : " , 'B'
        ,"How many faces does a Dodecahedron have? : " , 'D'
         ,"What company was initially known as 'Blue Ribbon Sports' ? : " , 'C'
          ,"What software company is headquartered in Redmond, Washington? : " , 'A'
           ,"What is acrophobia a fear of?" , 'A'
            ,"Which day of the week does the Jewish Sabbath begin? : " , 'B'
             ,"What is the name of the Chinese philosophical system that emphasizes harmony with nature? : " , 'D'
              ,"What is the worlds largest retailer? : " , 'C'
]

options = [["A) Honk Kong", "B) USA", "C) England", "D) Turkiye"],
           ["A) Black", "B) Stark", "C) Smiths", "D) Johnson"],
           ["A) Kassandra", "B) Apollo", "C) Cassiopia", "D) Zeus"],
           ["A) 7,502", "B) 10,080", "C) 9,200", "D) 3,600"],
           ["A) 1", "B) 2", "C) 6", "D) 12"],
           ["A) Balenciaga", "B) Puma", "C) Nike", "D) Adidas"],
           ["A) Microsoft", "B) Linux", "C) Mac", "D) Panda"],
           ["A) Heights", "B) Closed Place", "C) Dots", "D) Spiders"],
           ["A) Sunday", "B) Friday", "C) Tuesday", "D) Wednesday"],
           ["A) Budizm", "B) Atheism", "C) Deizm", "D) Taoism"],
           ["A) BIM A.S", "B) A101", "C) Walmart", "D) Amazon"]]

answers = []

def new_game(questions,options):
  for i in range(0,len(questions),2):
    while True:
        print(questions[i])
        print("\n".join(options[i//2]))
        answer = input("Your answer is :").upper()
        if answer in ('A', 'B', 'C', 'D'):
          answers.append(answer)
          break
        else:
          print('Your options are (A,B,C,D)')
          input('Press Enter To Answer Again.')
        print('-'*50)
      
           
  
def check_answer(questions, answers):
    point = 0  
    for i in range(1, len(questions), 2):  
        if answers[i//2] == questions[i]:  
            point += 1  
    print('Your score is =' ,point)
    point = 0
    return point
        
    
    
  
def play_again():
  response = input('Do you want to play again ? (yes or no):').lower()
  if response == "yes":
        answers.clear()
        new_game(questions, options)
        check_answer(questions,answers)
        play_again()
        
  else:
        print("Thanks for playing!")
        quit()
    
while True:
  new_game(questions,options)
  check_answer(questions,answers)
  play_again()
  
  
