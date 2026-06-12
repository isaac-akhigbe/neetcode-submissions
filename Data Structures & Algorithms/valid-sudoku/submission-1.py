class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        rows = [set() for _ in range(9)]
        column = [set() for _ in range(9)]
        box = [set() for _ in range(9)]
        
        for r in range(9):
            for c in range(9):
                num = board[r][c]

                if num == '.':
                    continue
                
                if num in rows[r] or num in column[c]:
                    return False
                else:
                    rows[r].add(num)
                    column[c].add(num)

                box_index = (r // 3) * 3 + (c // 3)
                if num in box[box_index]:
                    return False
                else:
                    box[box_index].add(num)
        return True

                
