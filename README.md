SecureFix AI 🛡️
Detect. Repair. Verify. Secure.

SecureFix AI is an AI-assisted security analysis platform designed to identify potentially vulnerable code in C/C++ applications, particularly in IoT firmware.

It aims to help developers detect unsafe coding practices, understand security risks, and move towards safer code through AI-assisted repair and independent verification.



🚨 Problem Statement

C and C++ are widely used in embedded systems and IoT devices. However, unsafe memory operations, buffer overflows, and improper input handling can introduce serious security vulnerabilities.

Identifying and correcting these issues manually can be difficult, especially for beginners and developers working with resource-constrained systems.

💡 Our Solution

SecureFix AI provides a focused workflow for analysing potentially vulnerable C/C++ code.

It uses static analysis to identify suspicious coding patterns and presents findings with their severity, location, and explanations.

The platform is designed to extend this process with AI-assisted repair and security verification.

✨ Key Features

- Vulnerability Detection: Identifies potentially unsafe coding patterns in C/C++ source code.
- Severity Classification: Organises findings by security severity.
- Detailed Explanations: Displays the affected code location and vulnerability description.
- AI-Assisted Repair: Planned integration to suggest safer alternatives for vulnerable code.
- Security Rescanning: Designed to check suggested repairs for remaining known issues.
- Developer-Friendly Interface: Provides a simple interface to submit code and review scan results.

⚙️ Technology Stack

| Component | Technology |

| Frontend | React, TypeScript |
| Backend | Python, FastAPI |
| Static Analysis | Flawfinder |
| Deployment | Render |
| AI Integration | LLM-based repair (integration in progress) |

🔄 How It Works

1. Submit Code: The developer uploads or submits C/C++ source code.
2. Detect: The backend analyses the code using Flawfinder.
3. Explain: Security findings are presented with severity and descriptions.
4. Repair: The planned AI component suggests safer code alternatives.
5. Rescan: The repaired code can be checked again for known vulnerability patterns.
6. Verify: Further testing and verification are intended to strengthen confidence in the suggested changes.

🧪 Sample Test

The repository includes `vulnerable.c`, an intentionally vulnerable C program containing unsafe input handling using `gets()`.

It can be used to demonstrate how SecureFix AI identifies potentially unsafe operations such as buffer-overflow risks.

Important: This file is for static-analysis demonstration only. Do not compile or execute it.

🚀 Getting Started

 Prerequisites
- Python 3.12
- pip
- Git

Installation

Clone the repository:

bash
git clone YOUR_GITHUB_REPOSITORY_URL


Navigate to the project directory:

bash
cd YOUR_PROJECT_FOLDER


Install dependencies:

bash
pip install -r requirements.txt


Start the FastAPI application:

bash
uvicorn main:app --reload


Open the API documentation:

text
http://127.0.0.1:8000/docs


Note: These instructions assume `main.py` contains the FastAPI application and the required dependencies are listed in `requirements.txt`.

🔮 Future Scope

- Complete LLM-based code repair integration.
- Secure compilation and automated testing in an isolated environment.
- Support for additional vulnerability categories.
- More comprehensive security verification.
- Expanded support for IoT and embedded-system security workflows.

👥 Team

Team Name: The Debuggers  
Project: SecureFix AI

---

*SecureFix AI aims to make secure coding more accessible by combining static analysis with AI-assisted development and verification.*
