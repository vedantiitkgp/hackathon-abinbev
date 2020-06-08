import requests
import os
import json
import pandas as pd

class timelogfun:
    def __init__(self, token):
        self.token = token

    def add_employee(self, fname, lname, email, EmployeeID):
        t1="https://people.zoho.in/people/api/employee/records?authtoken="+self.token+"&xmlData=<Request><Record><field name='EmployeeID'>"
        t2="</field><field name='FirstName'>"
        t3="</field><field name='LastName'>"
        t4="</field><field name='EmailID'>"
        t5="</field><field name='Marital_status'>Married</field></Record></Request>"

        url=''.join([t1,str(EmployeeID),t2,fname,t3,lname,t4,email,t5])
        response=requests.post(url)
        msg = 'Employee added successfully' if response.status_code == 200 else 'Some error while processing.'
        res={'msg':msg,'data':None}
        return res

    def all_employees(self):
        params={'authtoken': self.token}
        url='https://people.zoho.in/people/api/forms/P_EmployeeView/records'
        response=requests.post(url, params=params)
        
        res={'msg':None,'data':pd.read_json(response.text)[['First Name','Email ID','recordId','EmployeeID','Employee Role']]}
        return res

    def search_employee(self, email):
        t1='https://people.zoho.in/people/api/forms/P_EmployeeView/records?authtoken='+self.token+'&searchColumn=EMPLOYEEMAILALIAS&searchValue='
        url=''.join([t1,str(email)])
        response=requests.post(url)
        res={'msg':None,'data':pd.read_json(response.text)[['First Name','Last Name','Email ID','EmployeeID','Employee Role']]}
        return res

    def all_jobs(self, value):
        t='https://people.zoho.in/people/api/timetracker/getjobs?authtoken='+self.token+'&assignedTo='
        url=''.join([t,str(value)])
        response=requests.post(url)
        
        res={'msg':None,'data':pd.DataFrame(pd.read_json(response.text).iloc[1,0])[['jobName','jobStatus','fromDate','jobId']]}
        return res

    def change_job_status(self, jobid,status):
        t='https://people.zoho.in/people/api/timetracker/modifyjobstatus?authtoken='+self.token+'&jobId='
        t1='&jobStatus='
        url=''.join([t,jobid,t1,status])
        response=requests.post(url)
        
        res={'msg':json.loads(response.text)['response']['message'],'data':None}
        return res

    def add_job(self, user,jobName,workdate,hrs):
        t='http://people.zoho.in/people/api/timetracker/addtimelog?authtoken='+self.token+'&user='
        t1='&jobName='
        t2='&workDate='
        t3='&billingStatus=Billable'
        t4='&hours='

        url=''.join([t,str(user),t1,jobName,t2,workdate,t3,t4,str(hrs)])
        response=requests.post(url)
        
        res={'msg':json.loads(response.text)['response']['message'],'data':None}
        return res

    def get_timelog(self, user,fromDate,toDate):
        t1='http://people.zoho.in/people/api/timetracker/gettimelogs?authtoken='+self.token+'&user='
        t2='&jobId=all&fromDate='
        t3='&toDate='
        t4='&billingStatus=all'

        url=''.join([t1,user,t2,fromDate,t3,toDate,t4])
        response=requests.post(url)
        
        res={'msg':None,'data':pd.DataFrame(pd.read_json(response.text).iloc[1,0])[['employeeFirstName','workDate','timelogId','jobName','jobIsCompleted','hours']]}
        return res
