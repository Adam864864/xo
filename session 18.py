import streamlit as st


if "board" not in st.session_state:
    st.session_state.board = [""] * 9
    st.session_state.turn = "X"
    st.session_state.winner = None


def check_winner(board):
    combos = [(0,1,2), (3,4,5), (6,7,8),
              (0,3,6), (1,4,7), (2,5,8),
              (0,4,8), (2,4,6)]
    for i, j, k in combos:
        if board[i] == board[j] == board[k] != "":
            return board[i]
    if "" not in board:
        return'tie'
    return None

def reset():
    st.session_state.board = [""] * 9
    st.session_state.turn = "X"
    st.session_state.winner = None

st.title(('xo game'))


cols = st.columns(3)
for i in range(3):
    for j in range(3):
        idx = 3 * i + j
        if st.session_state.board[idx] == "":
            if st.session_state.winner or st.button(" ", key=idx):
                if not st.session_state.winner:
                    st.session_state.board[idx] = st.session_state.turn
                    st.session_state.winner = check_winner(st.session_state.board)
                    if not st.session_state.winner:
                        st.session_state.turn = "O" if st.session_state.turn == "X" else "X"
        else:
            cols[j].button(st.session_state.board[idx], key=idx, disabled=True)


if st.session_state.winner:
    if st.session_state.winner == "tie":
        st.success('the game has been finished!')
    else:
        st.success(f"the player {st.session_state.winner} won!")
    if st.button("play again"):
        reset()
