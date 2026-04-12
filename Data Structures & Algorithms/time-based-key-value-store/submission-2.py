class StampedValue:
    _data: str
    _timestamp: int

    def __init__(self, data: str, timestamp: int) -> None:
        self._data = data
        self._timestamp = timestamp
    
    def get_data(self) -> str:
        return self._data
    
    def get_timestamp(self) -> int:
        return self._timestamp  

class TimeValue:
    data: list[StampedValue]

    def __init__(self) -> None:
        self.data = []
    
    def set(self, value: str, timestamp: int) -> None:
        self.data.append(StampedValue(value, timestamp))
    
    def get(self, timestamp: int) -> str:
        if len(self.data) == 0:
            return ""
        if timestamp >= self.data[-1].get_timestamp():
            return self.data[-1].get_data()
        if len(self.data) == 1:
            return ""

        left = 0 
        right = len(self.data) - 1

        res = ""
        
        while left <= right:
            midpoint = (left + right) // 2
            mid_timestamp = self.data[midpoint].get_timestamp()

            if mid_timestamp == timestamp:
                return self.data[midpoint].get_data()
            elif mid_timestamp < timestamp:
                res = self.data[midpoint].get_data()
                left = midpoint + 1
            else:
                right = midpoint - 1

        return res

class TimeMap:
    hashmap: dict[str, TimeValue]

    def __init__(self):
        self.hashmap = {}

    def set(self, key: str, value: str, timestamp: int) -> None:
        if key in self.hashmap:
            self.hashmap[key].set(value, timestamp)
        else:
            self.hashmap[key] = TimeValue()
            self.hashmap[key].set(value, timestamp)
        

    def get(self, key: str, timestamp: int) -> str:
        if key in self.hashmap:
            return self.hashmap[key].get(timestamp)
        else:
            return ""

