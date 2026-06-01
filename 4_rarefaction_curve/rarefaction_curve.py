#!/usr/bin/env python
# coding: utf-8

# In[3]:


import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import os
import glob

# --- Step 1: Collect all transition files ---
all_records = []

folders = glob.glob("clusters_*_seqs_trial_*")

for folder in folders:
    try:
        # Extract metadata from folder name
        # Example: clusters_50_seqs_trial_5
        parts = folder.split("_")
        seq_count = int(parts[1])
        trial = int(parts[-1])

        # Find the transitions file inside the folder
        file_path = glob.glob(os.path.join(folder, "*transitions_parsedon_TCstatus.tsv"))[0]

        df = pd.read_csv(file_path, sep="\t")

        # --- Step 2: Filter for TC → McLeod transitions ---
        tc_df = df[df["Transition"] == "TC_county_mcleod"].copy()

        # Count total transitions in this trial
        count = tc_df["Count"].sum()

        all_records.append({
            "seq_count": seq_count,
            "trial": trial,
            "Count": count
        })

    except Exception as e:
        print(f"Skipping {folder}: {e}")

# --- Step 3: Build combined dataframe ---
combined_df = pd.DataFrame(all_records)

# --- Step 4: Aggregate (same logic as your original script) ---
summary = (
    combined_df
    .groupby("seq_count", as_index=False)
    .agg(
        mean_count=("Count", "mean"),
        std_count=("Count", "std"),
        n_trials=("Count", "count")
    )
    .sort_values("seq_count")
)

summary["std_count"] = summary["std_count"].fillna(0)
summary["sem"] = summary["std_count"] / np.sqrt(summary["n_trials"])

# --- Step 5: Plot rarefaction curve ---
fig, ax = plt.subplots(figsize=(8, 6))

ax.errorbar(
    summary["seq_count"],
    summary["mean_count"],
    yerr=summary["sem"],
    fmt='-o',
    capsize=4,
    linewidth=1.5,
    markersize=6,
    elinewidth=1.2
)

ax.set_title('Rarefaction Curve (TC County → McLeod)', fontsize=13, pad=12)
ax.set_xlabel('Sequences from McLeod', fontsize=11)
ax.set_ylabel('Introductions into McLeod (TC County)', fontsize=11)

ax.grid(True, linewidth=0.8)
ax.set_axisbelow(True)

plt.tight_layout()
plt.savefig('rarefaction_TC_county_mcleod.png', dpi=150, bbox_inches='tight')
plt.show()


# In[5]:


import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import os
import glob

# --- Step 1: Collect all transition files ---
all_records = []

folders = glob.glob("clusters_*_seqs_trial_*")

for folder in folders:
    try:
        # Extract metadata from folder name
        # Example: clusters_50_seqs_trial_5
        parts = folder.split("_")
        seq_count = int(parts[1])
        trial = int(parts[-1])

        # Find the transitions file inside the folder
        file_path = glob.glob(os.path.join(folder, "*transitions_parsedon_TCstatus.tsv"))[0]

        df = pd.read_csv(file_path, sep="\t")

        # --- Step 2: Filter for TC → McLeod transitions ---
        tc_df = df[df["Transition"] == "greater-MN_mcleod"].copy()

        # Count total transitions in this trial
        count = tc_df["Count"].sum()

        all_records.append({
            "seq_count": seq_count,
            "trial": trial,
            "Count": count
        })

    except Exception as e:
        print(f"Skipping {folder}: {e}")

# --- Step 3: Build combined dataframe ---
combined_df = pd.DataFrame(all_records)

# --- Step 4: Aggregate (same logic as your original script) ---
summary = (
    combined_df
    .groupby("seq_count", as_index=False)
    .agg(
        mean_count=("Count", "mean"),
        std_count=("Count", "std"),
        n_trials=("Count", "count")
    )
    .sort_values("seq_count")
)

summary["std_count"] = summary["std_count"].fillna(0)
summary["sem"] = summary["std_count"] / np.sqrt(summary["n_trials"])

# --- Step 5: Plot rarefaction curve ---
fig, ax = plt.subplots(figsize=(8, 6))

ax.errorbar(
    summary["seq_count"],
    summary["mean_count"],
    yerr=summary["sem"],
    fmt='-o',
    capsize=4,
    linewidth=1.5,
    markersize=6,
    elinewidth=1.2
)

