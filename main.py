from random import randrange, randint, choice
from imdb import Cinemagoer
import pyjokes
# import music
import wikipedia
from colorama import init, Fore, Back, Style
from selenium import webdriver
from selenium.webdriver.common.by import By

print('Вітаю! Оберіть, будь ласка, послугу з "Меню послуг":')
def menu():
    menu = print()
    while menu != '0':
        match menu:
            case '1':
                select_movie()
            case '2':
                select_song()
            case '3':
                select_game()
            case '4':
                select_wiki()
            case '5':
                play_game()
            case '6':
                select_joke()
            case '0':
                break
        menu = input('Меню послуг:\n1. Порадити фільм\n2. Порадити музику\n3. Порадити гру\n'
                     '4. Прочитати статтю з вікіпедії\n5. Пограти в гру\n6. Пожартувати\n0. Вийти\n'
                     'Зробіть Ваш вибір\n')
def select_movie():
     io = Cinemagoer()
     movie = io.get_movie(randrange(1, 250))#29899729
     print(Fore.CYAN + f'Величний Шар рандому рекомендує тобі сьогодні подивитись: {movie}'+ Style.RESET_ALL)
def select_song():

    browser = webdriver.Edge()
    link = 'https://open.spotify.com/playlist/37i9dQZEVXbNG2KDcFcKOF'
    browser.get(link)
    song_artist = []
    song_name = []
    try:
        browser.implicitly_wait(10)
        save_the_song = browser.find_elements(By.CLASS_NAME, 'iCQtmPqY0QvkumAOuCjr')
        for song in save_the_song:
            artist = song.find_element(By.CLASS_NAME, 'Type__TypeElement-sc-goli3j-0.dvSMET.rq2VQ5mb9SDAFWbBIUIn.standalone-ellipsis-one-line').text
            name = song.find_element(By.CLASS_NAME, 'Type__TypeElement-sc-goli3j-0.kHHFyx.t_yrXoUO3qGsJS4Y6iXX.standalone-ellipsis-one-line').text
            song_artist.append(artist)
            song_name.append(name)
        all_sang_list = (list(zip(song_artist, song_name)))
    finally:
        # browser.implicitly_wait(10)
        browser.quit()

    song = choice(all_sang_list)
    print(f'Насолодись однією з 50-ти найяскравіших пісень сьогодення: {song}')
def select_game():
    genre = print('Оберіть жанр ігри: \n')
    while genre != '0':
        genre = input('1. Екшен\n2. Пригодницькі\n3. РПГ\n4. Стратегії\n0. Вийти\n')
        if genre == '1':
            print(choice(['Half-Life', 'Batman', 'Max Payne', 'The Elder Scrolls 5: Skyrim']))
        elif genre == '2':
            print(choice(['Assassin`s Creed Odyssey', 'The Walking Dead', 'The Last of Us: Remastered']))
        elif genre == '3':
            print(choice(['Fallout 2', 'God of War', 'Star Wars: Knights of the Old Republic']))
        elif genre == '4':
            print(choice(['Warcraft 3: The Frozen Throne', 'Civilization 6', 'Command & Conquer: Red Alert 2']))
        elif genre == '0':
            print('Виходжу...')
            menu()
        else:
            print('Оберіть, будь ласка, жанр гри')
def select_wiki():
    wikipedia.set_lang('uk')
    wiki = wikipedia.page(choice(['Російське вторгнення в Україну (2022)', 'Арестович Олексій Михайлович',
            'Україна', 'Бандера Степан Андрійович', 'Збройні сили України', 'Київ', 'Путін Володимир',
            'Залужний Валерій Федорович', 'Російсько-українська війна (з 2014)', 'Українська мова']))
    print(wiki.content[:30])
    print('Читай повну статтю за посиланням: ', wiki.url)
def play_game():
    game_menu = input('1. Орел і решка\n2. Вгадай число\n0. Вихід\n')
    if game_menu == '1':
        print('Орел(Напиши "1") або решка(Напиши "2")? 0 - Вихід\n')
        users_choice = input()
        answer = choice(['1', '2'])
        print(answer)
        if users_choice == answer:
            print(Fore.GREEN + 'Ого! Ти виграв Штучний Інтелект, можливо повстання машин не так скоро...' + Style.RESET_ALL)
            play_game()
        if users_choice == '0':
            play_game()
        else:
            print(Fore.RED + 'На жаль ти програв. Спробуй ще' + Style.RESET_ALL)
            play_game()
    if game_menu == '2':
        users_num = print('Вгадай число від 1 до 9. Натисни 0 для виходу')

        while users_num != '0':
            users_num = input('')
            comp_answer = randrange(1,10)
            print(comp_answer)
            if users_num == comp_answer:
                print(Fore.GREEN + 'Ти переміг!!! Вітаю!!!' + Style.RESET_ALL)
            if users_num == '0':
                play_game()
            else:
                print(Fore.RED + 'Пощастить у коханні' + Style.RESET_ALL)
    if game_menu == '0':
        menu()

def select_joke():
    my_joke = pyjokes.get_joke(language="en", category="all")
    print(my_joke)
# def exit():
#     print('Бувай! Завжди тебе чекатиму!:)')
menu()
