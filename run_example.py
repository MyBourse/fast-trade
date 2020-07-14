from fast_trade import run_backtest, dataframe_from_path, build_data_frame
import pandas as pd
import json
import os
import datetime

if __name__ == "__main__":
    csv_path = "/Users/jedmeier/BTCUSDT.csv"
    # ohlcv_path = "/Users/jedmeier/2017_standard/BTCUSDT.csv"
    # print(csv_path)
    # ~/binance_2020_04_16/BTCUSDT.csv
    with open("./example_strat_2.json", "r") as json_file:
        strategy = json.load(json_file)


    strategy["chart_period"] = "4m"
    # strategy["start"] = "2018-01-01 00:00:00"
    # strategy["stop"] = "2018-05-04 00:00:00"
    start_time = (datetime.datetime.utcnow() - datetime.timedelta(days=7)).strftime("%Y-%m-%d %H:%M:%S")
    # stop_time.strftime("%Y-%m-%d %H:%M:%S")
    strategy['start'] = start_time

    df = dataframe_from_path(csv_path)

    df = build_data_frame(df, strategy)

    res = run_backtest(df, strategy)

    print(json.dumps(res["summary"], indent=2))
