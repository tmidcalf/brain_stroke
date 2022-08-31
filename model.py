import numpy as np
import pickle

def mlearn(age, height, weight, sex, married, work, res, smoke, hyper, heart, agl):
    loaded_model = pickle.load(open("flask/finalized_model.sav", 'rb'))
    data = []

    age=float(age)
    height=float(height)
    weight=float(weight)
    sex=float(sex)
    married=float(married)
    work=float(work)
    res=float(res)
    smoke=float(smoke)
    hyper=float(hyper)
    heart=float(heart)
    agl=float(agl)

    bmi = (weight * 0.45359237)/((height * 0.0254 )*(height * 0.0254 ))
    data.append(hyper)
    data.append(heart)
    data.append(agl)
    data.append(bmi)
    data.append(sex)
    data.append(age)
    data.append(married)
    data.append(work)
    data.append(res)
    data.append(smoke)
    new_data = np.array([data])
    results = loaded_model.predict(new_data)[0]

    if results == 0:
        return "With the information provided you are NOT prone to brain stroke"

    else:
        return "With the information provided you ARE prone to brain stroke"

loaded_model = pickle.load(open("finalized_model.sav", 'rb'))

new_data = np.array([[0, 0, 162.23, 27.3, 0, 56, 1, 0, 0, 0]])

results = loaded_model.predict(new_data)[0]

print(results)