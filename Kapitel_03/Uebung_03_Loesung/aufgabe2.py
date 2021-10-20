# Aufgabe 2

def check_longitude(val):
    if (val > 180) or (val < -180):
        print(f"The longitude value {val} either too small or too large."
               " Wrapping it into the interval [-180, 180]")
    
    # modulo trick
    new_val = (180 + val) % 360 - 180
    
    # by the above formula the values for 180, 3*180, 5*180, ... 
    # are always -180 instead of 180 (which in this case is the same anyway)
    # we can fix these special cases:
    div, mod = divmod(val, 180)   
    if (val > 0) and (mod == 0) and (div % 2 == 1):   # check: div is odd and no remainder (mod = 0) 
        new_val = 180
    
    return new_val

def check_latitude(val):
    if (val > 90) or (val < -90):
        print(f"The latitude value {val} either too small or too large."
              " Wrapping it into the interval [-90, 90]")
    
    new_val = (90 + val) % 180 - 90
    
    div, mod = divmod(val, 90)
    if (val > 0) and (mod == 0) and (div % 2 == 1):
        new_val = 90
    
    return new_val


class WGS84Coord:
    def __init__(self, longitude=0, latitude=0):
        self.longitude = longitude
        self.latitude = latitude


    def _set_longitude(self, longitude):
        self._longitude = check_longitude(longitude)

    def _get_longitude(self):
        return self._longitude


    def _set_latitude(self, latitude):
        self._latitude = check_latitude(latitude)
        
    def _get_latitude(self):
        return self._latitude

    longitude = property(_get_longitude, _set_longitude)
    latitude = property(_get_latitude, _set_latitude)


if __name__ == '__main__':
    P1 = WGS84Coord(575, -320)
    print(P1.longitude)
    print(P1.latitude)