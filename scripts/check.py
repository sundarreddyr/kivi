"""Check the Maven module map and local Markdown links without a Java installation."""
from pathlib import Path
import re
import xml.etree.ElementTree as ET

root = Path(__file__).resolve().parents[1]
ns = {"m": "http://maven.apache.org/POM/4.0.0"}
reactor = ET.parse(root / "pom.xml")
for module in reactor.findall("m:modules/m:module", ns):
    pom = root / module.text / "pom.xml"
    child = ET.parse(pom)
    parent = child.findtext("m:parent/m:relativePath", namespaces=ns)
    if (pom.parent / parent).resolve() != root / "pom.xml":
        raise SystemExit(f"Invalid parent in {pom}")

for doc in [*root.glob("*.md"), *(root / "docs").rglob("*.md")]:
    for link in re.findall(r"\]\(([^)]+)\)", doc.read_text()):
        path = link.split("#", 1)[0]
        if path and "://" not in path and not (doc.parent / path).exists():
            raise SystemExit(f"Broken link in {doc.name}: {link}")
print("Maven module paths, XML and Markdown links OK")
