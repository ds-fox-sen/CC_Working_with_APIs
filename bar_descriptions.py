import pygal
from pygal.style import LightColorizedStyle as LCS,LightenStyle as LS

my_style = LS('#333366', base_style=LCS)
chart = pygal.Bar(style=my_style, x_label_rotation=45, show_legend=False)

chart.title = 'Python Projects'
chart.x_labels = ['httpie', 'django', 'flask']

plot_dicts = [
    {'value': 100, 'label': 'httpe description'},
    {'value': 80, 'label': 'django is cool'},
    {'value': 60, 'label': 'I don\'t know what flask is'}
    ]

chart.add('', plot_dicts)
chart.render_to_file('bar_descriptions.svg')
