from okx.MarketData import MarketAPI  # 导入行情数据

if __name__ == '__main__':
  # 行情数据无需添加key、secret与passphrase  flag = '0' 实盘 flag = '1' 模拟盘
  market = MarketAPI(flag = '0' )
  # 获取现货交易BTC-USDT的行情信息
  result = market.get_ticker(instId='BTC-USDT')
  print(result)