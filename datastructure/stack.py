class Stack():
    def __init__(self):
        self.items = []

    #栈是否为空
    def is_empty(self):
        return self.items == []

    #向栈添加一个元素
    def push(self, item):
        self.items.append(item)

    #栈弹出一个元素
    def pop(self):
        return self.items.pop()

    #获取栈顶元素(不弹出)
    def peek(self):
        if len(self.items):
            return self.items[len(self.items)-1]
        return None

    #查看栈中元素个数
    def size(self):
        return len(self.items)

#打印一个栈
def print_stack(stack):
    print('{:↑^11}'.format('栈顶'))
    for i in range(len(stack.items)):
        print('{:↑^11}'.format(stack.items[len(stack.items) - i - 1]))
    print('{:↑^11}'.format('栈底'))


#经典案例1：括号匹配
def is_brackets_correct(str):
    stack = Stack()
    for i in range(len(str)):
        if str[i] == '(' or str[i] == '[' or str[i] == '{':
            stack.push(str[i])
            continue

        top = stack.peek()
        if str[i] == ')':
            if top != '(':
                return False
            stack.pop()
        if str[i] == ']':
            if top != '[':
                return False
            stack.pop()
        if str[i] == '}':
            if top != '{':
                return False
            stack.pop()

    return stack.is_empty()


#经典案例2：中缀表达式转换后缀表达式，并求值
def translate(str):
    stack = Stack()
    lst = str.split()
    nlst = []
    for i in range(len(lst)):
        top = stack.peek()
        if lst[i] == '+' or lst[i] == '-':
            if top in ['*', '/']:
                nlst.append(stack.pop())
                stack.push(lst[i])
                top = stack.peek()
                if top in ['+', '-']:
                    nlst.append(stack.pop())
        elif lst[i] == '*' or lst[i] == '/':
            stack.push(lst[i])
        else:
            nlst.append(lst[i])

    for i in range(stack.size()):
        nlst.append(stack.pop())

    return ' '.join(nlst)

            
def calculate(n1, n2, opertor):
    pass


str1 = '1 + 2 * 3 / 4'
str2 = '2 * 4 / 5 + 3 * 2'

print(translate(str1))
print(translate(str2))
