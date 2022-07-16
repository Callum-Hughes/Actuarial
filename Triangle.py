import pandas as pd
import numpy as np

class Triangle:
    def __init__(self, data):
        self.data = data

    def getData(self):
        return self.data

    def triangle(self):
        self.data['development_period'] = 12*(self.data['development_year'] - self.data['origin_year']) + 12
        self.data['development_period'].apply(str)
        triangle = self.data.pivot(index = 'origin_year', columns = 'development_period', values = 'values')
        return triangle

    def development_factors(self):
        t1 = self.triangle()
        development_periods = t1.columns
        
        t2 = t1.iloc[:,1:]
        t2.set_axis(development_periods[0:-1], axis = 1, inplace = True)
        t3 = t2/t1
        new_column_names = [str(development_periods[i]) + '-' + str(development_periods[i+1]) for i in range(len(development_periods) - 1)]
        
        development_factors = t3.iloc[0:-1, 0:-1]

        development_factors.set_axis(new_column_names, axis = 1, inplace = True)
        return development_factors

    def average_development_factors(self):
        development_factors = self.development_factors()
        return development_factors.apply(np.mean)

    def weighted_average_development_factors(self):
        t1 = self.triangle().fillna(0)
        development_periods = t1.columns
        
        t2 = t1.iloc[:,1:]
        t2.set_axis(development_periods[0:-1], axis = 1, inplace = True)
        t3 = t2.apply(sum)/t1.apply(sum)
        new_column_names = [str(development_periods[i]) + '-' + str(development_periods[i+1]) for i in range(len(development_periods) - 1)]
        
        development_factors = t3[0:-1]

        development_factors.set_axis(new_column_names, axis = 0, inplace = True)
        return development_factors
