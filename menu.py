import curses
import os

# Simula a obtenção de mensagens de commit (substitua pela sua função real)
def get_commit_messages():
    return ["fix(authentication): add password regex pattern",
            "feat(storage): add new test cases",
            "chore(docs): update README",
            "Generate new commit messages",
            "Exit"]

# Função para exibir o menu e capturar a escolha do usuário
def show_menu(stdscr, commit_messages):
    curses.curs_set(0)  # Esconde o cursor
    current_row = 0

    while True:
        stdscr.clear()  # Limpa a tela

        for idx, message in enumerate(commit_messages):
            x = 0
            y = idx
            if idx == current_row:
                stdscr.attron(curses.color_pair(1))
                stdscr.addstr(y, x, message)
                stdscr.attroff(curses.color_pair(1))
            else:
                stdscr.addstr(y, x, message)
        
        stdscr.refresh()

        key = stdscr.getch()

        if key == curses.KEY_UP and current_row > 0:
            current_row -= 1
        elif key == curses.KEY_DOWN and current_row < len(commit_messages) - 1:
            current_row += 1
        elif key == curses.KEY_ENTER or key in [10, 13]:
            return current_row

def main(stdscr):
    # Configurações iniciais do curses
    curses.start_color()
    curses.init_pair(1, curses.COLOR_BLACK, curses.COLOR_WHITE)

    commit_messages = get_commit_messages()
    selected_option = show_menu(stdscr, commit_messages)

    # Aqui você adicionaria sua lógica para tratar a opção selecionada
    # Por exemplo, chamar a função para commitar com a mensagem selecionada
    print(f"Você selecionou: {commit_messages[selected_option]}")

# Executa o programa principal dentro do wrapper do curses para inicialização e finalização adequadas
curses.wrapper(main)
