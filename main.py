import yfinance as yf
from dash import Dash, html, dcc, callback_context
import dash_bootstrap_components as dbc
import components as cmp
import plotly.graph_objects as go
import pandas as pd
import pandas_ta as ta
from dash.dependencies import Input, Output


# data = yf.download("TATAMOTORS.ns", interval="1m", period='1d')
# data.reset_index(inplace=True)

def fnLineChart(df, sma,ema):
    fig = go.Figure()
    try:
        fig.add_trace(go.Scatter(x=df['Datetime'], y=df['Close'],
                                 mode='lines',
                                 name='Close'))
    except Exception:
        fig.add_trace(go.Scatter(x=df['Date'], y=df['Close'],
                                 mode='lines',
                                 name='Close'))
    fig.add_trace(go.Scatter(x=df['Datetime'], y=df['High'],
                             mode='lines',
                             name='High')),
    fig.add_trace(go.Scatter(x=df['Datetime'], y=df['Low'],
                             mode='lines',
                             name='Low')),
    fig.add_trace(go.Scatter(x=df['Datetime'], y=df['Open'],
                             mode='lines',
                             name='Open')),
    fig.add_trace(go.Scatter(x=df['Datetime'], y=sma,
                             mode='lines',
                             name='SMA10'))
    fig.add_trace(go.Scatter(x=df['Datetime'], y=ema,
                             mode='lines',
                             name='ema10_ohlc4'))

    fig.update_layout(
        # title=title,
        yaxis_title='Price', xaxis_title='DateTime', xaxis_rangeslider_visible=False)

    return fig


def fnCandleChart(df, title):
    try:
        fig = go.Figure(data=[go.Candlestick(x=df['Datetime'],
                                             open=df['Open'], high=df['High'],
                                             low=df['Low'], close=df['Close'])
                              ])

        fig.update_layout(
            title=title,
            yaxis_title='Price', xaxis_title='DateTime', xaxis_rangeslider_visible=False)

        return fig
    except KeyError:
        try:
            fig = go.Figure(data=[go.Candlestick(x=df['Date'],
                                                 open=df['Open'], high=df['High'],
                                                 low=df['Low'], close=df['Close'])
                                  ])

            fig.update_layout(title=title,
                              yaxis_title='Price', xaxis_title='DateTime', xaxis_rangeslider_visible=False)

            return fig
        except KeyError:
            fig = go.Figure(data=[go.Candlestick(x=df['index'],
                                                 open=df['Open'], high=df['High'],
                                                 low=df['Low'], close=df['Close'])
                                  ])

            fig.update_layout(title=title,
                              yaxis_title='Price', xaxis_title='DateTime', xaxis_rangeslider_visible=False)

            return fig


peroiod, interval = '1d', '1m'
app = Dash(external_stylesheets=[dbc.themes.CYBORG])
server = app.server

app.layout = dbc.Row(
    [cmp.fnNavbar(), dbc.Row(cmp.fnDropdown(), style={'margin': '5px'}),
     html.Div(style={'border-bottom': '2px solid black'}),
     dbc.Row([dbc.Col(html.Div('Select Interval', style={'color': 'black'})),
              dbc.Col(html.Div('Select Period', style={'color': 'black'}))],
             style={'margin': '5px', 'padding': '3px'}),
     dbc.Row([dbc.Col(cmp.fnIntervalsBtn()), dbc.Col(cmp.fnPeriodsBtn())]),
     html.Div(style={'border-bottom': '2px solid black'}),
     dbc.Row(dbc.Col(dcc.Graph(id='ohlc-graph'))), dbc.Row(dbc.Col(dcc.Graph(id='line-graph'))), dcc.Interval(
        id='interval-component',
        interval=1 * 61000,  # in milliseconds
        n_intervals=0
    )], className='mx-3 my-3',
    style={'background': 'white', 'border-radius': '15px'})


