players = ['Lara', 'Williams', 'John']
games = ('Cricket', 'NBA', 'Football')

z = zip(players,games)
#print(z) #<zip object at 0x01EFA0E8>
print(list(z)) #[('Lara', 'Cricket'), ('Williams', 'NBA'), ('John', 'Football')]

countries = ['WI', 'USA', 'UK']
z1 = tuple(zip(players,games,countries))
print(z1) #(('Lara', 'Cricket', 'WI'), ('Williams', 'NBA', 'USA'), ('John', 'Football', 'UK'))

#use case - 
#person table, address in contact table, salary 

#unzipping
p,g,c = zip(*z1)
print(p)
print(g)
print(c)




