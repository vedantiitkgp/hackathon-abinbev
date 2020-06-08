import requests
import os
import json
import pandas as pd

class timelogfun:
    def add_employee(fname, lname, email, EmployeeID):
        t1="https://people.zoho.in/people/api/employee/records?authtoken=31d865f824a8c223a558ef393fe59a21&xmlData=<Request><Record><field name='EmployeeID'>"
        t2="</field><field name='FirstName'>"
        t3="</field><field name='LastName'>"
        t4="</field><field name='EmailID'>"
        t5="</field><field name='Marital_status'>Married</field></Record></Request>"

        url=''.join([t1,str(EmployeeID),t2,fname,t3,lname,t4,email,t5])
        response=requests.post(url)
        res={'msg':json.loads(response.text)['response']['message'],'data':None}
        return res

    def all_employees():
        params={'authtoken': '31d865f824a8c223a558ef393fe59a21'}
        url='https://people.zoho.in/people/api/forms/P_EmployeeView/records'
        response=requests.post(url, params=params)
        
        res={'msg':None,'data':pd.read_json(response.text)[['First Name','Last Name','Email ID','recordId','EmployeeID','Employee Role']]}
        return res

    def search_employee(email):
        t1='https://people.zoho.in/people/api/forms/P_EmployeeView/records?authtoken=31d865f824a8c223a558ef393fe59a21&searchColumn=EMPLOYEEMAILALIAS&searchValue='
        url=''.join([t1,str(email)])
        response=requests.post(url)
        res={'msg':None,'data':pd.read_json(response.text)[['First Name','Last Name','Email ID','EmployeeID','Employee Role']]}
        return res

    def all_jobs(value):
        t='https://people.zoho.in/people/api/timetracker/getjobs?authtoken=31d865f824a8c223a558ef393fe59a21&assignedTo='
        url=''.join([t,str(value)])
        response=requests.post(url)
        
        res={'msg':None,'data':pd.DataFrame(pd.read_json(response.text).iloc[1,0])[['jobName','jobStatus','fromDate','jobId']]}
        return res

    def change_job_status(jobid,status):
        t='https://people.zoho.in/people/api/timetracker/modifyjobstatus?authtoken=31d865f824a8c223a558ef393fe59a21&jobId='
        t1='&jobStatus='
        url=''.join([t,jobid,t1,status])
        response=requests.post(url)
        
        res={'msg':json.loads(response.text)['response']['message'],'data':None}
        return res

    def add_job(user,jobName,workdate,hrs):
        t='http://people.zoho.in/people/api/timetracker/addtimelog?authtoken=31d865f824a8c223a558ef393fe59a21&user='
        t1='&jobName='
        t2='&workDate='
        t3='&billingStatus=Billable'
        t4='&hours='

        url=''.join([t,str(user),t1,jobName,t2,workdate,t3,t4,str(hrs)])
        response=requests.post(url)
        
        res={'msg':json.loads(response.text)['response']['message'],'data':None}
        return res

    def get_timelog(user,fromDate,toDate):
        t1='http://people.zoho.in/people/api/timetracker/gettimelogs?authtoken=31d865f824a8c223a558ef393fe59a21&user='
        t2='&jobId=all&fromDate='
        t3='&toDate='
        t4='&billingStatus=all'

        url=''.join([t1,user,t2,fromDate,t3,toDate,t4])
        response=requests.post(url)
        
        res={'msg':None,'data':pd.DataFrame(pd.read_json(response.text).iloc[1,0])[['employeeMailId','employeeFirstName','workDate','timelogId','jobName','jobIsActive','jobIsCompleted','hours']]}
        return res
