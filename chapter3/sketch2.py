import os
import pickle
os.chdir('C:\hub\pythontest\headfirstpython\chapter3')

man=[]
other=[]

try:
        data=open('sketch.txt')
        for each_line in data:
                try:
                        (role,line_spoken) = each_line.split(':',1)
                        line_spoken=line_spoken.strip()
                        if role=='Man':
                                man.append(line_spoken)
                        if role=='Other Man':
                                other.append(line_spoken)
                except ValueError:
                        pass
        data.close()
	
except IOError:
        print('the data file is missing!')
        

try:
        with open('man_data.txt','wb')as man_file:
                pickle.dump(man,man_file)
        with open('other_data.txt','wb')as other_file:
                pickle.dump(other,other_file)
                
except IOError as err:
        print('File error:'+str(err))
except PickleError as err:
        print('File error:'+str(err))
    
