# Ground Rules for Exoplanet Visualization Project

## 1. AUDIENCE & EXPLANATION LEVEL

### Three Distinct Audiences

#### 1.1 High School Students (Ages 14-18)
**Baseline Knowledge:**
- Know what planets are
- Have basic idea of stars
- Unfamiliar with: Kepler's laws, spectroscopy, orbital mechanics

**Explanation Style:**
- Use analogies to Earth/solar system
- Avoid jargon; define technical terms plainly before using them
- Show "why this matters" (emotional connection)

**Learning Goal:**
- Inspire curiosity about space
- Understand that planets are diverse and common
- Answer the question: "Are we alone?"

---

#### 1.2 College Astronomy Majors (Undergrad/Grad)
**Baseline Knowledge:**
- Understand exoplanet detection methods (transit, radial velocity, imaging)
- Know about habitable zones and stellar properties
- Familiar with observational astronomy concepts

**Explanation Style:**
- Technical but accessible
- Welcome scientific terms with brief definitions
- Focus on methodology and data interpretation

**Learning Goal:**
- See data patterns and observational biases
- Use visualization as teaching tool for observational astronomy
- Understand how detection methods shape the sample

---

#### 1.3 Data Scientists (Any Background)
**Baseline Knowledge:**
- Strong in statistics, data visualization, coding
- Unfamiliar with: Exoplanet astrophysics details (but can learn quickly)

**Explanation Style:**
- Focus on data structure, bias, methodology
- Technical accuracy matters
- Discuss sampling bias, missing data patterns, data quality

**Learning Goal:**
- Understand dataset quality and limitations
- See visualization techniques for storytelling with data
- Assess methodology and potential biases

---

## 2. UNIFIED EXPLANATION APPROACH

All visualizations must follow these principles:

### 2.1 Start Simple
- Assume everyone knows what planets are, nothing more
- Do not assume prior knowledge of exoplanet science
- Introduce concepts layered (basic → technical)

### 2.2 Add Layers
- Offer tooltips and expandable sections for deeper science
- Progressive disclosure: simple labels first, detailed explanations on hover/click
- Let users control their depth of engagement

### 2.3 Avoid Jargon
- Use plain language first, then define technical terms
- Example: "Hot Jupiter" → "Jupiter-like planets that orbit extremely close to their star (closer than Mercury to our Sun)"
- Always explain the significance of technical details

### 2.4 Show Context
- Always compare to Earth/solar system as reference
- Example: Use "Earth radii" instead of just "km" for planet sizes
- Highlight what makes exoplanets unusual compared to what we know locally

---

## 3. DESIGN EVALUATION CRITERIA

A successful design must satisfy ALL of these criteria:

### ✓ Criterion 1: Multi-Audience Design
- Work for all three audiences simultaneously
- No separate versions for each audience
- A high schooler, an astronomy major, and a data scientist can all engage meaningfully

### ✓ Criterion 2: Coherent Story
- Tell a narrative, not just "here's data"
- Have a clear beginning (question), middle (exploration), end (insight)
- Each visualization should answer a specific question

### ✓ Criterion 3: Graceful Missing Data Handling
- Do not hide important planets due to missing values
- Show missing data explicitly where relevant
- Explain why some data is missing (e.g., "older discoveries lack this measurement")

### ✓ Criterion 4: Detection Bias Narrative
- Core insight: We haven't found a representative sample; we've found what's easiest to detect
- Visualize detection method dominance
- Show why certain planet types are overrepresented

### ✓ Criterion 5: Implementability
- Be implementable without overly complex code
- Use standard visualization libraries (Plotly, D3, Observable Plot, etc.)
- Data processing should be straightforward with Pandas/Python

### ✓ Criterion 6: Avoid Overwhelming Beginners
- Maximum 3-4 visual dimensions at once
- Do not combine: position (x, y) + size + color + shape + animation all at once
- Use progressive disclosure (basic chart → detailed view on interaction)

---

## 4. DESIGN PROCESS REQUIREMENTS

