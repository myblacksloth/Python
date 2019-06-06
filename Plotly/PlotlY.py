# (C) Antonio Maulucci 2019 ~ https://sites.google.com/view/antomau
# web: plot.ly/python/line-charts/

# # apt-get install pyton3-pip

#import plotly.plotly as ply
# $ python3 -m pip install plotly
import plotly.offline as plyOFFL
import plotly.graph_objs as pobj
import numpy as np
# $ pyton3 -m pip install numpy

N=10

xData = np.linspace(0,1,N)

print()
print("xData")
print("************************************")
print(xData)
print()

#yData = [9]
yData = np.random.randn(N)


print("yData")
print("************************************")
print(yData)
print()

trace = pobj.Scatter(x=xData, y=yData)


print("trace")
print("************************************")
print(trace)
print()

########
#data = [trace]


# print()
# print()
########
#print(data)

#ply.plot(data, filename='lineare')

########
#plyOFFL.plot(data, filename="grafico.html", auto_open=False)





x2 = [0, 1, 2, 3, 4, 5, 6]
y2 = [12, 13, 14, 15, 16, 17]

trace2 = pobj.Scatter(x=x2, y=y2, name='Nulla', mode='markers')


###########
data = [trace, trace2]


print("data")
print("************************************")
print(data)
print()



plyOFFL.plot(data, filename="grafico.html", auto_open=False)





''' $out>

xData
************************************
[0.         0.11111111 0.22222222 0.33333333 0.44444444 0.55555556
 0.66666667 0.77777778 0.88888889 1.        ]

yData
************************************
[-0.42121557 -1.33095398  0.38013207 -0.75611109  0.00381983 -1.72087729
  0.01834745  1.04475998  0.86285437 -0.48301227]

trace
************************************
Scatter({
    'x': array([0.        , 0.11111111, 0.22222222, 0.33333333, 0.44444444, 0.55555556,
                0.66666667, 0.77777778, 0.88888889, 1.        ]),
    'y': array([-0.42121557, -1.33095398,  0.38013207, -0.75611109,  0.00381983,
                -1.72087729,  0.01834745,  1.04475998,  0.86285437, -0.48301227])
})

data
************************************
[Scatter({
    'x': array([0.        , 0.11111111, 0.22222222, 0.33333333, 0.44444444, 0.55555556,
                0.66666667, 0.77777778, 0.88888889, 1.        ]),
    'y': array([-0.42121557, -1.33095398,  0.38013207, -0.75611109,  0.00381983,
                -1.72087729,  0.01834745,  1.04475998,  0.86285437, -0.48301227])
}), Scatter({
    'mode': 'markers', 'name': 'Nulla', 'x': [0, 1, 2, 3, 4, 5, 6], 'y': [12, 13, 14, 15, 16, 17]
})]


'''







