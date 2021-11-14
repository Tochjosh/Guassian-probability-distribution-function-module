# Guassian probability Distribution Function Module

This module is a statistical tool for calculations involving the Guassian probability distribution function

This module contain the following methods:

###**read_data_file(file_name, sample=True)**
This method reads in the data from a txt file, and calculates the mean and standard deviation of the data set. The sample arguments is set to True by default, but should be set to False if working with a population data set.

###**calculate_mean()**
This method takes no parameter and returns the mean of the data set.

###**calculate_stand_dev(sample=True)**
This method takes a default sample parameter that is set to true by default. Sample should be set to false when working with a population data set.

### **plot_histogram()**
This method plots a histogram of the data set. It takes no parameter.

###**pdf()**
This method calculates and returns the probability distribution function of the data set. It takes no parameter.

###**plot_histogram_pdf(n_space=50)**
This method takes the number of space as a parameter. The space number is set to 50 by default. The method plots a histogram for the probability distribution function function.

The addition operation magic method has been overridden to allow the addition of two or more guassian objects.
 