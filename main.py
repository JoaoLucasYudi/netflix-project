import os
import random
from dotenv import load_dotenv
import pandas as pd

from data import load_data


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
            print(
                """
                Available genres:
                Action, Adventure, Animation, Biography, Comedy, Crime, Documentary, Drama, Family, Fantasy, Film-Noir,
                Game-Show, History, Horror, Music, Musical, Mystery, News, Reality-TV, Romance, Sci-Fi, Short, Sport, Talk-Show, Thriller, War, Western
                """
            )
            genre = input("Enter a genre: ").capitalize()
            list_films(genre)

        elif op == "2":
            print(
                """
                Available genres:
                Action, Adventure, Animation, Biography, Comedy, Crime, Documentary, Drama, Family, Fantasy, Film-Noir,
                Game-Show, History, Horror, Music, Musical, Mystery, News, Reality-TV, Romance, Sci-Fi, Short, Sport, Talk-Show, Thriller, War, Western
                """
            )
            genre = input("Enter a genre: ").capitalize()
            filter_films(genre)

        elif op == "5":
            print("Exiting...")
            exit()

        else:
            print("Invalid option. Please try again.")


def list_films(): ...


def get_random_film(): ...


if __name__ == "__main__":
    menu()
