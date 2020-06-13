def analyse(model,vect,list_review):
    mo = model
    ve = vect
    data = list_review
    predict = mo.predict(ve.transform(data))
    p = 0
    n = 0
    for value in predict:
        if value == 1:
            p= p+1
        else:
            n= n+1
    if p>n:
        return 'Must Buy', p, n
    else:
        return 'Do not Buy', p, n



