from api_wrappers.BinanceWrapper import BinanceWrapper

class BookWorm:
	"""Pulls historical and live financial price data from APIWrappers. """

	def historical_candles(self, api_wrapper, symbol: str, interval:str, start_time: str, end_time: str):
		return api_wrapper.historical_candles(symbol, interval, start_time, end_time)

	def last_candles(self, num, api_wrapper, symbol: str, interval: str):
		return api_wrapper.last_candles(num, symbol, interval)

	def run_for_user():
		"""Terminal access for user to download data from any api wrappers"""
		api_wrappers = [BinanceWrapper]
		
		while True:
			index = int(input("Select APIWrapper: 1. BinanceWrapper"))	
			api_wrapper =  api_wrappers[index]

			symbol = input("Choose symbol: ")
			start_time = input("Choose start_time: ")
			end_time = input("Choose end_time: ")
			interval = input("Choose interval: ")
			save_path = input("Choose save_path to save .csv into: ")

			df = api_wrapper.historical_candles(symbol, interval, start_time, end_time)

			# save to .cscv
			df.to_csv(save_path, index=False)


if __name__ == '__main__':
	run_for_user()