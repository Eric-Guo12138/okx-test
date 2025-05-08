from okx.Account import AccountAPI
from okx.Funding import FundingAPI
from okx.Trade import TradeAPI
from okx.MarketData import MarketAPI

# 初始化API
api_key = ''
api_secret_key = ''
passphrase = ''
flag = '1'  # 1: 模拟盘，0: 实盘

account_api = AccountAPI(api_key, api_secret_key, passphrase, flag=flag)
funding_api = FundingAPI(api_key, api_secret_key, passphrase, flag=flag)
trade_api = TradeAPI(api_key, api_secret_key, passphrase, flag=flag)
market_api = MarketAPI(api_key, api_secret_key, passphrase, flag=flag)

# 1. 查询余额
# 资金账户余额
def get_balance():
    ccy = 'USDT'  # 若为空，则查询所有币种的余额
    result = funding_api.get_balances(ccy)
    print("查询资金余额结果:", result)
# 交易账户余额
def get_account_balance():
    ccy = 'USDT'  # 若为空，则查询所有币种的余额
    result = account_api.get_account_balance(ccy)
    print("查询交易余额结果:", result)

# 2. 提现
def withdraw():
    ccy = 'USDT'  # 提现币种
    amt = '0.3'  # 提现数量
    dest = '4'  # 提现地址类型，4: 链上地址
    toAddr = '0xd44284114de4b802a7432991df8376e7eca9d842'  # 提现地址(验证)
    chain = 'USDT-Arbitrum One'  # 链名称
    result = funding_api.withdrawal(ccy, amt, dest, toAddr, chain)
    print("提现结果:", result)

# 3. 下现货单
def place_order():
    instId = 'BTC-USDT'  # 交易对
    tdMode = 'cash'  # 交易模式，cash: 现货
    side = 'buy'  # 交易方向，buy: 买入，sell: 卖出
    ordType = 'limit'  # 订单类型，limit: 限价单
    px = '2'  # 价格
    sz = '0.01'  # 数量
    result = trade_api.place_order(instId=instId, tdMode=tdMode, side=side, ordType=ordType, px=px, sz=sz)
    print("下现货单结果:", result)

# 4. 撤单
def cancel_order():
    instId = 'BTC-USDT'  # 交易对
    ordId = '2489537280773857280'   # 订单号
    result = trade_api.cancel_order(instId, ordId)
    print("撤单结果:", result)

# 5. 查询深度
def get_order_book():
    instId = 'BTC-USDT'  # 交易对
    sz = '10'  # 深度数量
    result = market_api.get_orderbook(instId, sz)
    print("查询深度结果:", result)
    # asks卖方深度，bids买方深度，ts时间戳
    # 示例输出["411.8","10", "0","4"] 411.8为深度价格，10为此价格的数量 （合约交易为张数，现货/币币杠杆为交易币的数量），0该字段已弃用(始终为0)，4为此价格的订单数量

# 调用示例
# get_balance()
# get_account_balance()
# withdraw()
# place_order()
# cancel_order()
# get_order_book()