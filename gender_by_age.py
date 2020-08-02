import random


def gender_age(seeds):
    if seeds in range(1, 897):  # 11.2% of population is age range from 25-35
        random.seed(seeds)
        age = random.randrange(25, 35, 1)

        if seeds in range(1, 354):  # 39.4% of population is male
            random.seed(seeds)
            gender = 0
        else:
            # remainder of population is female
            random.seed(seeds)
            gender = 1

        return age, gender
    elif seeds in range(898, 2473):  # 19.8% of population is age range from 36-45
        random.seed(seeds)
        age = random.randrange(36, 45, 1)

        if seeds in range(898, 1666):  # 48.5% of population is male
            random.seed(seeds)
            gender = 0
        else:
            # remainder of population is female
            random.seed(seeds)
            gender = 1

        return age, gender

    elif seeds in range(2474, 4306):  # 22.9% of population is age range 46-55
        random.seed(seeds)
        age = random.randrange(46, 55, 1)

        if seeds in range(2474, 3498):  # 55.9% of population is male
            random.seed(seeds)
            gender = 0
        else:
            # remainder of population
            random.seed(seeds)
            gender = 1

        return age, gender

    elif seeds in range(4307, 6627):  # 29% of population is age range 56-65
        random.seed(seeds)
        age = random.randrange(56, 65, 1)
        if seeds in range(4307, 5919):  # 69.5% of population is male
            random.seed(seeds)
            gender = 0
        else:
            # remainder of population
            random.seed(seeds)
            gender = 1

        return age, gender

    else:
        # remainder of population
        random.seed(seeds)
        age = random.randrange(66, 75, 1)  # 17% of population is age range 66-75
        if seeds in range(6628, 7748):  # 82.4% of population is male
            random.seed(seeds)
            gender = 0

        else:
            # remainder of population
            random.seed(seeds)
            gender = 1
        return age, gender

