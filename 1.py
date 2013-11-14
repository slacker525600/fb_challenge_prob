first_example = """4
0 1 balance 1 on its left side # can have multiple balances ... 
0 2 balance 2 on its right side
0 
0 3 Balance 1 has balance 3 on its right side
'3' Balance 2 has three pounds on its left side
'0'
'0' Balance 3 has nothing on it
'0' Balance 3 has nothing on it"""

class scale(object):
  def __init__(self, nLeftWeight, anLeftScales, nRightWeight, anRightScales):
    self.left_weight  = nLeftWeight
    self.left_scales  = anLeftScales
    self.right_weight = nRightWeight
    self.right_scales = anRightScales
    self.balanced = False
    self.weight = 0 #all should weigh 10+ 0 level never needs to weigh self. 
    self.added = [0,0]
  def balance(self, acScales):
    #add to left or right depending on how much they weigh. 
    #ask them to weigh themselves
    self.balanced = True
  def weigh_self(self, acScales):
    if self.weight != 0:
      return self.weight
    if len(self.left_scales) + len(self.right_scales) > 0:
      nLeftScale = 0
      for nScale in self.left_scales: 
        nLeftScale += acScales[nScale].weigh_self(acScales)

      nRightScale = 0
      for nScale in self.right_scales:
        #have them weigh self. 
        nRightScale += acScales[nScale].weigh_self(acScales)

      #print(self.left_scales, nLeftScale, self.right_scales, nRightScale)
      self.left_weight += nLeftScale
      self.right_weight += nRightScale 
    #now have total weights. 
    nMax = max( self.left_weight, self.right_weight) 
    #print(nMax, self.left_weight, self.right_weight)
    self.add_weight(nMax - self.left_weight, nMax - self.right_weight) #add the difference
    #sides are [weight, scale]
    self.weight = nMax *2 + 10 #both sides now equal max
    #print(self.weight)
    return self.weight
  def add_weight(self, nLeft, nRight):
    self.added = [nLeft, nRight]
  def print_str(self):
    return str(self.added[0]) + ' ' + str(self.added[1])
#first number number of scales?

#
acScales = []

#asLines = sInput.split('\n')[1:] #remove first row, num rows gives enough info

sLeftScale = ''
nRange = int(raw_input())
for n in range(nRange*2): #sLine in asLines:
  if len(sLeftScale) > 0:
    #sLine is right scale
    #raw input will not work if newlines not observed. 
    asLeftLine =  sLeftScale.split(' ')
    asRightLine = str(raw_input()).split(' ')
    #print(map(int, asLeftLine[1:]))
    acScales.append(scale(int(asLeftLine[0] ), map(int, asLeftLine[1:]), 
                          int(asRightLine[0]), map(int, asRightLine[1:]) ) ) 
    sLeftScale = ''
  else:
    #sLine is left scale
    sLeftScale = str(raw_input())
  #acScales.append(       scale([int(raw_input()) , int(raw_input())], [int(raw_input()) , int(raw_input())])
    
#how to convert it to a height model. if nice, will already be in order.   
#acScales.sort('highest')

#assume sorted
nScalesCalced = 0
bNotDone = True
for sScale in acScales:
  #if (sScale.weight == 0):
  #  print(sScale.left_scales, sScale.right_scales, sScale.right_weight, sScale.left_weight, 
  sScale.weigh_self(acScales)
for nRow, sScale in enumerate(acScales):
  #print(sScale)
  print(str(nRow) +': ' + sScale.print_str())
