# Playwright Demonstration
Repository to demonstrate main playwright features, using them during a presentation about Web Interface Tests (ACH2006 - Information Systems Engeneering)

---

## Environment Setup (WSL / Linux)

### 1. Create and activate the virtual environment
From the project root, create and activate the `.venv`:

```bash
python3 -m venv .venv
source .venv/bin/activate
```

---

### 2. Install Playwright and browser binaries
With .venv activated, install the Python package and download the browsers (Chromium, Firefox, WebKit) along with FFmpeg:

```bash
pip install playwright
playwright install
```

---

### 3. Install OS-level dependencies (WSL / Ubuntu)
To avoid missing shared library errors when launching browsers on Linux/WSL, run install-deps pointing explicitly to the executable inside .venv (since sudo typically resets PATH):

```bash
sudo .venv/bin/playwright install-deps
```

(Optional) To install dependencies for Chromium only:

```bash
sudo .venv/bin/playwright install-deps chromium
```

---

## Demonstrations
The scripts below illustrate core Playwright capabilities in Python for live demos or screen recordings used in the presentation.

### 1. Native Auto-Wait (`auto_wait.py`)
Demonstrates how Playwright automatically waits for elements to become attached, visible, enabled, and actionable without manual `sleep` calls or explicit wait statements.

```bash
python demonstrations/auto_wait.py
```

**What to observe / interact with:** A Chromium window opens with `slow_mo` enabled, navigates to the TodoMVC demo app, locates `input.new-todo`, fills `"Aprender Playwright"`, and presses `Enter` once the input is ready.

---

### 2. Isolated Browser Contexts (`multiple_contexts.py`)
Demonstrates session isolation using separate `BrowserContext` instances within the same browser process so cookies, storage, and authentication state are not shared between users.

```bash
python demonstrations/multiple_contexts.py
```

**What to observe / interact with:**
* **Context 1** opens the login page, signs in with `tomsmith` / `SuperSecretPassword!`, and verifies `"Secure Area"`.
* **Context 2** opens the same login URL in a separate session and verifies that `#username` remains empty (unauthenticated).
* *Tip:* Arrange both browser windows side by side before running to clearly show the isolated sessions.

---

### 3. Failure Analysis with Trace Viewer (`trace_viewer.py`)

Runs a script with tracing enabled that intentionally times out on a non-existent locator (`GhostElement123456`), saving `trace.zip` (along with execution video and HAR under the configured context options) so you can inspect the failure step by step.

**Run the test to generate the trace:**
```bash
python demonstrations/trace_viewer.py
```

**Open the Trace Viewer:**
```bash
playwright show-trace demonstrations/trace.zip
```

**What to observe / interact with:** Scrub through the top timeline to pinpoint the red failure step, inspect the visual page snapshots, examine the DOM state and action log, and review network activity in the **Network** tab.

---

### 4. Test Generation with Codegen (`no file`)

Launches the Playwright Inspector to record browser interactions and generate Python test code in real time.

```bash
playwright codegen --target python demo.playwright.dev
```

**What to observe / interact with:** Click links, type text, or interact with elements inside the browser window and watch the corresponding Python code appear in the Playwright Inspector window. Copy the generated snippet when finished.

---