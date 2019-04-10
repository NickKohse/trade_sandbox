class FundsError(Exception):
    def __init__(self, cost, bal):
        super().__init__(f"Insufficient funds. Transaction value: {cost} Current balance: {bal}")

class AssetNotOwnedError(Exception):
    def __init__(self, name):
        super().__init__(f"Cannot sell {name} from this account, as it does not currently contain that asset")

class InsufficientHoldingsError(Exception):
    def __init__(self, name, have, want):
        super().__init__(f"Attempt to sell {want} shares of {name} failed becuase this account only has {have} shares available")