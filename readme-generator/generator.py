from utils.file_utils import read_template


def generate_readme(data):

    template = read_template("templates/basic.md")

    readme = template.format(
        project_name=data["project_name"],
        description=data["description"],
        installation=data["installation"],
        usage=data["usage"],
        language=data["language"],
        author=data["author"],
        license=data["license"]
    )

    return readme