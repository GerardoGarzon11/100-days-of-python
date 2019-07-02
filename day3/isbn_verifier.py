def verify(isbn):
    _isbn = [x for x in isbn if x.isdigit() or x == 'X']
    
    if len(_isbn) != 10 :
    	return False
    elif _isbn[9] != 'X' and not _isbn[9].isdigit() :
    	return False
    elif 'X' in _isbn[0:9] :
    	return False
    elif _isbn[9] == 'X' :
    	_isbn[9] = '10'

    _isbn = list(map(int,_isbn))

    return (_isbn[0] * 10 + _isbn[1] * 9 + _isbn[2] * 8 + _isbn[3] * 7
    	+_isbn[4] * 6 + _isbn[5] * 5 + _isbn[6] * 4 + _isbn[7] * 3
    	+_isbn[8] * 2 + _isbn[9] * 1) % 11 == 0
