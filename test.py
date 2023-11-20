import os
import subprocess
import filecmp

def run_test(program, name):
    input_file = f'test/{program}.{name}.in'
    expected_output_file = f'test/{program}.{name}.out'
    arg_expected_output_file = f'test/{program}.{name}.arg.out'

    # Run program on STDIN
    process = subprocess.Popen(['python', f'prog/{program}.py'], stdin=open(input_file), stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
    output, _ = process.communicate()

    # Check for STDIN output mismatch
    if not filecmp.cmp(expected_output_file, subprocess.PIPE):
        return f'FAIL: {program} {name} failed (TestResult.OutputMismatch)\n      expected:\n{expected_output_file}\n\n           got:\n{output}'

    # Run program with command-line argument
    process = subprocess.Popen(['python', f'prog/{program}.py', input_file], stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
    output, _ = process.communicate()

    # Check for argument output mismatch
    if not filecmp.cmp(arg_expected_output_file, subprocess.PIPE):
        return f'FAIL: {program} {name} failed in argument mode (TestResult.OutputMismatch)\n      expected:\n{arg_expected_output_file}\n\n           got:\n{output}'

    return 'OK'

def run_tests():
    failed_tests = 0
    total_tests = 0

    for program in ['wc', 'gron', 'custom']:  # Add more programs as needed
        for file_name in os.listdir('test'):
            if file_name.endswith('.in'):
                test_name = file_name.split('.')[1]
                total_tests += 1

                result = run_test(program, test_name)
                print(result)

                if result.startswith('FAIL'):
                    failed_tests += 1

    print(f'\nOK: {total_tests - failed_tests}\noutput mismatch: {failed_tests}\ntotal: {total_tests}')

    if failed_tests > 0:
        exit(1)

if __name__ == "__main__":
    run_tests()
