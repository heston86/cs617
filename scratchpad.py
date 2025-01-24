import pandas as pd

grades = pd.Series([90,91,97], index = ['chip','jhun','amie'])
print(grades)

print(grades.chip)
print(grades['jhun'])