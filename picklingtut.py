import pickle
# games = ['mario', 'poe', 'FF7', 1947]
file_name = 'gamespickle.pkl' #this file will get created automatically
# open_file_w = open(file_name, 'wb') #to open the created file name in write Binary
#pickle.dump(games, open_file_w) #pickling
# open_file_w.close() #now this file cannot be read from outside as it is in binary

#now we unpickle
open_file_r = open(file_name, 'rb') #open file in read
obatined_games = pickle.load(open_file_r)     #print the object
print(obatined_games)


