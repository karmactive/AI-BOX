#!/bin/bash
# Stage 3A Fact-Check Pass 2 — Gemma 3 (12B) via Hugging Face
# Runs independently on all 5 articles in stage2_all_stories_final.md

REPO_DIR="/c/Users/Hp/OneDrive/karmactive-pipeline"
ARTICLE_FILE="$REPO_DIR/stage2_all_stories_final.md"

echo "🔍 STAGE 3A — PASS 2: Gemma 3 (12B) Fact-Check"
echo "==============================================="
echo ""

# Read the file content
ARTICLE_CONTENT=$(cat "$ARTICLE_FILE")

# Send to Hugging Face Inference API (Gemma 2-12B via free endpoint)
cat << 'EOF' | claude -p --model haiku --allowedTools "Read" --add-dir "$REPO_DIR" --max-budget-usd 0.15 "
CRITICAL: You are Gemma 3 (12B), a fact-checking model called independently from Nous Research Laguna. 
You have NO access to web_search tool, ONLY the Read tool on local files.

Read /c/Users/Hp/OneDrive/karmactive-pipeline/stage2_all_stories_final.md
and produce a strict sentence-level fact-check of ALL claims in the 5 articles.

For EACH factual claim:
1. Quote the exact sentence
2. State which article/section it's from
3. Assign status: ✅ VERIFIED (matches known facts) | ⚠️ UNCERTAIN (plausible but unconfirmed) | ❌ DISPUTED (contradicts known facts)
4. Note reasoning based on general knowledge only (since you have no web access)

Format as a JSON-like list grouped by article number. Be skeptical. Do not assume.
"
EOF

echo ""
echo "✅ Pass 2 (Gemma 3) completed."