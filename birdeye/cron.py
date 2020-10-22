from django.db import connections
from birdeye.helpers import parse_phone_number
from birdeye.helpers import dictfetchall


def parse_review_request(row):
    return {'name': row.ContactName, 'customer_email': row.CustomerEmail, 'phone': parse_phone_number(row.Phone),
            'employee_email': row.EmployeeEmail, 'contactid': row.ContactID, 'employeeid': row.EmployeeID}