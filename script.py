import openai
import sys
import os

# Configure sua chave da API do OpenAI aqui
openai.api_key = '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'

def get_git_diff():
    # Substitua 'your_diff_command' pelo comando correto para obter o diff do git
    diff_command = 'git diff'
    return os.popen(diff_command).read()

def generate_commit_messages(diff):

    response = openai.Completion.create(
        engine="gpt-3.5-turbo-instruct",
        prompt=f"suggest 3 commit messages based on the following diff:\n\n{diff}\n\ncommit messages should:\n  - follow conventional commits,\n  - message format should be: <type>[scope]: <description>,\n\n\"examples:\",\n\" - 🐛 fix(authentication): add password regex pattern\",\n\" -✨ feat(storage): add new test cases\",\n",
    )
    # response = openai.ChatCompletion.create(
    #     model="text-davinci-003",
    #     messages=[{"role": "user", "content": f"suggest 3 commit messages based on the following diff:\n\n{diff}\n\ncommit messages should:\n  - follow conventional commits,\n  - message format should be: <type>[scope]: <description>,\n\n\"examples:\",\n\" - 🐛 fix(authentication): add password regex pattern\",\n\" -✨ feat(storage): add new test cases\",\n"}]
    # )

    return response

def main():
    diff = get_git_diff()
    if not diff:
        print("No git diff found. Are you in a git repository?")
        sys.exit(1)

    commit_messages = generate_commit_messages(diff)
    print("Suggested commit messages:")
    print(commit_messages)

if __name__ == "__main__":
    main()
