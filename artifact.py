class Artifact:
    def __init__(self, raw: dict):
        self.raw = raw

        # TODO: Replace these keys with the actual JSON field names
        # Replaced with indicator_type,domain,IP,file_hash,comment
        self.case_id = raw.get("case_id", "UNKNOWN_CASE")
        self.indicator_type = raw.get("indicator_type", "unknown")
        self.domain = raw.get("domain","")
        self.ip = raw.get("ip","")
        self.file_hash = raw.get("file_hash", "")
        self.comment = raw.get("comment", "")

    def is_internal_ip(self) -> bool:
        # only relevant if artifact_type indicates an IP
        if self.indicator_type != "ip":
            return False
        return self.ip.startswith(("10.", "192.168."))

    def __str__(self) -> str:
        extra = f" ({self.comment})" if self.comment else ""
        return f"{self.indicator_type}: {self.value}{extra}"

    @property
    def value(self) -> str:
        if self.indicator_type == "domain":
            return self.domain
        if self.indicator_type == "ip":
            return self.ip
        if self.indicator_type == "file_hash":
            return self.file_hash
        return ""