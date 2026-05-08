# Security Policy Checker
# Evaluates organizational compliance with ISO 27001 basic controls

controls = [
    {
        "id": "A.5.1",
        "name": "Information Security Policy",
        "description": "A security policy document must exist and be approved by management",
        "implemented": False
    },
    {
        "id": "A.6.1",
        "name": "Internal Organization",
        "description": "Security roles and responsibilities must be defined",
        "implemented": False
    },
    {
        "id": "A.8.1",
        "name": "Asset Management",
        "description": "All information assets must be identified and inventoried",
        "implemented": False
    },
    {
        "id": "A.9.1",
        "name": "Access Control Policy",
        "description": "Access to information must be restricted based on business needs",
        "implemented": False
    },
    {
        "id": "A.12.1",
        "name": "Operational Procedures",
        "description": "Operating procedures must be documented and available",
        "implemented": False
    },
    {
        "id": "A.16.1",
        "name": "Incident Management",
        "description": "Procedures for reporting and handling security incidents must exist",
        "implemented": False
    },
    {
        "id": "A.18.1",
        "name": "Legal Compliance",
        "description": "All legal and regulatory requirements must be identified and documented",
        "implemented": False
    }
]

def run_assessment():
    print("=== ISO 27001 Security Policy Checker ===")
    print("Answer each control with yes (y) or no (n)\n")
    for control in controls:
        print(f"[{control['id']}] {control['name']}")
        print(f"    {control['description']}")
        answer = input("    Implemented? (y/n): ").strip().lower()
        control["implemented"] = answer == "y"
        print()

def generate_report():
    print("\n=== Compliance Report ===\n")
    implemented = 0
    for control in controls:
        status = "PASS" if control["implemented"] else "FAIL"
        print(f"[{status}] {control['id']} — {control['name']}")
        if control["implemented"]:
            implemented += 1

    total = len(controls)
    score = (implemented / total) * 100

    print(f"\nCompliance Score: {implemented}/{total} ({score:.1f}%)")

    if score == 100:
        print("Status: Fully Compliant")
    elif score >= 70:
        print("Status: Partially Compliant — improvements needed")
    elif score >= 40:
        print("Status: Low Compliance — significant gaps identified")
    else:
        print("Status: Non-Compliant — immediate action required")

run_assessment()
generate_report()