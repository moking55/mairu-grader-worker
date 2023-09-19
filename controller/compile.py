import subprocess

input_test = ["1", "2", "3", "4"]
expect_output = ["*\r\n"]

def executeFile(command, filename, case):
    # spawn a new process to execute the file
    # limit the time to 5 seconds
    # if the process takes longer than 5 seconds, kill it
    # return the output and error
    process = subprocess.Popen(command, stdout=subprocess.PIPE, stderr=subprocess.PIPE, stdin=subprocess.PIPE, shell=False)
    # if the input test case is not empty
    if case != "":
        # write the input test case to the process
        out, err = process.communicate(input=case.encode(), timeout=5)
    # wait for the process to finish
    try:
        out, err = process.communicate(timeout=5)
        process.communicate()
    except subprocess.TimeoutExpired:
        process.kill()
    
    # return the output and error
    return out.decode(), err.decode()

def compilePython(filename):
    # compile the python file
    # run the executeFile function from controller/compile.py

    grader_result = []

    # loop through the input test cases
    for case in input_test:
        # if input_test or expect_output length is not equal to each other then fill the less one with empty string
        if len(input_test) != len(expect_output):
            if len(input_test) > len(expect_output):
                expect_output.append("")
            else:
                input_test.append("")
        

        # run the executeFile function from controller/compile.py
        # pass the command to execute the file
        # pass the filename to execute

        out, err = executeFile(f"python submission/{filename}", filename, case)
        print(out, err)

        # if the output is not equal to the expected output
        if out != expect_output[input_test.index(case)] or case == "":
            # return the error
            grader_result.append({
                "case": case,
                "output": out,
                "error": err,
                "is_correct": False,
            })
        else:
        
            grader_result.append({
                "case": case,
                "output": out,
                "expected_output": expect_output[input_test.index(case)],
                "is_correct": True,
            })
    return grader_result