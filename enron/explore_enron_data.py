#!/usr/bin/python

"""
    Starter code for exploring the Enron dataset (emails + finances);
    loads up the dataset (pickled dict of dicts).

    The dataset has the form:
    enron_data["LASTNAME FIRSTNAME MIDDLEINITIAL"] = { features_dict }

    {features_dict} is a dictionary of features associated with that person.
    You should explore features_dict as part of the mini-project,
    but here's an example to get you started:

    enron_data["SKILLING JEFFREY K"]["bonus"] = 5600000

"""

import pickle

enron_data = pickle.load(open("/Users/geunseong-gai/Documents/Python/Udacity/MLND/enron/final_project/final_project_dataset.pkl", "r"))

searching_name = "Fastow".upper()

for key in enron_data.keys():
    if searching_name in key:
        print(key)


# CEO - "Jeffrey Skilling"
# Chairman - "Ken Lay"
# CFO - "Andrew Fastow"

# 'salary', 'to_messages', 'deferral_payments', 'total_payments',
# 'exercised_stock_options', 'bonus', 'restricted_stock', 'shared_receipt_with_poi',
# 'restricted_stock_deferred', 'total_stock_value', 'expenses', 'loan_advances',
# 'from_messages', 'other', 'from_this_person_to_poi', 'poi', 'director_fees',
# 'deferred_income', 'long_term_incentive', 'email_address', 'from_poi_to_this_person'

print(enron_data["SKILLING JEFFREY K"]["total_payments"])
print(enron_data["LAY KENNETH L"]["total_payments"])
print(enron_data["FASTOW ANDREW S"]["total_payments"])
