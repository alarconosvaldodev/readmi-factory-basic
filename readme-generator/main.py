from prompts import ask_questions
from generator import generate_readme
from utils.file_utils import write_file


def main():

    print("README Generator\n")

    data = ask_questions()

    readme_content = generate_readme(data)

    write_file("README.md", readme_content)

    print("\nREADME.md generated successfully!")


if __name__ == "__main__":
    main()