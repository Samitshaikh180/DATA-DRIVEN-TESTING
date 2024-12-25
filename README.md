# DATA-DRIVEN-TESTING

**COMPANY**: CODTECH IT SOLUTIONS

**NAME**: SAMIT ISMAIL SHAIKH

**INTERN ID**: CT08GDS

**DOMAIN**: AUTOMATION TESTING

**BATCH DURATION**: DEC 25th,2024 to JAN 25th, 2025

**MENTOR NAME**: NEELA SANTOSH

Data-Driven Testing in Automation Testing

Data-driven testing is a systematic approach used in automation testing to enhance test efficiency and coverage by leveraging externalized test data. This methodology involves separating test logic from test data, enabling the execution of the same test script with multiple sets of input data. This approach reduces script duplication and supports the automation of tests with various input combinations, making it highly efficient for validating diverse scenarios.

Process of Data-Driven Testing

1. Identify Test Scenarios:
The first step is to identify the test scenarios that involve varying input data. This could include form validations, boundary testing, or workflows requiring different data combinations.


2. Prepare Test Data:
Test data is created and stored in an external source, such as Excel files, CSV files, databases, or XML files. These data sets typically include input values and their corresponding expected outputs.


3. Integrate Test Scripts and Data:
Automation scripts are written using tools like Selenium, TestNG, or JUnit. The scripts are designed to read and process the externalized data dynamically during execution.


4. Parameterization:
Test scripts are parameterized to accept external inputs. This involves using placeholders or variables within the scripts to fetch data from the external source.


5. Set Up Data Connections:
Data-driven frameworks require connections to the data source. For example, in Selenium, libraries such as Apache POI (for Excel) or JDBC (for databases) can be used to establish these connections.


6. Run Tests:
Once the scripts and data are configured, the tests are executed. Each row of data is used as a unique test case, allowing the same script to iterate through all data sets.


7. Analyze Results:
After execution, the test results are reviewed to validate whether the application behaved as expected for all input combinations. Any discrepancies between actual and expected results indicate defects.

**OUTPUT** 

username,password,result,message
user1,pass1,Pass,Login successful
user2,pass2,Fail,Login failed
user3,pass3,Error,NoSuchElementException: Unable to locate element
