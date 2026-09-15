"""
All the actual program content lives here, kept separate from the app/UI code
in app.py. If you ever want to change a rep scheme, swap an exercise, or
tweak the nutrition numbers, this is the only file you need to touch.
"""

# ---------------------------------------------------------------------------
# WEEKLY SCHEDULE
# ---------------------------------------------------------------------------
SCHEDULE = {
    "Monday": {
        "practice": "Basketball practice — light, ~1hr (evening)",
        "gym_title": "Lower Body Strength + Jump",
        "gym_subtitle": "Basketball priority day",
        "warmup": [
            "Leg swings — 10 each direction/leg",
            "Ankle circles — 10 each direction",
            "Knee-to-wall ankle mobility — 10 each side",
            "90/90 hip rotations — 8 each side",
            "Heel walks — 15-20m",
            "Toe walks — 15-20m",
        ],
        "exercises": [
            {"name": "Romanian Deadlift", "sets_reps": "3×8"},
            {"name": "Bulgarian Split Squat", "sets_reps": "3×8/leg"},
            {"name": "Step-Up", "sets_reps": "2×6/leg"},
            {"name": "Single-Leg Calf Isometric Hold", "sets_reps": "3×30s/leg"},
            {"name": "Tibialis Raises", "sets_reps": "2×20"},
            {"name": "Pallof Press", "sets_reps": "3×8/side"},
        ],
        "note": "The RDL stays here as your posterior-chain/jump-power foundation — it's what "
                "translates into vertical jump. No depth jumps or max-effort jumping on this day; "
                "mixing heavy lifting with high-intensity plyometrics in the same session dilutes both.",
    },
    "Tuesday": {
        "practice": None,
        "gym_title": "Upper Body: Shoulders + Triceps",
        "gym_subtitle": "Athletic-physique day",
        "warmup": [
            "Shoulder circles — 10 each direction",
            "Band pull-aparts — 2×15",
            "Arm swings — 10 each direction",
        ],
        "exercises": [
            {"name": "Lateral Raise", "sets_reps": "3×12-15"},
            {"name": "Overhead Press", "sets_reps": "3×6-8"},
            {"name": "Rear Delt Fly", "sets_reps": "3×12-15"},
            {"name": "Close-Grip Bench Press or Dips", "sets_reps": "3×8-10"},
            {"name": "Overhead Triceps Extension", "sets_reps": "3×10-12"},
            {"name": "Incline or Flat Bench Press", "sets_reps": "2×8-10"},
        ],
        "note": "Lateral raise leads the session, bench closes it — deliberately. Whatever comes "
                "first gets the priority. Shoulders and arms build the 'athletic' look without "
                "tipping toward a bodybuilder look the way an overdeveloped chest does.",
    },
    "Wednesday": {
        "practice": "Basketball practice — light, ~1hr (evening)",
        "gym_title": "Low-Intensity Cardio",
        "gym_subtitle": "Easy pace, separate from any lifting",
        "warmup": [],
        "exercises": [
            {"name": "Steady-State Cardio", "sets_reps": "45-60 min, easy/conversational pace"},
        ],
        "note": "Incline walk, stairmaster, or steady bike. This should feel easy the whole way "
                "through — you're not chasing a training effect here beyond aerobic base and recovery blood flow.",
    },
    "Thursday": {
        "practice": None,
        "gym_title": "Upper Body: Back + Arms",
        "gym_subtitle": "Athletic-physique day",
        "warmup": [
            "T-spine rotations — 8 each side",
            "Band pull-aparts — 2×15",
        ],
        "exercises": [
            {"name": "Pull-Up or Lat Pulldown", "sets_reps": "3×8-10"},
            {"name": "Flat Row", "sets_reps": "3×8-10"},
            {"name": "Face Pull", "sets_reps": "2×12-15"},
            {"name": "Barbell or Dumbbell Curl", "sets_reps": "3×8-10"},
            {"name": "Hammer Curl", "sets_reps": "2×10-12"},
            {"name": "Hanging Leg Raise", "sets_reps": "2×8-10"},
        ],
        "note": "Flat row instead of incline keeps the tension on mid-traps instead of upper traps. "
                "Pull volume stays moderate on purpose — chasing a dramatic V-taper starts to read "
                "as bodybuilder rather than athlete.",
    },
    "Friday": {
        "practice": "Basketball practice — light, ~1hr (evening)",
        "gym_title": "Reactive Power + Core",
        "gym_subtitle": "Basketball priority day",
        "warmup": [
            "Leg swings — 10 each direction/leg",
            "Ankle circles — 10 each direction",
            "Heel walks — 15-20m, then toe walks — 15-20m",
            "Pogo Hops — 2×10 (easy, priming the tendons)",
        ],
        "exercises": [
            {"name": "Snap-Downs", "sets_reps": "2×4"},
            {"name": "Low Depth/Drop Jumps", "sets_reps": "2×3"},
            {"name": "Squat", "sets_reps": "3×6"},
            {"name": "Single-Leg Romanian Deadlift", "sets_reps": "2×8/leg"},
            {"name": "Hip Thrust", "sets_reps": "2×8"},
            {"name": "Pallof Press", "sets_reps": "3×8/side"},
            {"name": "Single-Leg Calf Raise", "sets_reps": "2×12/leg"},
        ],
        "note": "Reactive work (snap-downs, depth jumps) comes first while your nervous system is "
                "freshest. Volume stays deliberately low here — quality ground-contact time is the "
                "entire point, and fatigue is what ruins it.",
    },
    "Saturday": {
        "practice": None,
        "gym_title": "High-Intensity Cardio",
        "gym_subtitle": "Short and all-out",
        "warmup": [
            "Light jog or bike — 5 min",
            "Leg swings — 10 each direction/leg",
        ],
        "exercises": [
            {"name": "Sprint or Hill Sprint Intervals", "sets_reps": "6-8 rounds × 20-30s all-out, full recovery between"},
        ],
        "note": "A pickup game or scrimmage can substitute here if one's available that week. "
                "Nothing moderate — this is meant to be genuinely hard and genuinely short.",
    },
    "Sunday": {
        "practice": None,
        "gym_title": "Rest + Mobility",
        "gym_subtitle": "Protected recovery day",
        "warmup": [],
        "exercises": [
            {"name": "Mobility Flow", "sets_reps": "10-15 min"},
            {"name": "Easy Walk", "sets_reps": "optional, 10-20 min"},
        ],
        "note": "This is the one fully protected day in the week. If fatigue is building up, this "
                "is not the day to trim — trim Saturday's cardio or a set somewhere else first.",
    },
}

