x1, y1, x2, y2 = map(int, input().split())
a1, b1, a2, b2 = map(int, input().split())

ans_x1, ans_x2, ans_y1, ans_y2 = 0,0,0,0

ans_x1 = min(x1, x2, a1, a2)
ans_x2 = max(x1, x2, a1, a2)
ans_y1 = min(y1, y2, b1, b2)
ans_y2 = max(y1, y2, b1, b2)

print( abs(ans_x2 - ans_x1) * abs(ans_y2 - ans_y1) )