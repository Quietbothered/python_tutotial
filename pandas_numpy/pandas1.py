# import pandas as pd

# import statsmodels.formula.api as smf

# data = pd.DataFrame({'choice': ['A', 'B', 'A', 'C', 'B', 'C', 'A', 'B', 'C', 'A'], 'feature1': [1, 2, 3, 4, 5, 6, 7, 8, 9, 10], 'feature2': [10, 9, 8, 7, 6, 5, 4, 3, 2, 1]})

# model = smf.mnlogit(formula='choice ~ feature1 + feature2', data=data).fit()
import pandas as pd
import statsmodels.formula.api as smf

# Example dummy data
data = pd.DataFrame({
    'choice': ['A', 'B', 'C', 'A', 'B', 'C', 'A', 'B', 'C', 'A'],
    'feature1': [1,2,3,4,5,6,7,8,9,10],
    'feature2': [10,9,8,7,6,5,4,3,2,1]
})

# Convert target to categorical codes
data['choice'] = pd.Categorical(data['choice']).codes

# Fit the multinomial logistic regression model
model = smf.mnlogit(formula='choice ~ feature1 + feature2', data=data).fit()

print(model.summary())