DAY_ORDER = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]

# ---------------------------------------------------------------------------
# EXERCISE LIBRARY — how to actually do each movement
# ---------------------------------------------------------------------------
EXERCISES = {
    "Romanian Deadlift": {
        "target": "Hamstrings, glutes, lower back — jump power engine",
        "instructions": "Stand with feet hip-width apart, holding a barbell or dumbbells in front "
                         "of your thighs. Keeping a soft bend in your knees and your back flat, push "
                         "your hips backward and lower the weight down the front of your legs until "
                         "you feel a deep stretch in your hamstrings — usually around shin height. "
                         "Drive your hips forward to stand back up, squeezing your glutes at the top.",
        "cue": "Hinge, don't squat — push your hips back, not straight down.",
    },
    "Bulgarian Split Squat": {
        "target": "Single-leg strength — quads, glutes",
        "instructions": "Stand a couple feet in front of a bench with one foot resting on it behind "
                         "you (laces down). Lower your back knee toward the floor by bending the front "
                         "leg, keeping your front knee tracking over your toes. Push through the front "
                         "foot to stand back up. Complete all reps on one leg before switching.",
        "cue": "Most of your weight should stay on the front foot — the back foot is just for balance.",
    },
    "Step-Up": {
        "target": "Single-leg strength, takeoff-leg power",
        "instructions": "Place one foot fully on a sturdy bench or box. Drive through that foot to "
                         "stand up on the bench, avoiding pushing off with the trailing leg. Control "
                         "the descent back down rather than dropping.",
        "cue": "Drive through the working leg on the way up, control the way down.",
    },
    "Single-Leg Calf Isometric Hold": {
        "target": "Ankle stability, calf strength",
        "instructions": "Rise onto the ball of one foot as high as you can, holding your ankle "
                         "stacked directly under your hip. Hold the top position without wobbling for "
                         "the prescribed time, then switch legs.",
        "cue": "A stable, quiet ankle matters more than how high you rise.",
    },
    "Tibialis Raises": {
        "target": "Shin muscles (opposes calves) — ankle balance",
        "instructions": "Lean your back against a wall with heels a foot or two in front of you. "
                         "Keeping your legs straight, lift your toes and the front of your feet up "
                         "toward your shins as high as you can, then lower with control.",
        "cue": "Small range of motion, controlled tempo — this is a burn-focused exercise, not a heavy one.",
    },
    "Pallof Press": {
        "target": "Anti-rotation core stiffness",
        "instructions": "Anchor a resistance band or cable at chest height and stand side-on to it, "
                         "holding the handle at your chest with both hands. Press the handle straight "
                         "out in front of you and hold for a moment, resisting the band's pull that "
                         "wants to rotate your torso toward the anchor. Bring it back to your chest "
                         "with control.",
        "cue": "Nothing should move except your arms — your hips and shoulders stay square.",
    },
    "Lateral Raise": {
        "target": "Side deltoids — shoulder width",
        "instructions": "Hold a light dumbbell in each hand at your sides. With a slight bend in your "
                         "elbows, raise both arms out to the sides until they're roughly shoulder "
                         "height, leading with your elbows rather than your hands. Lower with control.",
        "cue": "Light weight, strict form — this is not a lift to ego-load.",
    },
    "Overhead Press": {
        "target": "Shoulders, triceps",
        "instructions": "Holding a barbell at shoulder height or a dumbbell in each hand, press the "
                         "weight straight overhead until your arms are fully extended, then lower back "
                         "to shoulder height with control. Keep your ribcage down rather than arching "
                         "your lower back.",
        "cue": "Brace your core like you're about to be punched in the stomach.",
    },
    "Rear Delt Fly": {
        "target": "Rear deltoids, upper back",
        "instructions": "Hinge forward at the hips with a slight bend in your knees, holding a light "
                         "dumbbell in each hand hanging below your shoulders. With a slight bend in "
                         "your elbows, raise both arms out to the sides and slightly back, squeezing "
                         "your shoulder blades together at the top.",
        "cue": "Think about squeezing a pencil between your shoulder blades at the top.",
    },
    "Close-Grip Bench Press or Dips": {
        "target": "Triceps, chest",
        "instructions": "Close-grip bench: set your hands just inside shoulder width on the bar, "
                         "lower it to your lower chest keeping elbows tucked, then press back up. "
                         "Dips: on parallel bars, lower your body by bending your elbows until your "
                         "upper arms are roughly parallel to the ground, then press back up.",
        "cue": "Keep elbows tucked close to your body rather than flared out.",
    },
    "Overhead Triceps Extension": {
        "target": "Triceps",
        "instructions": "Holding a dumbbell with both hands overhead, lower it behind your head by "
                         "bending your elbows, keeping your upper arms still and pointed at the "
                         "ceiling. Extend your arms back to full overhead extension.",
        "cue": "Only your forearms should move — your upper arms stay fixed.",
    },
    "Incline or Flat Bench Press": {
        "target": "Chest (kept moderate on purpose this week)",
        "instructions": "Lying on a bench (flat or slightly inclined), lower the bar or dumbbells to "
                         "chest level with control, then press back up to full arm extension without "
                         "locking out aggressively.",
        "cue": "This is deliberately placed last and kept to 2 sets — supporting volume, not the focus.",
    },
    "Pull-Up or Lat Pulldown": {
        "target": "Lats, upper back",
        "instructions": "Pull-up: from a dead hang on a bar, pull your chest toward the bar, leading "
                         "with your elbows down and back. Lat pulldown: seated at a cable machine, "
                         "pull the bar down to your upper chest, then control it back up.",
        "cue": "Lead with your elbows, not your hands.",
    },
    "Flat Row": {
        "target": "Mid-back, mid-traps (not upper traps)",
        "instructions": "Hinge forward holding a barbell or dumbbells, back flat. Pull the weight "
                         "toward your lower ribs/stomach, squeezing your shoulder blades together, "
                         "then lower with control.",
        "cue": "Pull to your stomach, not your chest — and keep shoulders down away from your ears.",
    },
    "Face Pull": {
        "target": "Rear delts, upper back, shoulder health",
        "instructions": "Set a cable or band at head height. Pull the rope or band toward your face, "
                         "flaring your elbows out wide and rotating your hands so your knuckles end up "
                         "facing behind you at the finish.",
        "cue": "Aim the pull at your eyebrows, elbows high and wide.",
    },
    "Barbell or Dumbbell Curl": {
        "target": "Biceps",
        "instructions": "Standing with a barbell or dumbbell in each hand, curl the weight up toward "
                         "your shoulders by bending your elbows, keeping your upper arms pinned to "
                         "your sides. Lower with control.",
        "cue": "No swinging — if you need momentum, the weight's too heavy.",
    },
    "Hammer Curl": {
        "target": "Biceps, forearms",
        "instructions": "Same motion as a dumbbell curl, but held with a neutral grip (palms facing "
                         "each other, thumbs up) throughout the movement.",
        "cue": "Keep your wrists neutral the whole way up and down.",
    },
    "Hanging Leg Raise": {
        "target": "Core (function, not size) — hip flexors",
        "instructions": "Hang from a pull-up bar with arms fully extended. Without swinging, raise "
                         "your legs (straight or bent at the knee) up toward your chest, then lower "
                         "with control.",
        "cue": "Control the descent — the lowering half is doing most of the work.",
    },
    "Snap-Downs": {
        "target": "Reactive strength, landing mechanics",
        "instructions": "Start on your toes, then quickly drop into a strong, stable athletic "
                         "landing position (like a mini-squat) as fast as possible, absorbing the drop "
                         "through your legs.",
        "cue": "Speed of the drop matters more than depth — land fast and stick it.",
    },
    "Low Depth/Drop Jumps": {
        "target": "Reactive power — tendon stiffness",
        "instructions": "Step off a low box (roughly knee height), and the instant your feet touch "
                         "the ground, explode straight upward into a maximum-height jump. The goal is "
                         "minimum time spent on the ground between landing and takeoff.",
        "cue": "Think 'ground is hot' — off it as fast as possible.",
    },
    "Squat": {
        "target": "Quads, glutes — overall lower body strength",
        "instructions": "With a barbell on your back (or holding a dumbbell/kettlebell at your "
                         "chest), lower your hips down and back as if sitting into a chair, keeping "
                         "your chest up and knees tracking over your toes, until thighs are roughly "
                         "parallel to the ground. Drive back up through your whole foot.",
        "cue": "Clean reps, no grinding — this week's version isn't meant to be a max effort.",
    },
    "Single-Leg Romanian Deadlift": {
        "target": "Hamstrings, glutes, balance",
        "instructions": "Standing on one leg holding a dumbbell in the opposite hand, hinge forward "
                         "at the hips while your free leg extends straight back behind you, keeping "
                         "your body in a straight line from head to heel. Return to standing.",
        "cue": "Keep your hips square to the ground — don't let them rotate open.",
    },
    "Hip Thrust": {
        "target": "Glutes — hip extension power",
        "instructions": "Sit on the ground with your upper back against a bench, a barbell or "
                         "dumbbell resting across your hips. Drive your hips up toward the ceiling by "
                         "squeezing your glutes, until your body forms a straight line from shoulders "
                         "to knees, then lower with control.",
        "cue": "Squeeze your glutes hard at the top — don't just lift the weight, drive through them.",
    },
    "Single-Leg Calf Raise": {
        "target": "Calves — takeoff power",
        "instructions": "Standing on one foot (holding onto something for balance if needed), rise "
                         "onto the ball of your foot as high as possible, then lower all the way down "
                         "under control until you feel a stretch in your calf.",
        "cue": "Full range of motion — don't cut the bottom stretch short.",
    },
}

