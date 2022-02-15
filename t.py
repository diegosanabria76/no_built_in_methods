class my_stats:
    '''Class my_stats, is made out of  4 methods,
    that can calculate basic statistics formulas like mean, variance, standard deviation.
    '''
    def mean(self,list):
        '''This method requires a list variable as a parameter,
        then is going to do a for loop to sum items and count them.
        then calculate their average.
        '''
        sum = 0
        counter = 0

        for i in list:
            sum += i
            counter += 1

        mean= sum/counter
        return mean
    def user_input(self):
        '''This method does not requiere any argument,
        it is meant to generate a list of number from user input.'''
        list = []
        n = int(input("How many numbers do you want to enter ?"))

        for i in range(0,n):
            num = int(input("please enter a number"))
            list.append(num)
        return list

    def variance(self, data):
        """This method accepts a list the use 2 for loops, then  doing  some calculations
        and finally return variance

        """
        n = len(data)
        list = []
        av = self.mean(data)
        sum = 0
        for i in range(len(data)):
            data[i] = (data[i] - av)**2
            list.append(data[i])

        for i in list:
            sum += i
        variance = sum / (n-1)
        return variance
    def s_d(self, variance):
        '''This method requieres a variance
        then calculates the square root of that value to return, the standard deviation.
        '''
        sd = variance**(1/2)
        return sd
