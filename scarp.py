from plotly.graph_objs import bar
from plotly import offline



data = [
    {
        "type":"bar",
        "x": repo_names,
        "y": stars,
        "marker": {
            "color":"rgb(60,100,150)",
            "line":{"width":1.5, "color":"rgb(25,25,25)"},
        },
        "opacity":0.6,
    }
]

my_layout = {
    "title": "Most-Starred Python Projects from GIThub",
    "xaxis":{"title": "Repository"},
    "yaxis":{"title": "Stars"}
}

fig ={"data":data, "layout":my_layout}

offline.plot(fig, filename="pyhton_repos.html")





