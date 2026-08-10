import sys, time, json
sys.path.insert(0, r"C:\Users\Hp\AppData\Local\hermes")
from firefox_driver import FirefoxDriver, COMPOSER

draft = open(r"C:\Users\Hp\OneDrive\karmactive-pipeline\trial-hurricane-aug10\stage2_draft.md",
             encoding="utf-8").read()
# extract just the article body (between the '## Three Atlantic...' heading and '---')
start = draft.find("## Three Atlantic")
end = draft.find("\n---", start)
article = draft[start:end].strip()

d = FirefoxDriver(spawn=False)   # connect to the persistent geckodriver on 9445, reuse existing tabs

PROMPT = ("You are a professional fact checker. Fact-check the following news article sentence by sentence. "
          "For each sentence say: is it factual? Are there inaccuracies or made-up details? Cross-check the "
          "key numbers (NHC formation percentages, NOAA 2026 season counts, Saharan Air Layer wind speeds, "
          "Sept 10 peak) against what you know. Are the quoted statements factual? List any non-factual element, "
          "however minor, and the correction. Respond in a structured list per sentence. Keep it under 400 words.\n\n"
          "ARTICLE:\n" + article)

results = {}
for model in ["chatgpt","gemini","copilot"]:
    d._switch(d.tabs[model]); time.sleep(2)
    sel = COMPOSER[model]
    el = d._find_element(sel)
    if not el:
        results[model] = "NO COMPOSER"; continue
    d._element_clear(el); time.sleep(0.5)
    d._type_keys(el, PROMPT); time.sleep(1.5)
    d._press_enter_element(el)
    answered = False; last = ""
    for _ in range(10):   # up to 50s
        time.sleep(5)
        txt = d.read_response(model) or ""
        if len(txt) > len(article) + 150:   # answer clearly present
            answered = True; last = txt; break
        last = txt
    results[model] = {"answered": answered, "chars": len(last), "text": last[-2500:]}
    print(f"\n===== {model}: answered={answered} chars={len(last)} =====")
    print(last[-1200:])

d.close()
out = {m: (r if isinstance(r,str) else r.get("text","")) for m,r in results.items()}
with open(r"C:\Users\Hp\OneDrive\karmactive-pipeline\trial-hurricane-aug10\stage3a_factcheck.json","w",encoding="utf-8") as f:
    json.dump(out, f, indent=2, ensure_ascii=False)
print("\nSAVED stage3a_factcheck.json")
