# STAGE 2 PROMPT: Refine all 5 stories
Model: claude --haiku (one-shot, non-agentic)
Purpose: Take Stage 1 drafts and refine them into publish-ready articles

## INSTRUCTIONS
You are an editor for karmactive.com. Refine all 5 Stage 1 article drafts into publish-ready form. For each article:

1. **Read the existing Stage 1 draft from the consolidated file:** `/c/Users/Hp/OneDrive/karmactive-pipeline/stage1_all_stories_consolidated.md`
2. Apply karmactive editorial standards:
   - Ensure issue-first narrative is tight (open with the core problem/conflict)
   - Remove any hedging language, strengthen investigative framing
   - Ensure all [Source attribution needed] flags are either verified or kept as-is (do NOT fabricate)
   - Verify YAML frontmatter is complete and parseable
   - Check category taxonomy matches karmactive's system
   - Ensure no factual claims lack a primary source link
   - Tighten prose, remove redundancies
   - End each article with a forward-looking or accountability conclusion
3. Apply karmactive author conventions:
   - Sonali Tiwary = UK / Health / Policy focus
   - Sunita Somvanshi = Business / Policy / Social welfare focus
   - Rahul Somvanshi = Environment / Technology / Sustainability focus
   - Govind Tekale = Politics / Daily news / Wildlife focus
   - Karmactive Staff = General news, weather, general investigations
4. Save all 5 refined articles into a single consolidated file with clear separation

## OUTPUT
- File: `/c/Users/Hp/OneDrive/karmactive-pipeline/stage2_all_stories_final.md`
- Include: YAML frontmatter per article + full refined content
- Use karmactive's category taxonomy from memory:
  - Environment: climate, weather, sustainability
  - Health
  - UK (for UK-specific stories)
  - India
  - Australia
  - Business / Policy / Politics
  - Aviation / Disaster
- Total word count: 8,000-11,000 words across all 5 pieces

## COST CONTROL
--model haiku --max-budget-usd 0.75 --allowedTools "Read Edit Write" --add-dir /c/Users/Hp/OneDrive/karmactive-pipeline