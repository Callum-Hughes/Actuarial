from Triangle import Triangle
import pandas as pd

data = pd.DataFrame(data = {
    'origin_year': [2018, 2018, 2018, 2019, 2019, 2020],
    'development_year': [2018, 2019, 2020, 2019, 2020, 2020],
    'values': [1000, 2000, 3000, 500, 1000, 100]
})

tr = Triangle(data)

print(tr.getData())

print(tr)

data['development_period'] = 12*(data['development_year'] - data['origin_year']) + 12

triangle = tr.triangle()
#print(triangle.columns)
#cols = triangle.columns
#
#development_factors = triangle[0:-1]
#labels = []
#print(development_factors)
#
#for c in range(len(cols)-1):
#    development_factors.iloc[:,c] = development_factors.iloc[:,c+1] / development_factors.iloc[:,c]
#    labels.append(str(cols[c]) + '-' + str(cols[c+1]))
#
#development_factors.drop(labels = cols[-1], axis = 1, inplace = True)
#development_factors.set_axis(labels, axis = 1, inplace = True)

print(t1:= triangle.fillna(0))
print(t2:= t1.iloc[:,1:])
t2.set_axis(t1.columns[0:-1], axis = 1, inplace = True)
print(t3:= t2.apply(sum) / t1.apply(sum))
print(t4:= t3[0:-1])
print('--------------------------------done')

print(tr.weighted_average_development_factors())

expected_weighted_average_development_factors = pd.Series(data = [1.875, 1.000], index = ['12-24', '24-36'])

print(list(expected_weighted_average_development_factors.values))