from polygonscan.enums.actions_enum import ActionsEnum as actions
from polygonscan.enums.fields_enum import FieldsEnum as fields
from polygonscan.enums.modules_enum import ModulesEnum as modules


class Stats:
    @staticmethod
    def get_total_matic_supply() -> str:
        url = (
            f"{fields.MODULE}"
            f"{modules.STATS}"
            f"{fields.ACTION}"
            f"{actions.ETH_SUPPLY}"
        )
        return url

    @staticmethod
    def get_matic_last_price() -> str:
        url = (
            f"{fields.MODULE}"
            f"{modules.STATS}"
            f"{fields.ACTION}"
            f"{actions.ETH_PRICE}"
        )
        return url
