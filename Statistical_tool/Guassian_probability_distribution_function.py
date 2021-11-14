import math
import matplotlib.pyplot as plt


class Gaussian:
    """ Gaussian distribution class for calculating and
    visualizing a Gaussian distribution.

    Attributes:
        mean: (float) representing the mean value of the distribution
        stand_dev: (float) representing the standard deviation of the distribution
        data: (list of floats) a list of floats extracted from the data file

    """

    def __init__(self, mu=0, sigma=1):

        self.mean = mu
        self.stand_dev = sigma
        self.data = []

    def calculate_mean(self):

        """Function to calculate the mean of the data set.

        Returns:
            float: mean of the data set
        """

        self.mean = 1.0 * sum(self.data) / len(self.data)
        return self.mean

    def calculate_stand_dev(self, sample=True):

        """Function to calculate the standard deviation of the data set.

        Args:
            :param sample: A bool value that shows if its a sample or population data set

        Returns:
            float: standard deviation of the data set

        """

        if sample:
            n = len(self.data) - 1
        else:
            n = len(self.data)

        sigma = 0
        for i in self.data:
            sigma += (i - self.mean) ** 2

        self.stand_dev = math.sqrt(sigma / n)
        return self.stand_dev

    def read_data_file(self, file_name, sample=True):

        """Function to read in data from a txt file.
        File should have one number (float) per line.
        The numbers are stored in the data attribute.
        After reading in the file, the mean and standard deviation are calculated

        Args:
           :param file_name: name of file containing data list
           :param sample: A bool value that shows if its a sample or population data set

        Returns:
            None

        """

        with open(file_name) as file:
            data_list = []
            line = file.readline()
            while line:
                data_list.append(int(line))
                line = file.readline()
        file.close()

        self.data = data_list
        self.mean = self.calculate_mean()
        self.stand_dev = self.calculate_stand_dev(sample)

    def plot_histogram(self):
        """Function to output a histogram of the instance variable data using
        matplotlib pyplot library.

        Returns:
            None
        """
        plt.hist(self.data)
        plt.title('Histogram of a the data against the frequency')
        plt.xlabel('data')
        plt.ylabel('frequency')

    def pdf(self, x):
        """Probability density function calculator for the gaussian distribution.

        Args:
            :param: A float point for calculating the probability density function

        Returns:
            float: probability density function output
        """
        numerator = 1.0 * math.exp(-0.5 * ((x - self.mean) / self.stand_dev) ** 2)
        denominator = (self.stand_dev * math.sqrt(2 * math.pi))
        return numerator / denominator

    def plot_histogram_pdf(self, n_spaces=50):

        """Function to plot the normalized histogram of the data and a plot of the
        probability density function along the same range

        Args:
           :param n_spaces: int  number of data points

        Returns:
            list: x values for the pdf plot
            list: y values for the pdf plot

        """

        min_range = min(self.data)
        max_range = max(self.data)

        # calculates the interval between x values
        interval = 1.0 * (max_range - min_range) / n_spaces

        x = []
        y = []

        # calculate the x values to visualize
        for i in range(n_spaces):
            tmp = min_range + interval * i
            x.append(tmp)
            y.append(self.pdf(tmp))

        # make the plots
        fig, axes = plt.subplots(2, sharex=True)
        fig.subplots_adjust(hspace=.5)
        axes[0].hist(self.data, density=True)
        axes[0].set_title('Normed Histogram of Data')
        axes[0].set_ylabel('Density')

        axes[1].plot(x, y)
        axes[1].set_title('Normal Distribution for \n Sample Mean and Sample Standard Deviation')
        axes[0].set_ylabel('Density')
        plt.show()

        return x, y

    def __add__(self, other):

        """Function to add together two Gaussian distributions

        Args:
            :param other (Gaussian): Gaussian instance

        Returns:
            Gaussian: Gaussian distribution

        """

        result = Gaussian()
        result.mean = self.mean + other.mean
        result.stand_dev = math.sqrt(self.stand_dev ** 2 + other.stand_dev ** 2)
        return result

    def __repr__(self):

        """Function to output the characteristics of the Gaussian instance

        Args:
            None

        Returns:
            string: characteristics of the Gaussian

        """
        return "mean {}, standard deviation {}".format(self.mean, self.stand_dev)
