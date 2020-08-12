class StrategyBase:
    """
    strategy base for more complex logic
    """
    def __init__(self, **kwargs):
        self.name = kwargs.get('name', 'generated')
        self.chart_period = kwargs.get('chart_period', '1m')
        self.start = kwargs.get('start')
        self.stop = kwargs.get('stop')
        self.exit_on_end = kwargs.get('start')
    
    def validate(self):
        if not self.enter:
            raise "Missing enter logic"
        
        if not self.exit:
            raise "Missing exit logic"

        if not self.indicators:
            raise "Missing indicators"

class LogizBase:
    def __init__(self, df_name=None, operator=None, indicator_name=None):
        self.df_name = df_name
        self.operator = operator
        self.indicator_name = indicator_name
    
    def validate(self):
        if not self.df_name:
            raise "Missing data name"

        if not self.operator:
            raise "Missing operator"

        if not self.indicator_name:
            raise "Missing indicator name"

class IndicatorBase:
    def __init__(self, **kwargs):
        self.name = kwargs.get("name")
        self.func = kwargs.get("func")
        self.args = kwargs.get("args")
        self.df = kwargs.get("df")