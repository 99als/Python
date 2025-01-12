from math import cos, sin, radians

def triangle_legs(hyp, angle):
    adj = hyp * cos(radians(angle))
    opp = hyp * sin(radians(angle))
    if adj > opp:
        return (opp, adj)
    return (adj, opp)
