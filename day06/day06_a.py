from aocd import lines


class Fish:
    def __init__(self, _timer, _new = False):
        self.initial_reproduction_timer = 6
        self.cycle = 1
        if _new:
            self.reproduction_timer = int(_timer) + 2
        else:
            self.reproduction_timer = int(_timer)
    
    def pass_day(self):
        new_fish = None
        if self.reproduction_timer == 0:
            self.reproduction_timer = self.initial_reproduction_timer
            self.cycle += 1
            new_fish = Fish(self.initial_reproduction_timer, True)
        else:
            self.reproduction_timer -= 1
        
        return new_fish


fishes = [Fish(timer) for timer in lines[0].split(',')]
nb_days = 80

for day in range(1, nb_days + 1):
    new_fishes = []
    for fish in fishes:
        new_fish = fish.pass_day()
        if not new_fish is None:
            new_fishes.append(new_fish)
    fishes.extend(new_fishes)

print(len(fishes))