### 4.1 Design-First Approach
- **DESIGN.md must be committed to git BEFORE any implementation code is written**
- Rationale: Ensure clear specification that all audiences understand before development
- Design → Implementation (not implementation → documentation)

### 4.2 Design Exploration
- Explore at least 2 distinct design concepts before choosing
- Document why each was chosen or rejected
- Explain trade-offs and reasoning

### 4.3 Goal Restatement
- Agent must restate the goal before final design proposal
- Ensures alignment with original vision
- Prevents scope creep during design iteration

### 4.4 Explainability
- Design must be explainable without reading DESIGN.md
- If you need the document to understand why something was chosen, the design isn't clear enough
- Decisions should be self-evident from the visualization

### 4.5 Reverse Direction Scenarios
- Design must accommodate data-driven adjustments
- If implementation reveals unexpected patterns, design adapts
- Example: If timeline shows steady growth instead of acceleration, adjust narrative
- The visualization serves the data, not vice versa

### 4.6 Ground Rules Documentation
- All ground rules, audiences, and criteria must be saved and referenced
- Ensures consistency if multiple people work on the project
- Serves as reference for future design decisions

---

## 5. DATA-DRIVEN DESIGN PHILOSOPHY

**The visualization serves the data, not vice versa.**

### 5.1 If Data Contradicts Design Assumptions
- Timeline shows steady growth instead of acceleration? Adjust the narrative.
- Hot Jupiters aren't overrepresented? Find another overrepresented type.
- Audiences can't be satisfied with one design? Add progressive disclosure layers.

### 5.2 Integrity Over Aesthetics
- Accurate representation of data > beautiful visualization
- Missing data shown explicitly > hidden or misrepresented
- Limitations acknowledged > limitations ignored

### 5.3 Iterative Refinement
- Initial design is a hypothesis, not gospel
- Testing with real users may reveal needed changes
- Document changes and the reasoning behind them

---

## 6. SUCCESS MEASURES

### 6.1 High School Student Success
- [ ] Understands the main question without explanation
- [ ] Can state a key finding in one sentence
- [ ] Feels inspired or curious to learn more
- [ ] Does not feel lost or overwhelmed

### 6.2 Astronomy Major Success
- [ ] Recognizes detection method biases in the data
- [ ] Appreciates the methodology and data interpretation
- [ ] Can explain why certain planet types are overrepresented
- [ ] Sees this as a useful teaching tool

### 6.3 Data Scientist Success
- [ ] Can assess data quality and completeness
- [ ] Understands the sampling bias and its implications
- [ ] Appreciates the visualization techniques
- [ ] Recognizes the integrity of the analysis

### 6.4 Project Success
- [ ] All three audiences engage meaningfully without separate versions
- [ ] The visualization tells a coherent story
- [ ] Users leave understanding both WHAT we found and WHY we found it
- [ ] Design decisions are documented and justified

---

## 7. DECISION LOG

Use this section to track major design decisions and their rationale.

### Decision Template
```
**Decision:** [What decision was made?]
**Rationale:** [Why was this chosen?]
**Trade-offs:** [What was sacrificed?]
**Reverse Scenario:** [What if we're wrong? How would we adapt?]
**Status:** [Approved / Under Review / Rejected]
```

### Current Decisions

**Decision 1:** Two-view dashboard (Habitability Funnel + Discovery Deep Dive)  
**Rationale:** Combines emotional appeal (funnel for all audiences) with technical depth (timeline+classification for curious users)  
**Trade-offs:** Slightly more complex navigation; must ensure cross-view coherence  
**Reverse Scenario:** If users don't understand the connection, add bridging explanations  
**Status:** Approved

---

## 8. REFERENCES

- **Project Goal:** Reveal discovery patterns and observational bias in exoplanet data
- **Data Source:** NASA Exoplanet Archive (~5,600 planets)
- **Key Metrics:** Discovery year, detection method, planet radius, equilibrium temperature, planet mass
- **Habitable Zone:** ~250–350K for Earth-like conditions (simplified for general audience)
- **Detection Bias:** Transit method favors large, close-orbiting planets; Radial Velocity favors massive planets
