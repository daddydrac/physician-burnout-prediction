import random
import pydash as _


def employment_status(_idx, _data):
    _scope = {
        "employment_status": None
    }

    # owner:  45.9% of a population of 8000 =3672
    if _idx in range(0, 3672, 1):
        _scope["employment_status"] = (1, "owner")

    # Employee: 47.4% of a population of 8000=3792
    elif _idx in range(3673, 7465, 1):
        _scope["employment_status"] = (2, "employee")

    else:
        _scope["employment_status"] = (3, "Independent contractor")

    result = _.assign(_data[_idx], {"employment_status": _scope["employment_status"]})

    return result


def antistress_program(_idx, _data):

    _scope = {
        "antistress_program": None
    }

    # 1: Yes : workplace offers a program to reduce stress 30% of a population of 8000=2400
    if _idx in range(0, 2400, 1):
        _scope["antistress_program"] = 1

    # 2: No : 48% of a population of 8000=3840
    if _idx in range(2401, 6241, 1):
        _scope["antistress_program"] = 2
    # 3: unspecified : 22% of a population of 8000
    else:
        _scope["antistress_program"] = 3

    result = _.assign(_data[_idx], {"anti_stress_program": _scope["antistress_program"]})

    return result


def specialties(_idx, _data):
    _scope = {
        "speciality": None,
        "salary": None

    }

    # Allergist / Immunologist: 0.45% of a population of 8000 =36
    if _idx in range(0, 36, 1):
        _scope["speciality"] = (1, "Allergist / Immunologist")
        # avg salary: 275000
        if _data[_idx]["gender"] == 0:
            _scope["salary"] = random.randrange(247500, 302500, 2)
        else:
            _scope["salary"] = random.randrange(169400, 211750, 2)

    # Anesthesiologist:  5.7% of a population of 8000 = 456
    if _idx in range(37, 493, 1):
        _scope["speciality"] = (2, "Anesthesiologist")
        # avg salary: 392000
        if _data[_idx]["gender"] == 0:
            _scope["salary"] = random.randrange(352800, 431200, 2)
        else:
            _scope["salary"] = random.randrange(246960, 301840, 2)

    # Dermatologist: 1.52% of a population of 8000 = 122
    if _idx in range(494, 616):
        _scope["speciality"] = (3, "Dermatologist")
        # avg salary: 419000
        if _data[_idx]["gender"] == 0:
            _scope["salary"] = random.randrange(377100, 460900, 2)
        else:
            _scope["salary"] = random.randrange(263970, 322630, 2)



    # Emergency Doctor: 5.98% of a population of 8000 = 478
    elif _idx in range(617, 1095):
        _scope["speciality"] = (4, "Emergency Doctor")
        # avg salary: 353000
        if _data[_idx]["gender"] == 0:
            _scope["salary"] = random.randrange(317700, 388300, 2)
        else:
            _scope["salary"] = random.randrange(222390, 271810, 2)



    # Family Doctor: 14% of a population of 8000 = 1120
    elif _idx in range(1096, 2216):
        _scope["speciality"] = (5, "Family Doctor")
        #  avg salary: 230000
        if _data[_idx]["gender"] == 0:
            _scope["salary"] = random.randrange(207000, 253000, 2)
        else:
            _scope["salary"] = random.randrange(144900, 177100, 2)

    # Internist: 25.9% of a population of 8000 = 2072
    if _idx in range(2217, 4289):
        _scope["speciality"] = (6, "Internist")
        # avg salary: 243000
        if _data[_idx]["gender"] == 0:
            _scope["salary"] = random.randrange(218700, 267300, 2)
        else:
            _scope["salary"] = random.randrange(153090, 187110, 2)


    # Neurological Surgeon: 0.73% of a population of 8000 = 59
    elif _idx in range(4290, 4349):
        _scope["speciality"] = (7, "Neurological Surgeon")

        if _data[_idx]["gender"] == 0:
            _scope["salary"] = random.randrange(697500, 852500, 2)
        else:
            _scope["salary"] = random.randrange(488250, 596750, 2)



    # Obstetrician / Gynecologist: 5.17% of a population of 8000 = 414
    elif _idx in range(4350, 4764):
        _scope["speciality"] = (8, "Obstetrician / Gynecologist")
        # avg salary: 303000
        if _data[_idx]["gender"] == 0:
            _scope["salary"] = random.randrange(272700, 333300, 2)
        else:
            _scope["salary"] = random.randrange(190890, 233310, 2)



    # Orthopedic Surgeon: 3.26% of a population of 8000 = 261
    elif _idx in range(4765, 5026):
        _scope["speciality"] = (9, "Orthopedic Surgeon")
        # avg salary: 482000
        if _data[_idx]["gender"] == 0:
            _scope["salary"] = random.randrange(433800, 530200, 2)
        else:
            _scope["salary"] = random.randrange(303660, 371140, 2)


    # Otolaryngologist: 1.29% of a population of 8000 = 103
    elif _idx in range(5027, 5130):
        _scope["speciality"] = (10, "Otolaryngologist")
        # avg salary:461000
        if _data[_idx]["gender"] == 0:
            _scope["salary"] = random.randrange(414900, 507100, 2)
        else:
            _scope["salary"] = random.randrange(290430, 354970, 2)


    # Pathologist: 2.1% of a population of 8000 = 168
    elif _idx in range(5131, 5299):
        _scope["speciality"] = (11, "Pathologist")
        # avg salary: 308000
        if _data[_idx]["gender"] == 0:
            _scope["salary"] = random.randrange(277200, 338800, 2)
        else:
            _scope["salary"] = random.randrange(194040, 237160, 2)



    # Pediatrician: 9.44% of a population of 8000 = 755
    elif _idx in range(5300, 6055):
        _scope["speciality"] = (12, "Pediatrician")
        # avg salary: 225000
        if _data[_idx]["gender"] == 0:
            _scope["salary"] = random.randrange(202500, 247500, 2)
        else:
            _scope["salary"] = random.randrange(141750, 173250, 2)



    # Plastic Surgeons:  0.54% of a population of 8000 = 43
    elif _idx in range(6056, 6099):
        _scope["speciality"] = (13, "Plastic Surgeons")
        # avg salary: 471000
        if _data[_idx]["gender"] == 0:
            _scope["salary"] = random.randrange(423900, 518100, 2)
        else:
            _scope["salary"] = random.randrange(296730, 362670, 2)


    # Psychiatrist/Neurologist:  7.93% of a population of 8000 = 635
    elif _idx in range(6100, 6735):
        _scope["speciality"] = (14, "Psychiatrist/Neurologist")
        # avg salary: 260000
        if _data[_idx]["gender"] == 0:
            _scope["salary"] = random.randrange(234000, 286000, 2)
        else:
            _scope["salary"] = random.randrange(163800, 200200, 2)



    # Radiologist:   5.14% of a population of 8000 = 411
    elif _idx in range(6736, 7147):
        _scope["speciality"] = (15, "Radiologist")
        # avg salary : 419000
        if _data[_idx]["gender"] == 0:
            _scope["salary"] = random.randrange(377100, 460900, 2)
        else:
            _scope["salary"] = random.randrange(263970, 322630, 2)


    # Surgeons: 4.24%  of a population of 8000 = 340
    elif _idx in range(7148, 7488):
        _scope["speciality"] = (16, "Surgeons")
        # avg salary: 362000
        if _data[_idx]["gender"] == 0:
            _scope["salary"] = random.randrange(325800, 398200, 2)
        else:
            _scope["salary"] = random.randrange(228060, 278740, 2)



    # Urologist: 1.29%  of a population of 8000 = 103
    elif _idx in range(7489, 7592):
        _scope["speciality"] = (17, "Urologist")
        # avg salary: 408000
        if _data[_idx]["gender"] == 0:
            _scope["salary"] = random.randrange(367200, 448800, 2)
        else:
            _scope["salary"] = random.randrange(257040, 314160, 2)


    # Optometrist: 5.6% of a population of 8000 = 448
    else:
        _scope["speciality"] = (18, "Optometrist")
        # avg salary: 366000
        if _data[_idx]["gender"] == 0:
            _scope["salary"] = random.randrange(329400, 402600, 2)
        else:
            _scope["salary"] = random.randrange(230580, 281820, 2)

    result = _.assign(_data[_idx], {"salary": _scope["salary"], "speciality": _scope["speciality"]})

    return result
