class pix(object):
    def __init__(self):
        self.nPixels = 8

    # set-up starting state
    def start(self, conditions, colourDict, fixedBrightness, minBrightness, maxBrightness, conditionsDict):
        import random

        ## set variables internal to pix object
        self.maxBrightness = maxBrightness
        self.minBrightness = minBrightness
        self.increment = maxBrightness
        self.decrement = -1 * maxBrightness/10

        ## get pixel colours and intervals using weather conditions report
        weather = []
        for i in range(self.nPixels):
            weather.append({ 'colour' : 'white', 'interval': 0})
        for v in ['colour', 'interval']:
            weather[0][v] = conditionsDict[conditions['weather']][v]
            for i in range(self.nPixels-1):
                weather[i+1][v] = conditionsDict[conditions['forecast'][i]][v]

        ## set colours, intervals, starting brightnesses and number of flashing pixels
        self.intervals = []
        self.colours = []
        self.brightnesses = []
        self.nFlash = 0
        for w in weather:
            self.intervals.append(w['interval'])
            self.colours.append(colourDict[w['colour']])
            if w['interval'] == 0:
                self.brightnesses.append(fixedBrightness)
            else:
                self.nFlash += 1
                randomBrightness = random.randint(int(minBrightness*100),
                                                  int(maxBrightness*100))/100
                self.brightnesses.append(randomBrightness)

        ## set starting increments for brightness adjustments
        self.increments = []
        for b in self.brightnesses:
            if b > self.increment/2:
                self.increments.append(self.increment)
            else:
                self.increments.append(self.decrement)

    # update brightnesses and increments
    def update(self):
        for p in range(self.nPixels):
            ### flashing pixels
            if self.intervals[p] > 0:
                #### when at min brightness switch to positive change
                if self.brightnesses[p] <= self.minBrightness:
                    self.brightnesses[p] = self.minBrightness
                    self.increments[p] = self.increment / self.intervals[p]
                #### when at max brightness switch to negative change
                elif self.brightnesses[p] >= self.maxBrightness:
                    self.brightnesses[p] = self.maxBrightness
                    self.increments[p] = self.decrement / self.intervals[p]
            ### non-flashing pixels
            else:
                self.increments[p] = 0

            ### calculate new brightnesses
            self.brightnesses[p] = round(self.brightnesses[p] + self.increments[p], 3)        
