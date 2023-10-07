from bio_age import BioAge

if __name__ == '__main__':
    ba = BioAge()
    '''
    markers_male = {"albumin": 4.5, "alp": 74,
            "crp": 0.209999993443489, "totchol": 225, "creat": 0.968000045776367, "hba1c": 4.59999990463257,
            "sbp": 130, "bun": 14, "uap": 6.40000009536743, "lymph": 27.2000007629395, "mcv": 90.4000015258789,
            "wbc": 5.90000009536743}
    '''
    markers_male = {"albumin": 4.14, "alp": 50.17,
            "crp": 0.235, "totchol": 210.88, "creat": 0.93, "hba1c": 5.5,
            "sbp": 125, "bun": 15.97, "uap": 4.5, "lymph": 46.14, "mcv": 86.8,
            "wbc": 5.05}

    my_age = ba.calc_age(False, 38, markers_male)
    print(my_age)
