#day1 汉诺塔
'''
算法实现：递归
   [递归的]将 N-1 个圆盘从左边柱子移动到中间柱子。
   将最大的圆盘从左边柱子移动到右边柱子。
   [递归的]将 N-1 个圆盘从中间柱子移动到右边柱子。

def hanoi(n, a="left", b="middle", c="right"):
    if n == 1:
        print(a, "-->", c)
    else:
        hanoi(n-1, a, c, b)
        print(a, "-->", c)
        hanoi(n-1, b, a, c)
'''

def hanoi(height, left='left', right='right', middle='middle'):
    if height:
        hanoi(height - 1, left, middle, right)
        print(left, '=>', right)
        hanoi(height - 1, middle, right, left)


if __name__ == "__main__":
    hanoi(3)