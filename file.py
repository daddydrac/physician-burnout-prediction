def make_doctors():

    result = []

    # (3) this will generate the number of rows of data
    for i in range(1, 8001):
        # Create Customer ID
        doctor_ids = (0 + i)

        age, gender = gender_age(doctor_ids)

        data = {
            "id": doctor_ids,
            "age": age,
            "gender": gender,
        }

        result.append(data)

    return result