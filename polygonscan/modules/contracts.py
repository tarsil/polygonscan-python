from polygonscan.enums.actions_enum import ActionsEnum as actions
from polygonscan.enums.fields_enum import FieldsEnum as fields
from polygonscan.enums.modules_enum import ModulesEnum as modules


class Contracts:
    @staticmethod
    def get_contract_abi(address: str) -> str:
        url = (
            f"{fields.MODULE}"
            f"{modules.CONTRACT}"
            f"{fields.ACTION}"
            f"{actions.GET_ABI}"
            f"{fields.ADDRESS}"
            f"{address}"
        )
        return url

    @staticmethod
    def get_contract_source_code(address: str) -> str:
        url = (
            f"{fields.MODULE}"
            f"{modules.CONTRACT}"
            f"{fields.ACTION}"
            f"{actions.GET_SOURCE_CODE}"
            f"{fields.ADDRESS}"
            f"{address}"
        )
        return url