ax.set_title('Rarefaction Curve (Greater MN → McLeod)', fontsize=13, pad=12)
ax.set_xlabel('Sequences from McLeod', fontsize=11)
ax.set_ylabel('Introductions into McLeod (Greater MN)', fontsize=11)

ax.grid(True, linewidth=0.8)
ax.set_axisbelow(True)

plt.tight_layout()
plt.savefig('rarefaction_greater-MN_mcleod.png', dpi=150, bbox_inches='tight')
plt.show()


# In[6]:


import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import os
import glob

# --- Step 1: Collect all transition files ---
all_records = []

folders = glob.glob("clusters_*_seqs_trial_*")

for folder in folders:
    try:
        # Extract metadata from folder name
        # Example: clusters_50_seqs_trial_5
        parts = folder.split("_")
        seq_count = int(parts[1])
        trial = int(parts[-1])

        # Find transitions file
        file_path = glob.glob(os.path.join(folder, "*transitions_parsedon_TCstatus.tsv"))[0]

        df = pd.read_csv(file_path, sep="\t")

        # --- Step 2: Filter for Greater MN → McLeod ---
        gmn_df = df[df["Transition"] == "non-MN_mcleod"].copy()

        # Count total transitions in this trial
        count = gmn_df["Count"].sum()

        all_records.append({
            "seq_count": seq_count,
            "trial": trial,
            "Count": count
        })

    except Exception as e:
        print(f"Skipping {folder}: {e}")

# --- Step 3: Combine all trials ---
combined_df = pd.DataFrame(all_records)

# --- Sanity check (optional but recommended) ---
print("Trials per sequencing depth:")
print(combined_df.groupby("seq_count")["trial"].count())

# --- Step 4: Aggregate across trials ---
summary = (
    combined_df
    .groupby("seq_count", as_index=False)
    .agg(
        mean_count=("Count", "mean"),
        std_count=("Count", "std"),
        n_trials=("Count", "count")
    )
    .sort_values("seq_count")
)

summary["std_count"] = summary["std_count"].fillna(0)
summary["sem"] = summary["std_count"] / np.sqrt(summary["n_trials"])

# --- Confirm trial counts ---
print("\nSummary (should be 5 trials each):")
print(summary[["seq_count", "n_trials"]])

# --- Step 5: Plot rarefaction curve ---
fig, ax = plt.subplots(figsize=(8, 6))

ax.errorbar(
    summary["seq_count"],
    summary["mean_count"],
    yerr=summary["sem"],
    fmt='-o',
    capsize=4,
    linewidth=1.5,
    markersize=6,
    elinewidth=1.2
)

ax.set_title('Rarefaction Curve (Non MN → McLeod)', fontsize=13, pad=12)
ax.set_xlabel('Sequences from McLeod', fontsize=11)
ax.set_ylabel('Introductions into McLeod (Non MN)', fontsize=11)

ax.grid(True, linewidth=0.8)
ax.set_axisbelow(True)

plt.tight_layout()
plt.savefig('rarefaction_non-MN_mcleod.png', dpi=150, bbox_inches='tight')
plt.show()


# In[7]:


import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import os
import glob

# --- Step 1: Define transitions of interest ---
TRANSITIONS = {
    "TC_county_mcleod": "TC County",
    "greater-MN_mcleod": "Greater MN",
    "non-MN_mcleod": "Non-MN"
}

# --- Step 2: Collect all transition files ---
all_records = []

folders = glob.glob("clusters_*_seqs_trial_*")

for folder in folders:
    try:
        # Extract metadata
        parts = folder.split("_")
        seq_count = int(parts[1])
        trial = int(parts[-1])

        # Locate file
        file_path = glob.glob(os.path.join(folder, "*transitions_parsedon_TCstatus.tsv"))[0]
        df = pd.read_csv(file_path, sep="\t")

        # --- Extract counts for each transition type ---
        for key in TRANSITIONS.keys():
            subset = df[df["Transition"] == key]
            count = subset["Count"].sum()

            all_records.append({
                "seq_count": seq_count,
                "trial": trial,
                "Transition": key,
                "Count": count
            })

    except Exception as e:
        print(f"Skipping {folder}: {e}")

# --- Step 3: Build dataframe ---
combined_df = pd.DataFrame(all_records)

# --- Optional sanity check ---
print("\nTrials per group:")
print(combined_df.groupby(["Transition", "seq_count"])["trial"].count().unstack(0))

