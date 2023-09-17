Due_Date = input('Enter Date: ')
Task_Description = input('Enter Task:')

Options = ('High', 'Low')

Priority = input(f'Pick from one of these{Options}: ')


def Task_Entry():
    if Priority in Options:
        print('Succesfully Entered')
    else:
        Print('Invalid Entry Please Select Priority')

#i don't know why return isn't working i'll be back to look at it though
#return Priority

#class Entry:
    #def Data_Entry(self,Task_Description,Priority,Due_Date):
     #   self.Task_Description = Task_Description
      #  self.Priority = Priority
       # self.Due_Date = Due_Date

        print(f"You've Entered: {self.Task_Description}, {self.Priority}, {self.Due_Date}")
        




