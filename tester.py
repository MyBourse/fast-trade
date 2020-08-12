from fast_trade import StrategyBase, IndicatorBase

class Strat1(StrategyBase):

    def __init__(self):
        self.name = "Bober"

        self.ind1 = IndicatorBase(df_name="ind1", operator=">", ind_name="")





    # def enter(self):
        



if __name__ == "__main__":
    
    strat = Strat1()

    print(strat.name)
    print(strat.ind1())

    