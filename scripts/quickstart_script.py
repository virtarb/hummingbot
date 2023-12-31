from hummingbot.strategy.script_strategy_base import ScriptStrategyBase


class QuickstartScript(ScriptStrategyBase):

    # It is recommended to first use a paper trade exchange connector
    # while coding your strategy, and then switch to a real one once you're happy with it.
    markets = {"binance_paper_trade": {"BTC-USDT"}}
    # Next, let's code the logic that will be executed every tick_size (default=1sec)

    def on_tick(self):
        price = self.connectors["binance_paper_trade"].get_mid_price("BTC-USDT")
        msg = f"Bitcoin price: ${price}"
        self.logger().info(msg)
        self.notify_hb_app_with_timestamp(msg)
