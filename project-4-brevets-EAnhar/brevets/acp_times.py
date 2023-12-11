import arrow
minSpeedOnly = [15.0, 15.0, 15.0, 11.428, 13.333]
maxSpeedOnly = [34.0, 32.0, 30.0, 28.0, 26.0]

overall_time_limits = {
    200: (13, 30),
    300: (20, 0),
    400: (27, 0),
    600: (40, 0),
    1000: (75, 0)
}

def open_time(control_dist_km: float, brevet_dist_km: int, brevet_start_time: str) -> str:
    if brevet_dist_km < control_dist_km:
        control_dist_km = brevet_dist_km
    rawTime = timeCalculator(control_dist_km, maxSpeedOnly)
    finalTime = timeAdder(rawTime, brevet_start_time)
    return finalTime

def timeAdder(rawTime, initialTime):
    totMinutes = round(rawTime * 60)
    finalTime = arrow.get(initialTime).shift(minutes=+totMinutes).isoformat()
    return finalTime

def timeCalculator(kmGiven, speedTable):
    x = 0
    totTime = 0
    while kmGiven > 200:
        if x < 3:
            totTime = totTime + (200/speedTable[x])
            x += 1
            kmGiven = kmGiven - 200
        else:
            totTime = totTime + (200/speedTable[3])
            kmGiven = kmGiven - 200
    totTime = totTime + (kmGiven/speedTable[x])
    return totTime

def close_time(control_dist_km: float, brevet_dist_km: int, brevet_start_time: str) -> str:
    if brevet_dist_km < control_dist_km:
        control_dist_km = brevet_dist_km
    if control_dist_km == 0:
        finalTime = timeAdder(1, brevet_start_time)
        return finalTime
    elif control_dist_km in overall_time_limits:
        (hours, minutes) = overall_time_limits[control_dist_km]
        rawTime = hours + minutes / 60
    elif control_dist_km <= 60:
        rawTime = (control_dist_km / 20.0) + 1 
    else:
        rawTime = timeCalculator(control_dist_km, minSpeedOnly)
    
    finalTime = timeAdder(rawTime, brevet_start_time)
    return finalTime
