# -*- coding: utf-8 -*-
import pandas as pd
from pandas import DataFrame

def read_file(path: str, step: str = ",") -> DataFrame:
    return pd.read_csv(path, sep=step)

# ¿Cuál es el juego con el rating más alto (review_score)? Si hay más de uno, darlos todos.
def game_more_score(file: DataFrame) -> DataFrame:
    more_scores = file.review_score.max()
    return file[file.review_score == more_scores]

# ¿Cuál es el juego con el menor precio de lanzamiento (price)? Si hay más de uno, darlos todos.
def game_low_price(file: DataFrame) -> DataFrame:
    low_price = file.price.min()
    return file[file.price == low_price]

# ¿Cuál es el juego con el mejor rating por consola (console)? Si hay más de uno por consola, darlos todos.
def game_more_score_by_console(file: DataFrame) -> DataFrame:
    max_scores = file.groupby('console').review_score.max()
    df_list = []
    for console, score in max_scores.items():
        filtered_df = file[(file['console'] == console) & (file['review_score'] == score)]
        df_list.append(filtered_df)

    result_df = pd.concat(df_list)
    return result_df

# ¿Cuál es la categoría etaria (age_rating) con el mayor total de ventas (sales)? ¿Cuál es ese total? Si hay más de una, darlas todas. (Nota: Los valores están en unidades de millones de dólares)
def df_age_rating(file: DataFrame) -> DataFrame:
    all_sales = file.groupby("age_rating").sales.sum()
    age_rating = all_sales.idxmax()
    sales = all_sales.max()

    return pd.DataFrame({"age_rating": [age_rating], "sales": [sales]})

# ¿Cuáles son los juegos de más de 40 horas de duración (average_length)?
def more_40hs(file: DataFrame) -> DataFrame:
    return file[file.average_length > 40]

# ¿Cuál es la consola con mayor cantidad de juegos en la categoría E (for Everyone)? Si hay más de una, darlas todas.
def console_E(file: DataFrame) -> DataFrame:
    index = file.age_rating == "E"
    consoles = file[index]
    df_consoles_age = consoles.groupby("console").age_rating.count()
    return df_consoles_age.idxmax()

# ¿Año (year) con más juegos de X360? Si hay más de uno, darlos todos.
def xbox360_year(file: DataFrame) -> DataFrame:
    index = file.console == "X360"
    consoles = file[index]
    df_xbox_age = consoles.groupby("year").sales.sum()
    return df_xbox_age.idxmax()

archivo = read_file("video_games_curated.csv")

print(xbox360_year(archivo))
