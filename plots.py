from analysis import (
    duration_hist,
    year_counts,
    top_genres,
    genre_avg_duration,
    genre_trends,
)

def plot_duration_hist(df):
    return duration_hist(df)

def plot_year_counts(df):
    return year_counts(df)

def plot_top_genres(df):
    return top_genres(df)

def plot_genre_avg_duration(df):
    return genre_avg_duration(df)

def plot_genre_trends(df):
    return genre_trends(df)
