
from fastapi import FastAPI, Form, HTTPException
from fastapi.middleware.cors import CORSMiddleware
import subprocess
import tempfile
import os
import re

app = FastAPI(
    title="SecureFix AI",
    description="IoT firmware vulnerability detection and repair",
    version="1.0.0"
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=[
        "http://127.0.0.1:5500",
        "http://localhost:5500"
    ],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get("/")
def home():
    return {
        "message": "Welcome to SecureFix AI",
        "status": "Backend is running"
    }


@app.get("/health")
def health():
    return {
        "status": "healthy",
        "project": "SecureFix AI"
    }


def parse_report(report):
    findings = []

    pattern = re.compile(
        r"^(.*?):(\d+):\s+\[(\d+)\]\s+\((.*?)\)\s+([^:]+):\s*(.*)$"
    )

    lines = report.splitlines()

    for line in lines:
        match = pattern.match(line)

        if not match:
            continue

        file_path, line_no, level, category, function, description = match.groups()

        level = int(level)

        if level >= 4:
            severity = "High"
        elif level >= 2:
            severity = "Medium"
        else:
            severity = "Low"

        findings.append({
            "file": os.path.basename(file_path),
            "line": int(line_no),
            "level": level,
            "severity": severity,
            "category": category.strip(),
            "function": function.strip(),
            "description": description.strip()
        })

    return findings


@app.post("/scan")
async def scan_code(code: str = Form(...)):

    if not code.strip():
        raise HTTPException(
            status_code=400,
            detail="Code cannot be empty"
        )

    temp_path = None

    try:
        with tempfile.NamedTemporaryFile(
            mode="w",
            suffix=".c",
            delete=False,
            encoding="utf-8"
        ) as temp_file:
            temp_file.write(code)
            temp_path = temp_file.name

        result = subprocess.run(
            ["flawfinder", temp_path],
            capture_output=True,
            text=True,
            timeout=30
        )

        if result.returncode not in (0, 1):
            raise HTTPException(
                status_code=500,
                detail=result.stderr or "Scanner failed"
            )

        findings = parse_report(result.stdout)

        return {
            "status": "completed",
            "scanner": "Flawfinder",
            "total_vulnerabilities": len(findings),
            "high": sum(1 for f in findings if f["severity"] == "High"),
            "medium": sum(1 for f in findings if f["severity"] == "Medium"),
            "low": sum(1 for f in findings if f["severity"] == "Low"),
            "findings": findings,
            "report": result.stdout,
            "errors": result.stderr
        }

    except subprocess.TimeoutExpired:
        raise HTTPException(
            status_code=408,
            detail="Scan timed out"
        )

    except FileNotFoundError:
        raise HTTPException(
            status_code=500,
            detail="Flawfinder was not found. Please install Flawfinder."
        )

    finally:
        if temp_path and os.path.exists(temp_path):
            os.remove(temp_path)

