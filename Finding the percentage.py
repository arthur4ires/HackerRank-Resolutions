from decimal import Decimal

if __name__ == '__main__':
    n = int(input())
    
    student_marks = {}
    
    for _ in range(n):
        name, *line = input().split()
        scores = list(map(float, line))
        student_marks[name] = scores
        
    query_name = input()
    valueFloat =  0.00
    
    for x in student_marks[query_name]:
        valueFloat += x/3
    
    print(f'{valueFloat:.2f}')
