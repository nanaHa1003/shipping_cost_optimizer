import math

class Item:
    def __init__(self, name, weight, tracking_no=""):
        self.name = name
        self.weight = float(weight)
        self.tracking_no = tracking_no

class ShippingOptimizer:
    def __init__(self, first_kg_cost=137, next_kg_cost=112, surcharge_threshold=8, surcharge_fee=5, max_weight=20):
        self.FIRST_KG = first_kg_cost
        self.NEXT_KG = next_kg_cost
        self.SURCHARGE_LIMIT = surcharge_threshold
        self.SURCHARGE_FEE = surcharge_fee
        self.MAX_WEIGHT = max_weight

    def calculate_detailed_cost(self, items):
        """Returns (total, base_cost, surcharge)"""
        if not items: return 0, 0, 0
        
        total_weight = sum(item.weight for item in items)
        billed_weight = math.ceil(total_weight)
        
        # Base weight cost
        base_cost = self.FIRST_KG
        if billed_weight > 1:
            base_cost += (billed_weight - 1) * self.NEXT_KG
            
        # Surcharge cost
        surcharge = 0
        if len(items) > self.SURCHARGE_LIMIT:
            surcharge = (len(items) - self.SURCHARGE_LIMIT) * self.SURCHARGE_FEE
            
        return base_cost + surcharge, base_cost, surcharge

    def solve(self, items):
        n = len(items)
        dp = [float("inf")] * (n + 1)
        dp[0] = 0
        split_at = [0] * (n + 1)

        for i in range(1, n + 1):
            for j in range(i):
                current_parcel = items[j:i]
                cost, _, _ = self.calculate_detailed_cost(current_parcel)
                if dp[j] + cost < dp[i]:
                    dp[i] = dp[j] + cost
                    split_at[i] = j

        parcels = []
        curr = n
        while curr > 0:
            prev = split_at[curr]
            parcels.append(items[prev:curr])
            curr = prev
            
        all_in_one_cost, _, _ = self.calculate_detailed_cost(items)
        return dp[n], parcels[::-1], all_in_one_cost
