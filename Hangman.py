word_list = [
    'apple',
    'bicycle',
    'cat',
    'dog',
    'egg',
    'fish',
    'giraffe',
    'hat',
    'ice',
    'jacket',
    'kite',
    'lemon',
    'mouse',
    'notebook',
    'orange',
    'pencil',
    'queen',
    'rose',
    'sun',
    'tree',
    'umbrella',
    'violin',
    'water',
    'xylophone',
    'yarn',
    'zebra',
    'book',
    'chair',
    'desk',
    'ball',
    'star',
    'train',
    'cloud',
    'phone',
    'shoes',
    'plant',
    'shirt',
    'cup',
    'pizza',
    'bike',
    'door',
    'lamp',
    'computer',
    'toothbrush',
    'wallet',
    'guitar',
    'camera',
    'shoe',
    'watch',
    'plankton',
    'raccoon',
    'rocket',
    'skate',
    'space',
    'telescope',
    'vase',
    'whale',
    'window',
    'zoo'
]
hint_list = [
    'A fruit that keeps the doctor away',
    'A two-wheeled vehicle',
    'A common domestic animal that purrs',
    'A popular pet that barks',
    'A breakfast food that comes from chickens',
    'A water-dwelling animal with fins',
    'A tall African animal with a long neck',
    'A head covering',
    'Frozen water',
    'An outerwear garment',
    'A toy that flies in the sky',
    'A sour yellow fruit',
    'A small rodent often kept as a pet',
    'A book used for writing notes',
    'A fruit that is orange and citrusy',
    'An item used for writing',
    'A royal female figure',
    'A flower that is often red',
    'A bright star in the sky during the day',
    'A tall plant with leaves and branches',
    'A protective covering from rain',
    'A musical instrument with strings',
    'A clear liquid we drink',
    'A musical instrument made of wooden bars',
    'A thread used for knitting or weaving',
    'A striped black and white animal',
    'A reading material',
    'A piece of furniture to sit on',
    'A piece of furniture for working',
    'A round object used in sports',
    'A celestial body that shines at night',
    'A vehicle that runs on tracks',
    'A fluffy formation in the sky',
    'A device used for communication',
    'Footwear for walking',
    'A living organism that grows in the ground',
    'A piece of clothing worn on the upper body',
    'A container for drinking',
    'A type of Italian food with cheese and toppings',
    'A two-wheeled vehicle',
    'An entryway into a room or building',
    'A source of light',
    'A machine used for various tasks',
    'An item used for cleaning teeth',
    'A small item for holding money',
    'A stringed musical instrument',
    'A device used to capture images',
    'A timekeeping device worn on the wrist',
    'A covering for the head',
    'A tiny organism that floats in water',
    'A nocturnal animal with a ringed tail',
    'A spacecraft used for space travel',
    'A device used to glide on ice or pavement',
    'The universe beyond Earth',
    'An instrument for observing distant objects',
    'A container for flowers',
    'A large marine mammal',
    'An opening in a wall to let in light',
    'A place with animals and attractions'
]
stages = ['''
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========
''', '''
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
  |   |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
      |
      |
      |
=========
''', '''
  +---+
  |   |
      |
      |
      |
      |
=========
''']

logo = ''' 
 _                                             
| |                                            
| |__   __ _ _ __   __ _ _ __ ___   __ _ _ __  
| '_ \ / _` | '_ \ / _` | '_ ` _ \ / _` | '_ \ 
| | | | (_| | | | | (_| | | | | | | (_| | | | |
|_| |_|\__,_|_| |_|\__, |_| |_| |_|\__,_|_| |_|
                    __/ |                      
                   |___/    '''


import random
lives = 6
print(logo)
chosen_word = random.choice(word_list)
hint = hint_list[word_list.index(chosen_word)]
print("Hint: " + hint)
placeholder = ""
word_length = len(chosen_word)
for position in range(word_length):
    placeholder += "_"
print("Word to guess: " + placeholder)
game_over = False
correct_letters = []
while not game_over:
    print(f"****************************{lives}/6 LIVES LEFT****************************")
    guess = input("Guess a letter: ").lower()
    if guess in correct_letters:
        print(f"You've already guessed {guess}")
    display = ""
    for letter in chosen_word:
        if letter == guess:
            display += letter
            correct_letters.append(guess)
        elif letter in correct_letters:
            display += letter
        else:
            display += "_"
    print("Word to guess: " + display)
    if guess not in chosen_word:
        lives -= 1
        print(f"You guessed {guess}, that's not in the word. You lose a life.")
        if lives == 0:
            game_over = True

            print(f"***********************IT WAS {chosen_word}! YOU LOSE**********************")
    if "_" not in display:
        game_over = True
        print(f"THAT\'S RIGHT!! IT WAS {chosen_word}!")
        print("****************************YOU WIN****************************")
    print(stages[lives])
