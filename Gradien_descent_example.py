import numpy as np

#vrem sa gasim cea mai buna linie care trece prin cate mai
#multe training examples


def gradient_descent(x,y):
    m_current = b_current = 0
    iteratii = 1000
    n=len(x)

    #learning rate-ul perfect
    learning_rate=0.08

    for i in range(iteratii):
        #functia liniara mx+b
        y_predict = m_current*x + b_current
        #costul functiei dupa formula
        cost=(1/n)*sum([val**2 for val in (y-y_predict)])
        #derivata lui m
        md=-(2/n)*sum(x*(y-y_predict))
        #derivata lui b
        bd=-(2/n)*sum(y-y_predict)
        #schimbam coordonatele in functie de learning rate
        #si derivate
        m_current = m_current - learning_rate * md
        b_current = b_current - learning_rate * bd
        print("m {}, b {}, cost {}, iteratia {}".format(m_current,b_current,cost,i))

x=np.array([1,2,3,4,5])
y=np.array([5,7,9,11,13])

gradient_descent(x,y)
