import pandas as pd


def to_df(tracks):
    if not tracks:
        return pd.DataFrame()

    df = pd.DataFrame([t.__dict__ for t in tracks])

    # Długość z ms do min
    df["duration_ms"] = pd.to_numeric(df["duration_ms"], errors="coerce")
    df["duration_min"] = df["duration_ms"] / 60000

    df["release_date"] = pd.to_datetime(df["release_date"], errors="coerce")
    df["release_year"] = df["release_date"].dt.year.astype('Int64')

    # brakujące wartości
    df["genre"] = df["genre"].fillna("Unknown")
    df["album"] = df["album"].fillna("Unknown")

    return df


def filter_by_artist(df, artist):
    if df.empty:
        return df
    return df[df["artist"].str.lower() == artist.lower()]


def kpi(df):
    if df.empty:
        return {}

    return {
        "utwory": int(len(df)),
        "albumy": int(df["album"].nunique()),
        "gatunki": int(df["genre"].nunique()),
        "średnia_długość_min": float(df["duration_min"].mean().round(2)),
    }


def newest_tracks(df, n=10):
    return df.sort_values("release_date", ascending=False).head(n)


def duration_hist(df, step=0.5):
    if df["duration_min"].dropna().empty:
        return None
    s = df["duration_min"].dropna()
    s = (s / step).round() * step
    return s.value_counts().sort_index()


def year_counts(df):
    counts = (
        df["release_year"]
        .dropna()
        .astype(int)
        .value_counts()
        .sort_index()
    )
    counts.index = counts.index.astype(str)
    return counts


def top_genres(df, n=10):
    out = df["genre"].value_counts().head(n).reset_index()
    out.columns = ["genre", "tracks_count"]
    return out


def genre_avg_duration(df):
    return (
        df.groupby("genre")["duration_min"]
        .mean()
        .sort_values(ascending=False)
    )


def genre_trends(df):
    return (
        df.groupby(["release_year", "genre"])
        .size()
        .unstack(fill_value=0)
    )
