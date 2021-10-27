class Vector3:
    def __init__(self, x=0, y=0, z=0):
        self.x = x
        self.y = y
        self.z = z
        
    def __repr__(self):
        return f'{type(self).__name__}({self.x}, {self.y}, {self.z})'
    
    def magnitude(self):
        return (self.x**2 + self.y**2 + self.z**2)**.5

    def __eq__(self, other: object) -> bool:
        if isinstance(other, Vector3):
            return (self.x == other.x and
                    self.y == other.y and
                    self.z == other.z)
        return False
    
    def __str__(self):
        return f"({self.x}, {self.y}, {self.z})"
    
    
    def __add__(self, other):
        if isinstance(other, Vector3):
            return Vector3(
                self.x + other.x,
                self.y + other.y,
                self.z + other.z)
        raise TypeError(f'Can only add two instances of Vector3 (not {other.__class__.__name__})')
        
    def __sub__(self, other):
        if isinstance(other, Vector3):
            return Vector3(
                self.x - other.x,
                self.y - other.y,
                self.z - other.z)
        raise TypeError(f'Can only subtract two instances of Vector3 (not {other.__class__.__name__})')
        
    
    def __mul__(self, other):
        if isinstance(other, (int, float)):  # vector-scalar multiplication
            return Vector3(
                self.x * other,
                self.y * other,
                self.z * other,
            )
        elif isinstance(other, Vector3):  # element-wise vector-vector multiplication
            return Vector3(
                self.x * other.x,
                self.y * other.y,
                self.z * other.z,
            )
        
    def __rmul__(self, other):
        return self.__mul__(other)
        

    def normalize(self):
        l = self.magnitude()
        return Vector3(
            self.x / l,
            self.y / l,
            self.z / l,
        )
    
    def dot(self, other):
        if isinstance(other, Vector3):
            return self.x * other.x + self.y * other.y + self.z * other.z
        
        raise ValueError(f'The argument of dot-product must be a instace of Vector3, not {type(other)}')
            
            
    def cross(self, other):
        if isinstance(other, Vector3):
            x = (self.y * other.z) - (self.z * other.y)
            y = (self.z * other.x) - (self.x * other.z)
            z = (self.x * other.y) - (self.y * other.x)
            return Vector3(x, y, z)
        
        raise ValueError(f'The argument of cross-product must be a instace of Vector3, not {type(other)}')