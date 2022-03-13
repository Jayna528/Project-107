import plotly.graph_objects as go
import pandas as pd 
import csv
import plotly.express as px


df = pd.read_csv('data.csv')


studentGroupData = df.groupby(['level', 'student_id'], as_index = False)['attempt']
studentLevelData = studentGroupData.mean()

fig = px.scatter(studentLevelData, x = 'student_id', y = 'level', size = 'attempt', color = 'attempt')
fig.show()

#print(studentLevelData)
#print(studentData)