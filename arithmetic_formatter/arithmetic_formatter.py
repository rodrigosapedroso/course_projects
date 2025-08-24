def arithmetic_arranger(problems, show_answers=False):
    
    if len(problems) > 5:
        return 'Error: Too many problems.'
    
    row1complete = []
    row2complete = []
    row3complete = []
    row4complete = []

    for index in problems:
        
        sign=index.split(' ')[1].strip()
        problema = index.split(sign)[0].strip()
        problemb = index.split(sign)[1].strip()
        dashes = max(len(problema), len(problemb)) + 2
        spacesup = dashes - len(problema)
        spacesdown = dashes - len(problemb) -1

        if sign=='*' or sign=='/':
            return "Error: Operator must be '+' or '-'."

        if len(problema) > 4 or len(problemb) > 4:
            return 'Error: Numbers cannot be more than four digits.'

        if not problema.isdigit() or not problemb.isdigit():
            return 'Error: Numbers must only contain digits.'

        row1 = (' '*spacesup)+problema
        row2 = sign+(' '*spacesdown)+problemb
        row3 = ('-'*dashes)

        if show_answers:
            problema = int(problema)
            problemb = int(problemb)

            if sign=='+':
                solution = problema + problemb
            elif sign=='-':
                solution = problema - problemb

            spacesbottom = dashes - len(str(solution))
            row4 = (' '*spacesbottom)+ str(solution)
            row4complete.append(row4)

        row1complete.append(row1)
        row2complete.append(row2)
        row3complete.append(row3)

    problems_final = '    '.join(row1complete)+'\n'+'    '.join(row2complete)+'\n'+'    '.join(row3complete)

    if show_answers:
        problems_final = problems_final + '\n'+'    '.join(row4complete)

    return problems_final
  
print(f'\n{arithmetic_arranger(["1 + 2", "1 - 9380"])}')