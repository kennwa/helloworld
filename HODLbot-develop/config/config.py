#!/usr/bin/python
# config.py - Configuaration File for HOLDbot

config = {
    'main_fiat': "USD",
    'main_cc': "BTC",
    'total_initial_investment_fiat': 1000.00,
    'swap_threshold_percentage': 0.1,
    'min_trading_values': {
        'bitcoin': 0.001,
        'ripple': 10,
        'ethereum': 0.01,
        'bitcoin-cash': 0.001,
        'cardano': 10,
        'litecoin': 0.1,
        'iota': 1,
        'nem': 10,
        'dash': 0.01,
        'stellar': 10
    },
    'debug': False
}
