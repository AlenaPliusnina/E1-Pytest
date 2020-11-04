#! /usr/bin/env python
# -*- coding: utf-8 -*-
import random


def word_choice():
    words = ['skillfactory', 'testing', 'blackbox', 'pytest', 'unittest', 'coverage']
    choice = random.choice(words)

    return choice


def check_letter(letter, word):
    if letter in word:
        return True
    else:
        return False


def update_underscore(letter, word, underscore):
    guess_word = underscore.split()
    for i in range(len(word)):
        if letter == word[i]:
            guess_word[i] = letter

    return " ".join(guess_word)


def main():
    print('\nДавай, поиграем в "Виселицу"? Я загодаю слово, а ты попробуешь его угадать.')
    print('За каждую ошибку ты будешь получать штрафное очко. Если ошибёшься 4 раза, то проиграешь.\n')
    ready = input('Готов начать? (Y,N): ')

    if ready == 'Y':
        fails = 0
        max_fails = 4
        word = word_choice()
        underscore = ' _' * len(word)

        while fails < max_fails and underscore.replace(" ", "") != word:
            print('В твоем слове ' + str(len(word)) + ' букв: ' + underscore)
            letter = input('Введите букву: ')
            if letter in underscore and letter != '_':
                print('Ты уже угадывал эту букву, все ее повторения открыты.\n')
            elif check_letter(letter, word):
                underscore = update_underscore(letter, word, underscore)
                print('Ты угадал!\n')
            else:
                print('\nТы ошибся:(\n')
                fails += 1
                print('Количество ошибок -', fails)

        if underscore.replace(" ", "") == word:
            print('-------------------------------')
            print('Ты выиграл!')
        else:
            print('-------------------------------')
            print('Ты проиграл:(')

        print('Загаданное слово было -', word)
        print('Количество ошибок -', fails)
        print('-------------------------------')

    elif ready == 'N':
        print('Жаль, поиграем в следующий раз, до встречи!')
    else:
        print('Твой ответ должен быть: Y - если хочешь начать и N - если нет.')


if __name__ == '__main__':
    main()