import pandas as pd
import matplotlib

data = pd.read_csv('train.csv')

# Task 1.1
# print(data.columns)
# print(data[(data['Pclass'] == 1) & (data['Embarked'] == 'S')].shape[0])

# Task 2.2
# print(data[(data['Pclass'] == 3) & (data['SibSp'] > 1)].shape[0])

# Task 1.3
# print(data[(data['Pclass'] == 1) & (data['Fare'])]['Fare'].mean())

# Task 2.1
# print(data['Survived'].groupby([data['Pclass'], data['Sex']]).mean())

# Task 2.2
# print(data.Pclass.hist())
# data.groupby(['Pclass']).sum().plot(kind='pie', y='votes_of_each_class')
# data.groupby(['Pclass']).sum().plot(kind='pie', y='Age')

# Task 3.1
# data['FamilySize'] = data.SibSb + data.Parch
# data['Alone'] = data['FamilySize'].apply(lambda x: 1 if data['FamilySize'] else 0)
# del data['FamilySize']


