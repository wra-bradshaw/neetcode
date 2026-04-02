class Solution:
    DELIMITER = ";"
    ESCAPE_CHAR = "\\"

    def escape_char(self, s: str) -> str:
        if s[0] == ";":
            return "\\;"
        elif s[0] == "\\":
            return "\\\\"
        return s[0]

    def escape(self, s: str) -> str:
        return "".join([self.escape_char(c) for c in s])        

    def unescape(self, s: str) -> str:
        out: List[str] = []

        is_currently_escaped = False
        for i, c in enumerate(s):
            if is_currently_escaped:
                out.append(c)
                is_currently_escaped = False
            elif c == "\\":
                is_currently_escaped = True
            else:
                out.append(c)
        
        return "".join(out)

    def encode(self, strs: List[str]) -> str:
        if len(strs) == 0:
            return ""
        escaped = [re.escape(s) for s in strs]
        print(";".join(escaped) + ";")
        return ";".join(escaped) + ";"

    def decode(self, s: str) -> List[str]:
        unescaped: List[str] = []
        is_currently_escaped = False
        last_idx = 0

        for i, c in enumerate(s):
            if is_currently_escaped:
                print("is_currently_escaped=False")
                is_currently_escaped = False
            elif c == "\\":
                print("is_currently_escaped=True")
                is_currently_escaped = True
            elif c == ";":
                unescaped.append(s[last_idx:i])
                last_idx = i+1

        return [self.unescape(s) for s in unescaped]

