"""
Hoops Performance — your basketball training program as an interactive app.

Run locally with:
    streamlit run app.py

See README.md for how to deploy this for free so it's available on your phone too.
"""

import json
import os
from datetime import datetime

import streamlit as st

from data import (
    SCHEDULE,
    DAY_ORDER,
    EXERCISES,
    MOBILITY,
    GOATA,
    NUTRITION,
    RULES,
)

# ---------------------------------------------------------------------------
# PAGE CONFIG
# ---------------------------------------------------------------------------
st.set_page_config(
    page_title="Hoops Performance",
    page_icon="🏀",
    layout="centered",
    initial_sidebar_state="expanded",
)

# ---------------------------------------------------------------------------
# PROGRESS PERSISTENCE (simple local JSON file)
# ---------------------------------------------------------------------------
PROGRESS_FILE = "progress.json"


def load_progress():
    if os.path.exists(PROGRESS_FILE):
        try:
            with open(PROGRESS_FILE, "r") as f:
                return json.load(f)
        except Exception:
            return {}
    return {}


def save_progress(progress):
    try:
        with open(PROGRESS_FILE, "w") as f:
            json.dump(progress, f)
    except Exception:
        pass  # non-fatal — progress just won't persist this run


if "progress" not in st.session_state:
    st.session_state.progress = load_progress()


def is_checked(day, exercise_name):
    return st.session_state.progress.get(day, {}).get(exercise_name, False)


def set_checked(day, exercise_name, value):
    st.session_state.progress.setdefault(day, {})[exercise_name] = value
    save_progress(st.session_state.progress)


# ---------------------------------------------------------------------------
# SHARED RENDER HELPERS
# ---------------------------------------------------------------------------
def render_day(day_name, key_prefix=""):
    plan = SCHEDULE[day_name]

    if plan["practice"]:
        st.info(f"🏀 {plan['practice']}")

    st.subheader(plan["gym_title"])
    st.caption(plan["gym_subtitle"])

    if plan["warmup"]:
        with st.expander("Warm-up"):
            for item in plan["warmup"]:
                st.markdown(f"- {item}")

    st.markdown("**Session**")
    done_count = 0
    for ex in plan["exercises"]:
        name = ex["name"]
        checked = st.checkbox(
            f"{name} — {ex['sets_reps']}",
            value=is_checked(day_name, name),
            key=f"{key_prefix}{day_name}_{name}",
        )
        if checked != is_checked(day_name, name):
            set_checked(day_name, name, checked)
        if checked:
            done_count += 1

        if name in EXERCISES:
            with st.expander(f"How to: {name}", expanded=False):
                info = EXERCISES[name]
                st.markdown(f"*Target: {info['target']}*")
                st.write(info["instructions"])
                st.markdown(f"**Cue:** {info['cue']}")

    total = len(plan["exercises"])
    if total:
        st.progress(done_count / total, text=f"{done_count}/{total} exercises done")

    if plan.get("note"):
        st.markdown(f"> {plan['note']}")


# ---------------------------------------------------------------------------
# SIDEBAR NAVIGATION
# ---------------------------------------------------------------------------
st.sidebar.title("🏀 Hoops Performance")
page = st.sidebar.radio(
    "Navigate",
    [
        "Today",
        "Weekly Schedule",
        "Exercise Library",
        "Mobility",
        "GOATA",
        "Nutrition",
    ],
)

with st.sidebar.expander("Rules to actually follow"):
    for r in RULES:
        st.markdown(f"- {r}")

# ---------------------------------------------------------------------------
# PAGE: TODAY
# ---------------------------------------------------------------------------
if page == "Today":
    today_name = datetime.now().strftime("%A")
    st.title("Today")

    if today_name in SCHEDULE:
        default_day = today_name
    else:
        default_day = DAY_ORDER[0]

    chosen_day = st.selectbox(
        "Viewing plan for:",
        DAY_ORDER,
        index=DAY_ORDER.index(default_day),
    )
    if chosen_day == today_name:
        st.caption(f"📅 It's {today_name} — here's your plan for today.")
    else:
        st.caption(f"📅 Today is {today_name}. You're looking ahead at {chosen_day}.")

    render_day(chosen_day, key_prefix="today_")

