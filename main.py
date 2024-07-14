import streamlit as st
import random

st.set_page_config(layout="wide")
col1, col2 = st.columns(2)

with col1:
    st.image("images/designer.png")

with col2:
    st.title("SNAKE-WATER-GUN GAME")
    content = """
    You're referring to the classic "Rock, Paper, Scissors" game, but with a twist! Instead of rock, paper, and scissors, the game is played with snake, water, and gun. Here are the rules:

- Snake (represented by a hand gesture of a snake) beats Water (represented by a hand gesture of a wave)
- Water beats Gun (represented by a hand gesture of a gun)
- Gun beats Snake
To play, two players simultaneously throw one of the three hand gestures, and the winning hand beats the losing hand according to the rules above. If both players throw the same gesture, the game is a tie and can be replayed.
    """
    st.info(content)

col3, emptycol, col5 = st.columns([7, 1, 2])

with col3:
    st.markdown("<h1 style='text-align: center;'>Rules of the game explained</h1>",
    unsafe_allow_html = True)
    st.write("""
    You're referring to the classic "Rock, Paper, Scissors" game, but with a twist! Instead of rock, paper, and scissors, the game is played with snake, water, and gun. Here are the rules:
    
    - Snake (represented by a hand gesture of a snake) beats Water (represented by a hand gesture of a wave)
    - Water beats Gun (represented by a hand gesture of a gun)
    - Gun beats Snake
    
    To play, two players simultaneously throw one of the three hand gestures, and the winning hand beats the losing hand according to the rules above. If both players throw the same gesture, the game is a tie and can be replayed.
    
    This game is a fun variation of the classic "Rock, Paper, Scissors" game, and can be enjoyed by people of all ages!
    """)

with col5:
    st.markdown("<h4 style='text-align: center;'>Select hand:</h4>",
            unsafe_allow_html=True)
    user_hand = st.selectbox("", ["Snake", "Water", "Gun"], key="user_hand")

option_list = ["Snake", "Water", "Gun"]
computer_hand = random.choice(option_list)

if option_list:
    if computer_hand == user_hand:
        st.info(f"""
        You choose {user_hand}, Computer choose {computer_hand}
        The game is a draw!
    """)

    else:
        if computer_hand == "Snake":
            if user_hand == "Water":
                st.info(f"""
                You choose {user_hand}, Computer choose {computer_hand}
                Computer won!
    """)

            elif user_hand == "Gun":
                st.info(f"""
                You choose {user_hand}, Computer choose {computer_hand}
                You won!
    """)

        elif computer_hand == "Water":
            if user_hand == "Gun":
                st.info(f"""
                You choose {user_hand}, Computer choose {computer_hand}
                Computer won!""")

            elif user_hand == "Snake":
                st.info(f"""
                You choose {user_hand}, Computer choose {computer_hand}
                Computer won!
    """)

        elif computer_hand == "Gun":
            if user_hand == "Snake":
                st.info(f"""
                You choose {user_hand}, Computer choose {computer_hand}
                Computer won!
    """)

            elif user_hand == "Water":
                st.info(f"""
                You choose {user_hand}, Computer choose {computer_hand}
                You won!""")

