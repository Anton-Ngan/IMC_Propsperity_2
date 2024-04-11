from datamodel import OrderDepth, UserId, TradingState, Order
from typing import List
import string
import jsonpickle
import statistics

class Trader:
    
    def run(self, state: TradingState):
        # Only method required. It takes all buy and sell orders for all 
        # symbols as an input, and outputs a list of orders to be sent
        print(f"traderData: {state.traderData}")
        print(f"Observations: {state.observations}")

        # Decode values of interest from previous states
        # if state.traderData != "":
        #     thawed = jsonpickle.decode(state.traderData)
        #     storage = Storage(
        #         trailing_median = thawed.median_lst
        #     )

        # Orders to be placed on exchange matching engine
        result = {}

        # AMETHYST Trading Strategy
        order_depth = state.order_depths["AMETHYSTS"]
        myorders: List[Order] = []
        if len(order_depth.sell_orders) != 0:
            best_ask, best_ask_amount = sorted(list(order_depth.sell_orders.items()))[0]
            if int(best_ask) <= 9998.5:
                print(f"BUY {-best_ask_amount}x {best_ask}")
                myorders.append(Order("AMETHYSTS", best_ask, best_ask_amount))
        if len(order_depth.buy_orders) != 0:
            best_bid, best_bid_amount = sorted(list(order_depth.buy_orders.items()))[-1]   
            if int(best_bid) > 10000:
                print(f"SELL {best_bid_amount}x {best_bid}")
                myorders.append(Order("AMETHYSTS", best_bid, -best_bid_amount))
        result["AMETHYSTS"] = myorders

        # for product in state.order_depths:
        #     order_depth: OrderDepth = state.order_depths[product]         
        #     myorders: List[Order] = []

        #     # Value to calculate whether we should buy or sell a product
        #     acceptable_price = statistics.median(list(order_depth.sell_orders.items())[0][0]) if state.traderData == "" else storage.median_lst[-1];    
        #     print(f"Acceptable price: {acceptable_price}")
        #     print(f"Buy Order depth: {len(order_depth.buy_orders)} Sell order depth: {len(order_depth.sell_orders)}")
    
            # if len(order_depth.sell_orders) != 0:
            #     best_ask, best_ask_amount = sorted(list(order_depth.sell_orders.items()))[0]
            #     if int(best_ask) < acceptable_price:
            #         print(f"BUY {-best_ask_amount}x {best_ask}")
            #         myorders.append(Order(product, best_ask, best_ask_amount))
    
        #     if len(order_depth.buy_orders) != 0:
        #         best_bid, best_bid_amount = sorted(list(order_depth.buy_orders.items()))[-1]   
        #         if int(best_bid) > acceptable_price:
        #             print(f"SELL {best_bid_amount}x {best_bid}")
        #             myorders.append(Order(product, best_bid, -best_bid_amount))
            
        #     result[product] = myorders
        
        # Add the median to the median trailing list
        # sell_order_lst = list(order_depth.sell_orders.keys())
        # buy_order_lst = list(order_depth.buy_orders.keys())
        # order_lst = sell_order_lst.extend(buy_order_lst)
        # if state.traderData != "":
        #     complete_lst = order_lst.extend(storage.median_lst)
        # storage.median_lst.extend(statistics.median_high(complete_lst))
    
        # String value holding Trader state data required. 
        # It will be delivered as TradingState.traderData on next execution.
        # traderData = jsonpickle.encode(storage)
        
        traderData = "SAMPLE"

        conversions = None
        return result, conversions, traderData
    


class Storage:
    """ Store values that we are interested in here. """

    def __init__(self, trailing_median: List[int]) -> None:
        self.median_lst = trailing_median
        self.ame_price = 10000
    
    def get_median(self) -> int:
        return statistics.median(self.median_lst)