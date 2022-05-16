import dash
import dash_html_components as html

from balance.balances import Balances


app = dash.Dash(__name__)

balances = Balances(['binance', 'gateio', 'kucoin'])
await balances.get_wallets()
app.layout = html.Div([
    html.H1('Hello motherfucker')
])

if __name__ == '__main__':
    app.run_server(debug=True)