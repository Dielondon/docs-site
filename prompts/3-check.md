# Check

Read AGENTS.md, factory.conf and .factory/plan.md. Run the TEST_CMD from factory.conf, exactly as written.
Then read the diff ('git diff main') as an editor: is every new page linked from somewhere, are headings
consistent with the other pages, is anything inaccurate or contradicting another page, are there links
that leave these docs? If the link check fails, fix it, but only in files the plan names.
Do NOT fix the other findings: list each with a severity (high, medium, low) so the reviewer decides.
Write .factory/report.md with the final link-check output verbatim and the findings.
