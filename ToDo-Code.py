Task_Description = input('Enter Task:')

Options = ('High', 'Low')

Priority = input(f'Pick from one of these{Options}: ')
Due_Date = input('Enter Date')

def Task_Entry():
    if Priority in Options:
        print('Succesfully Entered')
    else:
        Print('Invalid Entry Please Select Priority')

#i don't know why return isn't working i'll be back to look at it though
#return Priority

class Entry:
    def Data_Entry(Self,Task_Description,Priority,Due_Date):
        self.Task_Description = Task_Description
        self.Priority = Priority
        self.Due_Date = Due_Date

        print(f"You've Entered: Task_Description, Priority, Due_Date")
        




