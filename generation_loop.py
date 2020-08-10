import json
import codecs
import random
import pydash as _
from random import seed
from random import randint
from gender_by_age import gender_age
from data_utils import \
     specialties, \
     work_hours_patient, \
     self_esteem, \
     employment_status, \
     antistress_program, \
     stressor_a, \
     stressor_b, \
     stresoor_c, \
     stressor_d, \
     stressor_e, \
     stressor_f, \
     stressor_g, \
     stressor_h, \
     stressor_i, \
     stressor_j \



def make_doctors():

    result = []

    # (3) this will generate the number of rows of data
    for i in range(1, 8001):
        # Create Doctor IDs
        _i = (0 + i)

        age, gender = gender_age(_i)

        data = {
            "id": _i,
            "age": age,
            "gender": gender,
        }

        result.append(data)

    _len = len(result)

    return random.sample(random.sample(result, _len), _len)


create_doctors = make_doctors()


for i in range(len(create_doctors)):
    specialties(i, create_doctors)
    work_hours_patient(i, create_doctors)
    self_esteem(i, create_doctors)
    employment_status(i, create_doctors)
    antistress_program(i, create_doctors)
    stressor_a(i, create_doctors)
    stressor_b(i, create_doctors)
    stressor_c(i, create_doctors)
    stressor_d(i, create_doctors)
    stressor_e(i, create_doctors)
    stressor_f(i, create_doctors)
    stressor_g(i, create_doctors)
    stressor_h(i, create_doctors)
    stressor_i(i, create_doctors)
    stressor_j(i, create_doctors)

with codecs.open('create_doctors.json', 'w', 'utf8') as f:
     f.write(json.dumps(create_doctors, indent=2))

