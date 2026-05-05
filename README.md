# DroidInspect

**Advanced Android Device Diagnostic, Inspection & Privacy Analysis Toolkit**

DroidInspect is a Python-based Android diagnostic toolkit built using **Android Debug Bridge (ADB)**.

It allows developers, testers, cybersecurity learners, and Android enthusiasts to inspect connected Android devices, analyze applications, monitor device health, perform permission audits, and generate detailed reports through an interactive terminal dashboard.

---

# Overview

DroidInspect provides deep Android device inspection directly from the terminal.

It combines:

* Android Diagnostics
* Device Monitoring
* Application Inspection
* Permission Analysis
* Privacy Risk Assessment
* Wireless Debugging
* Report Generation

The project was designed to demonstrate practical knowledge of:

* Python Automation
* Android System Communication
* Device Diagnostics
* Security Analysis
* CLI Application Development

---

# Core Features

---

## 1. Device Information Extraction

Retrieve detailed Android device specifications.

Includes:

* Device Model
* Brand
* Manufacturer
* Android Version
* Device Codename

Example:

```json id="az6w9m"
{
  "Model": "Redmi Note 12",
  "Brand": "Xiaomi",
  "Manufacturer": "Xiaomi",
  "Android Version": "14"
}
```

---

## 2. Battery Diagnostics

Analyze battery information in real time.

Displays:

* Battery Level
* Charging Status
* Battery Health
* Temperature
* Voltage

---

## 3. Storage Analysis

Inspect internal device storage.

Shows:

* Used Storage
* Free Storage
* Storage Utilization

---

## 4. Installed Applications Scanner

Lists all installed applications on the connected device.

Useful for:

* Application auditing
* Device inventory analysis

---

## 5. App Search

Search installed packages instantly by keyword.

Example:

```bash id="xdyb3v"
Enter app keyword: whatsapp
```

---

## 6. Screenshot Capture

Capture Android screenshots directly through terminal.

Generated Output:

```bash id="jryjs8"
screen.png
```

---

## 7. JSON Report Export

Generate structured JSON reports for diagnostics.

Output:

```bash id="pr8j8z"
report.json
```

---

## 8. PDF Report Export

Generate professional diagnostic reports.

Output:

```bash id="z3u4el"
device_report.pdf
```

---

## 9. Live Battery Monitor

Monitor battery status continuously in real time.

Useful for:

* Device stress testing
* Battery drain analysis

---

## 10. Wireless ADB Support

Connect to Android devices wirelessly after initial USB authorization.

Features:

* Enable Wireless Debugging
* Connect over TCP/IP
* Disconnect Wirelessly

Workflow:

1. Connect via USB
2. Enable Wireless ADB
3. Disconnect USB
4. Continue inspection wirelessly

---

## 11. Device Health Score

Calculates overall device health using:

* Battery Level
* Storage Utilization
* Diagnostic Metrics

Example:

```text id="74f8yf"
Health Score: 87/100
Status: Healthy
```

Health Categories:

* Healthy
* Moderate
* Critical

---

## 12. APK Inspector

Inspect detailed package metadata for installed applications.

Displays:

* Package Information
* Install Metadata
* Internal Components
* Runtime Configuration

---

## 13. Permission Security Audit

Analyzes sensitive Android app permissions.

Tracks access to:

* Camera
* Microphone
* Contacts
* Location
* SMS
* Call Logs
* Phone State
* Storage

Example:

```text id="64ygj0"
Camera: Allowed
Microphone: Allowed
Location: Allowed
SMS: Denied
```

---

## 14. Privacy Risk Analyzer

Evaluates installed apps using permission-based heuristic scoring.

Risk Levels:

* LOW
* MEDIUM
* HIGH

Example:

```text id="aq84qv"
com.whatsapp
Risk: HIGH
Score: 85
```

This does **not** detect malware.

It evaluates privacy exposure based on granted sensitive permissions.

---

## 15. Interactive CLI Dashboard

Professional menu-driven terminal interface.

