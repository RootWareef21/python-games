from typing import List
def calculateSacrificeProfit(buyPrices: List[float], sellPrices: List[float]) -> float:
       total = sum(sellPrices) - sum(buyPrices)
       return total
