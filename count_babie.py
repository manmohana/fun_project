
import glob
import pandas as pd

class Count(object):

    def __init__(self, name):
        self.name = name

    def get_file_names(self):
        '''
        returns list of fiile_names
        '''
        lst_file = sorted(glob.glob('baby_names/*.txt'))
        return lst_file

    def read_file(self, file_name):
        '''
        reads the file and returns tuple (year, female_babies, male_babies)
        '''
        year = int(filter(str.isdigit, file_name))
        data = pd.read_csv(file_name, sep=",", header=None)
        data = data.set_index([0])
        data = data.loc[self.name].values.tolist()
        return year, data[0][1], data[1][1]

    def get_popularity_trend(self):
        '''
        Returns 2 lists of tuples with year and gender wrt Name.
        One list per Gender
        '''
        m_list = []
        f_list = []
        all_files = self.get_file_names()
        data = map(self.read_file, all_files)
        for i in data:
            f_list.append((i[0], i[1]))
            m_list.append((i[0], i[2]))
        return m_list, f_list

if __name__ == '__main__':
    print Count('Benjamin').get_popularity_trend()