# ---------------------------------------------------------------------------
# MOBILITY / DAILY STRETCHING
# ---------------------------------------------------------------------------
MOBILITY = [
    {
        "name": "Leg Swings",
        "reps": "10 each direction, each leg",
        "instructions": "Holding onto a wall or rack for balance, swing one leg forward and back in "
                         "a controlled arc, then switch to side-to-side swings. Keep your torso "
                         "upright throughout.",
    },
    {
        "name": "Ankle Circles",
        "reps": "10 each direction, each ankle",
        "instructions": "Lift one foot slightly off the ground and rotate it slowly through a full "
                         "circle at the ankle, both clockwise and counterclockwise.",
    },
    {
        "name": "Knee-to-Wall Ankle Mobility",
        "reps": "10 each side",
        "instructions": "Facing a wall in a half-kneeling position, try to touch your front knee to "
                         "the wall while keeping your heel flat on the ground. Walk your foot back "
                         "until this is just barely achievable, and repeat.",
    },
    {
        "name": "90/90 Hip Rotations",
        "reps": "8 each side",
        "instructions": "Sit on the ground with one leg bent in front of you at 90°, the other bent "
                         "behind you at 90°. Rotate between switching which leg is in front, keeping "
                         "both knees bent through the transition.",
    },
    {
        "name": "T-Spine Rotations",
        "reps": "8 each side",
        "instructions": "On all fours, place one hand behind your head. Rotate your torso to open "
                         "that elbow up toward the ceiling, following it with your eyes, then rotate "
                         "back down and across toward the opposite arm.",
    },
    {
        "name": "Hamstring Mobility",
        "reps": "2×30s each leg",
        "instructions": "Prop one heel on a low surface with your leg straight, and hinge forward "
                         "from your hips (keeping your back flat) until you feel a stretch down the "
                         "back of that leg.",
    },
    {
        "name": "Hip-Flexor Mobility",
        "reps": "2×30s each side",
        "instructions": "From a half-kneeling lunge position, tuck your pelvis slightly and shift "
                         "your weight forward until you feel a stretch in the front of the hip of "
                         "your rear leg.",
    },
    {
        "name": "Heel Walks",
        "reps": "15-20m",
        "instructions": "Walk forward on your heels with your toes lifted off the ground as high as "
                         "possible, for the given distance.",
    },
    {
        "name": "Toe Walks",
        "reps": "15-20m",
        "instructions": "Walk forward on the balls of your feet with your heels lifted as high as "
                         "possible, for the given distance.",
    },
    {
        "name": "Band Pull-Aparts",
        "reps": "2×15",
        "instructions": "Hold a light resistance band with both hands at shoulder height, arms "
                         "extended. Pull the band apart by driving your arms out to the sides until "
                         "it touches your chest, then return with control.",
    },
    {
        "name": "Pogo Hops",
        "reps": "2×10",
        "instructions": "Small, fast, low hops off both feet, spending as little time on the ground "
                         "as possible each contact. Keep knees slightly bent and stay light on your feet.",
    },
]

