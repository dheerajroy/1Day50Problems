import os; print(len([i for i in os.listdir() if os.path.splitext(i)[1] == '.py'])-1, 'problems solved!')