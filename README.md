# sars-cov-2-mcleod
This repository contains all code and analysis pipelines used in the study of SARS-CoV-2 transmission dynamics in McLeod County, Minnesota, a densely sampled semi-rural community. The project evaluates whether intensive local genomic sampling can make a small community a reliable microcosm of broader regional transmission dynamics, and characterizes the limits of phylogenetic inference under realistic surveillance constraints.

Overview
McLeod County, MN achieved an unusually high SARS-CoV-2 genomic sampling proportion (~25–30%) during the pandemic, making it a rare opportunity to study semi-rural transmission. Using over 1,500 SARS-CoV-2 genomes collected between 2020 and 2024, this project applies phylogenetic and phylodynamic methods to:

- Compare variant frequency trajectories between McLeod County and the rest of Minnesota
- Infer viral introductions into and exports from McLeod County
- Characterize how sampling depth affects the reliability of phylogenetic inference via rarefaction analysis

Key finding: even with dense local sampling, introduction counts never stabilized, suggesting that reliable transmission inference requires sampling proportions that exceed what is practically achievable in semi-rural settings.

Installation
Requirements

Python 3.10+
Nextstrain Augur/Auspice (v23)
MAFFT
IQ-TREE
TreeTime
Baltic

Setup
Clone the repository:
bashgit clone https://github.com/moncla-lab/sars-cov-2-mcleod.git
cd sars-cov-2-mcleod
Install Python dependencies:
bashpip install -r requirements.txt
Install Nextstrain (if not already installed):
bashcurl -fsSL --proto '=https' https://nextstrain.org/cli/installer/linux | bash

Usage
1. Preprocessing & Metadata Harmonization
Scripts for cleaning and harmonizing sequence metadata (date, geography, vaccination status, age group, RUCA code, urban/rural status).
2. Sequencing Coverage Analysis
Compare weekly genomic sequence counts against confirmed COVID-19 case counts from the Minnesota Department of Health. Generates interactive HTML dashboards (Figures 1A and 1B).
Output: interactive HTML plots showing weekly sequences vs. cases and coverage tier (low/moderate/high) over the full pandemic timeline.
3. Nextstrain Phylogenetic Builds
Build time-resolved phylogenies using MAFFT, IQ-TREE, and TreeTime via the Nextstrain Augur pipeline. McLeod County sequences are combined with contextual sequences from the Twin Cities (TC_county), greater Minnesota (greater-MN), and other U.S. states (non-MN).
Metadata traits mapped include: vaccination status, RUCA code, state, urban/rural classification, age group, SARS-CoV-2 strain, Pango lineage, and source region.
4. Baltic Transition Parsing
Parse directional viral transitions (introductions into and exports from McLeod County) from Nextstrain time-scaled trees using the Baltic phylogenetic library.
5. Rarefaction Experiment
Incrementally subsample McLeod County sequences (50 to 700, in steps of 50, with 5 iterations each) against a fixed contextual backbone to generate rarefaction curves of introduction counts.
This produces rarefaction curves (Figure 3) showing whether introduction counts stabilize at an asymptote.
6. Variant Frequency Analysis
Estimate and visualize temporal lineage frequencies across McLeod, greater-MN, TC_county, and non-MN using augur frequencies.
Generates clade frequency plots for Alpha (GRY), Delta (GK), and Omicron (GRA) (Figures 4 and 5).

Data
Sequence data originates from two sources:

Minnesota sequences (n = 12,229): provided by the Minnesota Department of Health under a data use agreement. Includes 1,616 sequences from McLeod County and 10,613 from greater Minnesota.
Non-Minnesota sequences (n = 5,760): publicly available genomes from GISAID and GenBank (accession MN908947).


Due to the data use agreement with MDH, specific demographic information (age, vaccination status, geographic location) is not available in this public repository. Full metadata is available to authorized collaborators.


Citation
If you use this code or data, please cite:

Gorecki IR, Jaeger A, Malekshahi C, Maltepes M, Ort J, Morris K, Moncla LH. McLeod County as a Cautionary Case: What a Densely Sampled Semi-Rural Community Reveals About the Limits of Genomic Surveillance (2026).


Acknowledgements
This work was supported by the Centers for Disease Control and Prevention (CDC) and made possible by sequence and metadata provided by the Minnesota Department of Health (MDH). We thank Dr. Louise Moncla (PI), and Dr. Anna Jaeger (lead mentor) for their guidance throughout the project.
