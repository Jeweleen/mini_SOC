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
        #extra = f" ({self.comment})" if self.comment else ""
        #return f"{self.indicator_type}: {self.file_hash}{extra}"
        ## I will need to check to see which indicator_type, based on that it will print the value
        
        extra = f" ({self.comment})" if self.comment else ""

        if self.indicator_type == "domain":
            val = self.domain
        elif self.indicator_type == "ip":
            val = self.ip
        elif self.indicator_type == "file_hash":
            val = self.file_hash
        else:
            val = ""

        return f"{self.indicator_type}: {val}{extra}"