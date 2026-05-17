from utils.http_wrapper import HttpWrapper

class MarketWrapper(object):
    BASE_URL = 'https://api.coingecko.com/api/v3'

    def __init__(self, api_key=''):
        self.api_key = api_key

    def _headers(self):
        # CoinGecko Demo API key. Per-key quota (~30/min), bypasses IP rate limit.
        return {'x-cg-demo-api-key': self.api_key} if self.api_key else None

    async def get_price_usd(self, coin):
        r = await HttpWrapper.get(f'{self.BASE_URL}/coins/{coin}', headers=self._headers())
        try:
            return r['market_data']['current_price']['usd']
        except Exception as e:
            print(f'get_price_usd: {str(e)}')
            return 0

    async def get_price_history(self, coin, currency):
        r = await HttpWrapper.get(
            f'{self.BASE_URL}/coins/{coin}/market_chart?vs_currency={currency}&days=max&interval=daily',
            headers=self._headers(),
        )
        try:
            return r['prices']
        except Exception as e:
            print(f'get_price_history: {str(e)}')
            return []