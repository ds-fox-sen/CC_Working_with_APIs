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

names, plot_dicts = [], []
for repo_dict in repo_dicts:
    names.append(repo_dict['name'])
#    stars.append(repo_dict['stargazers_count'])
    plot_dict = {
        'value': repo_dict['stargazers_count'],
        'label': str(repo_dict['description']),
        'xlink': repo_dict['html_url']
        }
    plot_dicts.append(plot_dict)


# Make a visualization.
my_style = LS('#333366', base_style=LCS)

# Refine the chart.
my_config = pygal.Config()
my_config.x_label_rotation = 45
my_config.show_legend = False
my_config.title_font_size = 16
my_config.label_font_size = 10
my_config.major_label_font_size = 14
my_config.truncate_label = 15
my_config.show_y_guides = False
my_config.width = 1000


chart = pygal.Bar(my_config, style=my_style)
chart.title = 'Most-Starred Python Projects on GitHub'
chart.x_labels = names

chart.add('', plot_dicts)


chart.render_to_file('python_repos.svg')
chart.render_to_png('python_repos.png')

# Text summaries.
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
print(type(repo_dict['description']))
