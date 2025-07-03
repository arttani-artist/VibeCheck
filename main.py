pip install streamlit

import streamlit as st
import random
import math

# Configuration
st.set_page_config(
    page_title="Mood Playlist Suggester",
    page_icon="🎵",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Custom CSS for styling
st.markdown("""
<style>
    .main-header {
        text-align: center;
        color: #1DB954;
        font-size: 3rem;
        margin-bottom: 2rem;
        text-shadow: 2px 2px 4px rgba(0,0,0,0.1);
    }
    
    .playlist-card {
        background: linear-gradient(135deg, #1DB954, #1ed760);
        padding: 1.5rem;
        border-radius: 15px;
        margin: 1rem 0;
        color: white;
        box-shadow: 0 4px 15px rgba(29, 185, 84, 0.3);
        transition: transform 0.3s ease;
    }
    
    .playlist-card:hover {
        transform: translateY(-5px);
    }
    
    .mood-indicator {
        font-size: 1.2rem;
        margin: 0.5rem 0;
        padding: 0.5rem;
        border-radius: 10px;
        background: rgba(255, 255, 255, 0.1);
    }
    
    .generated-name {
        background: linear-gradient(135deg, #FF6B6B, #4ECDC4);
        padding: 1rem;
        border-radius: 15px;
        color: white;
        text-align: center;
        margin: 1rem 0;
        font-size: 1.5rem;
        font-weight: bold;
    }
    
    .stButton > button {
        background: linear-gradient(135deg, #1DB954, #1ed760);
        color: white;
        border: none;
        border-radius: 25px;
        padding: 0.75rem 2rem;
        font-size: 1.1rem;
        font-weight: bold;
        transition: all 0.3s ease;
    }
    
    .stButton > button:hover {
        background: linear-gradient(135deg, #1ed760, #1DB954);
        transform: translateY(-2px);
        box-shadow: 0 5px 15px rgba(29, 185, 84, 0.4);
    }
</style>
""", unsafe_allow_html=True)

# Playlist Database - Add your actual Spotify playlist links here
PLAYLISTS = {
    # High Energy Playlists
    "high_energy_happy": [
        {
            "name": "🔥 Workout Bangers",
            "url": "https://open.spotify.com/playlist/YOUR_PLAYLIST_ID_1",
            "description": "High-energy tracks to fuel your workout"
        },
        {
            "name": "⚡ Dance Party",
            "url": "https://open.spotify.com/playlist/YOUR_PLAYLIST_ID_2",
            "description": "Dance like nobody's watching"
        },
        {
            "name": "🎉 Feel Good Hits",
            "url": "https://open.spotify.com/playlist/YOUR_PLAYLIST_ID_3",
            "description": "Uplifting songs to boost your mood"
        }
    ],
    
    "high_energy_neutral": [
        {
            "name": "🚀 Motivation Station",
            "url": "https://open.spotify.com/playlist/YOUR_PLAYLIST_ID_4",
            "description": "Get things done with these energetic tracks"
        },
        {
            "name": "⚡ Power Hour",
            "url": "https://open.spotify.com/playlist/YOUR_PLAYLIST_ID_5",
            "description": "High-energy focus music"
        }
    ],
    
    "high_energy_sad": [
        {
            "name": "😤 Angry Workout",
            "url": "https://open.spotify.com/playlist/YOUR_PLAYLIST_ID_6",
            "description": "Channel your emotions into energy"
        },
        {
            "name": "🔥 Aggressive Beats",
            "url": "https://open.spotify.com/playlist/YOUR_PLAYLIST_ID_7",
            "description": "High-energy music for intense moods"
        }
    ],
    
    # Medium Energy Playlists
    "medium_energy_happy": [
        {
            "name": "☀️ Good Vibes Only",
            "url": "https://open.spotify.com/playlist/YOUR_PLAYLIST_ID_8",
            "description": "Balanced energy with positive vibes"
        },
        {
            "name": "🌈 Sunny Day Mix",
            "url": "https://open.spotify.com/playlist/YOUR_PLAYLIST_ID_9",
            "description": "Perfect for a pleasant day"
        }
    ],
    
    "medium_energy_neutral": [
        {
            "name": "🎵 Daily Driver",
            "url": "https://open.spotify.com/playlist/YOUR_PLAYLIST_ID_10",
            "description": "Your everyday listening companion"
        },
        {
            "name": "🎧 Background Beats",
            "url": "https://open.spotify.com/playlist/YOUR_PLAYLIST_ID_11",
            "description": "Perfect for work or casual listening"
        }
    ],
    
    "medium_energy_sad": [
        {
            "name": "💙 Melancholic Indie",
            "url": "https://open.spotify.com/playlist/YOUR_PLAYLIST_ID_12",
            "description": "Thoughtful songs for contemplative moments"
        },
        {
            "name": "🌧️ Rainy Day Vibes",
            "url": "https://open.spotify.com/playlist/YOUR_PLAYLIST_ID_13",
            "description": "For when you need to feel your feelings"
        }
    ],
    
    # Low Energy Playlists
    "low_energy_happy": [
        {
            "name": "😌 Peaceful Bliss",
            "url": "https://open.spotify.com/playlist/YOUR_PLAYLIST_ID_14",
            "description": "Gentle, happy songs for relaxation"
        },
        {
            "name": "🌸 Soft & Sweet",
            "url": "https://open.spotify.com/playlist/YOUR_PLAYLIST_ID_15",
            "description": "Tender music for quiet moments"
        }
    ],
    
    "low_energy_neutral": [
        {
            "name": "🌙 Late Night Chill",
            "url": "https://open.spotify.com/playlist/YOUR_PLAYLIST_ID_16",
            "description": "Perfect for winding down"
        },
        {
            "name": "☁️ Ambient Dreams",
            "url": "https://open.spotify.com/playlist/YOUR_PLAYLIST_ID_17",
            "description": "Atmospheric music for relaxation"
        }
    ],
    
    "low_energy_sad": [
        {
            "name": "💔 Heartbreak Hotel",
            "url": "https://open.spotify.com/playlist/YOUR_PLAYLIST_ID_18",
            "description": "For when you need to process emotions"
        },
        {
            "name": "🌊 Deep Feels",
            "url": "https://open.spotify.com/playlist/YOUR_PLAYLIST_ID_19",
            "description": "Profound sadness, beautiful music"
        }
    ],
    
    # Time-based playlists
    "morning": [
        {
            "name": "☕ Coffee Shop Vibes",
            "url": "https://open.spotify.com/playlist/YOUR_PLAYLIST_ID_20",
            "description": "Perfect morning soundtrack"
        },
        {
            "name": "🌅 Rise & Shine",
            "url": "https://open.spotify.com/playlist/YOUR_PLAYLIST_ID_21",
            "description": "Start your day right"
        }
    ],
    
    "evening": [
        {
            "name": "🌅 Golden Hour",
            "url": "https://open.spotify.com/playlist/YOUR_PLAYLIST_ID_22",
            "description": "Sunset vibes"
        },
        {
            "name": "🍷 Evening Wind Down",
            "url": "https://open.spotify.com/playlist/YOUR_PLAYLIST_ID_23",
            "description": "Relaxing evening music"
        }
    ],
    
    "night": [
        {
            "name": "🌙 Midnight Moods",
            "url": "https://open.spotify.com/playlist/YOUR_PLAYLIST_ID_24",
            "description": "Late-night listening"
        },
        {
            "name": "✨ After Hours",
            "url": "https://open.spotify.com/playlist/YOUR_PLAYLIST_ID_25",
            "description": "For those late-night vibes"
        }
    ],
    
    # Focus-based playlists
    "high_focus": [
        {
            "name": "🎯 Deep Focus",
            "url": "https://open.spotify.com/playlist/YOUR_PLAYLIST_ID_26",
            "description": "Instrumental focus music"
        },
        {
            "name": "📚 Study Session",
            "url": "https://open.spotify.com/playlist/YOUR_PLAYLIST_ID_27",
            "description": "Perfect for concentration"
        }
    ],
    
    "low_focus": [
        {
            "name": "🌀 Dreamy Escape",
            "url": "https://open.spotify.com/playlist/YOUR_PLAYLIST_ID_28",
            "description": "Let your mind wander"
        },
        {
            "name": "☁️ Ambient Flow",
            "url": "https://open.spotify.com/playlist/YOUR_PLAYLIST_ID_29",
            "description": "Atmospheric background music"
        }
    ]
}

def get_mood_category(energy, happiness):
    """Determine mood category based on energy and happiness levels"""
    if energy >= 70:
        energy_cat = "high_energy"
    elif energy >= 40:
        energy_cat = "medium_energy"
    else:
        energy_cat = "low_energy"
    
    if happiness >= 60:
        mood_cat = "happy"
    elif happiness >= 40:
        mood_cat = "neutral"
    else:
        mood_cat = "sad"
    
    return f"{energy_cat}_{mood_cat}"

def generate_playlist_name(energy, happiness, focus, time_of_day):
    """Generate a creative playlist name based on mood parameters"""
    
    energy_words = {
        "high": ["Electric", "Energetic", "Pumped", "Intense", "Dynamic"],
        "medium": ["Balanced", "Steady", "Smooth", "Flowing", "Grounded"],
        "low": ["Chill", "Mellow", "Calm", "Peaceful", "Gentle"]
    }
    
    happiness_words = {
        "happy": ["Joyful", "Bright", "Uplifting", "Sunny", "Radiant"],
        "neutral": ["Balanced", "Steady", "Even", "Centered", "Stable"],
        "sad": ["Melancholic", "Thoughtful", "Reflective", "Deep", "Contemplative"]
    }
    
    focus_words = {
        "high": ["Focus", "Concentration", "Zone", "Sharp", "Laser"],
        "low": ["Dreamy", "Flowing", "Ambient", "Spacey", "Atmospheric"]
    }
    
    time_words = {
        "morning": ["Dawn", "Sunrise", "Morning", "Fresh", "New"],
        "evening": ["Sunset", "Dusk", "Golden", "Twilight", "Evening"],
        "night": ["Midnight", "Nocturnal", "Late Night", "After Dark", "Moonlight"],
        "any": ["Current", "Today's", "Right Now", "Present", "This Moment"]
    }
    
    # Categorize values
    energy_cat = "high" if energy >= 70 else "medium" if energy >= 40 else "low"
    happiness_cat = "happy" if happiness >= 60 else "neutral" if happiness >= 40 else "sad"
    focus_cat = "high" if focus >= 70 else "low"
    
    # Generate name components
    energy_word = random.choice(energy_words[energy_cat])
    happiness_word = random.choice(happiness_words[happiness_cat])
    focus_word = random.choice(focus_words[focus_cat])
    time_word = random.choice(time_words[time_of_day])
    
    # Create different name patterns
    patterns = [
        f"{time_word} {energy_word} Mix",
        f"{happiness_word} {focus_word} Session",
        f"My {energy_word} {time_word} Mood",
        f"{focus_word} {happiness_word} Vibes",
        f"{time_word} {happiness_word} Playlist"
    ]
    
    return random.choice(patterns)

def get_matching_playlists(energy, happiness, focus, time_of_day):
    """Get playlists that match the current mood"""
    matching_playlists = []
    
    # Get mood-based playlists
    mood_category = get_mood_category(energy, happiness)
    if mood_category in PLAYLISTS:
        matching_playlists.extend(PLAYLISTS[mood_category])
    
    # Add time-based playlists
    if time_of_day != "any" and time_of_day in PLAYLISTS:
        matching_playlists.extend(PLAYLISTS[time_of_day])
    
    # Add focus-based playlists
    if focus >= 70 and "high_focus" in PLAYLISTS:
        matching_playlists.extend(PLAYLISTS["high_focus"])
    elif focus <= 30 and "low_focus" in PLAYLISTS:
        matching_playlists.extend(PLAYLISTS["low_focus"])
    
    # Remove duplicates and shuffle
    seen = set()
    unique_playlists = []
    for playlist in matching_playlists:
        if playlist["name"] not in seen:
            seen.add(playlist["name"])
            unique_playlists.append(playlist)
    
    random.shuffle(unique_playlists)
    return unique_playlists[:6]  # Return top 6 matches

def main():
    # Header
    st.markdown('<h1 class="main-header">🎵 Mood Playlist Suggester</h1>', unsafe_allow_html=True)
    st.markdown('<p style="text-align: center; font-size: 1.2rem; color: #666; margin-bottom: 2rem;">Tell us how you\'re feeling, and we\'ll find the perfect Spotify playlist for your mood</p>', unsafe_allow_html=True)
    
    # Sidebar controls
    st.sidebar.header("🎛️ Mood Controls")
    
    # Energy slider
    energy = st.sidebar.slider(
        "⚡ Energy Level",
        min_value=0,
        max_value=100,
        value=50,
        help="How energetic are you feeling? 0 = Sleepy, 100 = Energetic"
    )
    
    # Happiness slider
    happiness = st.sidebar.slider(
        "😊 Happiness Level",
        min_value=0,
        max_value=100,
        value=50,
        help="How happy are you feeling? 0 = Sad, 100 = Joyful"
    )
    
    # Focus slider
    focus = st.sidebar.slider(
        "🧠 Focus Level",
        min_value=0,
        max_value=100,
        value=50,
        help="How focused do you want to be? 0 = Dreamy, 100 = Laser Focus"
    )
    
    # Time of day
    time_of_day = st.sidebar.selectbox(
        "🕐 Time of Day",
        options=["any", "morning", "evening", "night"],
        format_func=lambda x: {
            "any": "Any Time",
            "morning": "Morning ☀️",
            "evening": "Evening 🌅",
            "night": "Night 🌙"
        }[x]
    )
    
    # Generate button
    if st.sidebar.button("🎲 Generate New Suggestions"):
        st.rerun()
    
    # Main content area
    col1, col2 = st.columns([2, 1])
    
    with col1:
        # Current mood display
        st.subheader("📊 Your Current Mood")
        
        mood_col1, mood_col2, mood_col3 = st.columns(3)
        
        with mood_col1:
            st.markdown(f'<div class="mood-indicator">⚡ Energy: {energy}%</div>', unsafe_allow_html=True)
        
        with mood_col2:
            st.markdown(f'<div class="mood-indicator">😊 Happiness: {happiness}%</div>', unsafe_allow_html=True)
        
        with mood_col3:
            st.markdown(f'<div class="mood-indicator">🧠 Focus: {focus}%</div>', unsafe_allow_html=True)
        
        # Generated playlist name
        generated_name = generate_playlist_name(energy, happiness, focus, time_of_day)
        st.markdown(f'<div class="generated-name">🎵 Suggested Playlist Name: "{generated_name}"</div>', unsafe_allow_html=True)
        
        # Matching playlists
        st.subheader("🎧 Your Spotify Playlists")
        
        matching_playlists = get_matching_playlists(energy, happiness, focus, time_of_day)
        
        if matching_playlists:
            for playlist in matching_playlists:
                st.markdown(f"""
                <div class="playlist-card">
                    <h3>{playlist['name']}</h3>
                    <p>{playlist['description']}</p>
                    <a href="{playlist['url']}" target="_blank" style="color: white; text-decoration: none; font-weight: bold;">
                        🎵 Open in Spotify →
                    </a>
                </div>
                """, unsafe_allow_html=True)
        else:
            st.info("No playlists match your current mood. Try adjusting your settings!")
    
    with col2:
        # Mood visualization
        st.subheader("🎨 Mood Visualization")
        
        # Create a simple mood chart
        mood_data = {
            "Energy": energy,
            "Happiness": happiness,
            "Focus": focus
        }
        
        st.bar_chart(mood_data)
        
        # Mood description
        st.subheader("💭 Mood Description")
        
        energy_desc = "High energy! 🔥" if energy >= 70 else "Medium energy 🌟" if energy >= 40 else "Low energy 😴"
        happiness_desc = "Very happy! 😄" if happiness >= 70 else "Neutral mood 😐" if happiness >= 40 else "Feeling down 😔"
        focus_desc = "Super focused! 🎯" if focus >= 70 else "Moderate focus 👀" if focus >= 40 else "Dreamy state 🌙"
        
        st.write(f"**Energy:** {energy_desc}")
        st.write(f"**Happiness:** {happiness_desc}")
        st.write(f"**Focus:** {focus_desc}")
        
        # Instructions
        st.subheader("📝 How to Use")
        st.write("""
        1. **Adjust the sliders** in the sidebar to match your current mood
        2. **Select time of day** for additional context
        3. **Click on any playlist** to open it directly in Spotify
        4. **Generate new suggestions** to discover different playlists
        """)
        
        # Tips
        st.subheader("💡 Tips")
        st.write("""
        - **High energy + Happy** = Workout & dance playlists
        - **Low energy + Sad** = Emotional & contemplative music
        - **High focus** = Instrumental & study playlists
        - **Evening/Night** = Chill & ambient playlists
        """)

if __name__ == "__main__":
    main()
