class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:

        for row in board:
            a = set()
            for num in row:
                if num != ".":
                    if num in a:
                        return False
                    a.add(num)

        
        for i in range(9):
            b = set()
            column = i
            for row in range(9):
                num = board[row][column]
                if  num != ".":
                    if num in b:
                        return False
                    b.add(num)

        box_level = 0
        box_horiz = 0
        for i in range(9):
        
            c = set()
            for row in range(3):
                for column in range(3):
                    num = board[box_level+row][column+box_horiz]
                    if num != ".":
                        if num in c:
                            return False
                        c.add(num)
                
            if (i+1)%3 == 0:
                box_level+=3
                box_horiz = 0
            else:
                box_horiz +=3

        return True