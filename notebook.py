"""Tiny experiment logger. Run: python notebook.py add --title X --hypothesis Y --method Z --result R"""
import argparse,json
from datetime import datetime,timezone
from pathlib import Path
DB=Path("experiments.jsonl")
def add(a):
 row={"id":datetime.now(timezone.utc).strftime("%Y%m%dT%H%M%S%fZ"),"title":a.title,"hypothesis":a.hypothesis,"method":a.method,"result":a.result,"created_at":datetime.now(timezone.utc).isoformat()}
 with DB.open("a",encoding="utf-8") as f:f.write(json.dumps(row,ensure_ascii=False)+"\\n")
 print("Saved",row["id"])
def listing():
 if not DB.exists():print("No experiments logged.");return
 for line in DB.read_text(encoding="utf-8").splitlines():
  r=json.loads(line);print(r["id"],"|",r["title"],"|",r["result"])
p=argparse.ArgumentParser();s=p.add_subparsers(dest="cmd",required=True);a=s.add_parser("add")
for k in ("title","hypothesis","method","result"):a.add_argument("--"+k,required=True)
s.add_parser("list");x=p.parse_args();add(x) if x.cmd=="add" else listing()