# --- Step 4: Aggregate ---
summary = (
    combined_df
    .groupby(["Transition", "seq_count"], as_index=False)
    .agg(
        mean_count=("Count", "mean"),
        std_count=("Count", "std"),
        n_trials=("Count", "count")
    )
)

summary["std_count"] = summary["std_count"].fillna(0)
summary["sem"] = summary["std_count"] / np.sqrt(summary["n_trials"])

# --- Step 5: Plot ---
fig, ax = plt.subplots(figsize=(9, 6))

colors = {
    "TC_county_mcleod": "steelblue",
    "greater-MN_mcleod": "orange",
    "non-MN_mcleod": "crimson"
}

for transition, label in TRANSITIONS.items():
    sub = summary[summary["Transition"] == transition].sort_values("seq_count")

    ax.errorbar(
        sub["seq_count"],
        sub["mean_count"],
        yerr=sub["sem"],
        fmt='-o',
        capsize=4,
        linewidth=1.8,
        markersize=6,
        elinewidth=1.2,
        label=label,
        color=colors[transition]
    )

# --- Labels ---
ax.set_title('Rarefaction Curves by Source → McLeod', fontsize=14, pad=12)
ax.set_xlabel('Sequences from McLeod', fontsize=11)
ax.set_ylabel('Introductions into McLeod', fontsize=11)

ax.grid(True, linewidth=0.8)
ax.set_axisbelow(True)

# --- Legend ---
ax.legend(title="Source Region")

plt.tight_layout()
plt.savefig('rarefaction_all_sources_mcleod.png', dpi=150, bbox_inches='tight')
plt.show()


# In[8]:


import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import os
import glob

# --- Step 1: Collect all transition files ---
all_records = []

folders = glob.glob("clusters_*_seqs_trial_*")

for folder in folders:
    try:
        # Extract metadata from folder name
        # Example: clusters_50_seqs_trial_5
        parts = folder.split("_")
        seq_count = int(parts[1])
        trial = int(parts[-1])

        # Find the transitions file inside the folder
        file_path = glob.glob(os.path.join(folder, "*transitions_parsedon_TCstatus.tsv"))[0]

        df = pd.read_csv(file_path, sep="\t")

        # --- Step 2: Filter for TC → McLeod transitions ---
        tc_df = df[df["Transition"] == "mcleod_TC_county"].copy()

        # Count total transitions in this trial
        count = tc_df["Count"].sum()

        all_records.append({
            "seq_count": seq_count,
            "trial": trial,
            "Count": count
        })

    except Exception as e:
        print(f"Skipping {folder}: {e}")

# --- Step 3: Build combined dataframe ---
combined_df = pd.DataFrame(all_records)

# --- Step 4: Aggregate (same logic as your original script) ---
summary = (
    combined_df
    .groupby("seq_count", as_index=False)
    .agg(
        mean_count=("Count", "mean"),
        std_count=("Count", "std"),
        n_trials=("Count", "count")
    )
    .sort_values("seq_count")
)

summary["std_count"] = summary["std_count"].fillna(0)
summary["sem"] = summary["std_count"] / np.sqrt(summary["n_trials"])

# --- Step 5: Plot rarefaction curve ---
fig, ax = plt.subplots(figsize=(8, 6))

ax.errorbar(
    summary["seq_count"],
    summary["mean_count"],
    yerr=summary["sem"],
    fmt='-o',
    capsize=4,
    linewidth=1.5,
    markersize=6,
    elinewidth=1.2
)

ax.set_title('Rarefaction Curve (McLeod → TC County)', fontsize=13, pad=12)
ax.set_xlabel('Sequences from McLeod', fontsize=11)
ax.set_ylabel('Introductions into TC County (McLeod)', fontsize=11)

ax.grid(True, linewidth=0.8)
ax.set_axisbelow(True)

plt.tight_layout()
plt.savefig('rarefaction_mcleod_TC_county.png', dpi=150, bbox_inches='tight')
plt.show()


# In[9]:


import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import os
import glob

# --- Step 1: Collect all transition files ---
all_records = []

folders = glob.glob("clusters_*_seqs_trial_*")

