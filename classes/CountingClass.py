import datetime

class Chickount:
    def __init__(self, idRef, imageData, count, timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S") ):
        self.idRef = idRef
        self.imageData = imageData
        self.timestamp = timestamp
        self.count = count

    def __str__(self):

        return f"idRef: {self.idRef}, imageData: {self.imageData}, timestamp: {self.timestamp}, count: {self.count}"
    
    def __repr__(self):

        return f"idRef: {self.idRef}, imageData: {self.imageData}, timestamp: {self.timestamp}, count: {self.count}"
    
    def to_dict(self):
        return {
            "idRef": self.idRef,
            "imageData": self.imageData,
            "timestamp": self.timestamp,
            "count": self.count
        }