from bio_age import BioAge

if __name__ == '__main__':
    ba = BioAge()
    '''
    markers_male = {"albumin": 4.5, "alp": 74,
            "lncrp": 0.190620354190046, "totchol": 225, "lncreat": 0.677017821890411, "hba1c": 4.59999990463257,
            "sbp": 130, "bun": 14, "uap": 6.40000009536743, "lymph": 27.2000007629395, "mcv": 90.4000015258789,
            "wbc": 5.90000009536743}'''

    markers_male = {"albumin": 4.5, "alp": 74,
            "lncrp": 0.190620354190046, "totchol": 225, "lncreat": 0.677017821890411, "hba1c": 4.59999990463257,
            "sbp": 130, "bun": 14, "uap": 6.40000009536743, "lymph": 27.2000007629395, "mcv": 90.4000015258789,
            "wbc": 5.90000009536743}
    my_age = ba.calc_age(False, 35, markers_male)
    print(my_age)
