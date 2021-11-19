from sqlite3.dbapi2 import connect
from data import database_manager as dm
import utils 
from matplotlib import pyplot
from linear_algebra import curve_fitting as cf
from numpy import arange, greater
from scipy.optimize import curve_fit

#####################################the sqlite section#########################################

# create a connection to the database
connection = dm.create_connection("longley.db")
# To-Do : retrieve rows of the table 
ROWS=dm.select_all(connection)
print("here are the rows of your longley table")
dm.print_rows(ROWS)
print(len(ROWS))
dm.close_connection(connection) #close the connection to the db file

#####################################the data type section#######################################
data=utils.convert_to_floats(ROWS)
print(data) #to see the format 
#####################################the data shape##############################################
print("the shape of our data is :",data.shape)
#####################################the linear algebra section#################################

# Let's check if the two variables GNP.deflator and year  are correlated 
def objective(x, a, b):
    	return a * x + b
 
# load the dataset

x, y = data[:, 4], data[:, -1]

a, b=cf.get_result(x,y)

# plotting the result 
pyplot.scatter(x, y)
# define a sequence of inputs between the smallest and largest known inputs
x_line = arange(min(x), max(x), 1)
# calculate the output for the range
y_line = cf.set_objective(x_line, a, b)
# create a line plot for the mapping function
pyplot.plot(x_line, y_line, '--', color='red')
pyplot.show()
