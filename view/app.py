from dash import Dash, dcc, html, Input, Output
from threading import Thread
import plotly.express as px
import asyncio

from balance.balances import Balances


balances = Balances(['binance', 'gateio', 'kucoin'])
df = asyncio.run(balances.get_wallets())
app = Dash(__name__)

app.layout = html.Div([
    html.H4('Crypto stuff'),
    dcc.Dropdown(id='exchange_dropdown',
                value='Binance',
                options=[{'label': exchange, 'value': exchange} for exchange in ['Binance', 'Kucoin', 'GateIO']]),
    dcc.Graph(id='crypto-chart')
])

@app.callback(
    Output('crypto-chart', 'figure'),
    Input('exchange_dropdown', 'value')
)
def display_chart(exchange):
    df=df[df['exchange']==exchange]
    fig = px.line(df, x='timestamp', y='value')
    return fig

if __name__ == '__main__':
    app.run_server(debug=True)