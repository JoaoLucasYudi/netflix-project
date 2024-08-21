import os
import random
from dotenv import load_dotenv
import pandas as pd

from data import load_data
from validations import validation


load_dotenv()

data = load_data(os.getenv("FILEPATH"))


def menu():
    while True:
        print(
            """
            Menu:
            
            Choose an option:
            1. List all films by genre
            2. Filter films by genre
            5. Exit
            """
        )
        op = input()

        if op == "1":
            list_films()

        elif op == "2":
            get_random_film()

        elif op == "5":
            print("Exiting...")
            exit()

        else:
            print("Invalid option. Please try again.")


def list_films():
    clear_console()
    print(
        """
        Available genres:
        Action, Adventure, Animation, Biography, Comedy, Crime, Documentary, Drama, Family, Fantasy, Film-Noir,
        Game-Show, History, Horror, Music, Musical, Mystery, News, Reality-TV, Romance, Sci-Fi, Short, Sport, Talk-Show, Thriller, War, Western
        """
    )
    genre = input("Enter a genre: ")
    if validation(genre):
        films = data[data["genre"].str.contains(genre, case=False, na=False)]
        random_films = films.sample(n=10, random_state=1) if len(films) >= 10 else films
        print(
            f"""
              
              Top 10 most popular films under the genre {genre}:
              
              """
        )
        i = 1
        for _, film in random_films.iterrows():
            print(f"{i} - {film['title']}")
            i += 1


def get_random_film():
    clear_console()
    print(
        """
        Available genres:
        Action, Adventure, Animation, Biography, Comedy, Crime, Documentary, Drama, Family, Fantasy, Film-Noir,
        Game-Show, History, Horror, Music, Musical, Mystery, News, Reality-TV, Romance, Sci-Fi, Short, Sport, Talk-Show, Thriller, War, Western
        """
    )
    genre = input("Enter a genre: ")
    if validation(genre):
        filtered_movies = data[data["genre"].str.contains(genre, case=False, na=False)]
    random_movie = filtered_movies.sample(n=1)
    print(
        f"""
          
          Filme sugerido: {random_movie['title'].values[0]}
          
          """
    )


def clear_console():
    return os.system("clear")


if __name__ == "__main__":
    menu()
