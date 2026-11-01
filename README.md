🛡️ SecureFix AI

Detect. Repair. Verify. Secure.

SecureFix AI is a security-focused code analysis platform designed to identify potentially vulnerable coding patterns in C/C++ source code, with a focus on IoT firmware security.

It helps developers identify unsafe coding practices, understand potential security risks, and review vulnerability findings through a simple interface.

🚨 Problem Statement

C and C++ are widely used in embedded systems and IoT devices. However, unsafe memory operations, improper input handling, and buffer overflow vulnerabilities can expose these systems to security risks.

Finding such issues manually can be challenging and time-consuming.

💡 Our Solution

SecureFix AI provides a platform for analysing C/C++ source code using static analysis.

It uses Flawfinder to identify potentially unsafe functions and coding patterns, then presents findings with their severity, code location, and descriptions.

The project aims to extend this workflow with AI-assisted code repair and independent security verification.

✨ Current Features

Static Vulnerability Detection: Scans submitted C code using Flawfinder.

Severity Classification: Categorises findings as High, Medium, or Low.

Detailed Findings: Displays the affected file, line number, function, category, and description.

Code Submission: Accepts source code through the backend API.

Backend Health Check: Provides an endpoint to check backend availability.

Developer-Friendly Interface: Offers a frontend for submitting code and viewing scan results.

🔄 How It Works

Submit: The developer submits C source code through the application.

Scan: The FastAPI backend sends the submitted code to Flawfinder.

Analyse: The scanner identifies potentially unsafe coding patterns.

Classify: Findings are organised according to severity.

Review: Developers can inspect the reported issues and understand the associated risks.

⚙️ Technology Stack

Component

Technology

Frontend

React, TypeScript

Backend

Python, FastAPI

Static Analysis

Flawfinder

Server

Uvicorn

Deployment

Render

🧪 Sample Test

The repository includes vulnerable.c, an intentionally vulnerable C program containing unsafe input handling using gets().

It can be used to demonstrate how SecureFix AI detects potentially unsafe coding patterns.

Note: This file is intended for static-analysis demonstration only. Do not compile or execute it.

🚀 Getting Started

Prerequisites

Python 3.12 or compatible version

pip

Git

1. Clone the repository

git clone https://github.com/swastipatni-tech/SecureFix-AI.git

2. Navigate to the project directory

cd SecureFix-AI

3. Install dependencies

pip install -r requirements.txt

4. Start the backend server

uvicorn main:app --reload

5. Access the API

Backend: http://127.0.0.1:8000/

Health check: http://127.0.0.1:8000/health

API documentation: http://127.0.0.1:8000/docs

API Endpoints

Method

Endpoint

Purpose

GET

/

Backend welcome message

GET

/health

Backend health status

POST

/scan

Scan submitted C code

The /scan endpoint accepts source code through a multipart form field named code.

🔮 Future Scope

Integration of an LLM for AI-assisted vulnerability repair.

Independent security rescanning of suggested repairs.

Secure compilation and automated testing in an isolated environment.

Support for additional vulnerability categories.

Expanded analysis capabilities for IoT and embedded-system security.

👥 Team

Team Name: The Debuggers
Project Name: SecureFix AI

SecureFix AI aims to make secure coding more accessible through focused vulnerability detection and a roadmap towards AI-assisted repair and verification.
