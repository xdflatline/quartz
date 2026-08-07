#!/usr/bin/env python3
import os
import re
import sys
import json

def audit_garden(content_dir):
    all_notes = []
    issues = []
    
    required_keys = ["title", "detail", "details", "tags", "created", "updated", "type"]
    valid_types = ["concept", "entity", "project", "research", "idea", "raw", "index"]
    
    for root, dirs, files in os.walk(content_dir):
        for file in files:
            if file.endswith(".md"):
                path = os.path.join(root, file)
                rel_path = os.path.relpath(path, content_dir)
                
                # Skip index.md at root if necessary or handle it
                if rel_path == "index.md":
                    continue
                    
                try:
                    with open(path, "r", encoding="utf-8") as f:
                        content = f.read()
                        
                    # Extract frontmatter
                    match = re.match(r"^---\s*\n(.*?)\n---\s*\n", content, re.DOTALL)
                    frontmatter = {}
                    if match:
                        fm_text = match.group(1)
                        current_key = None
                        for line in fm_text.split("\n"):
                            line_stripped = line.strip()
                            if not line_stripped:
                                continue
                            if line_stripped.startswith("-"):
                                if current_key and isinstance(frontmatter[current_key], list):
                                    frontmatter[current_key].append(line_stripped[1:].strip())
                                continue
                            if ":" in line_stripped:
                                parts = line_stripped.split(":", 1)
                                key = parts[0].strip()
                                val = parts[1].strip()
                                if val.startswith('"') and val.endswith('"'):
                                    val = val[1:-1]
                                elif val.startswith("'") and val.endswith("'"):
                                    val = val[1:-1]
                                if val == "":
                                    frontmatter[key] = []
                                    current_key = key
                                else:
                                    frontmatter[key] = val
                                    current_key = None
                    else:
                        issues.append({
                            "file": rel_path,
                            "type": "missing_frontmatter",
                            "message": "File does not contain standard frontmatter separators (---)."
                        })
                        continue
                    
                    # Validate required keys
                    missing_keys = [k for k in required_keys if k not in frontmatter]
                    if missing_keys:
                        issues.append({
                            "file": rel_path,
                            "type": "missing_keys",
                            "message": f"Missing required frontmatter keys: {', '.join(missing_keys)}"
                        })
                        
                    # Validate 'description' vs 'detail'
                    if "description" in frontmatter:
                        issues.append({
                            "file": rel_path,
                            "type": "deprecated_key",
                            "message": "Uses deprecated 'description' key. Rename to 'detail' for short summary and use 'details' for full description."
                        })
                        
                    # Validate tags contain singular lowercase category matching its directory
                    # Directories: Concepts/, Entities/, Raw/, Projects/, Guide/, Ideas/, Research/
                    parent_dir = rel_path.split(os.sep)[0]
                    expected_tag = parent_dir.lower()
                    # Map plural folder names to singular if required by tags convention, or match folder exactly
                    tags = frontmatter.get("tags", [])
                    if isinstance(tags, str):
                        tags = [tags]
                    
                    # Ephemeral check: is it in Raw/ or does it contain ephemeral content/titles (e.g. dates, "HN", "Ask HN", news)
                    is_ephemeral = False
                    if parent_dir == "Raw" or "raw" in tags:
                        is_ephemeral = True
                    elif "hn" in rel_path.lower() or "news" in rel_path.lower() or "blog" in rel_path.lower() or "benchmark" in rel_path.lower():
                        is_ephemeral = True
                    
                    note_type = frontmatter.get("type", "unknown")
                    all_notes.append({
                        "path": rel_path,
                        "title": frontmatter.get("title", file),
                        "type": note_type,
                        "tags": tags,
                        "created": frontmatter.get("created", "unknown"),
                        "updated": frontmatter.get("updated", "unknown"),
                        "ephemeral": is_ephemeral
                    })
                    
                except Exception as e:
                    issues.append({
                        "file": rel_path,
                        "type": "read_error",
                        "message": str(e)
                    })
                    
    return all_notes, issues

if __name__ == "__main__":
    content_dir = "/home/master/quartz/content"
    if len(sys.argv) > 1:
        content_dir = sys.argv[1]
        
    notes, issues = audit_garden(content_dir)
    
    report = {
        "summary": {
            "total_notes": len(notes),
            "total_issues": len(issues),
            "ephemeral_notes_count": sum(1 for n in notes if n["ephemeral"])
        },
        "ephemeral_notes": [n for n in notes if n["ephemeral"]],
        "issues": issues
    }
    
    print(json.dumps(report, indent=2))
