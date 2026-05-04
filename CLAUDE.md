# Exoplanet Data Visualization Project

## Project Overview
Design and build an interactive data visualization for ~5,600 exoplanets to reveal discovery patterns and observational bias.

**Target Audiences:** High school students, college astronomy majors, data scientists

---

## Design Process & Rules

### Design Commit Requirement
✅ **DESIGN.md must be committed to git BEFORE any implementation code is written.**

Rationale: This ensures we have a clear specification that all audiences understand before development begins. Design comes first; implementation follows.

### Design Criteria
A successful visualization must:
- ✓ Work for all three audiences simultaneously (no separate versions)
- ✓ Tell a coherent story (not just "here's data")
- ✓ Accommodate missing data gracefully
- ✓ Highlight the detection bias narrative (core insight)
- ✓ Be implementable without overly complex code
- ✓ Avoid overwhelming new audiences (max 3-4 visual dimensions at once)

### Explanation Approach
- **Start simple:** Assume everyone knows what planets are, nothing more
- **Add layers:** Offer tooltips and expandable sections for deeper science
- **Avoid jargon:** Use plain language first, then define technical terms
- **Show context:** Always compare to Earth/solar system as reference

---

## Design Status

### Current Design: Timeline + Classification Tree
**File:** DESIGN.md (fully documented with goal, audience, story hypothesis, visualization spec, text diagram, risks, reverse direction scenarios, and success checklist)

**Status:** Ready for implementation (pending git commit)

**Key Design Elements:**
- **Section A:** Discovery Timeline (stacked area chart, 1995–2025)
- **Section B:** Planetary Classification (bubble chart by type)
- **Color:** Discovery method (timeline) and temperature (classification)
- **Interaction:** Cross-linking, tooltips, filters, drill-down capability

---

## Development Workflow

### Phase 1: Foundation (Next)
- [ ] Commit DESIGN.md to git (seal the design)
- [ ] Load and validate exoplanet data
- [ ] Clean data: handle missing values, categorize planet types
- [ ] Build discovery timeline (stacked area chart)
- [ ] Build planetary classification (bubble/bar chart)

### Phase 2: Integration
- [ ] Connect timeline and classification (cross-filtering)
- [ ] Add interactive tooltips for all audiences
- [ ] Color by discovery method (timeline) and temperature (classification)
- [ ] Add reference lines (year 2010, Earth baseline)

### Phase 3: Polish & Narrative
- [ ] Add headlines and annotations
- [ ] Create simple definitions for technical terms
- [ ] Add "Examples" when users click a planetary type
- [ ] Optimize for all three audience levels
- [ ] Mobile-responsive design

### Phase 4: Testing
- [ ] Test with high school student (can they understand the story?)
- [ ] Test with astronomy major (are technical details correct?)
- [ ] Test with data scientist (is methodology transparent?)

---

## Implementation Notes

### Technology Stack
- **Visualization Library:** Plotly or Observable Plot (easy interactivity, web-native)
- **Data Processing:** Python (Pandas) for cleaning and categorization
- **Hosting:** Observable, Streamlit, or GitHub Pages

### Data Files
- `exoplanets.csv` - Main dataset (5,600+ planets)
- `exoplanets_data_dictionary.csv` - Column definitions

### Key Data Columns
| Column | Purpose |
|--------|---------|
| `disc_year` | Timeline X-axis |
| `discoverymethod` | Timeline colors |
| `pl_rade` | Classification categories |
| `pl_bmasse` | Classification categories |
| `pl_eqt` | Classification color, habitability |

---

## Design Philosophy

### Rule: Data Drives Design
If implementation reveals unexpected patterns, the design will adapt:
- If timeline shows steady growth instead of acceleration → adjust narrative
- If Hot Jupiters aren't overrepresented → find another overrepresented type
- If audiences can't be satisfied with one design → add progressive disclosure layers

**The visualization serves the data, not vice versa.**

---

## References
- **NASA Exoplanet Archive:** nasa.gov/exoplanets (data source)
- **Habitable Zone:** ~250–350K for Earth-like conditions
- **Detection Bias:** Method used (Transit vs. Radial Velocity) determines what we can detect

---

## Contact & Questions
All design decisions are documented in DESIGN.md. Review that file before asking "why did we choose X?"
