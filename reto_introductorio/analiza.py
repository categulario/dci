#!/usr/bin/env python3

if __name__ == '__main__':
    days = {str(i):0 for i in range(0, 8)}
    hours = {'{}:{}'.format(d, h):0 for d in range(0, 8) for h in range(0, 24)}
    directions = {'1': 0, '2': 0}

    # Things for weight measure
    wdays = {str(i):0 for i in range(0, 8)}
    whours = {'{}:{}'.format(d, h):0 for d in range(0, 8) for h in range(0, 24)}
    wdirections = {'1': 0, '2': 0}

    with open('data.csv', 'r') as datafile:
        next(datafile) # skip header

        for line in datafile:
            pieces = line.strip().split(',')
            day = pieces[3]
            hour = pieces[5]
            direction = pieces[4]
            unit = pieces[24]
            weight = pieces[25]

            days[pieces[3]] += 1
            hours['{}:{}'.format(day, hour)] += 1
            directions[direction] += 1

            # Now measure for weights
            if unit == 'TONELADAS':
                weight = float(weight)
                wdays[pieces[3]] += weight
                whours['{}:{}'.format(day, hour)] += weight
                wdirections[direction] += weight


    day, dcount = max(days.items(), key=lambda x:x[1])
    hour, hcount = max(filter(lambda x:x[0].startswith('5:'), hours.items()), key=lambda x:x[1])
    direction, rcount = max(directions.items(), key=lambda x:x[1])

    print("El día con más tráfico es {} con {} coches en suma".format(day, dcount))
    print('de ese día, las {} es la hora con más tráfico'.format(hour.split(':')[1]))
    print('El sentido {} es el más ocupado'.format(direction))
    print()

    day, dcount = max(wdays.items(), key=lambda x:x[1])
    hour, hcount = max(filter(lambda x:x[0].startswith('5:'), whours.items()), key=lambda x:x[1])
    direction, rcount = max(wdirections.items(), key=lambda x:x[1])
    
    print("El día con más peso es {} con {} toneladas en suma".format(day, dcount))
    print('de ese día, las {} es la hora más pesada'.format(hour.split(':')[1]))
    print('El sentido {} es el más ocupado'.format(direction))
