def print_board(board):
    # Fungsi ini digunakan untuk mencetak papan permainan Tic Tac Toe.
    # Menggunakan karakter garis horisontal dan vertikal untuk membuat tampilan papan.

    print("-------------")
    for i in range(3):
        print("|", end=" ")
        for j in range(3):
            print(board[i][j], "|", end=" ")
        print("\n-------------")

def check_winner(board):
    # Fungsi ini digunakan untuk memeriksa apakah ada pemenang dalam permainan Tic Tac Toe.
    # Memeriksa baris, kolom, dan diagonal untuk kemungkinan pemenang.

    # Cek baris
    for i in range(3):
        if board[i][0] == board[i][1] == board[i][2] != ' ':
            return board[i][0]

    # Cek kolom
    for j in range(3):
        if board[0][j] == board[1][j] == board[2][j] != ' ':
            return board[0][j]

    # Cek diagonal
    if board[0][0] == board[1][1] == board[2][2] != ' ':
        return board[0][0]
    if board[0][2] == board[1][1] == board[2][0] != ' ':
        return board[0][2]

    return None

def is_board_full(board):
    # Fungsi ini digunakan untuk memeriksa apakah papan permainan sudah penuh.
    # Jika tidak ada lagi ruang kosong (spasi), maka papan dianggap penuh.

    for row in board:
        if ' ' in row:
            return False
    return True

def play_game():
    # Fungsi utama untuk memulai permainan Tic Tac Toe.

    board = [[' ' for _ in range(3)] for _ in range(3)]  # Membuat papan permainan kosong
    current_player = 'X'  # Menandai pemain saat ini

    while True:
        print_board(board)  # Cetak papan permainan

        # Input posisi yang ingin diisi
        row = int(input("Masukkan nomor baris (0-2): "))
        col = int(input("Masukkan nomor kolom (0-2): "))

        # Periksa apakah posisi sudah terisi
        if board[row][col] != ' ':
            print("Posisi sudah terisi. Coba lagi.")
            continue

        # Isi posisi dengan simbol pemain saat ini
        board[row][col] = current_player

        # Periksa pemenang
        winner = check_winner(board)
        if winner:
            print_board(board)
            print("Selamat, pemain", winner, "menang!")
            break

        # Periksa jika permainan seri
        if is_board_full(board):
            print_board(board)
            print("Permainan seri!")
            break

        # Ganti giliran pemain
        current_player = 'O' if current_player == 'X' else 'X'

# Memulai permainan
play_game()
