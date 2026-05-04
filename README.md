# Exoplanet Data Visualization

An interactive web visualization exploring discovery patterns and observational bias in exoplanet data.

## 🚀 Quick Start

1. **Open the visualization**: Simply open `index.html` in your web browser
2. **Explore**: Toggle between two complementary views:
   - **Habitability Funnel**: Shows how many planets could support life
   - **Discovery Deep Dive**: Reveals how and why we found what we found

## 📂 Project Structure

- `index.html` - Main interactive visualization (all-in-one HTML file, ~18KB)
- `data.json` - Pre-processed exoplanet data (~5.3KB)
- `generate_visualization.py` - Python script to generate data.json from raw CSV
- `DESIGN.md` - Complete design specification and design decisions
- `GROUND_RULES.md` - Project ground rules, audience definitions, and evaluation criteria
- `CLAUDE.md` - Project overview and development workflow
- `exoplanets.csv` - Raw data (1,174 exoplanets from NASA Exoplanet Archive)
- `exoplanets_data_dictionary.csv` - Data column definitions

## 🎨 Design Overview

### Two-View Dashboard

**View 1: Habitability Funnel** (Emotional entry point)
- Shows: All planets → Habitable zone → Earth-sized & habitable → Future potential
- Question: "Are we alone? How many planets could support life?"
- Best for: All audiences, especially high school students
- Key insight: Only 6 planets are both habitable temperature AND Earth-sized (0.51%)

**View 2: Discovery Deep Dive** (Technical exploration)
- Timeline: Shows discovery acceleration and method dominance (Transit = 96%)
- Classification: Shows planetary types and why certain types are overrepresented
- Explains: Why habitable planets are rare (detection bias, not true absence)
- Best for: Astronomy majors and data scientists

## 📊 Key Findings

- **1,174 exoplanets discovered** (2002–2025)
- **Only 37 in habitable zone** (250–350K, suitable for liquid water)
- **Only 6 Earth-sized & habitable** (0.51% of total)
- **Transit method dominates**: 96% of discoveries (detects large planets in close orbits)
- **Hot Jupiters overrepresented**: Easy to detect, not representative of true population
- **95% discovered after 2009**: Rapid acceleration in discovery rate

## 👥 Audiences

The visualization works for three audiences simultaneously:

1. **High School Students** 
   - Learn that planets are diverse and discovery is accelerating
   - Understand basic habitability criteria
   - Feel inspired about space exploration

2. **Astronomy Majors** 
   - See detection method biases in action
   - Understand why Hot Jupiters are overrepresented
   - Learn how observational methods shape the sample

3. **Data Scientists** 
   - Assess dataset quality and sampling bias
   - See visualization techniques for storytelling
   - Understand data cleaning and categorization logic

## 💻 Development

### Setup

1. **Install dependencies**:

   ```bash
   pnpm install
   # or npm install / yarn install
   ```

2. **Start dev server**:

   ```bash
   pnpm dev
   # Opens http://localhost:8080 in your browser automatically
   ```

3. **Start server without opening browser**:

   ```bash
   pnpm start
   # Server runs at http://localhost:8080
   ```

### Regenerate Data

If you modify the raw data or categorization logic:

```bash
python generate_visualization.py > data.json
```

Then refresh `index.html` in your browser (or reload the dev server).

## 🛠 Technologies

- **Visualization**: Plotly.js (interactive charts, no build step)
- **Data Processing**: Python with Pandas
- **Hosting**: Static HTML (works offline, no server needed)
- **Browser**: Works in all modern browsers (Chrome, Firefox, Safari, Edge)

## 📚 References

- **NASA Exoplanet Archive**: https://exoplanetarchive.ipac.caltech.edu/
- **Habitable Zone**: ~250–350K for Earth-like conditions (simplified definition)
- **Detection Methods**:
  - Transit: Measure dip in starlight when planet passes in front of star
  - Radial Velocity: Measure star's wobble caused by planet's gravity
  - Imaging: Direct detection of light reflected by planet

## 🎯 Design Principles

1. **Start Simple**: Funnel view answers the core question first (emotional entry point)
2. **Add Layers**: Deep Dive view provides technical context and explanation
3. **Avoid Jargon**: Technical terms defined on hover; Earth/solar system as reference
4. **Show Context**: Always compare to Earth; highlight what makes exoplanets unusual
5. **Data-Driven**: Visualization adapts if data contradicts initial assumptions

## 🚀 Future Enhancements (Phase 2+)

- [ ] Scatter plot for detailed exploration (multi-dimensional analysis)
- [ ] Filters by discovery method, planet type, star properties
- [ ] More detailed planet information in tooltips
- [ ] Mobile-responsive optimization
- [ ] Export data as CSV
- [ ] Statistical analysis and correlation tools
- [ ] Timeline animation showing discoveries over time
- [ ] Comparison view (discovered vs. theoretically possible)

## 📋 Project Status

✅ **Design Phase Complete** (DESIGN.md and GROUND_RULES.md committed)
✅ **Phase 1: Foundation** (Data loading, cleaning, categorization)
✅ **Phase 2: Visualization** (HTML with Plotly.js charts)
⏳ **Phase 3: Integration** (Cross-view linking, advanced filters)
⏳ **Phase 4: Polish** (Mobile optimization, accessibility)
⏳ **Phase 5: Testing** (User testing with all three audiences)

## 📖 For Developers

See `DESIGN.md` and `GROUND_RULES.md` for detailed design documentation:
- Design choices and why they were made
- Target audiences and explanation approaches
- Evaluation criteria and success metrics
- Data-driven design philosophy
- Reverse direction scenarios (how design adapts if data is unexpected)

The code follows the design specification exactly. If you want to modify the visualization, first review the design document to understand the constraints and trade-offs.
