import pandas
import json

from timelog import timelogfun

class mediatorCall:
    def __init__(self,msg):
        self.msg=msg

    def run_query(self,msg):
        msg=msg.split()
        if(msg[0]=="Add" or msg[0]=="add"):
            output=self.command_add(msg)
        elif(msg[0]=="Show" or msg[0]=="show"):
            output=self.command_show(msg)
        elif(msg[0]=="Search" or msg[0]=="search"):
            output=self.command_search(msg)
        elif(msg[0]=="Change" or msg[0]=="change"):
            output=self.command_change(msg)

        return output

    def command_add(self,msg):
        if(msg[1]=='employee' or msg[1]=='Employee'):
            output=timelogfun.add_employee(msg[2],msg[3],msg[4],msg[5])
            return output

        elif(msg[1]=='job' or msg[1]=='Job'):
            output=timelogfun.add_job(msg[4],msg[2],msg[6],msg[8])
            return output

    def command_show(self,msg):
        if(msg[1]=='employee' or msg[1]=='Employee'):
            output=timelogfun.all_employees()
            #output="DEBUG"
            return output

        if(msg[1]=='jobs' or msg[1]=='Jobs'):
            output=timelogfun.all_jobs(msg[3])
            return output

        if(msg[1]=='timelog' or msg[1]=='Timelog'):
            output=timelogfun.get_timelog(msg[3],msg[5],msg[7])
            return output

    def command_search(self,msg):
            if(msg[1]=='employee' or msg[1]=='Employee'):
                output=timelogfun.search_employee(msg[2])
                return output

    def command_change(self,msg):
        if(msg[1]=='job' or msg[1]=='Job'):
            output=timelogfun.change_job_status(msg[4],msg[6])
            return output