# ---------------------------------------------------------------------------
# PAGE: WEEKLY SCHEDULE
# ---------------------------------------------------------------------------
elif page == "Weekly Schedule":
    st.title("Weekly Schedule")
    st.caption("Four lifting days, two cardio days, one protected rest day.")

    tabs = st.tabs(DAY_ORDER)
    for tab, day in zip(tabs, DAY_ORDER):
        with tab:
            render_day(day, key_prefix="week_")

# ---------------------------------------------------------------------------
# PAGE: EXERCISE LIBRARY
# ---------------------------------------------------------------------------
elif page == "Exercise Library":
    st.title("Exercise Library")
    st.caption("Every exercise in the program, with cues on how to do it right.")

    search = st.text_input("Search exercises", "")

    # build a reverse lookup of which day(s) each exercise appears on
    day_lookup = {}
    for day, plan in SCHEDULE.items():
        for ex in plan["exercises"]:
            day_lookup.setdefault(ex["name"], []).append(day)

    names = sorted(EXERCISES.keys())
    if search:
        names = [n for n in names if search.lower() in n.lower()]

    if not names:
        st.write("No exercises match that search.")

    for name in names:
        info = EXERCISES[name]
        with st.expander(name):
            st.markdown(f"*Target: {info['target']}*")
            st.write(info["instructions"])
            st.markdown(f"**Cue:** {info['cue']}")
            days = day_lookup.get(name, [])
            if days:
                st.caption(f"Appears on: {', '.join(days)}")

# ---------------------------------------------------------------------------
# PAGE: MOBILITY
# ---------------------------------------------------------------------------
elif page == "Mobility":
    st.title("Daily Mobility")
    st.caption("5-15 minutes, every day. Pick the pieces relevant to what you're warming up for.")

    for item in MOBILITY:
        with st.expander(f"{item['name']} — {item['reps']}"):
            st.write(item["instructions"])

# ---------------------------------------------------------------------------
# PAGE: GOATA
# ---------------------------------------------------------------------------
elif page == "GOATA":
    st.title("GOATA")
    st.caption(
        "Greatest Of All Time Actions — foundational human movement patterns "
        "(crawling, hanging, ground get-ups, deep squatting). No sport-specific "
        "skill work here on purpose."
    )

    for drill in GOATA:
        with st.expander(f"{drill['name']} — {drill['duration']}"):
            st.write(drill["instructions"])

# ---------------------------------------------------------------------------
# PAGE: NUTRITION
# ---------------------------------------------------------------------------
elif page == "Nutrition":
    st.title("Nutrition")

    season = NUTRITION["in_season"]
    st.subheader(season["label"])
    col1, col2, col3 = st.columns(3)
    col1.metric("Carbs", f"{season['carbs']}%")
    col2.metric("Protein", f"{season['protein']}%")
    col3.metric("Fat", f"{season['fat']}%")
    st.progress(season["carbs"] / 100, text="Carbs")
    st.progress(season["protein"] / 100, text="Protein")
    st.progress(season["fat"] / 100, text="Fat")
    st.caption(season["note"])

    with st.expander(f"{NUTRITION['off_season']['label']} split"):
        off = NUTRITION["off_season"]
        st.write(f"Carbs {off['carbs']}% / Protein {off['protein']}% / Fat {off['fat']}%")
        st.caption(off["note"])

    st.divider()
    st.subheader("Game Day Timing")
    for item in NUTRITION["game_day"]:
        st.markdown(f"**{item['when']}** — {item['what']}")

    st.divider()
    st.subheader("Hydration")
    st.write(NUTRITION["hydration"])

    st.divider()
    st.info(NUTRITION["aesthetics_note"])

# ---------------------------------------------------------------------------
# FOOTER
# ---------------------------------------------------------------------------
st.sidebar.divider()
st.sidebar.caption("Built with you, turn by turn, in conversation with Claude.")