Dashboard:

```text id="q4rqci"
========================================
         D R O I D  I N S P E C T
========================================

1. Device Info
2. Battery Info
3. Storage Info
4. Installed Apps
5. Capture Screenshot
6. Export JSON Report
7. Search App
8. Live Battery Monitor
9. Export PDF Report
10. Enable Wireless ADB
11. Connect Wirelessly
12. Disconnect Wireless
13. Device Health Score
14. APK Inspector
15. Permission Scanner
16. Suspicious Permission Report
17. Exit
```

---

# Technology Stack

## Programming Language

* Python 3

---

## Python Libraries

* Colorama
* ReportLab
* JSON
* Time
* Subprocess

---

## Android Tools

* Android Debug Bridge (ADB)

Android Debug Bridge

---

# Project Structure

```bash id="jghz6j"
DroidInspect/
│── main.py
│── adb_utils.py
│── device_info.py
│── battery.py
│── storage.py
│── apps.py
│── screenshot.py
│── report.py
│── pdf_report.py
│── monitor.py
│── dashboard.py
│── wireless.py
│── health.py
│── apk_inspector.py
│── permissions.py
│── risk_report.py
│── requirements.txt
│── README.md
│── screenshots/
│── reports/
```

---

# Installation

## Step 1: Clone Repository

```bash id="9eg0j5"
git clone https://github.com/yourusername/DroidInspect.git
cd DroidInspect
```

---

## Step 2: Install Dependencies

```bash id="7lln3h"
pip install -r requirements.txt
```

---

## Step 3: Install ADB

Install Android SDK Platform Tools.

Verify:

```bash id="x6q4h9"
adb version
```

Expected:

```bash id="z2e8m4"
Android Debug Bridge version ...
```

---

## Step 4: Enable Developer Options

On Android:

Settings → About Phone → Tap Build Number 7 times

Then:

Settings → Developer Options → Enable USB Debugging

---

## Step 5: Connect Device

Connect Android device using USB.

Verify:

```bash id="0az8me"
adb devices
```

Expected:

```bash id="cntrsy"
List of devices attached
XXXXXXXXXXXX    device
```

---

# Running DroidInspect

```bash id="kjx8rj"
python main.py
```

---

# Wireless Connection Setup

Initial USB authorization required.

Enable wireless:

```bash id="t4m8k3"
adb tcpip 5555
```

Connect:

```bash id="mjv8p2"
adb connect DEVICE_IP:5555
```

---

# Example Use Cases

## For Developers

Inspect Android test devices quickly.

---

## For QA Testers

Generate diagnostic reports for bug investigation.

---

## For Security Learners

Audit application permissions and privacy exposure.

---

## For Android Enthusiasts

Monitor device health and analyze installed apps.

---

# Learning Outcomes

This project demonstrates:

* Python Automation
* Android Device Communication
* ADB Integration
* Data Parsing
* Permission Analysis
* Heuristic Scoring Systems
* Report Generation
* CLI Dashboard Design
* Modular Programming

---

# Resume Project Description

**DroidInspect – Advanced Android Diagnostic & Privacy Analysis Toolkit**

Developed a Python-based Android diagnostic toolkit using ADB featuring device inspection, battery diagnostics, storage analysis, wireless debugging, permission auditing, privacy risk scoring, screenshot capture, and automated JSON/PDF report generation through an interactive CLI dashboard.

---

# Future Improvements

Planned upgrades:

* GUI Version using Tkinter
* Wireless Auto Device Discovery
* APK Static Analyzer
* Multi-device Monitoring
* HTML Dashboard Export
* Performance Benchmarking
* Crash Log Analyzer

---

# Contributing

Pull requests are welcome.

For major changes, open an issue first.

---

# License

MIT License

---

# Author

**Ajit Raj**

BCA Student | Python Developer | Cybersecurity Enthusiast

GitHub: https://github.com/amitraj231226-cmyk/DroidInspect.git

---

# Support

If you found this project useful, consider starring the repository.
