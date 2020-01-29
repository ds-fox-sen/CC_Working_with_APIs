"""Use requets to make an API call."""
import requests
import pygal
from pygal.style import LightColorizedStyle as LCS, LightenStyle as LS

# Make an API call and store the response.
url = 'https://api.github.com/search/repositories?q=language:python&sort=stars'
r = requests.get(url)
print("Status code:", r.status_code)

# Store API in a variable.
response_dict = r.json()

# Print some basic info on the response.
print("JSON keys:")
for key in response_dict.keys():
    print("-", key)

print("Total repos:", response_dict['total_count'])

# Explore info about repos (explode the items section).
repo_dicts = response_dict['items']

names, stars = [], []
for repo_dict in repo_dicts:
    names.append(repo_dict['name'])
    stars.append(repo_dict['stargazers_count'])

# Make visualization.
my_style = LS('#333366', base_style=LCS)
chart = pygal.Bar(style=my_style, x_label_rotation=45, show_legend=False)
chart.title = 'Most-Starred Python Projects on GitHub'
chart.x_labels = names

chart.add('', stars)
chart.render_to_file('python_repos.svg')
chart.render_to_png('python_repos.png')
print("Repos returned:", len(repo_dicts))

# Examine the first repo.
repo_dict = repo_dicts[0]
print("\nRepo Keys:", len(repo_dict))

for key in sorted(repo_dict.keys()):
    print("-", key)

# Details about the dataset.

for repo_dict in repo_dicts:
    print("\nSelected info about repos:")
    print("Name:", repo_dict['name'])
    print("Owner:", repo_dict['owner']['login'])
    print("Stars:", repo_dict['stargazers_count'])
    print("Repository:", repo_dict['html_url'])
    print("Created:", repo_dict['created_at'])
    print("Updated:", repo_dict['updated_at'])
    print("\nDescription:\n", repo_dict['description'])
