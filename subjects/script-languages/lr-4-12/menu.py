import sys
import importlib
sys.path.append('subjects/script-languages')

import functions as f
from functions import print_full_width_line as line
f = importlib.reload(f)

sys.path.append('subjects/script-languages/lr-4-12/task-1')
sys.path.append('subjects/script-languages/lr-4-12/task-2') 
sys.path.append('subjects/script-languages/lr-4-12/task-3')
sys.path.append('subjects/script-languages/lr-4-12/task-4')

import task1 as t1
import task2 as t2
import task3 as t3
import task4 as t4

line()
f.print_lr_start(4)
line()

def main():
    keep_going = True

    while keep_going:
        print('''ЛР№ 4
1 - задача 1
2 - задача 2  
3 - задача 3
4 - задача 4          
0 - выхад                                    
''')
        choice = int(input("> "))
        if choice == 1:
            t1.main()        
        elif choice == 2:
            t2.main()
        elif choice == 3:
            t3.main()
        elif choice == 4:
            t4.main()
        elif choice == 0:
            keep_going = False
            f.print_lr_end(3)
        else:
            f.print_unkown_choice()

if __name__ == "__main__":
    main()