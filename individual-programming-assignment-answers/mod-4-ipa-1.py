'''Module 4: Individual Programming Assignment 1

Parsing Data

This assignment covers your ability to manipulate data in Python.
'''

def relationship_status(from_member, to_member, social_graph):
    '''Relationship Status.
    20 points.

    Let us pretend that you are building a new app.
    Your app supports social media functionality, which means that users can have
    relationships with other users.

    There are two guidelines for describing relationships on this social media app:
    1. Any user can follow any other user.
    2. If two users follow each other, they are considered friends.

    This function describes the relationship that two users have with each other.

    Please see "assignment-4-sample-data.py" for sample data. The social graph
    will adhere to the same pattern.

    Parameters
    ----------
    from_member: str
        the subject member
    to_member: str
        the object member
    social_graph: dict
        the relationship data    

    Returns
    -------
    str
        "follower" if fromMember follows toMember,
        "followed by" if fromMember is followed by toMember,
        "friends" if fromMember and toMember follow each other,
        "no relationship" if neither fromMember nor toMember follow each other.
    '''
    # Replace `pass` with your code. 
    # Stay within the function. Only use the parameters as input. The function should return your answer.
    following_from_member=social_graph[from_member]["following"]
    following_to_member=social_graph[to_member]["following"]
    
    if from_member in following_to_member and to_member in following_from_member:
        return("friends")
    elif to_member in following_from_member:
        return("follower")
    elif from_member in following_to_member:
        return("followed by")
    else:
        return("no relationship")

def tic_tac_toe(board):
    '''Tic Tac Toe. 
    25 points.

    Tic Tac Toe is a common paper-and-pencil game. 
    Players must attempt to successfully draw a straight line of their symbol across a grid.
    The player that does this first is considered the winner.

    This function evaluates a tic tac toe board and returns the winner.

    Please see "assignment-4-sample-data.py" for sample data. The board will adhere
    to the same pattern. The board may by 3x3, 4x4, 5x5, or 6x6. The board will never
    have more than one winner. The board will only ever have 2 unique symbols at the same time.

    Parameters
    ----------
    board: list
        the representation of the tic-tac-toe board as a square list of lists

    Returns
    -------
    str
        the symbol of the winner or "NO WINNER" if there is no winner
    '''
    # Replace `pass` with your code. 
    # Stay within the function. Only use the parameters as input. The function should return your answer.
    
    # upper-left to lower-right
    diagonal_1=[board[i][i] for i in range(len(board))]
    diagonal_1 = set(diagonal_1)
    if len(diagonal_1)==1 and '' in diagonal_1: 
        diagonal_1.add("1")
        
    # lower-left to upper-right
    diagonal_2=[board[len(board)-1-i][i] for i in range(len(board))]
    diagonal_2 = set(diagonal_2)
    if len(diagonal_2)==1 and '' in diagonal_2: 
        diagonal_2.add("1")
    
    # horizontal
    horizontal=[]
    for i in board:
        horizontal += [set(i)]
    for i in horizontal:
        if {''} in horizontal:
            horizontal_set_index=horizontal.index({''})
            horizontal[horizontal_set_index].add("1")
    horizontal_bool=[]
    for i in horizontal:
        horizontal_bool.append(len(i)==1)
    
    # vertical
    vertical=[]
    vertical_list=[i for i in zip(*board)]
    for i in range(len(board)):
        vertical += [set(vertical_list[i])]
    for i in vertical:
        if {''} in vertical:
            vertical_set_index=vertical.index({''})
            vertical[vertical_set_index].add("1")
    vertical_bool=[]
    for i in vertical:
        vertical_bool.append(len(i)==1)
    
    # check
    if len(diagonal_1)==1:
        for i in diagonal_1:
            return(i)
    elif len(diagonal_2)==1:
        for i in diagonal_2:
            return(i)
    elif True in horizontal_bool:
        horizontal_index=horizontal_bool.index(True)
        for i in horizontal[horizontal_index]:
            return(i)
    elif True in vertical_bool:
        vertical_index=vertical_bool.index(True)
        for i in vertical[vertical_index]:
            return(i)
    else:
        return("NO WINNER")

def eta(first_stop, second_stop, route_map):
    '''ETA. 
    25 points.

    A shuttle van service is tasked to travel along a predefined circlar route.
    This route is divided into several legs between stops.
    The route is one-way only, and it is fully connected to itself.

    This function returns how long it will take the shuttle to arrive at a stop
    after leaving another stop.

    Please see "mod-4-ipa-1-sample-data.py" for sample data. The route map will
    adhere to the same pattern. The route map may contain more legs and more stops,
    but it will always be one-way and fully enclosed.

    Parameters
    ----------
    first_stop: str
        the stop that the shuttle will leave
    second_stop: str
        the stop that the shuttle will arrive at
    route_map: dict
        the data describing the routes

    Returns
    -------
    int
        the time it will take the shuttle to travel from first_stop to second_stop
    '''
    # Replace `pass` with your code. 
    # Stay within the function. Only use the parameters as input. The function should return your answer.
    stops_keys = [k for k in route_map.keys()]
    first_stops = [k[0] for k in stops_keys]
    second_stops = [k[1] for k in stops_keys]
    
    dict1_stop = first_stops.index(first_stop)
    dict2_stop = second_stops.index(second_stop)
    
    travel_time_list=[]
    for k in route_map.values():
        travel_time_list.append(k['travel_time_mins'])
    extended_travel_time_list=(travel_time_list+travel_time_list)
    
    if dict1_stop==dict2_stop:
        num=(list(route_map)[dict1_stop])
        return(int(route_map[num]['travel_time_mins']))
    elif dict1_stop < dict2_stop:
        condition2 = sum(travel_time_list[dict1_stop:dict2_stop+1])
        return(int(condition2))
    elif dict1_stop > dict2_stop:
        condition3 = sum(extended_travel_time_list[dict1_stop:len(travel_time_list)+dict2_stop+1])
        return(condition3)
    