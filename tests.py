import unittest
import pandas as pd
import numpy as np
from Triangle import Triangle


data = pd.DataFrame(data = {
    'origin_year': [2018, 2018, 2018, 2019, 2019, 2020],
    'development_year': [2018, 2019, 2020, 2019, 2020, 2020],
    'values': [1000, 2000, 3000, 500, 1000, 100]
})

expected_weighted_average_development_factors = pd.Series(data = [1.875, 1.000], index = ['12-24', '24-36'])


class TestTriangle(unittest.TestCase):
    
    data = pd.DataFrame(data = {
    'origin_year': [2018, 2018, 2018, 2019, 2019, 2020],
    'development_year': [2018, 2019, 2020, 2019, 2020, 2020],
    'values': [1000, 2000, 3000, 500, 1000, 100]
    })
    
    def test_weighted_average_development_factors(self):
        tr = Triangle(data)
        observed_weighted_average_development_factors = tr.weighted_average_development_factors()
        self.assertListEqual(list(observed_weighted_average_development_factors.values), list(expected_weighted_average_development_factors.values))

if __name__ == '__main__':
    unittest.main()