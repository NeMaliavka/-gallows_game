from random import choice
def game(word):
    global stop
    win = False    
    incorrect = 0
    picture = ['',
               ' _______         ',
               '|       |        ',
               '|       |        ',
               '|       O        ',
               '|      /0\       ',
               '|      / \       ',
               '|                ']
    letters = list(word)
    board = ['_']*len(word)
    
    
    while incorrect < len(picture)-1:
        answer = input('\nВведите букву: ').lower()
        if answer == 'стоп':
            stop = True
            break
        if answer in letters:            
            index_letter = letters.index(answer)
            board[index_letter] = answer
            letters[index_letter] = '+'
        else:
            incorrect += 1

        print('Слово: ', ''.join(board))
        print('\n'.join(picture[0:incorrect+1]))

        if '_' not in board:
            print('Поздравляю! Вы угадали слово!')
            win = True
            break
    if not win:
        print('Увы, Вы проиграли...')
        print(f'Было загадано слово: {word}')

print('''Добро пожаловать в игру "Виселица"
Вам предстоит определить, что за слова я буду загадывать.
Отвечать нужно, передавая слово по буквам.
Для завершения игры введите слово "стоп"''')       
words = ['корова', 'кошка', 'ключ', 'огурец', "помидор"]
count = 0
stop = False
while count < len(words):
    if not stop:
        random_word = choice(words)
        if random_word != 'no':
            #print(words)
            game(random_word)
            index_word = words.index(random_word)
            words[index_word] = 'no'
            count += 1
        else:
            continue
    else:
        break
    
        
        
