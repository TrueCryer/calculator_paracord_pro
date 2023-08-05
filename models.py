from decimal import Decimal


class GenericModel:

    COEFS = {
        '4mm' : ('0', '0', '0', '0'),
        '2mm' : ('0', '0', '0', '0'),
    }

    def __init__(self, bracelet_length: Decimal, rope_diameter: str):
        self.rope_diameter: str = rope_diameter
        self.bracelet_length: Decimal = bracelet_length

    def get_coef(self, k_number: int):
        try:
            k = self.COEFS[self.rope_diameter][k_number]
        except KeyError:
            k = '0'
        return Decimal(k)

    def get_length(self, k_number: int):
        length = self.bracelet_length * self.get_coef(k_number)
        return length.quantize(Decimal('0.1'))

    @property
    def l1(self):
        return self.get_length(0)
    
    @property
    def l2(self):
        return self.get_length(1)
    
    @property
    def l3(self):
        return self.get_length(2)
    
    @property
    def l4(self):
        return self.get_length(3)


class CobraModel(GenericModel):
    """ k1 - with strands
        k2 - without strands
        k3 - one side + 3/4 core
        k4 - one side + 1/4 core
 
               k1     k2     k3     k4
        2 mm - 11.0,   9.0,  6.0,   5.0
        4 mm - 12.5,  10.5,  6.75,  5.75
    """
    COEFS = {
        '4mm' : ('12.5', '10.5', '6.75', '5.75'),
        '2mm' : ('11.0',  '9.0', '6.00', '5.00'),
    }


class SnakeModel(GenericModel):
    """ k1 - one side
        k2 - both sides
 
               k1     k2   
        2 mm - 4.95,  9.9
        4 mm - 4.9,   9.8
    """
    COEFS = {
        '4mm' : ('4.9',  '9.8'),
        '2mm' : ('4.95', '9.9'),
    }


class FishtailModel(GenericModel):
    """ k1 - with strands
        k2 - without strands

               k1      k2
        2 mm - 10.2,   8.2
        4 mm -  9.55,  7.55
    """
    COEFS = {
        '4mm' : ( '9.55', '7.55'),
        '2mm' : ('10.20', '8.20'),
    }


class TrilobiteModel(GenericModel):
    """ k1 - with strands
        k2 - without strands
        
               k1    k2
        2 mm - 19.9, 15.9
        4 mm - 19.0, 15.0
    """ 
    COEFS = {
        '4mm' : ('19.0', '15.0'),
        '2mm' : ('19.9', '15.9'),
    }


class BoxModel(GenericModel):
    """ k1 - color 1
        k2 - color 2
        
               k1    k2
        2 mm - 7.65, 7.65
        4 mm - 9.32, 9.32
    """
    COEFS = {
        '4mm' : ('9.32', '9.32'),
        '2mm' : ('7.65', '7.65'),
    }


class SanctifiedModel(GenericModel):
    """ k1 - inner color
        k2 - outer color
        k3 - inner color without strands
        k4 - outer color without strands

               k1    k2    k3    k4
        2 mm - 12.0, 10.7, 10.0, 8.7
        4 mm - 13.5, 11.5, 11.5, 9.5
    """ 
    COEFS = {
        '4mm' : ('13.5', '11.5', '11.5', '9.5'),
        '2mm' : ('12.0', '10.7', '10.0', '8.7'),
    }          