from baseline.utils import jsonParser, writeTrainInfo
from baseline.utils import setup_logger
from datetime import datetime, timedelta

import logging
import os


_path_ = './cfg/demo_bi.json'

_parser_ = jsonParser(_path_)
_data_ = _parser_.loadParser()
_key_ = list(_data_.keys())


ACCESS_KEY = _data_['ACCESS_KEY']
SECRETE_KEY = _data_['SECRETE_KEY']
MARKET = _data_['MARKET']
LOG_MODE = _data_['LOG_MODE']

MAX_POSITION = _data_['MAX_POSITION'] if 'MAX_POSITION' in _key_ else 10
BACKTEST = _data_['BACKTEST'] if 'BACKTEST' in _key_ else False

if BACKTEST:
    STARTDAY = '2021-01-02 00:00:00'

    TIMEINTERVAL = 2


URL = "https://api.upbit.com"


_current_time_ = datetime.now()
_logger_ = logging.getLogger("Crypto_RL")
_logger_.setLevel(logging.ERROR)


_str_time_ = _current_time_.strftime("%m_%d_%Y_%H_%M_%S")
_log_path_ = os.path.join(
    './log', _str_time_
)
if not os.path.isdir(_log_path_):
    os.mkdir(_log_path_)

_indicator_log_path_ = os.path.join(
    _log_path_, 'indicator.log'
)


# Logging !!
if LOG_MODE:
    
    INDICT_LOGGER = setup_logger('indictator', _indicator_log_path_)
    _ask_log_path_ = os.path.join(
        _log_path_, 'ask.log'
    )
    _bid_log_path_ = os.path.join(
        _log_path_, 'bid.log'
    )
    _info_log_path_ = os.path.join(
        _log_path_, 'info.log'
    )

    ASK_LOGGER = setup_logger("ask", _ask_log_path_)
    BID_LOGGER = setup_logger("bid", _bid_log_path_)
    INFO_LOGGER = setup_logger("info", _info_log_path_)

    _ask_header_ = 'time,uuid,volume,market'
    _bid_header_ = 'time,uuid,price,market'
    _info_ = writeTrainInfo(_data_)

    INFO_LOGGER.info(_info_)
    ASK_LOGGER.info(_ask_header_)
    BID_LOGGER.info(_bid_header_)

# ------------------------------------------------