@app.callback(
    # Output(component_id='ohlc-graph', component_property='figure'),
    [Output(component_id='ohlc-graph', component_property='figure'),
     Output(component_id='line-graph', component_property='figure')],
    Input(component_id='stock-name', component_property='value'),
    Input(component_id='1d-p', component_property='n_clicks'),
    Input(component_id='5d-p', component_property='n_clicks'),
    Input(component_id='1mo-p', component_property='n_clicks'),
    Input(component_id='3mo-p', component_property='n_clicks'),
    Input(component_id='6mo-p', component_property='n_clicks'),
    Input(component_id='1y-p', component_property='n_clicks'),
    Input(component_id='5y-p', component_property='n_clicks'),
    Input(component_id='10y-p', component_property='n_clicks'),
    Input(component_id='ytd-p', component_property='n_clicks'),
    Input(component_id='max-p', component_property='n_clicks'),

    Input(component_id='1m-i', component_property='n_clicks'),
    Input(component_id='5m-i', component_property='n_clicks'),
    Input(component_id='15m-i', component_property='n_clicks'),
    Input(component_id='30m-i', component_property='n_clicks'),
    Input(component_id='1h-i', component_property='n_clicks'),
    Input(component_id='1d-i', component_property='n_clicks'),
    Input(component_id='5d-i', component_property='n_clicks'),
    Input(component_id='1mo-i', component_property='n_clicks'),
    Input('interval-component', 'n_intervals')
)
def fnHandleCallback(s_name, *args):
    global peroiod, interval
    trigger = callback_context.triggered[0]
    tr = trigger["prop_id"].split(".")[0]

    per_lst = ['1d-p', '5d-p', '1mo-p', '3mo-p', '6mo-p', '1y-p', '2y-p', '5y-p', '10y-p', 'ytd-p', 'max-p']
    int_lst = ['1m-i', '2m-i', '5m-i', '15m-i', '30m-i', '60m-i', '90m-i', '1h-i', '1d-i', '5d-i', '1wk-i', '1mo-i',
               '3mo-i']

    if 'interval-component' in tr:
        df = pd.DataFrame()
        df = df.ta.ticker(s_name, period="1d", interval='1m')
        df.reset_index(inplace=True)
        stock_name = s_name.split('.')[0]
        title = f' {stock_name} Details , Period = 1d and Interval = 1m'
        fig1 = fnCandleChart(df, title)
        df = pd.DataFrame()
        df = df.ta.ticker(s_name, peroiod='1y', interval='1d')
        df.reset_index(inplace=True)
        df.rename(columns={'Date': 'Datetime'}, inplace=True)
        sma10 = ta.sma(df["Close"], length=10)
        ema10_ohlc4 = df.ta.ema(close=df.ta.ohlc4(), length=10, suffix="OHLC4")
        fig2 = fnLineChart(df, sma10.fillna(0), ema10_ohlc4)
        return fig1, fig2

    elif tr in per_lst:
        peroiod = tr.split('-')[0]
        df = yf.download(s_name, period=peroiod, interval=interval)
        df.reset_index(inplace=True)
        s_name = s_name.split('.')[0]
        title = f' {s_name} , Period = {peroiod} , Interval = {interval}'
        fig1 = fnCandleChart(df, title)
        df = pd.DataFrame()
        df = df.ta.ticker(s_name, peroiod='1y', interval='1d')
        df.reset_index(inplace=True)
        df.rename(columns={'Date': 'Datetime'}, inplace=True)
        sma10 = ta.sma(df["Close"], length=10)
        ema10_ohlc4 = df.ta.ema(close=df.ta.ohlc4(), length=10, suffix="OHLC4")
        fig2 = fnLineChart(df, sma10.fillna(0), ema10_ohlc4)
        return fig1, fig2
    elif tr in int_lst:
        interval = tr.split('-')[0]
        df = yf.download(s_name, period=tr, interval=interval)
        df.reset_index(inplace=True)
        s_name = s_name.split('.')[0]
        title = f' {s_name} Details , Period = {peroiod} and Interval = {interval}'
        fig1 = fnCandleChart(df, title)
        df = pd.DataFrame()
        df = df.ta.ticker(s_name, peroiod='1y', interval='1d')
        df.reset_index(inplace=True)
        df.rename(columns={'Date': 'Datetime'}, inplace=True)
        sma10 = ta.sma(df["Close"], length=10)
        ema10_ohlc4 = df.ta.ema(close=df.ta.ohlc4(), length=10, suffix="OHLC4")
        fig2 = fnLineChart(df, sma10.fillna(0), ema10_ohlc4)
        return fig1, fig2
    else:
        df = pd.DataFrame()
        df = df.ta.ticker(s_name, period=peroiod, interval=interval)
        df.reset_index(inplace=True)
        stock_name = s_name.split('.')[0]
        title = f' {stock_name} Details , Period = {peroiod} and Interval = {interval}'
        fig1 = fnCandleChart(df, title)
        df = pd.DataFrame()
        df = df.ta.ticker(s_name, peroiod='1y', interval='1d')
        df.reset_index(inplace=True)
        df.rename(columns={'Date': 'Datetime'}, inplace=True)
        sma10 = ta.sma(df["Close"], length=10)
        ema10_ohlc4 = df.ta.ema(close=df.ta.ohlc4(), length=10, suffix="OHLC4")
        fig2 = fnLineChart(df, sma10.fillna(0),ema10_ohlc4)
        return fig1, fig2


if __name__ == "__main__":
    app.run_server(debug=True)
