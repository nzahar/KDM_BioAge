"""
albumin - Albumin (g/dL)
alp	- Alkaline phosphatase (U/L)
lncrp - Log(c-reactive protein) (mg/dL) !!
totchol - Total cholesterol (mg/dL)
lncreat - Log(creatinine) (mg/dL)
hba1c - Glycohemoglobin (%)
sbp - Systolic blood pressure (mm Hg)
bun - Blood urea nitrogen (mg/dL)
uap - Uric acid (mg/dL)
lymph - Lymphocyte percent (%)
mcv - Mean cell volume (fL)
wbc - White blood cell count (1000 cells/uL)
"""

import pandas as pd


class BioAge:
    # biomarkers = ["albumin","alp","lncrp","totchol","lncreat","hba1c","sbp","bun","uap","lymph","mcv","wbc"]
    def __init__(self):
        self.fem_s_ba2 = 1462.073
        self.male_s_ba2 = 2106.478
        self.fem_weights = pd.read_csv('fem_fit_table.csv')
        self.male_weights = pd.read_csv('male_fit_table.csv')

    def calc_age(self, is_female, age, markers):
        """
            calc_age calculates KDM (Klemera-Doubal Method) bioage.

            :param is_female: bool, true if person is female. False for male
            :param age: number corresponding to a person's astronomical age
            :param markers: dictionary with biomarkers and their values like {"albumin": value,"alp": value,
            "lncrp": value,"totchol": value,"lncreat": value,"hba1c": value,"sbp": value,"bun": value,"uap": value,
            "lymph": value,"mcv": value,"wbc": value}
            :return: number indicating biological age
            """

        weights = self.fem_weights if is_female else self.male_weights
        s_ba2 = self.fem_s_ba2 if is_female else self.male_s_ba2

        n1 = markers.copy()
        for key in n1.keys():
            row = weights.loc[weights['bm'] == key]
            n1[key] = (markers[key] - row.iloc[0]['q']) * (row.iloc[0]['k'] / (row.iloc[0]['s'] ** 2)) \
                if markers[key] is not None else 0

        BAe_n = sum(n1.values())
        BAe_d = weights['n2'].sum()

        kdm = (BAe_n + (age / s_ba2)) / (BAe_d + (1 / s_ba2))
        return kdm
