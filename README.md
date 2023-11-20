Nikunj Arvindbhai Gothadiya ngothadi@stevens.edu

# the URL of your public GitHub repo

https://github.com/nmscs/CS515A-Project-1-Test-Harness

# an estimate of how many hours you spent on the project

I spent around 27 hours on the project.

# a description of how you tested your code

To thoroughly test the wc.py code, I devised a series of test cases to evaluate its functionality across various scenarios. Each test case addressed different aspects of the specified extensions. Initially, I examined the handling of expected exit statuses, deliberately selecting values other than 0 to ensure the code accurately responded to diverse exit status conditions. Subsequently, I scrutinized the handling of standard error (STDERR) outputs, covering scenarios with both empty and non-empty expected STDERR outputs. Additionally, I tested the code's responsiveness to timeouts, verifying that it appropriately flagged test cases exceeding specified timeout durations. To guarantee the creation and cleanup of temporary directories functioned correctly, I assessed whether each command executed within a fresh temporary directory and confirmed the successful removal of temporary directories after execution. Finally, I validated the setup feature by creating tests utilizing ZIP files, ensuring that the code correctly unzipped files into the temporary directory. Throughout this testing process, I meticulously examined the printed outputs and any raised exceptions to confirm that the script adhered to the specified extensions, providing a comprehensive evaluation of its robustness and reliability.

I tested the gron.py code using a combination of positive and negative test cases, including scenarios with basic and nested JSON structures. I covered features such as custom base object names, running with arguments, handling malformed JSON, and checking exit status. I also tested extensions, such as expected STDERR, timeouts, temporary directories, and setup using ZIP files. The test suite includes a mix of manual inspection and automated execution using the test.py test harness, ensuring comprehensive coverage and correctness.

To test the csv_sum utility, I created a sample CSV file containing numeric values in various columns, including some empty strings. I ran the program with this test file, specifying different combinations of columns to sum. I intentionally included columns with empty strings to ensure that the code properly handles these cases without raising an error. Additionally, I tested the utility with both valid and nonexistent column names to verify the accuracy of the error messages. The program successfully calculated and displayed the sums for the specified columns, accounting for empty strings by treating them as zero during the sum calculation. This testing approach helped ensure the robustness of the utility under various scenarios and confirmed its ability to handle both valid and erroneous inputs gracefully.

# any bugs or issues you could not resolve

During the development and testing process, I encountered several challenges and addressed various issues in the gron.py and wc.py scripts. However, there were instances where I faced difficulty in handling specific edge cases or scenarios. One notable challenge was ensuring robust error handling for malformed JSON in gron.py and handling unexpected formats in wc.py. Despite extensive testing, there might be unanticipated issues that could arise in certain corner cases or under unique circumstances. Additionally, the implementation of features such as custom base object names, expected exit status, and timeouts involved intricate logic, and although efforts were made to address potential issues, there may still be room for refinement. As development progresses, ongoing testing and feedback will be crucial for identifying and resolving any bugs or issues that may emerge in diverse usage scenarios.

During testing sum.py, I did not encounter any significant bugs or issues that remained unresolved. The code appears to handle various scenarios well, including empty strings in the CSV file and valid/invalid column names. However, it's important to note that as with any software, there may be specific edge cases or unexpected input scenarios that could potentially lead to issues. Users are encouraged to provide feedback and report any unforeseen problems, and I am available to address and resolve any such issues that may arise in the future. As of the current testing, the utility performs as intended without any known unresolved bugs.


# an example of a difficult issue or bug and how you resolved it

One challenging issue I encountered during the development of the gron.py script involved handling nested JSON structures with arrays and ensuring the correct flattening of such complex hierarchies. Nested arrays posed a particular challenge as their structures needed careful traversal to avoid potential errors in the flattening process. To address this, I revised the flatten_json function to recursively handle both nested objects and arrays. This involved refining the logic to distinguish between JSON objects and arrays, ensuring that each element is appropriately processed. I also incorporated additional checks to handle edge cases where array elements might contain nested structures. By thoroughly testing the script with diverse nested JSON inputs and iteratively refining the flattening algorithm, I successfully resolved this issue, ensuring that the gron.py script can effectively handle and flatten complex JSON structures.

#a list of the three extensions you’ve chosen to implement, with appropriate detail on them for the CAs to evaluate them

1. Custom Base Object Name : Verify that the script correctly uses the specified base object name for flattened assignments. Ensure it works seamlessly with various JSON structures.
2. Expected Exit Status : Check that the script correctly reads and compares exit statuses. Verify functionality for both zero and non-zero exit statuses.
3. Timeouts : onfirm that the script adheres to the specified timeout and reports failures if the execution exceeds the defined time. Test with both short and long timeouts.