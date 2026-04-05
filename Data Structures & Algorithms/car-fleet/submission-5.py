from dataclasses import dataclass

@dataclass
class Car:
    position: int
    speed: int
    
    def __lt__(self, other) -> bool:
        return self.position < other.position
        
class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int: 
        if len(position) == 0:
            return 0

        cars: list[Car] = []
        for i in range(len(position)):
            cars.append(Car(position[i], speed[i]))
        
        cars_sorted = sorted(cars)
        
        stack: list[Car] = [cars_sorted[-1]]
        
        for i in reversed(range(len(cars_sorted)-1)):
            t = (target - stack[-1].position) / stack[-1].speed
            current_car = cars_sorted[i]
            delta_pos = stack[-1].position - current_car.position
            delta_speed = current_car.speed - stack[-1].speed

            if delta_speed > 0:
                catch_up_time = delta_pos / delta_speed
                if catch_up_time <= t:
                    continue
            stack.append(cars_sorted[i])
        
        return len(stack)
