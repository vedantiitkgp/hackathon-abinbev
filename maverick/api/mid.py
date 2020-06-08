from .features.timelog import timelogfun
from .features.tickets import ticket_func
from .features.covidcases import covidcasesfun
from .features.expense_managment import expense_management
from .features.token_generator import token_generator

class mediatorCall:
    def __init__(self,msg):
        self.msg=msg

        tok_gen = token_generator()
        token_expense = tok_gen.expense()
        token_ticket = tok_gen.ticket()

        self.ticket_func = ticket_func(token_ticket['access_token'], token_ticket['organization_id'])
        self.expense_management = expense_management(token_expense['access_token'], token_expense['organization_id']);
        self.timelogfun = timelogfun(tok_gen.timelog())

    def run_query(self):
        msg=self.msg.split()
        temp = msg[0].lower()
        if(temp=="add"):
            output=self.command_add(msg)
        elif(temp=="show"):
            output=self.command_show(msg)
        elif(temp=="search"):
            output=self.command_search(msg)
        elif(temp=="change"):
            output=self.command_change(msg)
        elif(temp == "create"):
            output=self.command_create(msg)
        elif(temp == "close"):
            output=self.command_close(msg)
        elif(temp == "delete"):
            output=self.command_delete(msg)
        return output

    def command_add(self,msg):
        if(msg[1].lower()=='employee'):
            output=self.timelogfun.add_employee(msg[2],msg[3],msg[4],msg[5])
        elif(msg[1].lower()=='job'):
            output=self.timelogfun.add_job(msg[4],msg[2],msg[6],msg[8])
        elif(msg[1].lower()=='expense'):
            output=self.expense_management.create_expense(msg[3],msg[7],msg[5])
        return output

    def command_show(self,msg):
        if(msg[1].lower()=='employee'):
            output=self.timelogfun.all_employees()
        elif(msg[1].lower()=='jobs'):
            output=self.timelogfun.all_jobs(msg[3])
        elif(msg[1].lower()=='timelog'):
            output=self.timelogfun.get_timelog(msg[3],msg[5],msg[7])
        elif(msg[1].lower()=='tickets'):
            output=self.ticket_func.show_tickets()
        elif(msg[1].lower()=='departments'):
            output=self.ticket_func.show_departments()
        elif(msg[1].lower()=='customers'):
            output=self.ticket_func.show_customers()
        elif(msg[1].lower()=='covid' and msg[2].lower()=='cases'):
            rest = msg[4:] 
            sep = rest.index('in')
            district = ' '.join(rest[:sep])
            state = ' '.join(rest[sep+1:])
            output=covidcasesfun.cases(state,district)
        elif(msg[1].lower()=='expenses'):
            output=self.expense_management.list_expenses()
        elif(msg[1].lower()=='expense'):
            output=self.expense_management.list_expense_history(msg[2])
        elif(msg[1].lower()=='accounts'):
            output=self.expense_management.list_accounts()
        return output

    def command_search(self,msg):
        if(msg[1].lower()=='employee'):
            output=self.timelogfun.search_employee(msg[2])
        elif(msg[1].lower()=='expense'):
            output=self.expense_management.get_expense(msg[2])
        return output

    def command_change(self,msg):
        if(msg[1].lower()=='job'):
            output=self.timelogfun.change_job_status(msg[4],msg[6])
        elif(msg[1].lower()=='expense'):
            output=self.expense_management.update_expense(msg[2],msg[4],msg[6],msg[8])
        return output

    def command_create(self, msg):
        if(msg[1].lower() == 'ticket'):
            output = self.ticket_func.create_ticket(msg[3], msg[5], ' '.join(msg[7:]))
        return output

    def command_close(self, msg):
        if(msg[1].lower() == 'ticket'):
            output = self.ticket_func.close_ticket(msg[2])
        return output
            
    def command_delete(self,msg):
        if(msg[1].lower()=='expense'):
            output=self.expense_management.delete_expense(msg[2])
        return output
