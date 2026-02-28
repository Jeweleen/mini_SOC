from enum import Enum
from artifact import Artifact

class Case:
    def __init__(self, case_id: str):
        self.case_id = case_id
        self.status = CaseStatus.NEW
        self.severity = Severity.LOW
        self.artifacts: list[Artifact] = []
        self.notes: list[str] = []

    def add_artifact(self, artifact: Artifact):
        self.artifacts.append(artifact)
        self.recalculate_severity()

    def add_note(self, note: str):
        self.notes.append(note)

    def recalculate_severity(self):
        # Simple rules (you may adjust based on your data):
        # HIGH if any file hash present
        # MEDIUM if any external IP or suspicious domain keyword
        # LOW otherwise

        has_hash = any(a.indicator_type in ["file_hash", "hash", "sha256"] for a in self.artifacts)
        if has_hash:
            self.severity = Severity.HIGH
            return

        has_external_ip = any(
            a.indicator_type == "ip" and not a.is_internal_ip()
            for a in self.artifacts
        )
        has_suspicious_domain = any(
            a.indicator_type == "domain"
            and a.value 
            and any(word in a.value.lower() for word in ["login", "verify", "secure"])
            for a in self.artifacts
        )

        if has_external_ip or has_suspicious_domain:
            self.severity = Severity.MEDIUM
        else:
            self.severity = Severity.LOW

    def summary(self) -> str:
        return f"{self.case_id} | {self.status.value} | {self.severity.value} | artifacts={len(self.artifacts)}"

    def __str__(self) -> str:
        lines = [self.summary(), "-" * 48, "Artifacts:"]
        for a in self.artifacts:
            lines.append(f"  - {a}")
        if self.notes:
            lines.append("Notes:")
            for n in self.notes:
                lines.append(f"  * {n}")
        return "\n".join(lines)
    
##Create Enum for Severity and Status

class Severity(Enum):
    LOW = "LOW"
    MEDIUM = "MEDIUM"
    HIGH = "HIGH"

class CaseStatus(Enum):
    NEW = "NEW"
    INVESTIGATING = "INVESTIGATING"
    RESOLVED = "RESOLVED"
    FALSE_POSITIVE = "FALSE_POSITIVE"