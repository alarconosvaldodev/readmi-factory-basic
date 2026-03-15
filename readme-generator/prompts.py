def ask_questions():
    data = {}

    data["project_name"] = input("Project name: ")
    data["description"] = input("Project description: ")
    data["installation"] = input("Installation command: ")
    data["usage"] = input("Usage example: ")
    data["language"] = input("Language for code example: ")
    data["author"] = input("Author: ")
    data["license"] = input("License: ")

    return data