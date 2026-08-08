# Setup

1. Create a repo named exactly Atif0110/Atif0110 (must match your GitHub username), public.
2. Copy everything in this folder into the root of that repo, keeping the folder structure:
   README.md, scripts/, .github/workflows/refresh.yml
3. Push to main. Go to the repo's Actions tab and run "Refresh profile widgets" once manually
   (workflow_dispatch) so contribheatmap.svg, shiplog.svg, and the data files get generated for
   real from your actual GitHub activity.
4. infocard.svg is static (no API calls), already generated from your resume info. Edit the
   FIELDS list in scripts/make_info_card.py and rerun it whenever your facts change, then commit
   the updated infocard.svg.
5. Both Live App links and the Shravan repo link now point to your real projects. Double check
   the Power Market Forecasting and Churn Engine "Source on GitHub" links point at your actual
   repos once you confirm their names, right now they point at your profile root.

Note: the workflow uses the built in GITHUB_TOKEN for the shiplog API calls (higher rate limit)
and needs permissions: contents: write (already set in refresh.yml) so it can commit the
regenerated SVGs back to the repo.
