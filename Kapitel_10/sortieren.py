def population(daten):
    # stadt = daten[0]
    # population = daten[1]
    return daten[1]

L =[ ['Buenos Aires',13076300], ['Dhaka',10356500], ['São Paulo',10021295], ['Tianjin',11090314],
     ['Shenzhen',10358381], ['Shanghai',22315474], 
     ['Guangzhou',11071424], ['Beijing',11716620], 
     ['Delhi',10927986],['Mumbai',12691836], 
     ['Seoul',10349312], ['Mexico City',12294193], 
     ['Karachi',11624219],['Moscow',10381222], ['Istanbul',14804116] ]


#L2 = sorted(L, key=population, reverse=True)

L2 = sorted(L, reverse=True, key=lambda daten: daten[1])

print(L2)
