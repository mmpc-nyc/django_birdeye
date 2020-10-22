from django.db import connections
from birdeye.helpers import parse_phone_number
from birdeye.helpers import dictfetchall


def get_review_requests(interval = 600):
    query = """
    SELECT
        E.Email AS EmployeeEmail,
        E.EmployeeID,
        C.ContactID,
        C.ContactName,
        C.Email AS CustomerEmail,
        C.Phone1A + C.Phone1 AS Phone

    FROM tblJobs AS J
    LEFT JOIN tblSchedules AS S ON S.ScheduleID = J.ScheduleID
    LEFT JOIN tblContact AS C ON C.ContactID = S.ContactID
    LEFT JOIN tblTeamEmployees AS TE ON TE.TeamID = S.TeamID
    LEFT JOIN tblTeams AS T ON T.TeamID = S.TeamID
    LEFT JOIN tblEmployees AS E ON TE.EmployeeID = E.EmployeeID
    LEFT JOIN lkpJobStatus AS JStatus ON JStatus.StatusID = J.StatusID
    LEFT JOIN lkpJobSubStatus AS JSubStatus ON JSubStatus.SubStatusID = J.SubStatusID

    WHERE
        DATEDIFF(SECOND,DATEADD(SECOND,J.StartTime+J.Duration*60,J.StartDate),GETDATE()) < ? AND
        DATEDIFF(SECOND,DATEADD(SECOND,J.StartTime+J.Duration*60,J.StartDate),GETDATE()) > 0 AND
        J.Extra11 = 'Yes'
        """
    with connections['ceo'].cursor() as cursor:
        cursor.execute(query, interval)
        return dictfetchall(cursor)


def parse_review_request(row):
    return {'name': row.ContactName, 'customer_email': row.CustomerEmail, 'phone': parse_phone_number(row.Phone),
            'employee_email': row.EmployeeEmail, 'contactid': row.ContactID, 'employeeid': row.EmployeeID}