# ---------------------------------------------------------------------------
# GOATA — Greatest Of All Time Actions
# Foundational human movement patterns: crawling, hanging, ground-based
# get-ups, deep squatting. No basketball-specific skill work here on purpose —
# this is about restoring/maintaining how the body is built to move, separate
# from sport skill.
# ---------------------------------------------------------------------------
GOATA = [
    {
        "name": "Deep Squat Hold",
        "duration": "2-3 min total, broken into sets if needed",
        "instructions": "Lower into a full squat with your feet flat on the ground, hips below your "
                         "knees. Rest your elbows against the inside of your knees and gently press "
                         "outward if it helps you settle in. Relax into the position and breathe "
                         "normally rather than fighting it.",
    },
    {
        "name": "Bear Crawl",
        "duration": "2×20m",
        "instructions": "On hands and feet with your hips low and knees hovering just off the "
                         "ground, crawl forward by moving your opposite hand and foot together, "
                         "keeping your back flat and hips level.",
    },
    {
        "name": "Crab Walk",
        "duration": "2×15m",
        "instructions": "Sit with your hands behind you, fingers pointing toward your feet, and lift "
                         "your hips off the ground. Walk forward, backward, or sideways on your hands "
                         "and feet while keeping your hips elevated the whole time.",
    },
    {
        "name": "Dead Hang",
        "duration": "2×20-30s (build up over time)",
        "instructions": "Hang from a pull-up bar with a relaxed grip, letting your shoulders and "
                         "spine lengthen out fully under your own bodyweight. Just hang and breathe — "
                         "no swinging or shrugging up.",
    },
    {
        "name": "Contralateral Crawl",
        "duration": "2×8 each side",
        "instructions": "On hands and knees, slowly reach one arm straight forward while "
                         "simultaneously extending the opposite leg straight back. Hold for a moment "
                         "to feel the balance challenge, then return and switch sides.",
    },
    {
        "name": "Ground-to-Standing Get-Up",
        "duration": "5-8 reps, varying the pattern each time",
        "instructions": "Starting flat on your back, get yourself up to standing using as few points "
                         "of contact with the ground as possible — avoid the default 'roll to knees, "
                         "push up' pattern most adults default to. Reverse it back down to lying with "
                         "control. Try a different route up each rep.",
    },
]

