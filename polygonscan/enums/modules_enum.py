from dataclasses import dataclass


@dataclass(frozen=True)
class ModulesEnum:
    ACCOUNT: str = "account"
    BLOCK: str = "block"
    CONTRACT: str = "contract"
    GASTRACKER: str = "gastracker"
    PROXY: str = "proxy"
    LOGS: str = "logs"
    STATS: str = "stats"
    TOKEN: str = "token"
    TRANSACTION: str = "transaction"

