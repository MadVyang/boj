import random
import subprocess

ans_code = 'ans.py'
my_code = input('Enter file name of my code: ')+'.py'

num_test = 100


# modify here
def parse_out(out):
    return out.communicate()[0].decode('utf-8').split('\n')[0]


for i in range(num_test):
    # modify here
    a = str(random.randrange(1, 1000000))
    b = str(random.randrange(1, 10))
    input_to_test = bytes(a+' '+b, 'utf-8')
    print('testing', a, b, '...')

    ans_p = subprocess.Popen(
        ['python', ans_code], stdin=subprocess.PIPE, stdout=subprocess.PIPE)
    ans_p.stdin.write(input_to_test)
    ans_out = parse_out(ans_p)

    my_p = subprocess.Popen(
        ['python', my_code], stdin=subprocess.PIPE, stdout=subprocess.PIPE)
    my_p.stdin.write(input_to_test)
    my_out = parse_out(my_p)

    if ans_out != my_out:
        print('ans:', ans_out)
        print('my:', my_out)
        break
    else:
        print('pass')
