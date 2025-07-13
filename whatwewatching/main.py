import streamlit as st
import openai
import datetime
import requests
from dotenv import load_dotenv
import os

# Load environment variables from .env
load_dotenv()

# Get api keys
api_key = os.getenv("OPENAI_API_KEY")


# --- App Styling ---
st.set_page_config(page_title="WhatWeWatching", page_icon="🎬", layout="centered")
st.markdown(
    """
    <style>
        body {
            font-family: 'TT Commons Pro', sans-serif;
            background-color: #fffaf1;
        }
        h1, h2, h3 {
            font-family: 'Montserrat', sans-serif;
            color: #2e2101;
        }
        .stButton>button {
            background-color: #f1b21f;
            color: white;
            border-radius: 10px;
        }
    </style>
""",
    unsafe_allow_html=True,
)

# --- Logo & Title ---
st.markdown(
    """
    <div style='text-align: center;'>
        <h1 style='color:#5b3814;'>🎬 WhatWeWatching</h1>
        <p style='font-size:16px; color:#5b3814;'>A Fafacodes product – Mood-based show recommendations only.</p>
    </div>
    <br>
""",
    unsafe_allow_html=True,
)

# --- User Inputs ---
st.subheader("🎯 Choose your vibe")

content_type = st.selectbox("Movie or Series", ["", "Movie", "Series"])

season_range = (None, None)
episode_range = (None, None)

if content_type == "Series":
    season_range = st.slider("Number of Seasons", 1, 10, (1, 3))
    episode_range = st.slider("Episodes per Season", 1, 30, (1, 10))


genres = st.multiselect(
    "Select Genre(s)",
    [
        "Action",
        "Drama",
        "Comedy",
        "Adventure",
        "Science Fiction",
        "Fantasy",
        "Thriller",
        "Horror",
        "Romance",
        "Animation",
    ],
)
release_year = st.slider(
    "Release Year Range", 1980, datetime.datetime.now().year, (2010, 2024)
)
industry = st.selectbox(
    "Select Industry",
    ["", "Hollywood", "Nollywood", "Bollywood", "Korean Cinema", "UK Cinema"],
)
services = st.multiselect(
    "Available On", ["Netflix", "Amazon Prime Video", "Disney+", "Max", "Hulu"]
)
actors = st.text_input("Actors or Actresses (e.g. Viola Davis, Shah Rukh Khan)")


# --- Prompt Construction ---
def build_prompt():
    season_text = ""
    if content_type == "Series" and "season_range" in locals() and "episode_range" in locals():
        season_text = f"\nIf the type is 'Series', recommend only shows with {season_range[0]}–{season_range[1]} seasons and {episode_range[0]}–{episode_range[1]} episodes per season."

    prompt = f"""
You are a global movie and TV series expert.
Return up to 5 highly rated and mood-based recommendations based on the criteria below.

Only recommend *{content_type if content_type else 'movies or series'}*. If "Movie" is selected, do NOT include series. If "Series" is selected, do NOT include movies.

Filter based on:
- Genre(s): {", ".join(genres) if genres else "Any"}
- Release Year Range: {release_year[0]} to {release_year[1]}
- Film Industry: {industry if industry else "Any"}
- Streaming Platforms: {", ".join(services) if services else "Any"}
- Featuring: {actors if actors else "Any"}{season_text}

Format each recommendation like this:
Title: ...
Description: (max 3 sentences)
Duration: ...
IMDb Rating: ...
Rotten Tomatoes Rating: ...
Available On: ...
Category: ...

If no filters are provided, return 1 globally top-rated {content_type if content_type else 'movie or series'} currently trending.
""".strip()

    return prompt


# --- Recommendation Engine ---
if st.button("🎬 Recommend Something Good"):
    prompt = build_prompt()

    with st.spinner("Finding your perfect watch list..."):
        try:
            # Create the OpenAI client
            client = openai.OpenAI(api_key=api_key)

            # Create a placeholder for live response
            response_box = st.empty()
            full_response = ""

            stream_response = client.chat.completions.create(
                model="gpt-4",
                messages=[
                    {
                        "role": "system",
                        "content": "You are an expert movie and series curator. Only return what is explicitly requested.",
                    },
                    {"role": "user", "content": prompt},
                ],
                temperature=0.8,
                max_tokens=1000,
                stream=True,  # <-- streaming enabled
            )

            # Show loading text
            st.subheader("🍿 Here's what you should watch:")
            placeholder = st.empty()

            collected_chunks = ""
            for chunk in stream_response:
                content = chunk.choices[0].delta.content
                if content:
                    collected_chunks += content
                    placeholder.markdown(collected_chunks)

        except Exception as e:
            st.error(f"Error fetching recommendations: {e}")

# Footer
st.markdown(
    """
    <br><hr>
    <div style='text-align:center;font-size:14px;color:#2e2101;'>
        Built with 💥 by <b>Fafacodes</b> 
    </div>
""",
    unsafe_allow_html=True,
)
