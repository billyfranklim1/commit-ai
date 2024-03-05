import openai
import sys
import os
from prompt_toolkit import prompt
from termcolor import colored
import re

openai.api_key = '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'

def get_git_diff():
    diff_command = 'git diff  --cached'
    return os.popen(diff_command).read()

def generate_commit_messages(diff):

    response = openai.chat.completions.create(
        messages=[
            {
                "role": "user",
                "content": f"suggest 3 commit messages based on the following diff, if diff is empty repository e first commit :\n\n{diff}\n\ncommit messages should:\n  - follow conventional commits,\n  - message format should be: <type>[scope]: <description>,\n\n\"examples:\",\n\" - 🐛 fix(authentication): add password regex pattern\",\n\" -✨ feat(storage): add new test cases\",\n seja preciso quanto aos emojis, sem bulet points",
            }
        ],
        model="gpt-3.5-turbo",
    )

    return response.choices[0].message.content

def main():
    try:
        while True:
            diff = get_git_diff()

            if not diff:
                print(colored("No changes to commit. Execute 'git add' to stage changes.", "red"))
                sys.exit(1)

            commit_messages = generate_commit_messages(diff)
            commit_messages = commit_messages.split("\n")
            commit_messages = [re.sub(r'^\d+\.\s+', '', message) for message in commit_messages if message]

            print(colored("Suggested commit messages:", "cyan"))

            for i, message in enumerate(commit_messages, start=1):
                print(colored(f"{i}: {message}", "cyan"))

            selected_option = input("Choose one of the options above (or press 'r' to refresh, 'q' to quit): \n")
            if selected_option.lower() == 'q':
                print(colored("Quitting...", "yellow"))
                break
            elif selected_option.lower() == 'r':
                print(colored("Refreshing commit messages...", "cyan"))
                continue

            selected_option = int(selected_option)
            if selected_option < 1 or selected_option > len(commit_messages):
                print(colored("Invalid option", "red"))
                continue

            commit_message = commit_messages[selected_option - 1]
            final_commit_message = prompt(f"Edit the commit message if needed: ", default=commit_message)

            print(colored(f'Final commit message: "{final_commit_message}"', "yellow"))
            os.system(f'git commit -m "{final_commit_message}"')
            break

    except KeyboardInterrupt:
        print(colored("\nOperation cancelled by user.", "red"))
        sys.exit(1)
    except ValueError:
        print(colored("Please enter a valid number.", "red"))
        main()



if __name__ == "__main__":
    main()
