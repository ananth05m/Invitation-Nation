# InvitationNation QA Automation

Selenium-based QA automation tests for Invitation Nation using Microsoft Edge.

## Test cases

1. **Login and User Dashboard**
   - Opens Invitation Nation
   - Opens Sign In / Sign Up
   - Switches to the login tab
   - Enters test credentials
   - Verifies the user dashboard

2. **Invitation Navigation**
   - Opens the Invitations section
   - Verifies that the Invitations control can be selected

3. **Festivities Template Navigation**
   - Opens Invitations
   - Selects the Festivities category
   - Opens the first template
   - Verifies navigation to the template page

4. **Live Demo**
   - Opens Invitations
   - Selects the first invitation category
   - Opens Live Demo
   - Verifies the new browser tab
   - Switches back to the original tab

5. **Google Sheets Logger**
   - Sends a sample test-result record to the configured Google Apps Script web app

## Requirements

- Python 3.x
- Microsoft Edge
- `msedgedriver.exe` compatible with the installed Edge browser
- Internet connection
- Selenium and Requests

Install dependencies:

```powershell
pip install -r requirements.txt
```

## Configuration

Do not put real credentials or deployment URLs directly into the Python files.

Set these environment variables in PowerShell:

```powershell
$env:INVITATION_TEST_EMAIL="your_test_email"
$env:INVITATION_TEST_PASSWORD="your_test_password"
$env:GOOGLE_SCRIPT_URL="your_google_apps_script_web_app_url"
```

These variables apply to the current PowerShell session.

## Run tests

```powershell
python test_login.py
python test_navigation.py
python test_template.py
python test_live_demo.py
python test_google_sheet.py
```

The Edge WebDriver executable should be available as `msedgedriver.exe` in the project directory, or the Selenium setup should otherwise be able to locate the compatible driver.

## Google Sheets integration

1. Create or open a Google Sheet.
2. Open Extensions → Apps Script.
3. Put the contents of `Code.gs` into the Apps Script project.
4. Deploy it as a Web app.
5. Configure the resulting web-app URL in `GOOGLE_SCRIPT_URL`.
6. Run `test_google_sheet.py` to verify the connection.

The login test also sends its PASS/FAIL result, execution time, and failure reason to the same endpoint.

## Notes

- `test_category_debug.py` and the temporary intentional-failure test were excluded from the final project because they were debugging artifacts.
- Test credentials are intentionally supplied through environment variables.
- The tests use the selectors that were working in the submitted project; website changes may require selector updates.
