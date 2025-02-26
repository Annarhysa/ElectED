import dash
import dash_core_components as dcc
import dash_html_components as html
import dash_bootstrap_components as dbc
import plotly.graph_objs as go
import pandas as pd
import plotly.express as px

# Load summaries from file
def load_summaries(file_path):
    with open(file_path, 'r') as f:
        summaries = f.read().split("\n\n")
    return summaries

summaries = load_summaries('summaries/summaries.txt')

# Load data into a DataFrame
df = pd.read_csv('data/data.csv')
data = pd.read_csv('data/all.csv')

# Create plots
bar_plot = px.bar(df, x='Party Abbreviation', y='Total')

hist_plot = px.histogram(df, x='Total')

top_5_parties = df.nlargest(5, 'Total')
top_5_bar_plot = px.bar(top_5_parties, x='Party Abbreviation', y='Total')

top_20_parties = df.nlargest(20, 'Total')
pie_chart = px.pie(top_20_parties, values='Total', names='Party Abbreviation', hole=0.2)


# Sort by Total Votes and select the top 20 candidates
top_candidates = data.nlargest(20, 'Total Votes')

# Data preparation for bar chart
candidates = top_candidates['Candidate'] + ' (' + top_candidates['Party'] + ')'
total_votes = top_candidates['Total Votes']

# Plotting (Plotly bar chart)
bar_chart = go.Figure(data=[go.Bar(x=total_votes, y=candidates, orientation='h')])

# Data preparation for vote distribution by party (using Plotly)
candidates = top_candidates['Candidate'] + ' (' + top_candidates['Party'] + ')'
percent_votes = top_candidates['% of Votes']

# Plotting (Plotly pie chart)
top_candidates_chart = go.Figure(data=[go.Pie(labels=candidates, values=percent_votes, hole=0.2)])

# Dash app setup
app = dash.Dash(__name__, external_stylesheets=[dbc.themes.BOOTSTRAP, '/assets/styles.css'])

# Layout of the app
app.layout = dbc.Container([
    dbc.Row([
        dbc.Col(html.H1("2024 Election Results (India) Dashboard"), className="mb-4 mt-4")
    ]),
    dbc.Row([
        dbc.Col(dbc.Card([
            dbc.CardHeader("Total Seats Won by Each Party"),
            dbc.CardBody([
                dbc.Row([
                    dbc.Col(dcc.Graph(id='bar-plot', figure=bar_plot), width=8),
                    dbc.Col(html.P(summaries[0], className="summary-text"), width=4)
                ])
            ])
        ]), width=12),
    ]),
    dbc.Row([
        dbc.Col(dbc.Card([
            dbc.CardHeader("Distribution of Total Seats Won"),
            dbc.CardBody([
                dbc.Row([
                    dbc.Col(html.P(summaries[1], className="summary-text"), width=4),
                    dbc.Col(dcc.Graph(id='hist-plot', figure=hist_plot), width=8)
                ])
            ])
        ]), width=12),
    ]),
    dbc.Row([
        dbc.Col(dbc.Card([
            dbc.CardHeader("Total Seats Won by Top 5 Parties"),
            dbc.CardBody([
                dbc.Row([
                    dbc.Col(dcc.Graph(id='top-5-bar-plot', figure=top_5_bar_plot), width=8),
                    dbc.Col(html.P(summaries[2], className="summary-text"), width=4)
                ])
            ])
        ]), width=12),
    ]),
    dbc.Row([
        dbc.Col(dbc.Card([
            dbc.CardHeader("Seats Distribution Among Top 20 Parties"),
            dbc.CardBody([
                dbc.Row([
                    dbc.Col(html.P(summaries[3], className="summary-text"), width=4),
                    dbc.Col(dcc.Graph(id='pie-chart', figure=pie_chart, config={"displayModeBar": False}), width=8)
                ])
            ])
        ]), width=12),
    ]),
    dbc.Row([
        dbc.Col(dbc.Card([
            dbc.CardHeader("Total Votes for Top 20 Candidates"),
            dbc.CardBody([
                dbc.Row([
                    dbc.Col(dcc.Graph(id='bar-chart', figure=bar_chart), width=8),
                    dbc.Col(html.P(summaries[4], className="summary-text"), width=4),
                ])
            ])
        ]), width=12),
    ]),
    dbc.Row([
        dbc.Col(dbc.Card([
            dbc.CardHeader("Vote Distribution Among Top 20 Candidates"),
            dbc.CardBody([
                dbc.Row([
                    dbc.Col(html.P(summaries[5], className="summary-text"), width=4),
                    dbc.Col(dcc.Graph(id='pie-chart', figure=top_candidates_chart, config={"displayModeBar": False}), width=8)
                ])
            ])
        ]), width=12),
    ]),
])

if __name__ == '__main__':
    app.run_server(debug=True)
