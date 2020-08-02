import json
import random
from gender_by_age import gender_age
from data_utils import \
    employment_status, \
    antistress_program



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
    employment_status(i, create_doctors)
    antistress_program(i, create_doctors)

print(json.dumps(create_doctors, indent=2))

