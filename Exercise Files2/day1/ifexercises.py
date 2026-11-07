# status_code = int(input("Status code: "))

# def check_status(status_code):
#     if status_code == 200:
#         return "PASS: OK"
#     elif status_code == 201:
#         return "PASS: Created"
#     elif status_code == 400:
#         return "FAIL: Bad Request"
#     elif status_code == 401:
#         return "FAIL: Unauthorized"
#     elif status_code == 404:
#         return "FAIL: Not Found"
#     elif status_code == 500:
#         return "FAIL: Server Error"
#     else:
#         return "FAIL: Unexpected status"

# print(check_status(500))

#######################_____________________
# def check_build(passed, failed, skipped):
#     if failed > 0:
#         return "Build FAILED"
#     elif passed ==0 and skipped > 0:
#         return  "Build SKIPPED"
#     elif passed > 0 and failed == 0:
#         return "Build PASSED"
#     else: 
#         return "No tests executed"

# print(check_build(10, 1, 3))

###################################
# env = input("Env: ")

# def print_env(env):
#     env = env.lower()
    
#     if env == "dev":
#         return "https://dev.example.com"
#     elif env == "qa":
#         return "https://qa.example.com"
#     elif env == "prod":
#         return "https://prod.example.com"
#     elif env == "stage":
#         return "https://stage.example.com"
#     else:
#         return "Invalid environment"

# print(print_env("QA"))

#################################

# def browser_launch(browser, headless):
#     browser = browser.lower()
#     if browser== "chrome" and headless:
#         return "Launch Chrome headless"
#     elif browser == "chrome" and not headless:
#         return "Launch Chrome UI"
#     elif browser == "firefox" and headless:
#             return "Launch Firefox headless"
#     elif browser == "firefox" and not headless:
#             return "Launch Firefox UI"
#     else:
#             return "Unsupported browser"

# print(browser_launch("firefox", True))

#############################

# def login_val(username, password):
#     if username == "" and password == "":
#         return "FAIL: missing credentials"
#     elif username == "":
#         return "FAIL: username required"
#     elif password == "":
#         return "FAIL: password required"
#     elif username == "testuser" and password == "Test@123":
#         return "PASS: login success"
#     else: 
#         return  "FAIL: invalid credentials"

# print(login_val("", "Test@123"))

############################

# def element_assert(is_displayed, is_enabled, text):
#     if not is_displayed:
#         return "FAIL: element not visible"
#     elif not is_enabled:
#         return "FAIL: element disabled"
#     elif text == "Submit":
#         return "PASS: ready to click"
#     else:
#         return "FAIL: unexpected text"

# print(element_assert(True, True, "Submit"))

###########################

# def retry(attempt, success):
#     if success:
#         return f"Test passed on attempt {attempt}"
#     elif attempt < 3:
#          return f"Retrying... attempt {attempt} failed"
#     else:
#          return "FAIL: max retries reached"

# print(retry(1, False))


#############################

# def repponse(status_code, time):
#     if 200 <= status_code <= 299 and time <= 2000:
#         return "PASS"
#     elif 200 <= status_code <= 299 and time > 2000:
#         return "PASS with WARNING: slow response"
#     elif 400 <= status_code <= 499:
#             return "FAIL: client error"
#     else:
#             return "FAIL: server error" 

# print(repponse(500, 2000))
####################################

# def file_upload_check(filename, size):
#     filename = filename.lower()
#     if not filename:
#         return "FAIL: no file"
#     elif not filename.endswith(('.png', '.jpg', '.pdf')):
#         return "FAIL: invalid file type"
#     elif size > 5:
#         return "FAIL: file too large"
#     else:
#         return "PASS: file accepted"

# print(file_upload_check("text.pdf", 500))
     
################################

# def release_gate(unit_passed, api_passed, ui_passed, critical_bug_open):
#     if critical_bug_open:
#         return "Do not deploy"
#     elif unit_passed and api_passed and ui_passed:
#         return "Deploy to QA"
#     elif unit_passed and api_passed and not ui_passed:
#         return  "Deploy backend only"
#     elif not unit_passed:
#         return "Fix unit tests first"
#     else:
#         return "Hold release"

# print(release_gate(True,True, True, True))
#########################
# def password_strength(data):
#     if len(data) < 8:
#         return "FAIL: too short"
#     elif not any(ch.isdigit() for ch in data):
#         return "FAIL: needs a number"
#     else:
#         return "PASS: strong enough"

# print(password_strength("abc"))

##############################
# def check_severity(severity):
#     severity = severity.lower()
#     if severity == "blocker":
#         return "Stop testing, fix now"
#     elif severity == "critical":
#         return "Fix before release"
#     elif severity == "major":
#         return "Fix in current sprint"
#     elif severity == "minor":
#         return "Backlog"
#     else:
#         return "Invalid severity"
# print(check_severity("major"))     # Fix in current sprint
# print(check_severity("blocker"))   # Stop testing, fix now
# print(check_severity("low")) 
##########################
# def check(is_logged_in, session_expired):
#     if not is_logged_in:
#         return "Go to login page"
#     elif session_expired:
#         return  "Refresh session"
#     elif not session_expired:
#         return  "Continue test"
#     else:
#         return "Unknown auth state"

# print(check(True, False))
#########################2

# def status_check(actual_status, expected_status):
#     if actual_status == expected_status:
#         return "ASSERT PASS"
#     elif actual_status == 500:
#         return "ASSERT FAIL: server down"
#     elif actual_status == 404:
#         return "ASSERT FAIL: endpoint missing"
#     else:
#         return f"ASSERT FAIL: expected {expected_status}, got {actual_status}"

# print(status_check(200, 200))

################################
# def check_width(device):
#     if device == "mobile":
#         return "Width: 375"
#     elif device == "tablet":
#         return "Width: 768"
#     elif device =="desktop":
#         return "Width: 1440"
#     else:
#         return "Unsupported device"

# print(check_width("tablet"))

####################
# def test(fail_count, total_runs):
#     if fail_count == 0:
#         return "Stable"
#     elif fail_count == total_runs:
#         return "Always failing"
#     elif fail_count == 1:
#         return "Maybe flaky"
#     else:
#         return "Unstable"

# print(test(0, 10))   # Stable
# print(test(10, 10))  # Always failing
# print(test(1, 10))   # Maybe flaky
# print(test(3, 10)) 
################################
# def form_val(email):
#     if not email:
#         return "FAIL: email required"
#     elif "@" not in email:
#         return "FAIL: invalid email"
#     elif email.endswith("@test.com"):
#         return "PASS: test email"
#     else:
#         return "PASS: email format ok"

# print(form_val(""))
##################################
# def run_decision(suite_size, ci):
#     if suite_size >= 50 and ci:
#         return  "Run parallel"
#     elif suite_size < 50:
#         return "Run sequential on CI"
#     elif not ci:
#         return "Run local sequential"
#     else:
#         return "Invalid input"

# print(run_decision(50, True))

#################################
# def locator_fallback(found_by_id, found_by_css, found_by_xpath):
#     if found_by_id:
#         return "Use ID locator"
#     elif found_by_css:
#         return "Use CSS locator"
#     elif found_by_xpath:
#         return "Use XPath locator"
#     else:
#         return "FAIL: element not found"

# print(locator_fallback(False, False, True))
#############################################
