import streamlit as st
from sources import ITunesSource
from analysis import (
    to_df,
    filter_by_artist,
    kpi,
    newest_tracks,
)
from plots import (
    plot_duration_hist,
    plot_year_counts,
    plot_top_genres,
    plot_genre_avg_duration,
    plot_genre_trends,
)

st.set_page_config(page_title="Analiza artysty", layout="wide")
st.title("Analiza utworów artysty (iTunes)")

artist = st.sidebar.text_input("Artysta", "Twenty One Pilots")

if st.sidebar.button("Pobierz i analizuj"):
    tracks = ITunesSource().fetch(query=artist, country="US", limit=200)
    df = to_df(tracks)
    df = filter_by_artist(df, artist)

    if df.empty:
        st.warning("Brak danych")
        st.stop()

    tab1, tab2, tab3, tab4 = st.tabs([
        "Wszystkie utwory",
        "Najnowsze utwory",
        "Analiza utworów",
        "Analiza gatunków"
    ])

    with tab1:
        st.subheader("Wszystkie utwory artysty")
        df_all = df.copy()
        
        # Zamiana nazw kolumn na polskie
        df_all = df_all.rename(columns={
            "track": "Tytuł utworu",
            "artist": "Artysta",
            "album": "Album",
            "genre": "Gatunek",
            "release_year": "Rok wydania",
            "duration_min": "Długość (minuty)"
        })
        
        df_all["Rok wydania"] = df_all["Rok wydania"].astype("string")
        df_all["Długość (minuty)"] = df_all["Długość (minuty)"].round(2)
        
        st.dataframe(
            df_all[[
                "Tytuł utworu",
                "Artysta",
                "Album",
                "Gatunek",
                "Rok wydania",
                "Długość (minuty)"
            ]],
            use_container_width=True,
            hide_index=True
        )


    with tab2:
        st.subheader("Najnowsze utwory artysty")
        newest_df = newest_tracks(df).copy()

        newest_df = newest_df.rename(columns={
            "track": "Tytuł utworu",
            "artist": "Artysta",
            "album": "Album",
            "genre": "Gatunek",
            "release_year": "Rok wydania",
            "duration_min": "Długość (minuty)"
        })

        newest_df.insert(0, "Lp.", range(1, len(newest_df)+1))
        newest_df["Długość (minuty)"] = newest_df["Długość (minuty)"].round(2)
        newest_df["Rok wydania"] = newest_df["Rok wydania"].astype(str)

        st.dataframe(
            newest_df[[
                "Tytuł utworu",
                "Artysta",
                "Album",
                "Gatunek",
                "Rok wydania",
                "Długość (minuty)"
            ]],
            use_container_width=True,
            hide_index=True
        )


    with tab3:
        metrics = kpi(df)
        c1, c2, c3 = st.columns(3)

        c1.metric("Utwory", metrics["utwory"])
        c2.metric("Gatunki", metrics["gatunki"])
        c3.metric("Śr. długość utworów (min)", metrics["średnia_długość_min"])
        col1, col2 = st.columns(2)
        with col1:
            st.subheader("Rozkład długości utworów")
            st.bar_chart(plot_duration_hist(df))
        with col2:
            st.subheader("Utwory wg roku wydania")
            st.line_chart(plot_year_counts(df))

    with tab4:
        st.subheader("Top gatunki")
        tg = plot_top_genres(df)

        tg = tg.rename(columns={
            "genre": "Gatunek",
            "tracks_count": "Liczba utworów"
        })

        tg["Procentowy udział"] = (tg["Liczba utworów"] / tg["Liczba utworów"].sum() * 100).round(1)

        st.dataframe(tg, use_container_width=True, hide_index=True)
        
        st.subheader("Trendy gatunkowe")
        st.area_chart(plot_genre_trends(df))
        
        st.subheader("Liczba utworów dla poszczególnych gatunków")
        st.bar_chart(tg.set_index("Gatunek")["Liczba utworów"])

        st.subheader("Średnia długość utworów wg gatunku")
        st.bar_chart(plot_genre_avg_duration(df))
