# Topside Control Unit (TCU) 2025 Code Repository

Welcome to the repository for the **2025** new Topside Control Unit (TCU) of Vortex ROV! This README will guide you through the file structure and highlight the **new tab-based design** for controlling the ROV, adjusting settings, and managing mission-specific tasks.

## Table of Contents

- [Introduction](#introduction)
- [Installation](#installation)
- [Repository-Structure](#repository-structure)

## Introduction

The Topside Control Unit (TCU) is the primary interface for controlling the Vortex ROV during underwater operations. It enables operators to monitor real-time data, stream video feeds, and send commands to the ROV, ensuring precise control and mission success.

### **What's New in 2025**

- **Tab-Based Interface:** A redesigned UI integrates multiple tabs, each dedicated to different features—e.g., ROV control, settings, and mission-specific tools.
- **Increased Versatility & Customization:** Operators can tailor the TCU to specific tasks or preferences, enabling more efficient workflows.
- **High Performance:** Despite its enhanced flexibility, the TCU remains lightweight and responsive, ensuring seamless real-time operations.

## Installation

To set up the TCU software on your development environment, follow these steps:

1. **Clone the Repository:**
   ```bash
   git clone https://github.com/Vortex-ROV/TCUevo-Code.git
   cd TCUevo-Code
   ```
2. **Create and Activate a Virtual Environment:**

   It's a good practice to use a virtual environment to manage dependencies. Run the following commands to create and activate one:

   - On macOS/Linux:
     ```bash
     python3 -m venv venv
     source venv/bin/activate
     ```
   - On Windows:
     ```bash
     python -m venv venv
     venv\Scripts\activate
     ```
3. **Install Packaged Dependencies:**
   ```bash
   pip install .
   ```
4. **Run the TCU Software:**
   ```bash
   python main.py
   ```

## Repository Structure

- **`/src`:** Core source code for communication, control, and data processing.
- **`/tests`:** Test cases to validate the software's functionality and performance.
- **`main.py`:** Main script used to launch the TCU.
- **`pyproject.toml`:** Configuration file for packaging TCU code.
