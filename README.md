# Hoops Performance

Your basketball performance + physique program as an interactive app — weekly
schedule, an exercise library with how-to instructions, daily mobility,
skill practice, and a nutrition guide.

Built with [Streamlit](https://streamlit.io), a Python framework that turns a
script into a real web app. That's the key to getting this on your phone
without writing any native app code.

---

## 1. Run it on your laptop

You need Python 3.9+ already installed. Then, in a terminal, inside this folder:

```bash
pip install -r requirements.txt
streamlit run app.py
```

A browser tab opens automatically at `http://localhost:8501` — that's the app.
Leave the terminal window running while you use it; closing it stops the app.

---

## 2. Quick option: view it on your phone over WiFi (no deployment needed)

If your laptop and phone are on the **same WiFi network**, you can open the
app on your phone directly from your laptop, with no internet deployment step:

1. Find your laptop's local IP address:
   - **Mac/Linux:** open Terminal, run `ipconfig getifaddr en0` (Mac) or `hostname -I` (Linux)
   - **Windows:** open Command Prompt, run `ipconfig`, look for "IPv4 Address" (something like `192.168.1.23`)
2. Run the app so it's reachable on the network, not just on the laptop itself:
   ```bash
   streamlit run app.py --server.address 0.0.0.0
   ```
3. On your phone's browser, go to `http://<that-ip-address>:8501`

Downside: this only works while your laptop is on, the app is running, and
you're on the same WiFi. For something you can open anytime, deploy it (next
section) — takes about 5 minutes and is also free.

---

## 3. Deploy it for free, so it's on your phone anytime, anywhere

This uses **Streamlit Community Cloud**, which is free for personal projects
like this one. You'll need a free GitHub account if you don't already have one.

1. **Put this folder on GitHub.**
   - Go to [github.com](https://github.com), create a free account if needed.
   - Create a new repository (it can be private).
   - Upload these files to it: `app.py`, `data.py`, `requirements.txt`, and
     the `.streamlit/` folder (with `config.toml` inside it). The easiest way
     if you're not familiar with git: on your new repo's GitHub page, use the
     "Add file → Upload files" button and drag all of them in, including the
     `.streamlit` folder.

2. **Deploy on Streamlit Community Cloud.**
   - Go to [share.streamlit.io](https://share.streamlit.io) and sign in with
     your GitHub account (also free).
   - Click "New app," pick the repository you just created, and set the main
     file path to `app.py`.
   - Click "Deploy." After a minute or two, you'll get a public URL like
     `https://your-app-name.streamlit.app`.

3. **Add it to your phone's home screen** so it behaves like an app icon:
   - **iPhone (Safari):** open the URL → tap the Share icon → "Add to Home Screen."
   - **Android (Chrome):** open the URL → tap the ⋮ menu → "Add to Home screen" (or "Install app").

Now you've got an icon that opens straight to your program, on any device,
without your laptop needing to be on.

**One thing to know:** the free tier's storage isn't permanent — if the app
goes to sleep from inactivity or gets redeployed, the checkbox progress
tracker may reset. The schedule, exercise library, mobility, and nutrition
content are unaffected either way; it's only the "which boxes did I check"
tracking that could reset occasionally. If that becomes annoying, it's a
sign you'd want a proper database instead of a JSON file — worth asking for
if you get there.

---

## 4. Updating the program later

Everything you'd actually want to change — sets/reps, exercises, nutrition
numbers, adding a new day — lives in **`data.py`**. `app.py` is just the
interface and shouldn't need to change for normal edits. If you're deployed
on Streamlit Cloud, push the updated file to GitHub and the live app updates
automatically within a minute or two.

---

## File overview

```
hoops_app/
├── app.py                  # the app itself (UI, navigation, progress tracking)
├── data.py                 # all program content — edit this to change anything
├── requirements.txt        # what pip installs
├── .streamlit/
│   └── config.toml         # color theme
└── README.md                # this file
```
