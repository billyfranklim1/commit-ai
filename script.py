import openai
import sys
import os

openai.api_key = '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'

def get_git_diff():
    diff_command = 'git diff  --cached'
    return os.popen(diff_command).read()

def generate_commit_messages(diff):

    response = openai.chat.completions.create(
        messages=[
            {
                "role": "user",
                "content": f"suggest 3 commit messages based on the following diff, if diff is empty repository e first commit :\n\n{diff}\n\ncommit messages should:\n  - follow conventional commits,\n  - message format should be: <type>[scope]: <description>,\n\n\"examples:\",\n\" - 🐛 fix(authentication): add password regex pattern\",\n\" -✨ feat(storage): add new test cases\",\n",
            }
        ],
        model="gpt-3.5-turbo",
    )

    return response.choices[0].message.content

def main():
    diff = get_git_diff()

    commit_messages = generate_commit_messages(diff)
    commit_messages = commit_messages.split("\n")
    print("Suggested commit messages:")

    for message in commit_messages:
        print(message)

    selected_option = input("Choose one of the options above: ")
    selected_option = int(selected_option)
    if selected_option < 1 or selected_option > 3:
        print("Invalid option")
        sys.exit(1)

    commit_message = commit_messages[selected_option - 1]
    os.system(f'git commit -m "{commit_message}"')
    print(f'Committed with message: "{commit_message}"')


if __name__ == "__main__":
    main()
