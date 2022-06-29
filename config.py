def config():

    """Retrieves input information from the user and constructs URLs.

    Football season year and week are obtained from the user. 
    Team position numbers are also obtained, then constructed
    into URLs depending on league scoring configuration. Lists 
    of position slot numbers, URLs, and total points per position 
    are organized into Python lists and passed into the 
    collectData function.

    Args:
        None

    Returns:
        configList: Python list that contains the year, week, scoring type, and position slots for the fantasy team.
        urlList: Python list that contains the URLs specific to each position.
        ptsList: Python list that contains the total points scored by the fantasy team's positions.
        playerNameList: Empty Python list that is initialized for use in collectData().
    """

    # grabbing user input for year, week, scoring preference, and number of players for each position
    year = input("Please input the year you are looking for.\n")
    week = input("Please input the week you are looking for.\n")
    qb = input("How many quarterback slots?\n")
    rb = input("How many runningback slots?\n")
    wr = input("How many wide receiver slots?\n")
    te = input("How many tight end slots?\n")
    flex = input("How many flex (WR/RB/TE) slots?\n")
    k = input("How many kicker slots?\n")
    defense = input("How many team defense slots?\n")
    scoring = input("Standard or PPR scoring? Please type out 'standard' or 'ppr'.\n")

    if scoring.lower() == 'ppr':
        # concatenating and grabbing url string for PPR scoring
        url = 'https://www.footballguys.com/playerhistoricalstats?pos=qb&yr=' + year + '&startwk=' + week + '&stopwk=' + week + '&profile=p'
        rburl = 'https://www.footballguys.com/playerhistoricalstats?pos=rb&yr=' + year + '&startwk=' + week + '&stopwk=' + week + '&profile=p'
        wrurl = 'https://www.footballguys.com/playerhistoricalstats?pos=wr&yr=' + year + '&startwk=' + week + '&stopwk=' + week + '&profile=p'
        teurl = 'https://www.footballguys.com/playerhistoricalstats?pos=te&yr=' + year + '&startwk=' + week + '&stopwk=' + week + '&profile=p'
        flexurl = 'https://www.footballguys.com/playerhistoricalstats?pos=flex&yr=' + year + '&startwk=' + week + '&stopwk=' + week + '&profile=p'
        kurl = 'https://www.footballguys.com/playerhistoricalstats?pos=pk&yr=' + year + '&startwk=' + week + '&stopwk=' + week + '&profile=p'
        defurl = 'https://www.footballguys.com/playerhistoricalstats?pos=td&yr=' + year + '&startwk=' + week + '&stopwk=' + week + '&profile=p'
    else:
        # concatenating and grabbing url string for standard scoring
        url = 'https://www.footballguys.com/playerhistoricalstats?pos=qb&yr=' + year + '&startwk=' + week + '&stopwk=' + week + '&profile=0'
        rburl = 'https://www.footballguys.com/playerhistoricalstats?pos=rb&yr=' + year + '&startwk=' + week + '&stopwk=' + week + '&profile=0'
        wrurl = 'https://www.footballguys.com/playerhistoricalstats?pos=wr&yr=' + year + '&startwk=' + week + '&stopwk=' + week + '&profile=0'
        teurl = 'https://www.footballguys.com/playerhistoricalstats?pos=te&yr=' + year + '&startwk=' + week + '&stopwk=' + week + '&profile=0'
        flexurl = 'https://www.footballguys.com/playerhistoricalstats?pos=flex&yr=' + year + '&startwk=' + week + '&stopwk=' + week + '&profile=0'
        kurl = 'https://www.footballguys.com/playerhistoricalstats?pos=pk&yr=' + year + '&startwk=' + week + '&stopwk=' + week + '&profile=0'
        defurl = 'https://www.footballguys.com/playerhistoricalstats?pos=td&yr=' + year + '&startwk=' + week + '&stopwk=' + week + '&profile=0'

    # initializing each variable for points scored by each position to zero before returning
    qbPts, rbPts, wrPts, tePts, flexPts, kPts, defPts = 0, 0, 0, 0, 0, 0, 0

    # initializing each list
    configList, urlList, ptsList = [year, week, qb, rb, wr, te, flex, k, defense, scoring], [url, rburl, wrurl, teurl, flexurl, kurl, defurl], [qbPts, rbPts, wrPts, tePts, flexPts, kPts, defPts]
    playerNameList = []

    return configList, urlList, ptsList, playerNameList