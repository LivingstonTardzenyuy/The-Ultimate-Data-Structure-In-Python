#updatingAndDeleting

names=["Kongyuy","Joel","Serge","Betrand"]
print(names)

#updating a list in python we use index. the time and space complecty here is 0[1]
names[0]="Updated Kongnyuy"
names[3]="Wirba Betrand"
print(names)


#Inserting in a list we can use Insert(), append()
#with the append we can only insert at the end of the list and it takes only one argurment with no index provided

names.insert(0,"Gracious")
names.append("Collins")
names.insert(3,"Clovis")

print(names) 