for folder in folders:
    try:
        # Extract metadata from folder name
        # Example: clusters_50_seqs_trial_5
        parts = folder.split("_")
        seq_count = int(parts[1])
        trial = int(parts[-1])

        # Find the transitions file inside the folder
        file_path = glob.glob(os.path.join(folder, "*transitions_parsedon_TCstatus.tsv"))[0]

        df = pd.read_csv(file_path, sep="\t")

        # --- Step 2: Filter for TC → McLeod transitions ---
        tc_df = df[df["Transition"] == "mcleod_greater-MN"].copy()

        # Count total transitions in this trial
        count = tc_df["Count"].sum()

        all_records.append({
            "seq_count": seq_count,
            "trial": trial,
            "Count": count
        })

    except Exception as e:
        print(f"Skipping {folder}: {e}")

# --- Step 3: Build combined dataframe ---
combined_df = pd.DataFrame(all_records)

# --- Step 4: Aggregate (same logic as your original script) ---
summary = (
    combined_df
    .groupby("seq_count", as_index=False)
    .agg(
        mean_count=("Count", "mean"),
        std_count=("Count", "std"),
        n_trials=("Count", "count")
    )
    .sort_values("seq_count")
)

summary["std_count"] = summary["std_count"].fillna(0)
summary["sem"] = summary["std_count"] / np.sqrt(summary["n_trials"])

# --- Step 5: Plot rarefaction curve ---
fig, ax = plt.subplots(figsize=(8, 6))

ax.errorbar(
    summary["seq_count"],
    summary["mean_count"],
    yerr=summary["sem"],
    fmt='-o',
    capsize=4,
    linewidth=1.5,
    markersize=6,
    elinewidth=1.2
)

ax.set_title('Rarefaction Curve (McLeod → Greater MN)', fontsize=13, pad=12)
ax.set_xlabel('Sequences from McLeod', fontsize=11)
ax.set_ylabel('Introductions into Greater MN (McLeod)', fontsize=11)

ax.grid(True, linewidth=0.8)
ax.set_axisbelow(True)

plt.tight_layout()
plt.savefig('rarefaction_mcleod_greater-MN.png', dpi=150, bbox_inches='tight')
plt.show()


# In[10]:


import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import os
import glob

# --- Step 1: Collect all transition files ---
all_records = []

folders = glob.glob("clusters_*_seqs_trial_*")

for folder in folders:
    try:
        # Extract metadata from folder name
        # Example: clusters_50_seqs_trial_5
        parts = folder.split("_")
        seq_count = int(parts[1])
        trial = int(parts[-1])

        # Find the transitions file inside the folder
        file_path = glob.glob(os.path.join(folder, "*transitions_parsedon_TCstatus.tsv"))[0]

        df = pd.read_csv(file_path, sep="\t")

        # --- Step 2: Filter for TC → McLeod transitions ---
        tc_df = df[df["Transition"] == "mcleod_non-MN"].copy()

        # Count total transitions in this trial
        count = tc_df["Count"].sum()

        all_records.append({
            "seq_count": seq_count,
            "trial": trial,
            "Count": count
        })

    except Exception as e:
        print(f"Skipping {folder}: {e}")

# --- Step 3: Build combined dataframe ---
combined_df = pd.DataFrame(all_records)

# --- Step 4: Aggregate (same logic as your original script) ---
summary = (
    combined_df
    .groupby("seq_count", as_index=False)
    .agg(
        mean_count=("Count", "mean"),
        std_count=("Count", "std"),
        n_trials=("Count", "count")
    )
    .sort_values("seq_count")
)

summary["std_count"] = summary["std_count"].fillna(0)
summary["sem"] = summary["std_count"] / np.sqrt(summary["n_trials"])

# --- Step 5: Plot rarefaction curve ---
fig, ax = plt.subplots(figsize=(8, 6))

ax.errorbar(
    summary["seq_count"],
    summary["mean_count"],
    yerr=summary["sem"],
    fmt='-o',
    capsize=4,
    linewidth=1.5,
    markersize=6,
    elinewidth=1.2
)

ax.set_title('Rarefaction Curve (McLeod → Non MN)', fontsize=13, pad=12)
ax.set_xlabel('Sequences from McLeod', fontsize=11)
ax.set_ylabel('Introductions into Non MN (McLeod)', fontsize=11)

ax.grid(True, linewidth=0.8)
ax.set_axisbelow(True)

plt.tight_layout()
plt.savefig('rarefaction_mcleod_non-MN.png', dpi=150, bbox_inches='tight')
plt.show()


# In[11]:


import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import os
import glob

# --- Step 1: Define transitions of interest ---
TRANSITIONS = {
    "TC_county_mcleod": "TC County",
    "greater-MN_mcleod": "Greater MN",
    "non-MN_mcleod": "Non-MN"
}

