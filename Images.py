def Images(element, w_type, bonus):
    if bonus == 0:
        bonus = 'simple'
        image = 'images/{0}/{1}/a.png'.format(w_type, bonus)
    else:
        image = 'images/{0}/{1}/a.png'.format(w_type, bonus[:-1])
    return image




