from dash import Dash, html, dcc
import dash_bootstrap_components as dbc


def fnNavbar():
    return dbc.Nav([dbc.NavItem(html.H2('Stock Analysis'))],
                   className='navbar navbar-expand-lg navbar-dark bg-primary', justified='center',
                   style={'margin-bottom': '3px'})


def fnDropdown():
    lst = [{'label': 'TATASTEEL', 'value': 'TATASTEEL.ns'},
           {'label': 'TATAMOTORS', 'value': 'TATAMOTORS.ns'},
           {'label': 'TATA CONSULTANCY SERVICES LIMITED', 'value': 'TCS.ns'},
           {'label': 'WIPRO', 'value': 'WIPRO.ns'}, ]
    return dbc.Row(
        [dbc.Col(dbc.Label('Select Stock',style={'color':'black'}), width=1),
         dbc.Col(dcc.Dropdown(lst, value='TATASTEEL.ns', placeholder='SELECT STOCK', id='stock-name'),
                 width=3)
         ], style={'margin': '5px', 'padding': '3px'})


# 1d,5d,1mo,3mo,6mo,1y,2y,5y,10y,ytd,max
def fnPeriodsBtn():
    return html.Div([dbc.Button("1d", id='1d-p', outline=True, color="primary", className="me-1"),
                     dbc.Button("5d", id='5d-p', outline=True, color="primary", className="me-1"),
                     dbc.Button("1mo", id='1mo-p', outline=True, color="primary", className="me-1"),
                     dbc.Button("3mo", id='3mo-p', outline=True, color="primary", className="me-1"),
                     dbc.Button("6mo", id='6mo-p', outline=True, color="primary", className="me-1"),
                     dbc.Button("1y", id='1y-p', outline=True, color="primary", className="me-1"),
                     # dbc.Button("2y",id='1d', outline=True, color="primary", className="me-1"),
                     dbc.Button("5y", id='5y-p', outline=True, color="primary", className="me-1"),
                     dbc.Button("10y", id='10y-p', outline=True, color="primary", className="me-1"),
                     dbc.Button("ytd", id='ytd-p', outline=True, color="primary", className="me-1"),
                     dbc.Button("max", id='max-p', outline=True, color="primary", className="me-1"),
                     ], style={'margin': '5px', 'padding': '3px'})


# 1m,2m,5m,15m,30m,60m,90m,1h,1d,5d,1wk,1mo,3mo

def fnIntervalsBtn():
    return html.Div([dbc.Button("1m", id='1m-i', outline=True, color="primary", className="me-1"),
                     dbc.Button("2m", id='2m-i', outline=True, color="primary", className="me-1"),
                     dbc.Button("5m", id='5m-i', outline=True, color="primary", className="me-1"),
                     dbc.Button("15m", id='15m-i', outline=True, color="primary", className="me-1"),
                     dbc.Button("30m", id='30m-i', outline=True, color="primary", className="me-1"),
                     # dbc.Button("60m", outline=True, color="primary", className="me-1"),
                     # dbc.Button("90m", outline=True, color="primary", className="me-1"),
                     dbc.Button("1h", id='1h-i', outline=True, color="primary", className="me-1"),
                     dbc.Button("1d", id='1d-i', outline=True, color="primary", className="me-1"),
                     dbc.Button("5d", id='5d-i', outline=True, color="primary", className="me-1"),
                     # dbc.Button("1wk", outline=True, color="primary", className="me-1"),
                     dbc.Button("1mo", id='1mo-i', outline=True, color="primary", className="me-1"),
                     # dbc.Button("3mo", outline=True, color="primary", className="me-1"),
                     ], style={'margin': '5px', 'padding': '3px'})
