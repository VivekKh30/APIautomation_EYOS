Structure-

- Tests are designed using Behave BDD and Python Requests package.
- This project is a standard Python project
- Feature file is present at /API_automation_EYOS/features folder

How to Run- 

- Clone this repository from github, import it to Pycharm (or any other IDE).
- To execute the feature file run  behave --no-capture from terminal
  - To view the reports alongside run, please follow below steps:
    - Download allure
    - run behave --no-capture -f allure_behave.formatter:AllureFormatter -o AllureReports from terminal
    - Above command will create a Json file in AllureReports folder of the project
    - Run allure serve {path of Json}
    - Sample report can be found in http://192.168.0.16:58345/index.html

Issues Found-

- No validations in place for invalid country code. A test case has written to cover this validation however is failing every time.
- No response returned if multiple country code passes in query parameter.

Improvements:

- Tests are currently running sequentially, some changes may required to run them in parallel
- Sometimes API returns 429 error due to rate limit, improvement can be done to handle the error by adding wait as required.
- Logging can be improved.


