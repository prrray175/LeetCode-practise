import copy
class Solution:
    def solveSudoku(self, board: list[list[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        row = {i: [] for i in range(9)}
        col = {j: [] for j in range(9)}
        gong = {k: [] for k in range(9)}
        possible = [[ [] for c in range(9) ] for _ in range(9) ] #每个单位格的可能取值
        for i in range(9):
            for j in range(9):
                if board[i][j] == '.':
                    continue
                else:
                    row[i].append(board[i][j])
                    col[j].append(board[i][j])
                    s = (i//3 * 3) + j//3 #宫号
                    gong[s].append(board[i][j])
        for i in range(9):
            for j in range(9):
                if board[i][j] != '.':
                    continue
                else:
                    s = (i // 3 * 3) + j // 3
                    for m in range(1, 10):
                        if str(m) not in gong[s] and str(m) not in row[i] and str(m) not in col[j]:
                            possible[i][j].append(m)
#已经记录完毕每个单元格的可能取值
        for i in range(9):
            for j in range(9):
                if board[i][j] != '.':
                    continue
                s1 = (i // 3 * 3) + j // 3
                tboard = copy.deepcopy(board) #临时数组
                tpossible = copy.deepcopy(possible)
                flag = True
                for each in tpossible[i][j]:
                    tboard[i][j] = each
                    for m in range(i + 1, 9): #同行去值，同列去值，同宫去值'''
                        if flag == False:
                            break
                        if each in possible[i][m]:
                            tpossible[i][m].remove(each)
                            if len(tpossible[i][m]) == 1:
                                tboard[i][m] = tpossible[i][m][0]
                            elif len(tpossible[i][m]) == 0:
                                flag = False
                    for n in range(j + 1, 9):
                        if flag == False:
                            break
                        if each in possible[n][j]:
                            tpossible[n][j].remove(each)
                            if len(tpossible[n][j]) == 1:
                                tboard[n][j] = tpossible[n][j][0]
                            elif len(tpossible[n][j]) == 0:
                                flag = False
                    rr = i // 3 * 3
                    bb = j // 3 * 3
                    for p in range(rr, rr + 3):
                        if flag == False:
                            break
                        for q in range(bb, bb + 3):
                            if flag == False:
                                break
                            if p == i and q == j:
                                continue
                            else:
                                if each in possible[p][q]:
                                    tpossible[p][q].remove(each)
                                    if len(tpossible[m][j]) == 1:
                                        tboard[i][j] = tpossible[m][j][0]
                                    elif len(tpossible[m][j]) == 0:
                                        flag = False
                                        break
                    if flag == False:
                        continue

'''
没做出来
日后再战'''



