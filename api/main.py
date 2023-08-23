import requests

# fjpiedade

response = requests.get("https://gitlab.com/api/v4/users/fjpiedade/projects")
# print(response.text)  # string datatype is return
# print(response.json())  # return projects as list datatype
my_projects = response.json()

for project in my_projects:
    print(f"Project Name: {project['name']} and Url: {project['web_url']}")
