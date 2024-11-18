import time
import os

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

def draw_tunnel():
    tunnel_length = 20
    for i in range(tunnel_length):
        clear_screen()
        print(" " * (tunnel_length - i) + "||")
        print(" " * (tunnel_length - i) + "||")
        print(" " * (tunnel_length - i) + "||")
        time.sleep(0.1)

def welcome_message():
    clear_screen()
    print("WELCOME TO THE IT")

if __name__ == "__main__":
    draw_tunnel()
    welcome_message()

