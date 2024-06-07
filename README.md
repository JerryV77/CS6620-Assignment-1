# CS6620-Assignment-1

## Introduction
For this assignment, I made a simple calculator. I will explain how to use this repo in the following steps. This repo is a simple workflow example which I will use as template to do further assignments and final project.

### Step 1: Clone the repository
  1. Open Terminal in your software.
  2. Clone this repository by using the following command:
     ```
     git clone https://github.com/JerryV77/CS6620-Assignment-1.git
     ```
  3. Navigate to the repository directory

### Step 2: Set up the Python Environment
  1. Ensure you have the latest version of Python is installed:
     
     * Make sure Python 3.13 is installed on your machine. You can download it from [python.org](https://www.python.org/downloads/).

  2. Create a Virtual Environment (optional but strongly recommended):
     ```
     python -m venv venv
     ```
  3. Activate the Virtual Environment:
     * On macOS/Linux:
     ```
     source venv/bin/activate
     ```
     * On Windows:
     ```
     .\venv\Scripts\activate
     ```

### Step 3: Install Dependencies
  1. Install Dependencies using 'pip' command:
     ```
     pip install -r requirements.txt
     ```

### Step 4: Run the code
  1. Run the Main Script:
      ```
      python main.py
      ```
      
      This script contains four functions: add, subtract, multiply and divide. Running this script will execute these functions and print their results.

### Step 5: Run the Tests
  1. Run the Tests using unittest:
     ```
     python -m unittest discover -s . -p "test.py"
     ```
     
     This command will discover and run the tests defined in test.py to ensure the functions in main.py are working correctly.

  2. When you run the tests using python -m unittest discover -s . -p "test.py", you should see an output indicating the tests passed:
     ```
      ...
      ----------------------------------------------------------------------
      Ran 4 tests in 0.001s

      OK

     ```
### Step 6: Check the yml file if you get any errors
* "main.yml" file shown the whole workflow process for this assignment. Please check it if you get any type of error.
  
### Conclusion
By following above instructions, you should be able to run the code and tests in the repository successfully. If you encounter any issues, ensure that Python and all required dependencies are correctly installed.
