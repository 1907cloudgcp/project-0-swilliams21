class transaction_exception(Exception):
    pass

class negative_transaction_exception(transaction_exception):
    pass

class not_enough_money_exception(transaction_exception):
    pass