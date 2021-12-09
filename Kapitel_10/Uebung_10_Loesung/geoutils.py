import warnings
warnings.simplefilter('always', UserWarning)


def check_longitude(lon):
    if not (-180 <= lon <= 180):
        warnings.warn(f"The longitude value {lon} either too small or too large."
                       " Wrapping it into the interval [-180, 180]")
    
    # 1) transform values so that [-180,180] --> [0, 360]
    # 2) modulo with 360
    # 3) undo the first transformation
    new_lon = (180 + lon) % 360 - 180
    
    # this solution converts 180, 180+360, 180+(2*360), ...
    # to -180 which is actually the same, but we can handle this:
    div, mod = divmod(lon, 180)   
    if (lon > 0) and (mod == 0) and (div % 2 == 1): 
        new_lon = 180
    
    return new_lon


def check_latitude(lat):
    if not (-90 <= lat <= 90):
        warnings.warn(f"The latitude value {lat} either too small or too large."
                       " Wrapping it into the interval [-90, 90]")
    
    new_lat = (90 + lat) % 180 - 90
    
    div, mod = divmod(lat, 90)
    if (lat > 0) and (mod == 0) and (div % 2 == 1):
        new_lat = 90
    
    return new_lat