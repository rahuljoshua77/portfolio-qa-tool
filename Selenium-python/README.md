Test Repository
===============

This repository contains test scripts using Python and Selenium for testing web applications using LambdaTest Cloud Selenium Grid.

Installation and Usage
----------------------

1.  Clone this repository to your local computer.
2.  Install Python and dependencies using the following command:
    
        pip install -r requirements.txt
    
3.  Replace the LambdaTest username and access key in the test scripts with your own credentials.
4.  Run the test scripts using pytest in parallel to execute the test scenarios on LambdaTest Cloud Selenium Grid.

Test Scenarios
--------------

*   Test Scenario 1: Open the https://www.lambdatest.com/selenium-playground page and validate the title.
*   Test Scenario 2: Open the https://www.lambdatest.com/selenium-playground page, click "Drag & Drop Sliders" and validate the slider value.
*   Test Scenario 3: Open the https://www.lambdatest.com/selenium-playground page, click "Input Form Submit", fill in the form, and validate the success message.

Dependencies
------------

*   Python: 3.7+
*   Selenium: 3.141+
*   pytest: 6.2+
*   webdriver: Chrome or Firefox