# ---------------------------------------------------------------------------
# NUTRITION
# ---------------------------------------------------------------------------
NUTRITION = {
    "in_season": {
        "label": "In-Season (current)",
        "carbs": 55, "protein": 25, "fat": 20,
        "note": "Prioritizes glycogen refill and performance to support practices, games, and the "
                "added training volume.",
    },
    "off_season": {
        "label": "Off-Season (reference)",
        "carbs": 40, "protein": 30, "fat": 30,
        "note": "Prioritizes building and repairing tissue when there's no game schedule to fuel around.",
    },
    "game_day": [
        {"when": "~4 hours before", "what": "Solid, balanced meal — complex carbs + lean protein, light on fat/fiber"},
        {"when": "~1 hour before", "what": "Light snack — banana or a small energy bar"},
        {"when": "During play", "what": "Simple sugars — sports drink or gel to keep energy up"},
    ],
    "hydration": "Stay consistent through the day with electrolytes included — not just water at practice.",
    "aesthetics_note": "How visible any physique changes are still comes down mostly to your total "
                        "intake. This program builds the muscle and keeps you lean-capable, but "
                        "whether that shows up as visible definition depends on whether you're "
                        "eating at maintenance, a surplus, or a deficit.",
}

# ---------------------------------------------------------------------------
# GENERAL RULES
# ---------------------------------------------------------------------------
RULES = [
    "Team practice and games count as training — don't treat them as separate from your workload.",
    "Keep explosive work (Friday's snap-downs/depth jumps) short and high-quality; stop the set the moment quality drops.",
    "Chase performance, not soreness.",
    "With six active days in the mix, protect Sunday — if fatigue creeps in, trim Saturday's cardio "
    "or a set here and there before touching practice or the Monday/Friday basketball-priority days.",
    "Sharp pain is different from training fatigue — stop and get it looked at by a qualified "
    "professional rather than pushing through.",
]
