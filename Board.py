from Hexagon import Hexagon
from TilePile import TilePile


class Board:
    def __init__(self):
        self.unplayedTiles = TilePile().getTiles()
        self.playedTiles = []
        self.board_hexagons = []
        self.tiles_on_the_board = []
        self.initialze_standard_board()
        self.possibleTiles = [[1,0],[1,1],[1,2],[17,0]]
        self.possibleTilesIndex = 0
        self.lastLocation = (100,100)

        

    def initialze_standard_board(self):
        # NOTE: Odd rows only have odd columns, even rows only have even columns
        '''
        This function will build out a standard board of 1830, it'll do so by categorizing each hex
        Categories include:
        -----------------------
            off_board_hexes
            
            on_board_hexes
    
            grey_hexes

            one_city_hexes
            
            two_city_hexes
            
            one_village_hexes
            
            two_villlage_hexes
            
            rr_start_hexes
        '''
        
        # ----- off_board_hexes -----
        self.off_board_hexes = [(1, 1), (1, 3), (1, 5), (1, 7), (1, 13), (1, 15), (1, 21), (1, 23),
                         (2, 2), (2, 4), (2, 6), (2, 8),
                         (3, 1), (3, 3), (3, 5),
                         (5, 1),
                         (7, 1), (7, 21), (7, 23),
                         (8, 20), (8, 22), (8, 24),
                         (9, 21), (9, 23),
                         (10, 16), (10, 18), (10, 20), (10, 22), (10, 24),
                         (11, 1), (11, 3), (11, 5), (11, 7), (11, 9), (11, 11), (11, 17), (11, 19), (11, 21), (11, 23)]
        
        # ----- on_board_hexes -----
        on_board_hexes = []
        for i in range(1, 12): # Rows A-K
            if i % 2 == 1:
                for j in range(1, 24, 2): # Add all valid hexes in odd rows (ones that aren't in off_board_hexes)
                    if((i, j) not in self.off_board_hexes):
                        on_board_hexes.append((i, j))
            else:
                for j in range(2, 25, 2): # Add all valid hexes in even rows (ones that aren't in off_board_hexes)
                    if((i, j) not in self.off_board_hexes):
                        on_board_hexes.append((i, j))
        
        # ----- grey_hexes -----
        grey_hexes = [(1, 17), (1, 19),
                      (3, 15),
                      (4, 2), (4, 14), (4, 24),
                      (5, 9),
                      (6, 6), (6, 24),
                      (8, 12),
                      (9, 19),
                      (11, 15)]
        
        # ----- one_city_hexes -----
        one_city_hexes = [(1, 19),
                          (2, 10), (2, 16),
                          (4, 2), (4, 14),
                          (5, 19), (5, 23),
                          (6, 4), (6, 6), (6, 16), (6, 22),
                          (8, 4), (8, 10), (8, 12), (8, 16),
                          (9, 15),
                          (10, 14),
                          (11, 15)]
        
        # ----- two_city_hexes -----
        two_city_hexes = [((4, 10), "OO"),
                          ((5, 5), "OO"), ((5, 11), "OO"),
                          ((7, 19), "NY"),
                          ((8, 18), "OO")]
        
        # ----- one_village_hexes -----
        one_village_hexes = [(2, 20),
                             (3, 15),
                             (4, 4),
                             (5, 7),
                             (6, 10), (6, 24),
                             (9, 19)]
        
        # ----- two_vilage_hexes -----
        two_village_hexes = [(6, 20),
                             (7, 7), (7, 17)]
        
        # ----- rr_start_hexes -----
        rr_start_hexes = [((1, 19), "Canadian Pacific RR"),
                          ((5, 11), "Erie RR"), ((5, 19), "New York Central RR"), ((5, 23), "Boston & Maine RR"),
                          ((6, 6), "Chesapeake & Ohio RR"),
                          ((7, 19), "New York & New Haven RR"),
                          ((8, 12), "Pennsylvania RR"),
                          ((9, 15), "Baltimore & Ohio RR")]
        
        # ----- entryExitStation -----
        # (row, column), [[entry, exit, station]] exit == 0 for no exit, station == 0 for blank station, station == 10 no station
        entryExitStationList = [((1,9), [[3,0,10]]), ((1,11), [[3,0,10],[4,0,10]]),  ((1,17),[[3,4,10]]), ((1,19), [[3,4,0]]),
                            ((2,24), [[4,0,10], [5,0,10]]),
                            ((3,15), [[1,5,10]]),
                            ((4,2), [[2,3,0]]), ((4,14), [[2,5,0], [2,4,0], [4,5,0]]), ((4,24),[[4,5,10]]),
                            ((5,9), [[6,1,10]]), ((5,19), [[0,0,0]]), ((5,23), [[1,3,0]]),
                            ((6,2),[[1,0,10], [2,0,10], [3,0,10]]), ((6,6), [[3,4,0]]), ((6,24),[[5,6,10]]),
                            ((7,19), [[1,0,0], [4,0,0]]),
                            ((8,12), [[2,5,0], [2,5,10]]),
                            ((9,1),[[2,0,10]]), ((9,15), [[2,4,0]]), ((9,19), [[5,6,10]]),
                            ((10,2), [[1,0,10], [2,0,10]]), 
                            ((11,13), [[1,0,10], [6,0,10]]), ((11,15), [[6,0,0]])
            ]
        # ----- voidSides_hexes -----
        # (row, column), [void sides]
        voidSidesList = [((2,10),[5]), ((2,12),[1]), ((2,14),[1,6]), ((2,16),[6]), ((2,20), [1]), ((2,22), [1,6]),
                     ((3,7), [1,4,5,6]), ((3,9), [6]), ((3,11), [3]), ((3,13), [3,4]), ((3,17), [5,6]), ((3,23), [2]),
                     ((4,2), [4,5,6,1]), ((4,4),[1,6]), ((4,6), [1,6]), ((4,12), [1,6]), ((4,14), [1,6]), ((4,16), [6]), 
                     ((5,3), [5]), ((5,5), [3]), ((5,7), [2,3,4]), ((5,11), [5]), ((5,23), [2]),
                     ((6,4), [2]), ((6,8), [1,5,6]), ((6,10), [6]), ((6,20), [3]), ((6,22), [3,4]),
                     ((7,3), [5]), ((7,19), [2,3]),
                     ((8,2),[4,5,6]), ((8,18), [2]),
                     ((9,15),[3]), ((9,17), [3,4]),
                     ((10,4), [3,4]), ((10,6), [3,4]), ((10,8), [3,4]), ((10,10), [3,4]), ((10,12), [4]), ((10,14), [2]),
                     ((11,15), [1,2,3,4,5])
            ]
        
        # ----- hexTile -----
        hexTile = None

        # Create the hexagon objects
        for hex in on_board_hexes:
            #-----Hex ID-----
            hex_id = hex
            
            #-----Village Count-----
            if(hex in one_village_hexes):
                vil_count = 1
            elif(hex in two_village_hexes):
                vil_count = 2
            else:
                vil_count = 0
            
            #-----City Count-----
            hex_city_count_ind = None
            
            if(hex in one_city_hexes): # Case for checking if there is only one city
                city_count = 1
            else: # Case hit for two cities or no cities
                for ind, item in enumerate(two_city_hexes): # Find if there is matching hex and get its ind
                    if(item[0] == hex):
                        hex_city_count_ind = ind
                        break
                if hex_city_count_ind is None: # If there was no match, then city_count is 0
                    city_count = 0
                else:
                    city_count = two_city_hexes[hex_city_count_ind][1] # If there are two cities, then return OO or NY
            
            #-----Color-----
            if(hex in grey_hexes):
                color = "grey"
            else:
                color = "blank"
        
            #-----Railroad Start-----
            hex_rr_ind = None
            for ind, item in enumerate(rr_start_hexes):
                if(item[0] == hex):
                    hex_rr_ind = ind
                    break
            if hex_rr_ind is None:
                rr_start = ""
            else:
                rr_start = rr_start_hexes[hex_rr_ind][1]
                
            #-----EntryExitStation-----
            entryExit = None
            for item in entryExitStationList:
                if item[0] == hex:
                    entryExit = item[1]
                    break
            if entryExit is None:
                entryExitStation = []
            else:
                entryExitStation = entryExit
            
            #-----VoidSides-----
            hexVoidSides = None
            for item in voidSidesList:
                if item[0] == hex:
                    hexVoidSides = item[1]
                    break
            if hexVoidSides is None:
                voidSides = []
            else:
                voidSides = hexVoidSides
            
            #-----HexTile-----
        
            # Initialize the hex object
            hex_to_append = Hexagon(hex_id, vil_count, city_count, color, rr_start, entryExitStation, voidSides, hexTile)
            self.board_hexagons.append(hex_to_append)

    def print_board(self):
        for a_hex in self.board_hexagons:
            print(a_hex.hex_id, "v =", a_hex.vil_count, "c =", a_hex.city_count, "col = ", a_hex.color, "ees =", a_hex.entryExitStation, "hv =", a_hex.voidSides, "t =", a_hex.hexTile,  a_hex.rr_start)
            print("---------------")  
        foundTile = self.checkThroughUnplayedTiles(57)
        print("Found Tile " + str(foundTile.tile_id))
            
     
    # This method take in information from the GUI and returns tiles that can be played 
    def checkForPlayableTile(self, location, company, trainList, newStation):
        # this is a list of the hexes rail spurs around the location with the correcponding side of the location in that direction
        # for example the first hex returned by findAdjacentHexes is above and to the left, if that hex has a rail on
        # side 3 then that correspnds to side 6 on the location hex [(3,6), ...]
        listOfPairedSides = [(3,6),(4,1),(2,5),(5,2),(1,4),(6,3)]   # top left, top right, left, right, lower left, lower right
        self.possibleTiles = []
        railInDirection = []
        hexList = self.findAdjacentHexes(location)
        self.lastLocation = location
        
        # check for rail lines leading into hex
        index = 0
        for hex in hexList:
            hexObject = self.findHex(hex) 
            print(hexObject)
            if hexObject is not None: 
                for loc in hexObject.entryExitStation:
                    # [[3,0,10],[4,0,10]]
                    entrySide = loc[0]
                    exitSide = loc[1]
                    print("entry=" + str(entrySide) + " exit=" + str(exitSide) + " index=" + str(index))
                    if entrySide == listOfPairedSides[index][0] or exitSide == listOfPairedSides[index][0]:
                        if listOfPairedSides[index][1] not in railInDirection:
                            railInDirection.append(listOfPairedSides[index][1])
            index +=1
            
        # check for void sides on the location hex
        locationHex = self.findHex(location)
        print("Location Hex at memory location: " + str(locationHex))
        voidInDirection = []
        voidInDirection = locationHex.voidSides
        print("Hex Current Tile = " + str(locationHex.hexTile))
        print ("Void sides = " + str(voidInDirection))
        print("CityCount = " + str(locationHex.city_count))
        possibleTiles = []
        if locationHex.hexTile is None:       # hex with no tile to upgrade
            if railInDirection:
                startTiles = [1, 2, 3, 4, 7, 8, 9, 55, 56, 57, 58, 69]
                
                for tileNumber in startTiles:
                    testTile = self.checkThroughUnplayedTiles(tileNumber) 
                    if testTile.city_count == locationHex.city_count and testTile.village_count == locationHex.vil_count:
                        possibleTiles.append(tileNumber)
                        print(str(len(testTile.path_pairs)))
                print(possibleTiles)
            
        else:                               # hex with tile associated with it
            possibleTiles = location.upgrade_list
            
        # this section looks through each tile in possibleTiles and selects and rotates the legal placements
        for tTile in possibleTiles:                                         # look through each possible tile number
            tile = self.checkThroughUnplayedTiles(tTile)                    # get the tile object for that number
            print(tile)
            print(tile.path_pairs)
            print(len(tile.path_pairs))
            
            pairList = []                                                   # make a list of all teh tuple values for pair sides
            for ee in range (len(tile.path_pairs)):
                for i in range(2):
                    pairList.append(tile.path_pairs[ee][i])
            print(pairList)
            
            for hexRailDirection in railInDirection:                        # look at each hex side that faces a rail
                for eeSide in pairList:                                     # look at each enrty/exit side on the tile
                    validRotation = True                                        # flag to tell if the rotation being tested is valie
                    offset = hexRailDirection - eeSide                      # find the number of rotation steps needed to line up the rails
                    if offset < 0:                                          # tile entry/exit is left of hex rail direction
                        offset += 6  
                    for testSide in pairList:                               # go through each of the tile rail sides
                        if testSide == eeSide:                              # if the side is the one that set the rotation, skip it
                            continue
                        newTestSide = testSide + offset                     # rotate the test side to match the tile rotation
                        if newTestSide > 6:
                            newTestSide -=6
                        if newTestSide in locationHex.voidSides:            # check if that rotated side is lined up with a hex void side
                            validRotation = False                           # if so set the flag to exclude this rotation for the tile
                    if validRotation == True:
                        self.possibleTiles.append((tile.tile_id, offset))   # add the tile number and rotation to the list
                    
            '''
            for hexRailDirection in railInDirection:                        # look at each hex side that faces a rail
                for j in range(len(tile.path_pairs)):
                    for i in range(2):                                      # tiles have pairs of connected sides so need 0 and 1
                        print(tile.path_pairs[j][i])
                        offset = hexRailDirection - int(tile.path_pairs[j][i])
                        if offset < 0:                                      # tle entry/exit left of hex rail direction
                            offset += 6                                     # adding 6 will make the neg pos ie -1 -> +5
                        if i == 0:                                          # if dealing with the first value in e/e pair
                            tileExitSide = int(tile.path_pairs[j][1] )           # get the exit side
                            newExit = tileExitSide + offset                 # rotate the exit side by the offset
                            if newExit > 6:                                 # if rotating pushes the side past six then...
                                newExit -=6                                 # subtract 6 ie 8 -> 2
                            if newExit not in locationHex.voidSides:        # if the newExit is not pointing to a hex void side
                                self.possibleTiles.append((tile.tile_id, offset))   # add the tuple of tile # and rotation to possibleTiles
                        else:
                             tileExitSide = int(tile.path_pairs[j][0])              # get the exit side
                             newExit = tileExitSide + offset                # rotate the exit side by the offset
                             if newExit > 6:                                # if rotating pushes the side past six then...
                                 newExit -=6                                # subtract 6 ie 8 -> 2
                             if newExit not in locationHex.voidSides:       # if the newExit is not pointing to a hex void side
                                 self.possibleTiles.append((tile.tile_id, offset))   # add the tuple of tile # and rotation to possibleTiles
            '''           
        return self.possibleTiles
        
    
    # method to find hexes that surround the target hex
    def findAdjacentHexes(self, location):
        testList = []
        hexList = []
        locationFirst = location[0]
        locationSecond = location[1]
        # find the hexes around the location hex
        if locationFirst > 1:               # get tiles above
            if locationSecond > 1:          # get above and left
                testList.append((locationFirst - 1, locationSecond - 1))
            if locationSecond < 24:         # get above and right
                testList.append((locationFirst - 1, locationSecond + 1))
        if locationSecond >1:               # get left
            testList.append((locationFirst, locationSecond - 2))
        if locationSecond < 24:             # get right
            testList.append((locationFirst, locationSecond + 2))
        if locationFirst < 15:              # get tiles below 
            if locationSecond > 1:          # below and left
                testList.append((locationFirst + 1, locationSecond - 1))
            if locationSecond < 24:         # below and right
                testList.append((locationFirst + 1, locationSecond + 1))
        for loc in testList:
            if loc not in self.off_board_hexes:
                hexList.append(loc)
            else:
                hexList.append((0,0))
        return hexList
        
    
    def findHex(self, id):
        print("id = " + str(id))
        for hexObj in self.board_hexagons:
            if hexObj.hex_id == id:
                return hexObj    #return the hex upon a match
        return None     #If there was no match, return None
        
    def checkThroughUnplayedTiles(self, targetTile):
        ind = 0
        while ind < len(self.unplayedTiles):
            if self.unplayedTiles[ind].tile_id == targetTile:
                print(str(targetTile) + " targetTile cc = " + str(self.unplayedTiles[ind].city_count))
                return self.unplayedTiles[ind]
            else:
                ind += 1

























