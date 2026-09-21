# Invitation Nation QA Automation

Selenium-based web UI automation for Invitation Nation using Microsoft Edge, with optional Google Sheets result logging.

## Technologies

- Python 3
- Selenium WebDriver
- Microsoft Edge
- Microsoft Edge WebDriver
- Requests
- Google Apps Script
- Google Sheets
- GitHub

## Test Cases Covered

### Test Case 1 — Login and Dashboard

`test_browser.py`

1. Open Invitation Nation.
2. Click Sign In / Sign Up.
3. Switch to the authentication tab.
4. Enter test email and password.
5. Click Login.
6. Verify the `Welcome to Invitation Nation` dashboard heading.
7. Report PASS/FAIL and execution time.

### Navigation / Template Flow

`test_template.py`

1. Open Invitations.
2. Locate the Festivities category.
3. Navigate to `/invitations/festivities`.
4. Locate template cards.
5. Select the first available template.
6. Verify the template page opens.

## Setup

```powershell
python -m venv venv
venv\Scripts\Activate.ps1
pip install -r requirements.txt
```

Place a compatible `msedgedriver.exe` in the project root.

## Test Credentials

Credentials are intentionally not committed.

```powershell
$env:INVITATION_TEST_EMAIL="your-test-email@example.com"
$env:INVITATION_TEST_PASSWORD="your-test-password"
```

Run:

```powershell
python test_browser.py
python test_template.py
```

## Google Sheets Integration

1. Create a Google Sheet.
2. Add headers:

```text
Timestamp | Test Case | Status | Execution Time | Failure Reason
```

3. Open **Extensions → Apps Script**.
4. Copy `Code.gs` into the Apps Script editor.
5. Deploy it as a **Web app**.
6. Copy the deployed `/exec` URL.
7. Configure it without committing the URL:

```powershell
$env:GOOGLE_SCRIPT_URL="YOUR_DEPLOYED_WEB_APP_EXEC_URL"
```

8. Test:

```powershell
python test_google_sheet.py
```

Expected response:

```json
{"status":"success"}
```

## Logging Fields

- Timestamp
- Test case
- Status
- Execution time
- Failure reason

## Assumptions

- A valid test account exists.
- Invitation Nation is reachable during execution.
- EdgeDriver is compatible with the installed Edge browser.
- The Apps Script deployment has permission to write to the target sheet.

## Known Limitations

- The tests depend on the live website and current DOM structure.
- Changes to IDs, classes, text, or URLs may require locator updates.
- The template test validates the first available collection card only.
- EdgeDriver must remain compatible with the installed Edge version.
- Google Apps Script permissions or deployment changes can cause 403/404 responses.
- Network conditions can cause Apps Script requests to time out.
- Credentials, virtual environments, and deployment URLs are intentionally excluded from source control.

## Troubleshooting

### Selenium cannot start Edge

Check that `msedgedriver.exe` exists in the project root and matches the installed Edge version.

### Login fails

Verify the test credentials and inspect the current login page IDs.

### Template test fails

Verify these current selectors:

```text
button/span containing "Invitations"
a[href="/invitations/festivities"]
a.collection-card-link
```

### Google Sheets returns 403 or 404

Verify the Apps Script deployment, access settings, and `/exec` URL.

## Repository

https://github.com/ananth05m/InvitationNation_QA
