from enum import Enum
class roleEnum(str,Enum):
    admin = "admin"
    it = "it"
    marketing = "marketing"
    sales = "sales"
    frontend = "frontend"
    backend = "backend"
    hr = "hr"

class statusEnum(str,Enum):
    given="given"
    start="start"
    pending="pending"
    error="error"
    testing="testing"
    debug="debug"
    deployment="deployment"
    done="done"