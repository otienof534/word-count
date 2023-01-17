import pandas as pd
my_file = pd.read_csv(r'C:\Users\USER\OneDrive\Desktop\csvfile.txt')
my_file1 = my_file['Article']
splitted = my_file1.apply(lambda i : len(i.split()))
my_file.insert(2,'counts',splitted)
print(my_file)
