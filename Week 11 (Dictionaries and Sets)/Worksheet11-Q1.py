def is_capital(state, city):
    capitals = {'Victoria': 'Melbourne',
                'New South Wales': 'Sydney',
                'Queensland': 'Brisbane',
                'Tasmania': 'Hobart',
                'South Australia': 'Adelaide',
                'Western Australia': 'Perth'}

    if state in capitals.keys() and city in capitals.values():
        if capitals[state] == city:
            return True
        else:
            return False
    else:
        return False
