import random
from .emoji_dict import movie_dict

class EmojiGame():
    def show_movie_options():
        for name, value in movie_dict.items():
            print(f'{name} : {value}')

    def movie_edition():
        name, hint = random.choice(list(movie_dict.items()))
        print(hint)
        input('Press ENTER to get answer.')
        print(name)

if __name__ == '__main__':
    EmojiGame.movie_edition()