# Stage 3A Fact-Check Prompt (Haiku)
Model: Haiku (via claude CLI, print mode)
Instruction: Strict fact-check of all 5 articles in stage2_all_stories_final.md

## TASK
You are a fact-checker working independently on `stage2_all_stories_final.md`. For each factual claim in all 5 articles:

1. Identify the claim + article/section
2. Rate: ✅ VERIFIED | ⚠️ UNCERTAIN | ❌ DISPUTED  
3. Provide reasoning based on internal consistency, general knowledge, and source plausibility
4. Highlight any [Source attribution needed] flags needing external verification
5. Flag any claims contradicting known facts

## FOCUS AREAS
- Numerical claims (search volumes, death tolls, percentages)
- Proper names (people, organizations, places)
- Dates and timelines
- Scientific/technological facts
- Causal claims and policy implications

## OUTPUT FORMAT
Report per article, concise but thorough.