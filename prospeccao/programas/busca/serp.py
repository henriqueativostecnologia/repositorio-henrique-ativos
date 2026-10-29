import json,sys,urllib.request,os,hashlib,time
S=os.path.dirname(os.path.abspath(__file__))
def search(params):
    key=hashlib.md5(json.dumps(params,sort_keys=True).encode()).hexdigest()
    f=f"{S}/raw/{key}.json"
    if os.path.exists(f): return json.load(open(f))
    body={"jsonrpc":"2.0","id":1,"method":"tools/call","params":{"name":"search","arguments":{"params":params}}}
    req=urllib.request.Request("https://mcp.serpapi.com/mcp",data=json.dumps(body).encode(),headers={"Content-Type":"application/json","Accept":"application/json, text/event-stream"})
    r=urllib.request.urlopen(req,timeout=120).read().decode()
    if r.startswith("event:") or "data:" in r[:20]:
        r=[l[5:] for l in r.splitlines() if l.startswith("data:")][-1]
    j=json.loads(r)
    with open(f"{S}/calls.log","a") as L: L.write(json.dumps(params)+"\n")
    res=j.get("result",{})
    txt=res.get("content",[{}])[0].get("text","") if res.get("content") else ""
    sc=res.get("structuredContent")
    try: data=json.loads(txt)
    except Exception: data={"_raw":txt,"_sc":sc,"_err":j.get("error")}
    json.dump(data,open(f,"w"),ensure_ascii=False)
    return data
if __name__=="__main__":
    d=search(json.loads(sys.argv[1])); print(json.dumps(d,ensure_ascii=False)[:2500])
