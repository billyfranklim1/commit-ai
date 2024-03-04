import openai
import sys
import os
from prompt_toolkit import prompt
from prompt_toolkit.shortcuts import checkboxlist_dialog

openai.api_key = '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'

def get_git_diff():
    diff_command = 'git diff  --cached'
    return os.popen(diff_command).read()

def generate_commit_messages(diff):

    response = openai.chat.completions.create(
        messages=[
            {
                "role": "user",
                "content": f"suggest 3 commit messages based on the following diff, if diff is empty repository e first commit :\n\n{diff}\n\ncommit messages should:\n  - follow conventional commits,\n  - message format should be: <type>[scope]: <description>,\n\n\"examples:\",\n\" - 🐛 fix(authentication): add password regex pattern\",\n\" -✨ feat(storage): add new test cases\",\n seja preciso quanto aos emojis",
            }
        ],
        model="gpt-3.5-turbo",
    )

    return response.choices[0].message.content

def main():
    diff = get_git_diff()

    commit_messages = generate_commit_messages(diff).split("\n")
    commit_messages.append("Generate new commit messages")
    commit_messages.append("Exit")

    selected = checkboxlist_dialog(
        title="Commit Messages",
        text="Choose one of the options below:",
        values=[(i, msg) for i, msg in enumerate(commit_messages, start=1)]
    ).run()

    if not selected:
        print("No option selected")
        return

    for option in selected:
        if option == len(commit_messages) - 1:  # Generate new commit messages
            os.system('clear')  # or 'cls' on Windows
            main()
            return
        elif option == len(commit_messages):  # Exit
            sys.exit(0)
        else:
            commit_message = commit_messages[option - 1]
            os.system(f'git commit -m "{commit_message}"')
            print(f'Committed with message: "{commit_message}"')

if __name__ == "__main__":
    main()