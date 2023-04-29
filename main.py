# Python version 3.10

import csv,os,sys

folder_path = sys.argv[-1]

class merge_csv():
    def __init__(self,mapping_value,file_path):
        self.map_by       = mapping_value
        self.csv_filename = file_path
        self.csv_files = []
        for files in os.listdir(folder_path):
            self.csv_files.append(csv.DictReader(open(os.path.join(folder_path,files), "r")))
    
    def convert_to_csv(self):
        ''' This function will convert list of dictionary data into csv file '''
        keys = self.final_data[0].keys()
        with open(self.csv_filename, 'w', newline='') as output_file:
            dict_writer = csv.DictWriter(output_file, keys)
            dict_writer.writeheader()
            dict_writer.writerows(self.final_data)
        print('file created as '+file_path)
      
    def map_data(self):
        ''' This function will convert csv data into dictionary format '''
        data_mapped = {}
        for csv_file in self.csv_files:
            while True:
                try:
                    csv_data = next(csv_file)
                    index_value=csv_data[self.map_by]
                    if index_value in data_mapped:
                        data_mapped[index_value].update(csv_data)
                    else:
                        data_mapped[index_value] = csv_data
                except:
                    break
        self.final_data = list(data_mapped.values())

if __name__ == '__main__':
    mapping_value = 'Subject Number' # Column to be related with
    file_path     = 'result.csv' # Path in which final data should be
    obj = merge_csv(mapping_value,file_path)     
    obj.map_data()
    obj.convert_to_csv()


        
