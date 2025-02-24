class Hexagon:
    def __init__(self, hex_id):
        self.id = hex_id
        self.connections = [None] * 6  # 6 lados possíveis para se conectar
        self.piece = None

    def set_piece(self, piece):
        self.piece = piece

    def remove_piece(self):
        self.piece = None

    def __str__(self):
        connected_sides = [f"{i+1}: (Hex {hexa.id}, Piece {hexa.piece.id})" for i, hexa in enumerate(self.connections) if hexa and hexa.piece]
        return f"Hexagon {self.id}: [{', '.join(connected_sides)}]"


class Board:
    def __init__(self):
        self.hexagons = []
        self.OPPOSITE_SIDES = {0: 3, 1: 4, 2: 5, 3: 0, 4: 1, 5: 2}
    
    def add_hexagon(self, hexagon):
        self.hexagons.append(hexagon)
    
    def connect(self, hex1, side1, hex2):
        side2 = self.OPPOSITE_SIDES[side1]
        hex1.connections[side1] = hex2
        hex2.connections[side2] = hex1

    def solve(self, pieces):
        return self._backtrack(0, pieces)

    def _backtrack(self, hex_index, remaining_pieces):
        if hex_index == len(self.hexagons):
            return True
        current_hex = self.hexagons[hex_index]
        for i, piece in enumerate(remaining_pieces):
            if self._can_place_piece(current_hex, piece):
                current_hex.set_piece(piece)
                if self._backtrack(hex_index + 1, remaining_pieces[:i] + remaining_pieces[i+1:]):
                    return True
                current_hex.remove_piece()
        return False

    def _can_place_piece(self, hexagon, piece):
        for side, connected_hex in enumerate(hexagon.connections):
            if connected_hex and connected_hex.piece:
                if piece.values[side] != connected_hex.piece.values[self.OPPOSITE_SIDES[side]]:
                    return False
        return True


    def display_board_solution(board):
        for hexagon in board.hexagons:
            piece = hexagon.piece
            if piece:
                print(f"Hexagon {hexagon.id}: Piece {piece.id}")
            else:
                print(f"Hexagon {hexagon.id}: No piece connected")

    def __str__(self):
        return '\n'.join([str(hexa) for hexa in self.hexagons])

class Piece:
    VALID_VALUES = {"V2", "A3", "A1", "B3"}

    def __init__(self, piece_id, values):
        self.id = piece_id
        if not all(k in values and values[k] in Piece.VALID_VALUES for k in range(6)):
            raise ValueError("Invalid piece values.")
        self.values = values

    def __str__(self):
        return str(self.values)

if __name__ == '__main__':
    board = Board()
    hex1 = Hexagon(1)
    hex2 = Hexagon(2)
    hex3 = Hexagon(3)
    hex4 = Hexagon(4)
    hex5 = Hexagon(5)
    # hex6 = Hexagon(6)

    board.add_hexagon(hex1)
    board.add_hexagon(hex2)
    board.add_hexagon(hex3)
    board.add_hexagon(hex4)
    board.add_hexagon(hex5)
    # board.add_hexagon(hex6)


    '''EFM - CHINATOWN'''
    pieces = [
        Piece('Leaf1')
    ] 

    '''
    EFM 9
    board.connect(hex1, 2, hex2) # 1, 2
    board.connect(hex2, 3, hex3) # 2, 3
    board.connect(hex3, 4, hex4) # 3, 4
    board.connect(hex4, 5, hex5) # 4, 5
    board.connect(hex5, 0, hex6) # 5, 6
    board.connect(hex6, 1, hex1) # 6, 1
    pieces = [
        Piece(1, {0: "B3", 1: "B3", 2: "V2", 3: "V2", 4: "A3", 5: "A3"}), # FolhaU
        Piece(2, {0: "A1", 1: "A1", 2: "V2", 3: "V2", 4: "A3", 5: "A3"}), # HidrogenioU
        Piece(3, {0: "V2", 1: "V2", 2: "A3", 3: "A3", 4: "B3", 5: "B3"}), # AguaU
        Piece(4, {0: "V2", 1: "V2", 2: "A3", 3: "A3", 4: "A1", 5: "A1"}), # SolD1
        Piece(5, {0: "A1", 1: "A1", 2: "B3", 3: "B3", 4: "A3", 5: "A3"}), # AguaD
        Piece(6, {0: "V2", 1: "V2", 2: "B3", 3: "B3", 4: "A1", 5: "A1"}), # FolhaD
        Piece(7, {0: "A3", 1: "A3", 2: "A1", 3: "A1", 4: "V2", 5: "V2"}), # SolD1
    ]
    '''
    board.solve(pieces)
    # print(board)
    print()
    board.display_board_solution()
