'''class Solution:
    def isValidSudoku(self, board: list[list[str]]) -> bool:

        for i in range(9):
            for j in range(9):
                if board[i][j] == '.':
                    continue
                # 锚定要判断的数
                msg = board[i][j]
                # 先从行开始
                for m in range(j + 1, 9):
                    if board[i][m] == msg:
                        return False
                # 再从列开始
                for n in range(i + 1, 9):
                    if board[n][j] == msg:
                        return False
                # 再判断3*3宫,先找i, j 隶属于哪个宫
                g1 = i // 3
                g2 = j // 3
                for g1_start in range(g1 * 3, g1 * 3 + 3):
                    for g2_start in range(g2 * 3, g2 * 3 + 3):
                        if g1_start == i and g2_start == j:
                            continue
                        elif board[g1_start][ g2_start] == msg:
                            return False

        return True
board =[["8","3",".",".","7",".",".",".","."],["6",".",".","1","9","5",".",".","."],[".","9","8",".",".",".",".","6","."],["8",".",".",".","6",".",".",".","3"],["4",".",".","8",".","3",".",".","1"],["7",".",".",".","2",".",".",".","6"],[".","6",".",".",".",".","2","8","."],[".",".",".","4","1","9",".",".","5"],[".",".",".",".","8",".",".","7","9"]]
s= Solution()
print(s.isValidSudoku(board))'''
#我第一次的想法属于暴力破解，思考后决定采用哈希表来优化一下
class Solution:
    def isValidSudoku(self, board: list[list[str]]) -> bool:
        row = [set() for _ in range(9)]
        col = [set() for _ in range(9)]
        box = [set() for _ in range(9)]
        for i in range(9):
            for j in range(9):
                v = board[i][j]
                if board[i][j] == '.':
                    continue
                b = i // 3 + j // 3
                if v in row[i] or v in col[j] or v in box[b]:
                    return False
                row[i].add(v)
                col[j].add(v)
                box[b].add(v)
        return True
board =[["8","3",".",".","7",".",".",".","."],["6",".",".","1","9","5",".",".","."],[".","9","8",".",".",".",".","6","."],["8",".",".",".","6",".",".",".","3"],["4",".",".","8",".","3",".",".","1"],["7",".",".",".","2",".",".",".","6"],[".","6",".",".",".",".","2","8","."],[".",".",".","4","1","9",".",".","5"],[".",".",".",".","8",".",".","7","9"]]
s= Solution()
print(s.isValidSudoku(board))
"""
解题思路是哈希表，分别以列、行、宫为单位建立哈希表，如果一个哈希表中出现了两个相同的数字，则证明这个数独无效
这样的解法在时间复杂度上是O(n²)，相较于第一版更快，但空间复杂度上较大
"""
