# Playwright Demonstration
Repository to demonstrate main playwright features, using them during a presentation about Web Interface Tests (ACH2006 - Information Systems Engeneering)

## Environment Setup (WSL / Linux)

### 1. Create and activate the virtual environment
From the project root, create and activate the `.venv`:

```bash
python3 -m venv .venv
source .venv/bin/activate
```

### 2. Install Playwright and browser binaries
With .venv activated, install the Python package and download the browsers (Chromium, Firefox, WebKit) along with FFmpeg:

```bash
pip install playwright
playwright install
```

### 3. Install OS-level dependencies (WSL / Ubuntu)
To avoid missing shared library errors when launching browsers on Linux/WSL, run install-deps pointing explicitly to the executable inside .venv (since sudo typically resets PATH):

```bash
sudo .venv/bin/playwright install-deps
```

(Optional) To install dependencies for Chromium only:

```bash
sudo .venv/bin/playwright install-deps chromium
```