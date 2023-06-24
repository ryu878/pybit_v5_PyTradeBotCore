# Ryuryu's PyTradeBotCore for Bybit V5
# -------------------------------------------
# (C) 2023 Ryan Hayabusa 
# Github: https://github.com/ryu878 
# Discord: ryuryu#4087
# Mail: ev4AR2xihu3xXcdbYy5djGpfe01@gmail.com
# Web: https://aadresearch.xyz
# Discord: ryuryu#4087
# -------------------------------------------


class AccountBalance:
    def __init__(self, session, acc_type, coin):
        self.session = session
        self.acc_type = acc_type
        self.coin = coin
        self.total_equity = 0.0
        self.equity = 0.0
        self.wallet_balance = 0.0
        self.unrealised_pnl = 0.0
        self.cumRealisedPnl = 0.0
        self.totalPositionIM = 0.0
        self.totalPositionMM = 0.0


    def fetch_balance(self):
        try:
            balance = self.session.get_wallet_balance(accountType=self.acc_type, coin=self.coin)
            self.account_type = str(balance['result']['list'][0]['accountType'])
            self.total_equity = float(balance['result']['list'][0]['totalEquity'])
            self.equity = float(balance['result']['list'][0]['coin'][0]['equity'])
            self.wallet_balance = float(balance['result']['list'][0]['coin'][0]['walletBalance'])
            self.unrealised_pnl = float(balance['result']['list'][0]['coin'][0]['unrealisedPnl'])
            self.cumRealisedPnl = float(balance['result']['list'][0]['coin'][0]['cumRealisedPnl'])
            self.totalPositionIM = float(balance['result']['list'][0]['coin'][0]['totalPositionIM'])
            self.totalPositionMM = float(balance['result']['list'][0]['coin'][0]['totalPositionMM'])
        except (KeyError, TypeError, ValueError) as e:
            print(f'Error occurred while fetching balance: {e}')


class Position:
    def __init__(self, session, category, asset):
        self.session = session
        self.category = category
        self.asset = asset
        self.symbol = ''
        self.leverage = ''
        self.avgPrice = ''
        self.liqPrice = ''
        self.riskLimitValue = ''
        self.takeProfit = ''        
        self.positionValue = 0.0
        self.tpslMode = ''
        self.riskId = ''
        self.trailingStop = ''
        self.unrealisedPnl = 0.0
        self.markPrice = ''
        self.adlRankIndicator = ''
        self.cumRealisedPnl = ''
        self.positionMM = ''
        self.createdTime = ''
        self.positionIdx = ''
        self.positionIM = ''
        self.updatedTime = ''
        self.side = ''
        self.bustPrice = ''
        self.positionBalance = ''
        self.size = 0.0
        self.positionStatus = ''
        self.stopLoss = ''
        self.tradeMode = ''


    def fetch_position(self):
        try:
            positions = self.session.get_positions(category=self.category, symbol=self.asset)
            position = positions['result']['list'][0]
            self.symbol = position['symbol']
            self.leverage = position['leverage']
            self.avgPrice = position['avgPrice']
            self.liqPrice = position['liqPrice']
            self.riskLimitValue = position['riskLimitValue']
            self.takeProfit = position['takeProfit']
            self.positionValue = position['positionValue']
            self.tpslMode = position['tpslMode']
            self.riskId = position['riskId']
            self.trailingStop = position['trailingStop']
            self.unrealisedPnl = position['unrealisedPnl']
            self.markPrice = position['markPrice']
            self.adlRankIndicator = position['adlRankIndicator']
            self.cumRealisedPnl = position['cumRealisedPnl']
            self.positionMM = position['positionMM']
            self.createdTime = position['createdTime']
            self.positionIdx = position['positionIdx']
            self.positionIM = position['positionIM']
            self.updatedTime = position['updatedTime']
            self.side = position['side']
            self.bustPrice = position['bustPrice']
            self.positionBalance = position['positionBalance']
            self.size = position['size']
            self.positionStatus = position['positionStatus']
            self.stopLoss = position['stopLoss']
            self.tradeMode = position['tradeMode']
        except (KeyError, TypeError, ValueError) as e:
            print(f'Error occurred while fetching position: {e}')


class OrderManager:

    def __init__(self, session):
        self.session = session


    def get_entry_order_ids(self, category, asset, open_only=0, limit=10):
        get_entry_orders = self.session.get_open_orders(
            category=category,
            symbol=asset,
            openOnly=open_only,
            limit=limit
        )

        order_ids = []
        for order in get_entry_orders['result']['list']:
            order_ids.append(order['orderId'])

        return order_ids