REVERSE_TRANSITIONS = {
    "mcleod_TC_county": "TC County",
    "mcleod_greater-MN": "Greater MN",
    "mcleod_non-MN": "Non-MN"
}

# --- Step 2: Collect all transition files ---
all_records = []
folders = glob.glob("clusters_*_seqs_trial_*")
for folder in folders:
    try:
        # Extract metadata
        parts = folder.split("_")
        seq_count = int(parts[1])
        trial = int(parts[-1])

        # Locate file
        file_path = glob.glob(os.path.join(folder, "*transitions_parsedon_TCstatus.tsv"))[0]
        df = pd.read_csv(file_path, sep="\t")

        # --- Extract counts for forward transitions (source → McLeod) ---
        for key in TRANSITIONS.keys():
            subset = df[df["Transition"] == key]
            count = subset["Count"].sum()
            all_records.append({
                "seq_count": seq_count,
                "trial": trial,
                "Transition": key,
                "Direction": "into_mcleod",
                "Count": count
            })

        # --- Extract counts for reverse transitions (McLeod → source) ---
        for key in REVERSE_TRANSITIONS.keys():
            subset = df[df["Transition"] == key]
            count = subset["Count"].sum()
            all_records.append({
                "seq_count": seq_count,
                "trial": trial,
                "Transition": key,
                "Direction": "from_mcleod",
                "Count": count
            })

    except Exception as e:
        print(f"Skipping {folder}: {e}")

# --- Step 3: Build dataframe ---
combined_df = pd.DataFrame(all_records)

# --- Optional sanity check ---
print("\nTrials per group (into McLeod):")
fwd = combined_df[combined_df["Direction"] == "into_mcleod"]
print(fwd.groupby(["Transition", "seq_count"])["trial"].count().unstack(0))

print("\nTrials per group (from McLeod):")
rev = combined_df[combined_df["Direction"] == "from_mcleod"]
print(rev.groupby(["Transition", "seq_count"])["trial"].count().unstack(0))

# --- Step 4: Aggregate ---
summary = (
    combined_df
    .groupby(["Transition", "Direction", "seq_count"], as_index=False)
    .agg(
        mean_count=("Count", "mean"),
        std_count=("Count", "std"),
        n_trials=("Count", "count")
    )
)
summary["std_count"] = summary["std_count"].fillna(0)
summary["sem"] = summary["std_count"] / np.sqrt(summary["n_trials"])

# --- Step 5: Plot ---
fig, ax = plt.subplots(figsize=(9, 6))

colors = {
    "TC County":   "steelblue",
    "Greater MN":  "orange",
    "Non-MN":      "crimson"
}

# Forward transitions: solid lines (source → McLeod)
for key, label in TRANSITIONS.items():
    sub = summary[
        (summary["Transition"] == key) &
        (summary["Direction"] == "into_mcleod")
    ].sort_values("seq_count")

    ax.errorbar(
        sub["seq_count"],
        sub["mean_count"],
        yerr=sub["sem"],
        fmt='-o',
        capsize=4,
        linewidth=1.8,
        markersize=6,
        elinewidth=1.2,
        label=f"{label} → McLeod",
        color=colors[label]
    )

# Reverse transitions: dashed lines (McLeod → source)
for key, label in REVERSE_TRANSITIONS.items():
    sub = summary[
        (summary["Transition"] == key) &
        (summary["Direction"] == "from_mcleod")
    ].sort_values("seq_count")

    ax.errorbar(
        sub["seq_count"],
        sub["mean_count"],
        yerr=sub["sem"],
        fmt='--s',
        capsize=4,
        linewidth=1.8,
        markersize=6,
        elinewidth=1.2,
        label=f"McLeod → {label}",
        color=colors[label],
        alpha=0.75
    )

# --- Labels ---
ax.set_title('Rarefaction Curves: Introductions Into and Out of McLeod', fontsize=14, pad=12)
ax.set_xlabel('Sequences from McLeod', fontsize=11)
ax.set_ylabel('Transition Count', fontsize=11)
ax.grid(True, linewidth=0.8)
ax.set_axisbelow(True)

# --- Legend: two-column layout to keep it tidy ---
ax.legend(
    title="Direction",
    ncol=2,
    fontsize=9,
    title_fontsize=9,
    framealpha=0.9
)

plt.tight_layout()
plt.savefig('rarefaction_all_sources_mcleod.png', dpi=150, bbox_inches='tight')
plt.show()


# In[ ]:




